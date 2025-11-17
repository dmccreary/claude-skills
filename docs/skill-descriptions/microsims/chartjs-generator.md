# Chart Generator Using ChartJS

## Overview

The **Chart.js Generator** skill creates professional, interactive data visualizations using the Chart.js library, supporting all eight major chart types (line, bar, pie, doughnut, radar, polar area, bubble, scatter). This skill generates complete MicroSim packages with HTML, CSS, and documentation, optimized for embedding in educational content, reports, and dashboards built with MkDocs Material theme.

Chart.js is a powerful, flexible JavaScript library known for its responsive design, smooth animations, and extensive customization options.

## When to Use This Skill

Use the Chart.js Generator skill when you need to create:

- **Statistical Visualizations** - Display data trends, comparisons, and distributions
- **Educational Charts** - Illustrate concepts with clear, interactive visualizations
- **Dashboard Components** - Create individual charts for data monitoring
- **Report Graphics** - Generate publication-ready charts for documents
- **Interactive Data Exploration** - Allow users to interact with data through tooltips and legends
- **Comparative Analysis** - Show relationships between multiple datasets
- **Time Series Data** - Visualize trends over time periods
- **Proportional Relationships** - Display part-to-whole relationships

## Supported Chart Types

The skill supports all eight Chart.js chart types:

### 1. Line Charts
**Best for**: Time series, trends, continuous data

**Use cases**:
- Stock prices over time
- Temperature trends
- Student progress tracking
- Sales growth patterns
- Population changes

**Variations**: Multi-line, filled areas, stepped lines, smooth curves

### 2. Bar Charts
**Best for**: Comparisons, categorical data

**Use cases**:
- Sales by region
- Test scores by subject
- Product comparisons
- Survey results
- Resource allocation

**Variations**: Vertical, horizontal, stacked, grouped

### 3. Pie Charts
**Best for**: Proportions, percentages (≤6 categories)

**Use cases**:
- Market share distribution
- Budget allocation
- Survey response percentages
- Time allocation (daily activities)
- Demographic breakdowns

**Limitations**: Not suitable for precise comparisons or many categories

### 4. Doughnut Charts
**Best for**: Proportions with central space for labels

**Use cases**:
- Same as pie charts, but with space for total/summary in center
- Progress indicators (percentage complete)
- Resource utilization

**Advantages**: More modern appearance, space for additional information

### 5. Radar Charts
**Best for**: Multi-dimensional data, comparing profiles

**Use cases**:
- Skill assessments (spider charts)
- Product feature comparisons
- Student competency profiles
- Performance evaluations across metrics
- Sports player statistics

**Ideal for**: 3-8 variables, multiple entities compared

### 6. Polar Area Charts
**Best for**: Proportions with emphasis on differences

**Use cases**:
- Similar to pie charts but emphasizing magnitude
- Seasonal patterns (circular time periods)
- Directional data with magnitude

**Difference from pie**: Segments have equal angles, varying radius

### 7. Bubble Charts
**Best for**: Three-dimensional data (x, y, size)

**Use cases**:
- Impact vs Effort matrices (with bubble size = priority)
- Risk assessment (probability, impact, exposure)
- Portfolio analysis (return, risk, investment size)
- Geographic data (latitude, longitude, population)
- Multi-variate correlations

**Data structure**: Each point has x, y, and radius (r) values

### 8. Scatter Charts
**Best for**: Correlations, distributions, relationships

**Use cases**:
- Correlation analysis (height vs weight)
- Regression analysis
- Outlier detection
- Clustering visualization
- Scientific data plotting

**Ideal for**: Showing relationships between two continuous variables

## Key Features

### Interactive Elements

- **Hover Tooltips** - Display detailed data on mouseover
- **Clickable Legends** - Show/hide datasets by clicking legend items
- **Smooth Animations** - Professional animations on load and data updates
- **Zoom and Pan** - Optional plugins for data exploration
- **Click Events** - Custom interactions with chart elements

### Visual Design

- **Responsive Layout** - Automatically adapts to container size
- **Customizable Colors** - Flexible color schemes for branding/accessibility
- **Grid Lines and Axes** - Clear visual guides for reading values
- **Professional Styling** - Modern, clean aesthetics
- **Print-Friendly** - CSS optimized for printing

### Data Handling

- **Multiple Datasets** - Display multiple series on one chart
- **Dynamic Updates** - Update chart data programmatically
- **Mixed Chart Types** - Combine different chart types (line + bar)
- **Data Labels** - Optional plugin for value labels on elements
- **Custom Formatting** - Format numbers, dates, percentages

### Accessibility

- **Color Contrast** - WCAG-compliant color schemes
- **Semantic HTML** - Proper structure for screen readers
- **Keyboard Navigation** - Accessible controls
- **Alternative Text** - Descriptive documentation
- **Colorblind-Safe Palettes** - Distinguishable without color

## How It Works

### Workflow

The skill follows an 8-step process:

1. **Determine Chart Type** - Select from 8 supported types based on data and purpose
2. **Gather Data and Requirements** - Collect data structure, labels, configuration preferences
3. **Create Directory Structure** - Set up `docs/sims/[chart-name]/` following MicroSim pattern
4. **Create main.html** - Generate HTML with Chart.js CDN and configuration
5. **Create style.css** - Apply responsive styling and visual design
6. **Create index.md** - Generate documentation with iframe embed and customization guide
7. **Integrate into Navigation** - Add entry to `mkdocs.yml` (if applicable)
8. **Test and Validate** - Verify visual display, interactivity, and documentation

### User Interaction

The skill prompts users for:

- **Chart type** - If not specified, offers options with best-use descriptions
- **Data structure** - Values, labels, categories, time periods, units
- **Chart configuration** - Title, axis labels, legend preferences, color scheme
- **Context** - Purpose (educational, analytical, reporting), integration location
- **Special features** - Stacked, grouped, filled areas, custom formatting

## Example Use Cases

### 1. Student Performance Tracking (Line Chart)

**Scenario**: A teacher needs to visualize student test scores across a semester.

**Output**:
- Multi-line chart with one line per student
- X-axis: Test dates (Sept, Oct, Nov, Dec)
- Y-axis: Scores (0-100)
- Interactive tooltips showing exact scores
- Legend for toggling individual students
- Educational metadata: Bloom's level = "Analyze", concepts = ["Academic Progress", "Data Interpretation"]

### 2. Budget Allocation (Pie Chart)

**Scenario**: A nonprofit organization needs to show how donations are spent.

**Output**:
- Pie chart with 5 slices (Programs, Administration, Fundraising, Marketing, Reserves)
- Color-coded segments with percentages
- Central total amount (for doughnut variant)
- Hover tooltips with dollar amounts
- Print-friendly styling for annual reports

### 3. Product Feature Comparison (Radar Chart)

**Scenario**: Compare three smartphones across multiple features.

**Output**:
- Radar chart with 6 axes (Battery Life, Camera Quality, Performance, Screen Size, Price, Design)
- Three overlapping datasets (iPhone, Samsung, Google)
- 0-10 scale for each feature
- Color-coded areas with transparency
- Educational use: Teaching multi-dimensional comparison

### 4. Regional Sales Analysis (Bar Chart)

**Scenario**: Display quarterly sales for different regions.

**Output**:
- Grouped bar chart (Q1, Q2, Q3, Q4 per region)
- X-axis: Regions (North, South, East, West)
- Y-axis: Sales revenue ($)
- Color-coded by quarter
- Stacked variant option to show total
- Horizontal orientation option for many regions

### 5. Risk Assessment Matrix (Bubble Chart)

**Scenario**: Visualize project risks by likelihood and impact.

**Output**:
- Bubble chart with quadrants
- X-axis: Likelihood (0-10)
- Y-axis: Impact (0-10)
- Bubble size: Risk exposure (severity × likelihood)
- Color-coded by risk category (Technical, Financial, Operational)
- Quadrant backgrounds (low/medium/high zones)

### 6. Correlation Study (Scatter Chart)

**Scenario**: Analyze relationship between study hours and test scores.

**Output**:
- Scatter plot with one point per student
- X-axis: Study hours per week
- Y-axis: Final exam score
- Optional trend line (requires plugin)
- Color-coded by grade level
- Educational metadata: Bloom's level = "Analyze", concepts = ["Correlation", "Statistical Analysis"]

## Technical Details

### Technology Stack

- **Library**: Chart.js 4.4.0 (latest stable)
- **CDN**: jsdelivr.net (fast, reliable delivery)
- **Format**: HTML5, CSS3, JavaScript (ES6+)
- **Dependencies**: Chart.js core (required), optional plugins (data labels, zoom)
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

### File Structure

Each generated chart creates:

```
docs/sims/[chart-name]/
├── main.html           # Standalone HTML page with chart
├── style.css           # Responsive styling
└── index.md            # Documentation with iframe embed
```

### Chart.js Configuration Structure

All charts follow this basic structure:

```javascript
const config = {
    type: 'line',  // bar, pie, doughnut, radar, polarArea, bubble, scatter
    data: {
        labels: ['Jan', 'Feb', 'Mar'],
        datasets: [{
            label: 'Dataset 1',
            data: [12, 19, 3],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgb(75, 192, 192)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Chart Title' },
            legend: { position: 'top' },
            tooltip: { enabled: true }
        },
        scales: {  // For charts with axes (line, bar, scatter, bubble)
            y: { beginAtZero: true }
        }
    }
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
);
```

### Iframe Embedding

Charts are embedded in MkDocs pages using:

```markdown
<iframe src="main.html" width="100%" height="700" frameborder="0"></iframe>

[View Fullscreen](main.html){:target="_blank"}
```

**Typical heights by chart type**:
- Line/Bar: 500-700px
- Pie/Doughnut: 500-600px
- Radar/Polar: 600-700px
- Bubble/Scatter: 700-800px

## Customization Options

### Data Modification

**Changing values**:
```javascript
// In main.html, find the data object
data: {
    labels: ['New', 'Labels', 'Here'],
    datasets: [{
        data: [10, 20, 30, 40]  // Update these values
    }]
}
```

**Adding datasets** (for multi-series charts):
```javascript
datasets: [
    { label: 'Series 1', data: [...], borderColor: 'red' },
    { label: 'Series 2', data: [...], borderColor: 'blue' },
    { label: 'Series 3', data: [...], borderColor: 'green' }
]
```

### Color Customization

**Single color**:
```javascript
backgroundColor: 'rgba(255, 99, 132, 0.8)'
```

**Multiple colors** (for pie, doughnut, bar):
```javascript
backgroundColor: [
    'rgba(255, 99, 132, 0.8)',   // Red
    'rgba(54, 162, 235, 0.8)',   // Blue
    'rgba(255, 206, 86, 0.8)',   // Yellow
    'rgba(75, 192, 192, 0.8)',   // Green
    'rgba(153, 102, 255, 0.8)',  // Purple
    'rgba(255, 159, 64, 0.8)'    // Orange
]
```

**Gradient backgrounds** (advanced):
```javascript
const ctx = document.getElementById('myChart').getContext('2d');
const gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, 'rgba(75, 192, 192, 0.8)');
gradient.addColorStop(1, 'rgba(75, 192, 192, 0.1)');
backgroundColor: gradient
```

### Chart Options

**Aspect ratio**:
```javascript
options: {
    aspectRatio: 2  // Width:height ratio (2:1)
}
```

**Axis configuration**:
```javascript
scales: {
    x: {
        title: { display: true, text: 'Time Period' },
        grid: { display: false }
    },
    y: {
        title: { display: true, text: 'Values' },
        beginAtZero: true,
        max: 100
    }
}
```

**Legend customization**:
```javascript
plugins: {
    legend: {
        position: 'bottom',  // top, left, right, bottom
        labels: {
            color: '#333',
            font: { size: 14 }
        }
    }
}
```

**Tooltip customization**:
```javascript
plugins: {
    tooltip: {
        callbacks: {
            label: function(context) {
                return context.dataset.label + ': $' + context.parsed.y.toFixed(2);
            }
        }
    }
}
```

### Animations

**Custom duration and easing**:
```javascript
options: {
    animation: {
        duration: 2000,  // milliseconds
        easing: 'easeInOutQuart'  // easing function
    }
}
```

**Disable animations** (for performance):
```javascript
options: {
    animation: false
}
```

## Educational Framework Integration

### Bloom's Taxonomy Alignment

Charts support multiple cognitive levels:

- **Remember** - Identify data points and labels
- **Understand** - Interpret trends and relationships shown in charts
- **Apply** - Use charts to make predictions or decisions
- **Analyze** - Compare datasets, identify patterns, detect outliers
- **Evaluate** - Assess data quality, validity of conclusions
- **Create** - Design custom visualizations for specific purposes

### Learning Objectives

Generated charts include explicit learning objectives such as:

- "Interpret line charts to identify trends over time"
- "Compare categorical data using bar charts"
- "Understand proportional relationships through pie charts"
- "Analyze multi-dimensional data using radar charts"
- "Identify correlations using scatter plots"

### ISO 11179 Metadata

Chart metadata follows ISO 11179 standards:

- **Precise** - Exact data sources and units clearly documented
- **Concise** - Focused descriptions of chart purpose
- **Distinct** - Clear differentiation between chart types
- **Non-circular** - Independent definitions
- **Free of business rules** - Focus on educational value

## Best Practices

### Chart Type Selection

1. **Match chart to data type**:
   - Continuous → Line, Area, Scatter
   - Categorical → Bar, Column
   - Proportional → Pie, Doughnut
   - Multi-dimensional → Radar, Bubble

2. **Consider audience**:
   - General public → Simple charts (line, bar, pie)
   - Technical audience → Advanced charts (radar, bubble, scatter)
   - Students → Interactive, educational charts with clear labels

3. **Limit complexity**:
   - Maximum 6 slices for pie charts
   - Maximum 4-5 datasets for line charts
   - Maximum 8 variables for radar charts

### Data Preparation

1. **Clean data** - Remove duplicates, handle missing values
2. **Consistent formatting** - Use same units and scales
3. **Meaningful labels** - Clear, descriptive category names
4. **Appropriate scale** - Start axes at zero (unless good reason not to)
5. **Sort data** - Logical ordering (chronological, alphabetical, by value)

### Visual Design

1. **Color accessibility** - Use colorblind-safe palettes
2. **Contrast** - Ensure WCAG AA compliance (4.5:1 minimum)
3. **Font size** - Minimum 12px for labels, 14px for titles
4. **Grid lines** - Subtle, not distracting
5. **White space** - Adequate padding around chart elements

### Documentation

1. **Clear explanations** - Explain what the chart shows
2. **Code examples** - Provide exact, working code snippets
3. **Customization guide** - Step-by-step modification instructions
4. **Interpretation help** - Guide users on reading the chart
5. **Data sources** - Credit data sources appropriately

## Troubleshooting

### Chart Not Displaying

**Symptoms**: Blank canvas or error in console

**Solutions**:
- Verify Chart.js CDN is loading correctly
- Check canvas element has correct ID
- Ensure JavaScript runs after DOM loads
- Validate data structure (no null/undefined values)
- Check browser console for errors

### Data Not Updating

**Symptoms**: Chart doesn't reflect new data

**Solutions**:
```javascript
// Update data
chart.data.datasets[0].data = newData;
chart.data.labels = newLabels;

// Must call update
chart.update();
```

### Labels Overlapping

**Symptoms**: X-axis labels overlap and are unreadable

**Solutions**:
```javascript
scales: {
    x: {
        ticks: {
            maxRotation: 45,  // Rotate labels
            minRotation: 45,
            autoSkip: true,   // Skip some labels
            maxTicksLimit: 10 // Limit number shown
        }
    }
}
```

### Colors Not Showing

**Symptoms**: Chart renders but colors are wrong/missing

**Solutions**:
- Verify color format (rgba, rgb, hex all valid)
- Ensure backgroundColor array length matches data length
- Check for typos in color property names
- Confirm alpha values (0.0-1.0 range for transparency)

### Responsive Issues

**Symptoms**: Chart doesn't resize properly

**Solutions**:
```javascript
options: {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 2  // Adjust as needed
}
```

```css
/* Container must have defined size */
.chart-container {
    position: relative;
    height: 400px;
    width: 100%;
}
```

### Animation Problems

**Symptoms**: Animations are jerky or cause performance issues

**Solutions**:
- Reduce animation duration
- Disable animations for large datasets
- Use `chart.update('none')` for instant updates
- Limit number of data points displayed

## Advanced Features

### Data Labels Plugin

Display values directly on chart elements:

```html
<!-- Add plugin CDN -->
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>
```

```javascript
options: {
    plugins: {
        datalabels: {
            anchor: 'end',
            align: 'top',
            formatter: (value) => '$' + value.toFixed(2)
        }
    }
}
```

### Mixed Chart Types

Combine different chart types in one visualization:

```javascript
{
    type: 'bar',
    data: {
        datasets: [
            { type: 'line', label: 'Target', data: [...] },
            { type: 'bar', label: 'Actual', data: [...] }
        ]
    }
}
```

### Custom Tooltips

Create fully custom tooltip content:

```javascript
plugins: {
    tooltip: {
        callbacks: {
            title: function(context) {
                return 'Custom Title';
            },
            label: function(context) {
                return 'Value: ' + context.parsed.y + ' units';
            },
            footer: function(context) {
                return 'Additional info here';
            }
        }
    }
}
```

### Click Events

Handle user interactions:

```javascript
options: {
    onClick: (event, elements) => {
        if (elements.length > 0) {
            const index = elements[0].index;
            const value = chart.data.datasets[0].data[index];
            alert('Clicked: ' + chart.data.labels[index] + ' = ' + value);
        }
    }
}
```

### Programmatic Updates

Update chart data dynamically:

```javascript
function updateChart(newData) {
    chart.data.datasets[0].data = newData;
    chart.update('active');  // Animation mode
}

function addDataPoint(label, value) {
    chart.data.labels.push(label);
    chart.data.datasets[0].data.push(value);
    chart.update();
}
```

## Comparison with Other Visualization Skills

### vs. Bubble Chart Generator

- **Chart.js Generator**: All chart types including basic bubbles
- **Bubble Chart Generator**: Specialized for priority matrices with quadrants

**Use Chart.js for**: General bubble charts, simple scatter plots
**Use Bubble Chart Generator for**: Impact/Effort matrices, strategic analysis

### vs. Mermaid Generator

- **Chart.js Generator**: Data-driven statistical charts
- **Mermaid Generator**: Flowcharts, process diagrams, conceptual visualizations

**Use Chart.js for**: Numerical data visualization
**Use Mermaid for**: Workflows, state machines, architecture diagrams

### vs. Timeline Generator

- **Chart.js Generator**: Time series line charts (continuous metrics)
- **Timeline Generator**: Event-based chronological visualization

**Use Chart.js for**: Continuous time-series data (temperature, stock prices)
**Use Timeline Generator for**: Discrete historical events with dates and descriptions

### vs. Venn Diagram Generator

- **Chart.js Generator**: Quantitative data visualization
- **Venn Diagram Generator**: Set relationships and overlaps

**Use Chart.js for**: Numbers, trends, comparisons
**Use Venn for**: Conceptual relationships, category overlaps

**Complementary Use**: Combine multiple visualization types for comprehensive content. Example: A business chapter might use bar charts (sales data), line charts (trends), and bubble charts (strategic positioning).

## Performance Optimization

For optimal performance:

- **Limit data points** - Best performance with <1000 points per dataset
- **Disable animations** - For large datasets or frequent updates
- **Use data decimation** - Reduce points displayed at low zoom levels
- **Lazy loading** - Load charts when visible (intersection observer)
- **Canvas reuse** - Destroy old charts before creating new ones

```javascript
// Destroy before recreating
if (window.myChart) {
    window.myChart.destroy();
}
window.myChart = new Chart(ctx, config);
```

## Accessibility Considerations

Charts are designed with accessibility in mind:

- **Color + Pattern** - Don't rely on color alone
- **Keyboard Navigation** - All interactive elements accessible
- **Screen Reader Support** - Semantic HTML and ARIA labels
- **High Contrast** - WCAG AA compliant color schemes
- **Text Alternatives** - Descriptive documentation provided
- **Printable** - CSS optimized for print media

## Version History

- **v1.0** (Chart.js 4.4.0): Initial release
  - Support for all 8 chart types
  - Responsive design
  - Interactive tooltips and legends
  - Customizable colors and options
  - Complete documentation templates
  - MkDocs integration
  - Educational metadata

## Related Skills

- **Bubble Chart Generator** - Specialized bubble charts for priority matrices
- **Timeline Generator** - Event-based chronological visualizations
- **Mermaid Generator** - Flowcharts and process diagrams
- **Venn Diagram Generator** - Set relationships and overlaps
- **MicroSim P5** - Custom interactive simulations (alternative for specialized visualizations)

## References

- [Chart.js Official Documentation](https://www.chartjs.org/docs/latest/) - Complete API reference
- [Chart.js Samples](https://www.chartjs.org/docs/latest/samples/) - Example gallery
- [Chart.js GitHub](https://github.com/chartjs/Chart.js) - Source code and issues
- [Chart Types Guide](https://www.chartjs.org/docs/latest/charts/) - Detailed chart type documentation
- [Chart.js Plugins](https://www.chartjs.org/docs/latest/developers/plugins.html) - Plugin development
- [Data Visualization Best Practices](https://www.storytellingwithdata.com/) - Design principles

## Quick Start Example

To generate a simple bar chart showing monthly sales:

```
Input Requirements:
- Chart Type: Bar Chart
- Title: Monthly Sales 2024
- Data:
  * January: $12,000
  * February: $15,000
  * March: $18,000
  * April: $14,000
  * May: $20,000
  * June: $22,000
- Color Scheme: Blue
- Axes: Months (X), Revenue (Y, starting at $0)
```

**Output**: Complete MicroSim package with:
- Interactive bar chart with hover tooltips
- Responsive design (desktop, tablet, mobile)
- Clickable legend
- Smooth animations
- Documentation with customization guide
- Educational metadata for MkDocs integration

---

*Generated charts seamlessly integrate into MkDocs Material textbooks as iframe-embedded MicroSims with professional styling and comprehensive customization options.*
