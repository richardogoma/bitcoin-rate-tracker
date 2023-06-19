document.addEventListener('DOMContentLoaded', function() {
    var currencySelect = document.getElementById('currency');
    var selectedCurrency = getURLParameter('currency');
    
    if (selectedCurrency) {
        currencySelect.value = selectedCurrency;
    }
    
    currencySelect.addEventListener('change', handleCurrencyChange);
});

function getURLParameter(name) {
    var searchParams = new URLSearchParams(window.location.search);
    return searchParams.get(name);
}

function handleCurrencyChange(event) {
    var selectedCurrency = event.target.value;
    var hostUrl = window.location.protocol + '//' + window.location.host;

    if (selectedCurrency === 'USD') {
        window.location.href = hostUrl;
    } else {
        var url = hostUrl + '?currency=' + selectedCurrency;
        window.location.href = url;
    }
}
