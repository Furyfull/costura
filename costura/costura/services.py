from pynfe.processamento.comunicacao import ComunicacaoSefaz
from pynfe.entidades.notafiscal import NotaFiscal
from pynfe.entidades.fonte_dados import _fonte_dados
from pynfe.processamento.serializacao import SerializacaoXML, SerializacaoQrcode
from pynfe.processamento.assinatura import AssinaturaA1
from pynfe.utils.flags import CODIGO_BRASIL
from pynfe.entidades.servico import Servico
from lxml import etree
from decimal import Decimal
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Spacer
from reportlab.lib import colors
from io import BytesIO

def emitir_nfce(certificado, senha, homologacao, token, csc, emitente_data, cliente_data, produtos):

    emitente = emitente_data
    cliente = cliente_data

    # Criar Nota Fiscal
    nota_fiscal = NotaFiscal(
        modelo=65, 
        serie='1',                      #(obrigatorio)
        numero_nf='111',                #(obrigatorio)
        data_emissao=datetime.datetime.now(),   #(obrigatorio)
        natureza_operacao='VENDA',      #(obrigatorio)
        tipo_documento=1,               #(obrigatorio)
        processo_emissao='0',           #(obrigatorio)
        tipo_impressao_danfe=4,         #(obrigatorio)
        tipo_pagamento=1,               # ex: 01 (Dinheiro)
        forma_emissao='1',              #(obrigatorio)
        finalidade_emissao='1',         #(obrigatorio)
        cliente_final=1,                #   0 (Não), 1 (Sim)
        indicador_presencial=1,         #   1 (Presencial), 2 (Internet)
        indicador_intermediador =0,     #   0 (Sem intermediador)
        indicador_destino=1,            #   1=interna 2=interestadual 3=com exterior

        uf=emitente_data.endereco_uf.upper(),
        municipio=emitente_data.endereco_cod_municipio,   # o codigo
        emitente=emitente,
        cliente=cliente,

        data_saida_entrada=datetime.datetime.now(),
        transporte_modalidade_frete=9,     # 9= Sem Ocorrência de Transporte.
        informacoes_adicionais_interesse_fisco='Mensagem complementar',
        totais_tributos_aproximado=Decimal('21.06'),
    )

    # Adicionar produtos
    for produto in produtos:
        nota_fiscal.adicionar_produto_servico(**produto)

    # Adicionar responsável técnico
    nota_fiscal.adicionar_responsavel_tecnico(
        cnpj='99999999000199',
        contato='TadaSoftware',
        email='tadasoftware@gmail.com',
        fone='11912341234'
    )

    # Serialização
    serializador = SerializacaoXML(_fonte_dados, homologacao=homologacao)
    nfce = serializador.exportar()

    # # Assinatura
    # a1 = AssinaturaA1(certificado, senha)
    # xml = a1.assinar(nfce)

    # # Geração do QRCode
    # xml_com_qrcode = SerializacaoQrcode().gerar_qrcode(token, csc, xml)

    # # Envio para SEFAZ
    # con = ComunicacaoSefaz(emitente_data['endereco_uf'], certificado, senha, homologacao)
    # envio = con.autorizacao(modelo='nfce', nota_fiscal=xml_com_qrcode)

    # Se tudo ocorreu corretamente, retornamos 0 e o XML
    # Quando for oficial vamos retornar o "envio"
    return 0, nfce  # 0 indicando sucesso

def gerar_servicos_relatorio_pdf(ordem_itens, filtro):
    styles = getSampleStyleSheet()
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elementos = []
    dados = [['Id','Cliente','Serviço', 'Quant.','Descrição', 'Comissão', 'Prazo']]
    
    for item in ordem_itens:
        if not filtro or item.ordem.status != 2:
            comissao_item = (Decimal(item.comissao) / 150) * item.quantidade * item.preco_total()
        #  Id -- Cliente -- Serviço -- Quant -- Descrição -- Comissão -- Prazo
            dados.append([
                item.ordem.id,
                Paragraph(item.ordem.cliente.nome, styles['Normal']),
                Paragraph(item.servico.nome, styles['Normal']),
                item.quantidade,
                Paragraph(item.descricao or 'Sem descrição', styles['Normal']),
                f"R$ {comissao_item:.2f} ({item.comissao}%)",
                item.ordem.data_entrega.strftime("%d/%m/%Y"),
            ])


    # Adicionar título
    titulo = Paragraph("Relatório de Serviços", styles['Title'])
    elementos.append(titulo)
    elementos.append(Spacer(1, 12))

    # Adicionar comentario
    comentario = Paragraph(
        "Este relatório apresenta uma lista detalhada de serviços realizados pelas costureiras, "
        "incluindo informações sobre a comissão e o valor total."
        , styles['Normal']
    )
    elementos.append(comentario)
    elementos.append(Spacer(1, 24)) 

    tabela = Table(dados, colWidths=[20, None, None, None, 150, None, None])
    estilo = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
    tabela.setStyle(estilo)
    elementos.append(tabela)

    # Adicionar data no rodapé
    data_atual = datetime.now().strftime('%d/%m/%Y')
    rodape = Paragraph(f"Data de emissão: {data_atual}", styles['Normal'])
    elementos.append(Spacer(1, 12))  # Espaço antes do rodapé
    elementos.append(rodape)

    doc.build(elementos)
    buffer.seek(0)

    return buffer
