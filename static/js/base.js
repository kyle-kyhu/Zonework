
// connect to the dashboardView class in the views.py file
var dashboardView = new DashboardView();


// get the dat for the chart from the server
var chartData = dashboardView.getChartData();

// create a chart using chart.js
var ctx = document.getElementById("evaluationsChart").getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: chartData.labels,
        datasets: [{
            label: 'Evaluations',
            data: chartData.data,
            backgroundColor: chartData.colors,
            borderColor: chartData.colors,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMin: 0,
                    suggestedMax: 10
                }
            }]
        }
    }
})