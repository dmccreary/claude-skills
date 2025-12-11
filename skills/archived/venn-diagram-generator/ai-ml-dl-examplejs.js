// Venn Diagram Example for AI, ML, and Deep Learning
/*

Here's the generalized rule for educational tooltips in Venn diagrams:

  Educational Tooltips Rule

  Use Definitions Instead of Size Values

  Problem: The default venn.js examples show size values (e.g., "150 users") which are not
  educational for learning-focused diagrams.

  Solution: Replace size numbers with educational definitions that explain what each region
  represents.

  Implementation Pattern:

  // 1. Create a definitions object mapping sets to educational content
  var definitions = {
      'SetA': 'Clear, concise definition of Set A',
      'SetB': 'Clear, concise definition of Set B',
      'SetA,SetB': 'Explanation of the relationship/overlap between A and B',
      'SetA,SetB,SetC': 'Explanation of triple intersection'
  };

  // 2. Create helper function to lookup definitions
  function getDefinition(sets) {
      var key = sets.sort().join(',');
      return definitions[key] || sets.join(" ∩ ");
  }

  // 3. Use in tooltip
  .on("mouseover", function(event, d) {
      tooltip.html(getDefinition(d.sets));  // NOT d.size
  })

  Definition Guidelines:

  1. Keep definitions concise (1 sentence, under 100 characters ideal)
  2. Focus on meaning not technical details
  3. Explain relationships for intersections (what the overlap means)
  4. Use accessible language appropriate for target audience
  5. Be consistent in tone and structure across all definitions

  Examples:

  Good definitions:
  - "Systems that simulate human intelligence and decision-making"
  - "Overlap: Methods that combine statistical analysis with AI"

  Poor definitions:
  - "Size: 150" ❌ (not educational)
  - "This is the intersection of sets A and B containing 40 elements" ❌ (too technical)
  - "Machine learning algorithms are..." (too long) ❌

  Why This Matters:

  - Makes diagrams self-documenting for students
  - Provides immediate context without reading external docs
  - Reinforces learning objectives through interaction
  - Replaces meaningless numbers with meaningful content

  Complete Educational Example:

  var definitions = {
      'Mammals': 'Warm-blooded vertebrates that nurse their young',
      'Carnivores': 'Animals that primarily eat meat',
      'Mammals,Carnivores': 'Meat-eating mammals like lions, wolves, and seals'
  };

  This pattern ensures every hover interaction is a teaching moment rather than just visual
  feedback.



*/


// Venn diagram data - Nested sets showing AI ⊃ ML ⊃ DL hierarchy
var sets = [
  {sets: ['AI'], size: 150},
  {sets: ['ML'], size: 90},
  {sets: ['Deep Learning'], size: 40},
  {sets: ['AI', 'ML'], size: 90},
  {sets: ['ML', 'Deep Learning'], size: 40},
  {sets: ['AI', 'Deep Learning'], size: 40},
  {sets: ['AI', 'ML', 'Deep Learning'], size: 40}
];

// Color configuration - Blue gradient from light (AI) to dark (DL)
var colorScheme = [
  {set: 'AI', color: '#87CEEB'},  // Light blue (outer)
  {set: 'ML', color: '#4169E1'},         // Medium blue (middle)
  {set: 'Deep Learning', color: '#1E3A8A'}             // Dark blue (inner)
];

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

    // Apply color scheme to all areas (including intersections)
    // For nested sets, use the most specific (innermost) set's color
    div.selectAll("g")
        .select("path")
        .style("fill", function(d) {
            // Determine color based on which sets are involved
            // Priority: Deep Learning > Machine Learning > AI
            if (d.sets.includes('DL')) {
                return '#1E3A8A';  // Dark blue for DL
            } else if (d.sets.includes('Machine Learning')) {
                return '#4169E1';  // Medium blue for ML
            } else if (d.sets.includes('AI')) {
                return '#87CEEB';  // Light blue for AI
            }
            return '#999';  // Fallback gray
        });

    // Ensure all text labels are dark gray and visible
    div.selectAll("text")
        .style("fill", "#333")
        .style("font-weight", "bold")
        .style("font-size", "16px");

    // Educational definitions for each set
    var definitions = {
        'AI': 'Systems that simulate human intelligence, reasoning, and decision-making',
        'ML': 'Algorithms that learn patterns from data without explicit programming',
        'Deep Learning': 'Neural networks with multiple layers that learn complex representations',
        'AI,ML': 'Machine Learning is a subset of AI that focuses on learning from data',
        'ML,Deep Learning': 'Deep Learning is a specialized form of ML using neural networks',
        'AI,Deep Learning': 'Deep Learning combines AI principles with neural network architectures',
        'AI,ML,Deep Learning': 'Deep Learning represents the intersection of AI and ML approaches'
    };

    // Helper function to get definition based on sets
    function getDefinition(sets) {
        var key = sets.sort().join(',');
        return definitions[key] || sets.join(" ∩ ");
    }

    // Add interactive tooltips
    var tooltip = d3.select("body").append("div")
        .attr("class", "venntooltip");

    // Hover effects - following official venn.js pattern
    div.selectAll("g")
        .on("mouseover", function(event, d) {
            // Sort all areas relative to current to ensure proper z-ordering
            venn.sortAreas(div, d);

            // Display tooltip with educational definition
            tooltip.transition().duration(400).style("opacity", 0.9);
            tooltip.html(getDefinition(d.sets))
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 28) + "px");

            // Highlight the current path - only change opacity, not fill color
            var selection = d3.select(this).transition("tooltip").duration(400);
            selection.select("path")
                .style("fill-opacity", d.sets.length == 1 ? 0.4 : 0.1)
                .style("stroke-opacity", 1);
        })
        .on("mouseout", function(event, d) {
            tooltip.transition().duration(400).style("opacity", 0);

            // Reset opacity only - use lower values so text remains readable
            var selection = d3.select(this).transition("tooltip").duration(400);
            selection.select("path")
                .style("fill-opacity", d.sets.length == 1 ? 0.25 : 0.0)
                .style("stroke-opacity", 0);
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
