document.addEventListener('DOMContentLoaded', function() {
    const serviceSelect = document.getElementById('servico');
    const valueInput = document.getElementById('valor');
    const quantityInput = document.getElementById('quantidade');
    const totalValueInput = document.getElementById('valor_total');

    serviceSelect.addEventListener('change', function() {
        const selectedService = serviceSelect.value;
        fetch('/services/json')
            .then(response => response.json())
            .then(data => {
                const service = data.services.find(s => s.nome === selectedService);
                if (service) {
                    valueInput.value = service.valor;
                    updateTotalValue();
                }
            });
    });

    quantityInput.addEventListener('input', updateTotalValue);

    function updateTotalValue() {
        const value = parseFloat(valueInput.value) || 0;
        const quantity = parseInt(quantityInput.value) || 0;
        totalValueInput.value = value * quantity;
    }
});
