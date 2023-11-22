

const data = {
  labels: [
    '代码能力',
    '数学能力',
    '创造力',
    '逻辑力',
    '语言能力',
    '文档书写能力',
    '决策能力'
  ],
  datasets: [{
    label: '前端开发能力',
    data: [70, 40, 80, 65, 65, 70, 55],
    fill: true,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgb(255, 99, 132)',
    pointBackgroundColor: 'rgb(255, 99, 132)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(255, 99, 132)'
  }, {
    label: '后端开发能力',
    data: [83, 48, 28, 80, 55, 65, 60],
    fill: true,
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgb(54, 162, 235)',
    pointBackgroundColor: 'rgb(54, 162, 235)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(54, 162, 235)'
  },
  {
    label: '数据分析能力',
    data: [82, 68, 50, 61, 55, 75, 72],
    fill: true,
    backgroundColor: 'rgba(255, 220, 0, 0.2)',
    borderColor: 'rgb(255, 255, 0)',
    pointBackgroundColor: 'rgb(255, 255, 0)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgb(255, 255, 0)'
  }]
};

document.addEventListener('DOMContentLoaded', function() {

    const ctx = document.getElementById('radarChart').getContext('2d');

    new Chart(ctx, {
    type: 'radar',
    data: data,
    options: {
        elements: {
        line: {
            borderWidth: 3
                }
        }
    }
    });


});

