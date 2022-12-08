// doc: https://www.chartjs.org/docs/2.9.4/configuration/title.html
// color pick : https://www.rapidtables.com/web/color/RGB_Color.html

function createPie(id, title, labels, data) {
    // data points Max 10 for Pie
    if (labels.length > 10) {
        labels = labels.slice(0, 10);
        data = data.slice(0, 10);
    }

    // Global Setting
    Chart.defaults.global.defaultFontFamily = "sans-serif";
    Chart.defaults.global.defaultFontSize = 12;
    Chart.defaults.global.defaultFontColor = "#D8D4D4";
    Chart.defaults.global.legend.position = "bottom";

    // Get by ID
    var canvas = document.getElementById(id);
    
    // Color gradient
    // var ctx = document.getElementById(id).getContext("2d");
    // const width = canvas.width;
    // const height = canvas.height;
    // const centerX = width/2;
    // const centerY = height/2;
    // const r = Math.min(
    //     (width - 0) / 2,
    //     (height - 0) / 2
    //   );
    // gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 200);
    // gradient.addColorStop(0, "rgba(145,196,242,0.8)");
    // gradient.addColorStop(0.7, "rgba(86,71,135, 0.8)");
    // gradient.addColorStop(1, "rgba(16,25,53,0.8)");

    gradient = [
        "rgba(102,0,51,0.6)",
        "rgba(102,51,0,0.6)",
        "rgba(102,102,0,0.6)",
        "rgba(51,102,0,0.6)",
        "rgba(0,102,0,0.6)",
        "rgba(0,102,102,0.6)",
        "rgba(0,51,102,0.6)",
        "rgba(0,0,102,0.6)",
        "rgba(51,0,102,0.6)",
        "rgba(102,0,102,0.6)",
    ]

    // Data mapping
    var pieData = {
        labels: labels, // array
        datasets: [
            {
                data: data, // array
                backgroundColor: gradient,
                borderWidth: 1
            }]
    };

    // Chart Config
    var pieChart = new Chart(canvas, {
    type: 'doughnut',
    data: pieData,
    options: {
        title: {
            display: true,
            text: title,
            fontColor: 'rgba(255,255,255, 0.8)',
            fontFamily: "Garamond, serif",
            fontSize: 30,
        },
        maintainAspectRatio: false
    }
    });
}

function createHist(id, title, labels, data) {
        // data points Max 10 for Pie
        if (labels.length > 10) {
            labels = labels.slice(0, 10);
            data = data.slice(0, 10);
        }
        console.log(labels);
        console.log(data);
        // Global Setting
        Chart.defaults.global.defaultFontFamily = "sans-serif";
        Chart.defaults.global.defaultFontSize = 12;
        Chart.defaults.global.defaultFontColor = "#D8D4D4";
        Chart.defaults.global.legend.position = "bottom";
    
        // Get by ID
        var canvas = document.getElementById(id);
        
        // Color gradient
        var ctx = document.getElementById(id).getContext("2d");
        console.log(canvas)
        var gradient = ctx.createLinearGradient(0, 0, 400, 0); // x1, y1, x2, y2
        gradient.addColorStop(0, 'rgba(102,0,204,0.8)');   
        gradient.addColorStop(1, 'rgba(204,102,0,0.8)');
    
        // Data mapping
        var barData = {
            labels: labels, // array
            datasets: [
                {
                    label: 'Amount by Category',
                    data: data, // array
                    backgroundColor: gradient,
                    borderWidth: 1
                }]
        };
    
        // Chart Config
        var barChart = new Chart(canvas, {
        type: 'bar',
        data: barData,
        options: {
            title: {
                display: true,
                text: title,
                fontColor: 'rgba(255,255,255, 0.8)',
                fontFamily: "Garamond, serif",
                fontSize: 30,
            },
            indexAxis: 'y',
            skipNull: true,
            maintainAspectRatio: false
        }
        });
}