const chart = new Chart("chart2", {
  type: "line",
  data: {
    datasets: [{
        borderColor: "#007cfb",
        backgroundColor: "#e3c04d",
      }
    ]
  },
  options: {
    plugins: {
      legend: {display: false},
      tooltip: {enabled: false},
    },
    scales: {
      x: {display: false},
      y: {display: false}
    },
  }
})

function updateChart(xValues, yValues) {
  chart.data.labels = xValues
  chart.data.datasets[0].data = yValues
  chart.update()
}
