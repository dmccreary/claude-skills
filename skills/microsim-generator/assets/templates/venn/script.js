/**
 * venn.js MicroSim Template Script
 * Renders an interactive Venn diagram with educational tooltips.
 *
 * See references/venn-js-reference.md for the full venn.js API.
 */

// ============================================
// DATA - Replace with the diagram's sets (Step 2 of venn-guide.md)
// ============================================
var sets = {{VENN_DATA}};

// ============================================
// COLOR SCHEME - One color per top-level set
// ============================================
var colorScheme = {{COLOR_SCHEME}};

// ============================================
// EDUCATIONAL DEFINITIONS - Replace size values with teaching content.
// Key is the sorted, comma-joined set name(s), e.g. "Java,Python" for the
// Java ∩ Python intersection. See venn-guide.md "Educational Tooltips".
// ============================================
var definitions = {{DEFINITIONS}};

function getDefinition(setNames) {
    var key = setNames.slice().sort().join(',');
    return definitions[key] || setNames.join(' ∩ ');
}

// ============================================
// RENDER THE DIAGRAM
// ============================================
var chart = venn.VennDiagram()
    .width(600)
    .height(450);

var div = d3.select('#venn-diagram');
div.datum(sets).call(chart);

// Apply the color scheme to each set
colorScheme.forEach(function (entry) {
    div.selectAll('.venn-circle path')
        .filter(function (d) {
            return d.sets.length === 1 && d.sets[0] === entry.set;
        })
        .style('fill', entry.color)
        .style('fill-opacity', 0.7)
        .style('stroke', entry.color)
        .style('stroke-width', 2);
});

// Set names/labels use 16px minimum font (handled in style.css via #venn-diagram text)

// ============================================
// EDUCATIONAL TOOLTIPS
// ============================================
var tooltip = d3.select('#tooltip');

div.selectAll('.venn-area')
    .on('mouseover', function (event, d) {
        d3.select(this).select('path').style('stroke-width', 3);
        tooltip
            .style('left', event.pageX + 15 + 'px')
            .style('top', event.pageY + 15 + 'px')
            .classed('visible', true)
            .html(getDefinition(d.sets));
    })
    .on('mousemove', function (event) {
        tooltip
            .style('left', event.pageX + 15 + 'px')
            .style('top', event.pageY + 15 + 'px');
    })
    .on('mouseout', function (event, d) {
        d3.select(this).select('path').style('stroke-width', 2);
        tooltip.classed('visible', false);
    });

// Responsive resize: venn.js has no built-in resize handler, so re-render
// on width changes wide enough to matter (debounced).
var resizeTimer;
window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
        var width = Math.min(600, window.innerWidth - 40);
        chart.width(width).height(width * 0.75);
        div.datum(sets).call(chart);
    }, 200);
});
