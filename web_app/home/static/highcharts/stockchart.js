// stockchart.js
document.addEventListener("DOMContentLoaded", function () {
    // Make an AJAX request to fetch the data
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                createChart(data);
            } else {
                console.error("Failed to fetch data: " + xhr.status);
            }
        }
    };

    // Define the URL for retrieving the data
    var url = dataRoute + "?currency=" + currencyVariable + "&timerange=48h";

    // Send the AJAX request
    xhr.open("GET", url, true);
    xhr.send();
});

function createChart(data) {
    // Calculate the average value
    var halfData = data.slice(0, Math.floor(data.length / 2));
    var average = halfData.reduce(function (sum, value) {
        return sum + value[1];
    }, 0) / halfData.length;

    // Create the chart using the fetched data
    Highcharts.stockChart('container-stock', {
        navigator: {
            enabled: true,
            series: {
                name: "Bitcoin " + currencyVariable + " price"
            }
        },
        rangeSelector: {
            buttons: [{
                type: 'minute',
                count: 30,
                text: '30m'
            },
            {
                type: 'hour',
                count: 1,
                text: '1h'
            },
            {
                type: 'hour',
                count: 4,
                text: '4h'
            },
            {
                type: 'day',
                count: 1,
                text: '1d'
            },
            {
                type: 'all',
                text: 'All'
            }],
            selected: 3
        },
        title: {
            text: 'Bitcoin ' + currencyVariable + ' price'
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            opposite: false,
            labels: {
                formatter: function () {
                    return Highcharts.numberFormat(this.value, 0, '.', ',');
                }
            }
        },
        tooltip: {
            formatter: function () {
                return Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + ' UTC' + '<br>' +
                    '<span style="font-weight:bold; font-size:14px;">' + Highcharts.numberFormat(this.y, 2, '.', ',') + '</span>';
            }
        },
        plotOptions: {
            series: {
                threshold: average,
                lineWidth: 3,
                color: 'green',
                negativeColor: 'red',
                dataLabels: {
                    enabled: true,
                    crop: false,
                    overflow: 'none',
                    formatter: function () {
                        if (this.point.x === this.series.xData[this.series.xData.length - 1]) {
                            return Highcharts.numberFormat(this.y, 2, '.', ',');
                        } else {
                            return null;
                        }
                    },
                    align: 'right',
                    verticalAlign: 'bottom',
                    x: 0,
                    y: 0,
                    style: {
                        color: 'black',
                        fontSize: '12px',
                        fontWeight: 'bold'
                    }
                }
            },
            line: {
                lineWidth: 1.5
            }
        },
        series: [{
            name: '',
            type: 'line',
            data: data
        }]
    });
}
