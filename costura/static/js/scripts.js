//pagina dashboard
function colorEntrega() {
    const hoje = new Date();

    const diaHoje = hoje.getDate();
    const mesHoje = hoje.getMonth() + 1;
    const anoHoje = hoje.getFullYear().toString().slice(-2);
    const dataHojeString = `${diaHoje}/${mesHoje}/${anoHoje}`;
    console.log(dataHojeString);

    // Seleciona todas as células que contêm a data de entrega
    const linhas = document.querySelectorAll('.dataccd');
    linhas.forEach(celula => {
        const dataEntregaString = celula.getAttribute('data-value');
        console.log(dataEntregaString + dataHojeString);

        // Converte as datas de strings para objetos Date
        const [diaEntrega, mesEntrega, anoEntrega] = dataEntregaString.split('/').map(Number);
        const dataEntrega = new Date(`20${anoEntrega}`, mesEntrega - 1, diaEntrega); // Ajuste do ano para formato completo
        const dataHoje = new Date(hoje.getFullYear(), hoje.getMonth(), hoje.getDate());

        // Verifica se a data de entrega é igual, anterior ou posterior à data de hoje
        if (dataEntrega.getTime() === dataHoje.getTime()) {
            celula.style.color = 'blue';
        } else if (dataEntrega.getTime() < dataHoje.getTime()) {
            celula.style.color = 'red';
        } else {
            celula.style.color = 'green';
        }
    });
}


//Page editar ordem
function atualizarPreco() {
    const produtoSelect = document.getElementById('servico');
    const precoOut = document.getElementById('preco');
    const quantidadeInput = document.getElementById('id_quantidade');
    const totalOut = document.getElementById('valor-total');

    // Obtém o preço unitário do produto selecionado (via data-preco)
    const selectedOption = produtoSelect.options[produtoSelect.selectedIndex];
    const preco = parseFloat(selectedOption.getAttribute('data-preco')) || 0;
    const quantidade = parseInt(quantidadeInput.value) || 1;

    // Calcula e atualiza o valor total
    totalOut.innerHTML = `Valor Total: R$ ${(preco * quantidade).toFixed(2)}`;
    precoOut.innerHTML = `Valor Unitário: R$ ${(preco).toFixed(2)}`;
}

// Função para abrir o modal
function openModal(orderId) {
    var modal = document.getElementById('modal-' + orderId);
    if (modal) {
        modal.style.display = 'block';
    }
}

// Função para fechar o modal
function closeModal(orderId) {
    var modal = document.getElementById('modal-' + orderId);
    if (modal) {
        modal.style.display = 'none';
    }
}
