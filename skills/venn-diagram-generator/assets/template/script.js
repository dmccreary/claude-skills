// Venn Diagram Configuration and Rendering
// This script is populated with data specific to each diagram

// Venn diagram data - Replace {{VENN_DATA}} with actual sets data
var sets = {{VENN_DATA}};

// Color configuration - Replace {{COLOR_SCHEME}} with actual colors
var colorScheme = {{COLOR_SCHEME}};

// Initialize the Venn diagram
function initVennDiagram() {
    // Create the Venn diagram chart
    var chart = venn.VennDiagram()
        .width(600)
        .height(450);

    // Select the container and bind data
    var div = d3.select("#venn")
        .datum(sets)
        .call(chart);

    // Apply color scheme to circles
    if (colorScheme && colorScheme.length > 0) {
        colorScheme.forEach(function(colorConfig) {
            d3.selectAll("#venn .venn-circle")
                .filter(function(d) {
                    return d.sets.length === 1 && d.sets[0] === colorConfig.set;
                })
                .select("path")
                .style("fill", colorConfig.color);
        });
    }

    // Add interactive tooltips
    var tooltip = d3.select("body").append("div")
        .attr("class", "venntooltip");

    // Hover effects
    div.selectAll("g")
        .on("mouseover", function(event, d) {
            // Sort all areas relative to current to ensure proper z-ordering
            venn.sortAreas(div, d);

            // Display tooltip
            tooltip.transition().duration(200).style("opacity", 0.9);

            // Generate tooltip text
            var tooltipText = d.sets.join(" ∩ ") + ": " + d.size;
            tooltip.html(tooltipText)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 28) + "px");

            // Highlight current area
            d3.select(this).select("path")
                .style("fill-opacity", 0.95)
                .style("stroke-width", "3px");
        })
        .on("mouseout", function(event, d) {
            tooltip.transition().duration(200).style("opacity", 0);

            // Reset styling
            d3.select(this).select("path")
                .style("fill-opacity", function(d) {
                    return d.sets.length === 1 ? 0.75 : 0.85;
                })
                .style("stroke-width", "2px");
        });

    // Make diagram responsive
    makeResponsive();
}

// Responsive behavior
function makeResponsive() {
    var container = d3.select("#venn");
    var svg = container.select("svg");

    if (!svg.empty()) {
        var width = parseInt(svg.attr("width"));
        var height = parseInt(svg.attr("height"));
        var aspect = width / height;

        svg.attr("viewBox", "0 0 " + width + " " + height)
           .attr("preserveAspectRatio", "xMidYMid meet")
           .attr("width", "100%")
           .attr("height", "100%");

        // Redraw on window resize
        d3.select(window).on("resize", function() {
            var targetWidth = container.node().getBoundingClientRect().width;
            svg.attr("width", targetWidth)
               .attr("height", targetWidth / aspect);
        });
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initVennDiagram();
});
