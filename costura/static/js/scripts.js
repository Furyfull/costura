//pagina dashboard
function colorEntrega() {
    const hoje = new Date();

    const diaHoje = hoje.getDate();
    const mesHoje = hoje.getMonth() + 1;
    const anoHoje = hoje.getFullYear().toString().slice(-2);
    const dataHoje = `${diaHoje}/${mesHoje}/${anoHoje}`;
    console.log(dataHoje)
    // Seleciona todas as células que contêm a data de entrega
    const linhas = document.querySelectorAll('.dataccd');
    linhas.forEach(celula => {
        const dataEntrega = celula.getAttribute('data-value');
        console.log(dataEntrega + dataHoje);

        // Verifica se a data de entrega é igual à data de hoje
        if (dataEntrega === dataHoje) {
            celula.style.color = 'blue';
        } else if (dataEntrega < dataHoje) {
            celula.style.color = 'red';
        } else {
            celula.style.color = 'green';
        }
    })
};

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
    precoOut.innerHTML = `Preço: R$ ${(preco).toFixed(2)}`;
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
