// script.js

document.addEventListener("DOMContentLoaded", function() {
    var data = JSON.parse('{{ data | safe }}');
    var currencyVariable = '{{ currency_variable }}';
    
    Highcharts.stockChart('container', {
        navigator: {
            enabled: true
        },
        rangeSelector: {
            selected: 5
        },
        // title: {
        //     text: 'Bitcoin ' + currencyVariable + ' price'
        // },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            labels: {
                formatter: function () {
                    return Highcharts.numberFormat(this.value, 0, '.', ',');
                }
            }
        },
        plotOptions: {
            series: {
                color: 'green',
                negativeColor: 'red',
                tooltip: {
                    valueDecimals: 4
                }
            }
        },
        series: [{
            name: 'Bitcoin ' + currencyVariable + ' price',
            type: 'line',
            data: data
        }]
    });
});
