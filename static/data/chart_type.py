# Reference: https://quickchart.io/gallery/

CHART_TYPES = """BAR, MULTIPLE_BAR, STACKED_BAR, LINE, MULTIPLE_BAR, RADAR, PIE, DOUGHNUT, SCATTER, BUBBLE, NONE"""

# single bar chart
BAR = """{
  type: 'bar',
  data: {
    labels: FAKE,
    datasets: [
      {
        label: FAKE,
        data: FAKE,
      },
    ]
  }
}"""

# multiple bar chart
MULTIPLE_BAR = """{
  type: 'bar',
  data: {
    labels: FAKE,
    datasets: [{
      label: FAKE,
      data: FAKE,
    }, {
      label: FAKE,
      data: FAKE,
    }]
  }
}"""

# stacked bar chart
STACKED_BAR = """{
  type: 'bar',
  data: {
    labels: FAKE,
    datasets: [
      {
        label: FAKE,
        backgroundColor: FAKE,
        data: FAKE,
      },
      {
        label: FAKE,
        backgroundColor: FAKE,
        data: FAKE,
      },
      {
        label: FAKE,
        backgroundColor: FAKE,
        data: FAKE,
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: FAKE,
    },
    scales: {
      xAxes: [
        {
          stacked: true,
        },
      ],
      yAxes: [
        {
          stacked: true,
        },
      ],
    },
  },
}"""

# line chart
LINE = """{
  type: 'line',
  data: {
    labels: FAKE,
    datasets: [
      {
        label: FAKE,
        backgroundColor: FAKE,
        borderColor: FAKE,
        data: FAKE,
        fill: false,
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: FAKE,
    },
  },
}"""

# multiple line chart
MULTIPLE_LINE = """{
  type: 'line',
  data: {
    labels: FAKE,
    datasets: [
      {
        label: FAKE,
        backgroundColor: FAKE,
        borderColor: FAKE,
        data: FAKE,
        fill: false,
      },
      {
        label: FAKE,
        fill: false,
        backgroundColor: FAKE,
        borderColor: FAKE,
        data: FAKE,
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: FAKE,
    },
  },
}"""

# radar chart
RADAR = """{
  type: 'radar',
  data: {
    labels: FAKE,
    datasets: [
      {
        label: FAKE,
        backgroundColor: FAKE,
        borderColor: FAKE,
        pointBackgroundColor: FAKE,
        data: FAKE,
      },
      {
        label: FAKE,
        backgroundColor: FAKE,
        borderColor: FAKE,
        pointBackgroundColor: FAKE,
        data: FAKE,
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: FAKE,
    },
  },
}"""

# pie chart
PIE = """{
  type: 'pie',
  data: {
    datasets: [
      {
        data: FAKE,
        backgroundColor: [
          FAKE
        ],
        label: FAKE,
      },
    ],
    labels: FAKE,
  },
}"""

# doughnut chart
DOUGHNUT = """{
  type: 'doughnut',
  data: {
    datasets: [
      {
        data: FAKE,
        backgroundColor: FAKE,
        label: FAKE,
      },
    ],
    labels: FAKE,
  },
  options: {
    title: {
      display: true,
      text: FAKE,
    },
  },
}"""

# scatter chart
SCATTER = """{
  "type": "scatter",
  "data": {
    "datasets": [
      {
        "label": FAKE,
        "borderColor": FAKE,
        "backgroundColor": FAKE,
        "data": {
          "x": FAKE,
          "y": FAKE
        }
      },
      {
        "label": FAKE,
        "borderColor": FAKE,
        "backgroundColor": FAKE,
        "data": {
          "x": FAKE,
          "y": FAKE
        }
      }
    ]
  },
  "options": {
    "title": {
      "display": true,
      "text": FAKE
    }
  }
}"""

# bubble chart
BUBBLE = """{
  type: 'bubble',
  data: {
    datasets: [
      {
        label: FAKE,
        backgroundColor: FAKE,
        borderColor: FAKE,
        borderWidth: 1,
        data: [
          {
            x: FAKE,
            y: FAKE,
            r: FAKE,
          },
        ],
      },
      {
        label: FAKE,
        backgroundColor: FAKE,
        borderColor: FAKE,
        borderWidth: 1,
        data: [
          {
            x: FAKE,
            y: FAKE,
            r: FAKE,
          },
        ],
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: FAKE,
    },
  },
}"""


CHART_DICT = {
    "BAR": BAR,
    "MULTIPLE_BAR": MULTIPLE_BAR,
    "STACKED_BAR": STACKED_BAR,
    "LINE": LINE,
    "MULTIPLE_BAR": MULTIPLE_BAR,
    "RADAR": RADAR,
    "PIE": PIE,
    "DOUGHNUT": DOUGHNUT,
    "SCATTER": SCATTER,
    "BUBBLE": BUBBLE,
    "NONE": "none",
}
