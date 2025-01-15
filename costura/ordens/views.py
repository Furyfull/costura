from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from . import forms,models
from servicos.models import servicos
from cliente.models import Cliente
from django.contrib import messages

from lxml import etree
from decimal import Decimal
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.cliente import Cliente
from pynfe.utils.flags import CODIGO_BRASIL
from costura.services import emitir_nfce
import base64
import xmltodict
import json


# Create your views here.
def ordens(request):
    orders= models.Ordem.objects.all().order_by('status')
    status_choices = models.Ordem._meta.get_field('status').choices
    
    return render(request, 'ordens/orders.html',{
        'orders':orders,
        'status_choices': status_choices,
        })

def update_status(request, id):
    order = get_object_or_404(models.Ordem, pk=id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status is not None:
            order.status = int(new_status)
            order.save()
    return redirect('ordens:ordens') 

def new_order(request):
    if request.method == 'POST':
        form = forms.CriaOrdem(request.POST)
        
        if form.is_valid():
            ordem = form.save(commit=False)
            ordem.save()
            return redirect('ordens:edit_order', id=ordem.id)
    else:
        form = forms.CriaOrdem()
    return render(request, 'ordens/new_order.html', {'form': form})

def edit_order(request, id):
    servico_especial, criado = models.servicos.objects.get_or_create(nome="Especial", defaults={'valor': 0})
    order = get_object_or_404(models.Ordem, pk=id)
    services = servicos.objects.all()
    client = order.cliente

    if request.method == "POST":
        form = forms.OrdemItemForm(request.POST)
        if form.is_valid():
            ordem_item = form.save(commit=False)
            ordem_item.ordem = order
            if ordem_item.servico.nome != "Especial":
                ordem_item.valor_unit = ordem_item.servico.valor
            ordem_item.save()

            # input_values = {key: request.POST.get(key) for key in request.POST.keys()}
            messages.success(request, f"Serviço Adicionado !!!")
            return HttpResponseRedirect(request.path)
        else:
            # Exibindo erros
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            messages.warning(
                request,
                f"Falha ao Adicionar o Serviço. Error: {', '.join(error_messages)}"
            )
    else:
        form = forms.OrdemItemForm()

    # usa d def total() criada no models
    total = order.total()
    # comando .itens vem do models (related_name='itens')
    ordem_itens = order.itens.all()
    
    return render(request, 'ordens/edit_order.html', {
        'ordem':order,
        'form': form,
        'cliente':client,
        'total':total,
        'ordem_itens': ordem_itens,
        'servicos':services,
        })

def delete_order_item(request, id):
    item = get_object_or_404(models.OrdemItem, pk=id)
    item.delete()
    # Redireciona de volta à página da ordem
    return redirect('ordens:edit_order', id=item.ordem.id)  

def delete_order(request, id):
    ordem = get_object_or_404(models.Ordem, pk=id)
    ordem.delete()
    return redirect('ordens:ordens')

def emitir_nfe_view(request,id):
    order = get_object_or_404(models.Ordem, pk=id)
    ordem_itens = order.itens.all()
    client = order.cliente

    if request.method == 'POST':
        # Configurações iniciais
        certificado = "caminho para o certificado.pfx"
        senha = "senha"
        # 'True' utilizado para realizar testes !!!IMPORTANTE!!!
        homologacao = True  
        # Necessarios para gerar QrCode
        token = 'seu_token'
        csc = 'seu_csc' #Código de Segurança do Contribuinte

        # Emitente
        emitente_data = Emitente(
            razao_social='NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL', #(obrigatorio)
            cnpj='99999999000199',              #(obrigatorio)
            inscricao_estadual='9999999999',    #(obrigatorio)
            cnae_fiscal='9999999', 
            inscricao_municipal='12345',        
            codigo_de_regime_tributario='1',    #(obrigatorio)
            endereco_logradouro='Rua da Paz',   #(obrigatorio)
            endereco_numero='666',              #(obrigatorio)
            endereco_bairro='Dom Aquino',       #(obrigatorio)
            endereco_cep='87704000',
            # endereco_pais=CODIGO_BRASIL,
            endereco_uf='MT',
            endereco_municipio='Cuiabá',        #(obrigatorio)
            endereco_cod_municipio = '3550308', #(obrigatorio)
        )

        # Cliente
        cliente_data = Cliente(
            razao_social= client.nome,          #(obrigatorio)
            email='email@email.com',
            tipo_documento='CPF',               #(obrigatorio)
            numero_documento=client.cpf,        #(obrigatorio)
            indicador_ie=9,                     #(obrigatorio)

            endereco_logradouro=client.endereco,    #(obrigatorio)
            endereco_numero=client.num,             #(obrigatorio)
            endereco_complemento='Ao lado de lugar nenhum',
            endereco_bairro='client.bairro',        #(obrigatorio)
            endereco_cep='12345123',
            endereco_pais=CODIGO_BRASIL,
            endereco_uf='DF',                       #(obrigatorio)
            endereco_municipio=client.cidade,       #(obrigatorio)
            endereco_telefone=client.telefone,
        )

        # Lista de produto
        produtos=[]
        for produto in ordem_itens:
            produtos.append ({
                'descricao': 'produto.costureira',
                'codigo': '000398',
                'ean': 'SEM GTIN',
                'ean_unidade_tributavel': 'SEM GTIN',
                'ncm': '99999999',
                'unidade_comercial': 'UN',
                'valor_unitario_comercial': Decimal('9.75'),
                'unidade_tributavel': 'UN',
                'quantidade_tributavel': Decimal('12'),
                'valor_unitario_tributavel': Decimal('9.75'),
                'ind_total': 1,
                
                'valor_tributos_aprox': Decimal('21.06'),
                'icms_csosn': '400',
                'icms_modalidade': '102',
                'cfop': '5102', 
                # 'quantidade_comercial': Decimal(produto.preco_total()),
                # 'valor_total_bruto': Decimal('117.00'),
                # 'icms_origem': 0,
                # 'pis_modalidade': '07',
                # 'cofins_modalidade': '07',
            })

        # Chama a função no services.py
        resposta  = emitir_nfce(certificado, senha, homologacao, token, csc, emitente_data, cliente_data, produtos)


        if resposta[0] == 0:

            # XML > string XML
            xml_str = etree.tostring(resposta[1], encoding="unicode").replace('\n', '').replace('ns0:', '')
            request.session['xml_autorizado'] = xml_str

            # string XML > DICT > JSON
            xml_dict = xmltodict.parse(xml_str)  
            json_data = json.dumps(xml_dict, indent=4)

            return render(request, 'ordens/sucesso.html', {'xml_data': json_data})
        else:
            erro = resposta[1].text
            return render(request, 'ordens/error.html', {'error': erro})
        
    return HttpResponse("Método inválido. Use POST para emitir a nota fiscal.", status=405)

def download_nfe(request):
    # Recupera o XML gerado da sessão
    xml_autorizado = request.session.get('xml_autorizado', None)

    if xml_autorizado:
        # Retorna o XML como um arquivo para download
        response = HttpResponse(xml_autorizado, content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="nota_fiscal.xml"'
        return response
    else:
        return HttpResponse('Erro: XML não encontrado!', status=404)
