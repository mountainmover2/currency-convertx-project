form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const amount = document.getElementById('amount').value;
    const sourceCurrency = document.getElementById('source_currency').value;
    const targetCurrency = document.getElementById('target_currency').value;

    try {
        const response = await fetch(`https://api.example.com/convert?amount=${amount}&from=${sourceCurrency}&to=${targetCurrency}`);
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        resultDiv.textContent = `Converted Amount: ${data.result}`;
    } catch (error) {
        console.error('Error:', error);
        resultDiv.textContent = 'Failed to fetch data. Please try again.';
    }
});
