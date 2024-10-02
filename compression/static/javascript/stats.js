function newChart(original, runLength, lyndon, burrows, final) {
  const xValues = [
    "Original File",
    "Run Lengh Encoded",
    "Lyndon Factorisation",
    "Burrows-Wheeler Transform",
    "All",
  ];
  const yValues = [original, runLength, lyndon, burrows, final];
  const barColors = ["red", "green", "blue", "orange", "brown"];
  new Chart("myChart", {
    type: "bar",
    data: {
      labels: xValues,
      datasets: [
        {
          backgroundColor: barColors,
          data: yValues,
        },
      ],
      backgroundColor: [
        "rgba(255, 0, 0, 0.5)",
        "rgba(0, 255, 0, 0.5)",
        "rgba(0, 0, 255, 0.5)",
      ],
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: "File sizes using different compression tools ",
      },
    },
  });
}

function relocate() {
  window.location.href = "/";
}
