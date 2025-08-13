   // Treasury Chart dashboard js
   const treasuryCtx = document.getElementById('treasuryChart').getContext('2d');
   new Chart(treasuryCtx, {
       type: 'line',
       data: {
           labels: ['1 Nov', '5 Nov', '10 Nov', '15 Nov', '20 Nov', '25 Nov', '30 Nov', '5 Déc', '10 Déc', '15 Déc'],
           datasets: [{
               label: 'Trésorerie (€)',
               data: [420000, 435000, 428000, 445000, 460000, 455000, 475000, 480000, 472000, 485750],
               borderColor: '#007bff',
               backgroundColor: 'rgba(0, 123, 255, 0.1)',
               fill: true,
               tension: 0.4
           }]
       },
       options: {
           responsive: true,
           maintainAspectRatio: false,
           plugins: {
               legend: {
                   display: false
               }
           },
           scales: {
               y: {
                   beginAtZero: false,
                   ticks: {
                       callback: function(value) {
                           return '€ ' + value.toLocaleString();
                       }
                   }
               }
           }
       }
   });

   // Expense Chart
   const expenseCtx = document.getElementById('expenseChart').getContext('2d');
   new Chart(expenseCtx, {
       type: 'doughnut',
       data: {
           labels: ['Salaires', 'Achats/Approvisionnement', 'Charges de personnel', 'Impots/taxes', 'Frais financiers','Frais transport/deplacement','Frais generaux','Assurance'],
           datasets: [{
               data: [35, 15, 11, 37, 5,10,20,10],
               backgroundColor: ['#007bff', '#28a745', '#ffc107', '#dc3545', '#6f42c1','#7226FF','#6700A3','#00033D']
           }]
       },
       options: {
           responsive: true,
           maintainAspectRatio: false,
           plugins: {
               legend: {
                   position: 'bottom'
               }
           }
       }
   });
   //previsions script
    // Forecast Chart
    const forecastCtx = document.getElementById('forecastChart').getContext('2d');
    new Chart(forecastCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun'],
            datasets: [{
                label: 'Optimiste',
                data: [485750, 520000, 550000, 580000, 620000, 650000],
                borderColor: '#28a745',
                backgroundColor: 'rgba(40, 167, 69, 0.1)',
                fill: false,
                tension: 0.4
            }, {
                label: 'Réaliste',
                data: [485750, 495000, 505000, 510000, 515000, 520000],
                borderColor: '#007bff',
                backgroundColor: 'rgba(0, 123, 255, 0.1)',
                fill: false,
                tension: 0.4
            }, {
                label: 'Pessimiste',
                data: [485750, 470000, 450000, 430000, 400000, 380000],
                borderColor: '#ffc107',
                backgroundColor: 'rgba(255, 193, 7, 0.1)',
                fill: false,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: false,
                    ticks: {
                        callback: function(value) {
                            return '€ ' + value.toLocaleString();
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top'
                }
            }
        }
    });
