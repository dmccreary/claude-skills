/**
 * Sine Function Visualization - Interactive Plotly.js Plot
 */

// Configuration
const config = {
    xMin: -6.28,  // Approximately -2π
    xMax: 6.28,   // Approximately 2π
    yMin: -1.5,
    yMax: 1.5,
    numPoints: 500,
    initialX: 0
};

// Mathematical function
function f(x) {
    return Math.sin(x);
}

// Generate data points for the function
function generateFunctionData() {
    const xValues = [];
    const yValues = [];
    const step = (config.xMax - config.xMin) / config.numPoints;

    for (let i = 0; i <= config.numPoints; i++) {
        const x = config.xMin + i * step;
        const y = f(x);
        xValues.push(x);
        yValues.push(y);
    }

    return { x: xValues, y: yValues };
}

// Create the plot
function createPlot(pointX) {
    const functionData = generateFunctionData();
    const pointY = f(pointX);

    // Function curve trace
    const curveTrace = {
        x: functionData.x,
        y: functionData.y,
        type: 'scatter',
        mode: 'lines',
        name: 'y = sin(x)',
        line: {
            color: '#007bff',
            width: 2
        },
        hovertemplate: '<b>x:</b> %{x:.3f}<br><b>y:</b> %{y:.3f}<extra></extra>'
    };

    // Interactive point trace
    const pointTrace = {
        x: [pointX],
        y: [pointY],
        type: 'scatter',
        mode: 'markers',
        name: 'Point',
        marker: {
            color: '#dc3545',
            size: 10,
            symbol: 'circle'
        },
        hovertemplate: '<b>Point</b><br>x: %{x:.3f}<br>y: %{y:.3f}<extra></extra>'
    };

    const data = [curveTrace, pointTrace];

    // Layout configuration
    const layout = {
        title: false,
        xaxis: {
            title: {
                text: 'x (radians)',
                font: { size: 14 }
            },
            range: [config.xMin, config.xMax],
            showgrid: true,
            gridcolor: '#e0e0e0',
            zeroline: true,
            zerolinecolor: '#333',
            zerolinewidth: 1
        },
        yaxis: {
            title: {
                text: 'y = sin(x)',
                font: { size: 14 }
            },
            range: [config.yMin, config.yMax],
            showgrid: true,
            gridcolor: '#e0e0e0',
            zeroline: true,
            zerolinecolor: '#333',
            zerolinewidth: 1
        },
        margin: {
            l: 50,
            r: 20,
            t: 10,
            b: 50
        },
        paper_bgcolor: 'white',
        plot_bgcolor: 'white',
        hovermode: 'closest',
        showlegend: true,
        legend: {
            x: 0.02,
            y: 0.98,
            bgcolor: 'rgba(255,255,255,0.8)',
            bordercolor: '#ccc',
            borderwidth: 1
        }
    };

    // Plotly configuration
    const plotConfig = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['lasso2d', 'select2d'],
        toImageButtonOptions: {
            format: 'png',
            filename: 'sine-function',
            height: 600,
            width: 800
        }
    };

    Plotly.newPlot('plot', data, layout, plotConfig);
}

// Update point position
function updatePoint(x) {
    const y = f(x);

    Plotly.restyle('plot', {
        x: [[x]],
        y: [[y]]
    }, [1]);  // Update trace index 1 (point trace)

    // Update slider display
    document.getElementById('x-value').textContent = x.toFixed(3);
}

// Initialize plot
createPlot(config.initialX);

// Slider event listener
document.getElementById('x-slider').addEventListener('input', function(e) {
    const x = parseFloat(e.target.value);
    updatePoint(x);
});

// Window resize handler for responsiveness
window.addEventListener('resize', function() {
    Plotly.Plots.resize('plot');
});
