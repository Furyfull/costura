document.getElementById('servico').onchange = function () { atualizarPreco() }
document.getElementById('id_quantidade').oninput = function () { atualizarPreco() }

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

