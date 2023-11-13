// dashboard.js

document.addEventListener("DOMContentLoaded", function() {
    var ongoingCount = parseInt('{{ subject.evaluation_set.all.count }}');
    var ongoingCountbydate = parseInt('{{ subject.evaluation_set.all.count|date: }}');


    // Assuming you have a variable 'evaluationsData' containing the data
    // Replace this with the actual data you want to display
    var evaluation = [
        // Example data: ['2023-11-11', 5], ['2023-11-12', 8], ...
        // why is the an error below?
        // recreate a the for loop 
        {% for evaluation in evaluations %}
            ['{{ evaluation.timestamp|date:"Y-m-d" }}', 1],
        {% endfor %}
    ];

    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: evaluationsData.map(item => item[0]),
            datasets: [{
                label: 'Number of Evaluations',
                data: evaluationsData.map(item => item[1]),
                backgroundColor: 'rgba(75, 192, 192, 0.2)', // Change the color as needed
                borderColor: 'rgba(75, 192, 192, 1)',     // Change the color as needed
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Evaluations'
                    }
                }
            }
        }
    });
});



