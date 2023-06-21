// wheelchart.js
Highcharts.chart('container-wheel', {
    chart: {
        type: 'dependencywheel'
    },
    title: {
        text: 'Bitcoin Price Tracking Application'
    },
    series: [{
        name: 'Bitcoin Price Tracking Application',
        keys: ['from', 'to', 'weight', 'color'],
        data: [
            ['Data Streaming Client', 'Database', 8, '#7cb5ec'],
            ['Web Service', 'Database', 10, '#434348'],
            ['Web Service', 'Highcharts API', 6, '#90ed7d'],
            ['Highcharts API', 'Database', 4, '#f7a35c']
        ],
        dataLabels: {
            color: '#333',
            textPath: {
                enabled: true,
                attributes: {
                    dy: 5
                }
            },
            distance: 10,
            format: '{point.name}',
            style: {
                fontWeight: 'bold',
                textOutline: false
            }
        },
        size: '95%',
        innerSize: '20%',
        colorByPoint: true,
        colors: ['#7cb5ec', '#434348', '#90ed7d', '#f7a35c'],
        borderColor: '#ffffff',
        borderWidth: 2,
        nullColor: '#eaeaea',
        tooltip: {
            pointFormat: '{point.fromNode.name} ➡ {point.toNode.name}: <b>{point.weight}</b> units'
        },
        events: {
            click: function (event) {
                console.log(event.point.name + ' clicked');
            }
        }
    }],
    credits: {
        enabled: false
    },
    legend: {
        enabled: true,
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle',
        labelFormatter: function () {
            return this.name + ': ' + this.userOptions.data.length;
        }
    },
    exporting: {
        enabled: true,
        buttons: {
            contextButton: {
                menuItems: [
                    'printChart',
                    'separator',
                    'downloadPNG',
                    'downloadJPEG',
                    'downloadPDF',
                    'downloadSVG'
                ]
            }
        }
    }
});
