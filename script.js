const form = document.getElementById('currency-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const amount = document.getElementById('amount').value;
    const sourceCurrency = document.getElementById('source_currency').value;
    const targetCurrency = document.getElementById('target_currency').value;

    const response = await fetch(`https://api.example.com/convert?amount=${amount}&from=${sourceCurrency}&to=${targetCurrency}`);
    const data = await response.json();

    resultDiv.textContent = `Converted Amount: ${data.result}`;
});
