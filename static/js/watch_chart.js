$( document ).ready(function() {

    var populationChart = $("#watch_chart");

        $.ajax({
        url: populationChart.data("url"),
        success: function (data) {

            var ctx = populationChart[0].getContext("2d");

            new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                label: 'Buy index',
                backgroundColor: 'blue',
                data: data.data
                }]          
            },

            options: {
                indexAxis: 'y',
                // Elements options apply to all of the options unless overridden in a dataset
                // In this case, we are setting the border of each horizontal bar to be 2px wide
                elements: {
                  bar: {
                    borderWidth: 2,
                  }
                },
                responsive: true,
                plugins: {
                  legend: {
                    position: 'bottom',
                  },
                  title: {
                    display: true,
                    text: 'Recommend Buy Index'
                  }
                }
              },


            });

        }
        });

});