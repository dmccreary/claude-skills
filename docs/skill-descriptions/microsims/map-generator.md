# Map Generator

## Overview

The **Map Generator** skill creates interactive geographic maps using the Leaflet JavaScript library. This skill generates complete MicroSim packages optimized for iframe embedding in intelligent textbooks built with MkDocs Material theme.

Maps are created with minimal padding and margins, specifically designed to fit within narrow page layouts where both a navigation sidebar (left) and table of contents (right) are present.

## When to Use This Skill

Use the Map Generator skill when you need to create:

- **Geographic Visualizations** - Display regions, countries, cities, or custom geographic areas
- **Location-Based Data** - Show points of interest, historical sites, landmarks, or facilities
- **Educational Maps** - Campus maps, facility layouts, or geographic learning content
- **Route Visualizations** - Display travel routes, migration patterns, or trade networks
- **Thematic Maps** - Create maps with highlighted borders, regions, or custom overlays
- **Interactive Exploration** - Allow students to explore geographic relationships through interactive markers and popups

## Key Features

### Interactive Elements

- **Zoom and Pan Controls** - Standard Leaflet controls for exploring the map
- **Marker Popups** - Click markers to reveal detailed information, images, or links
- **Layer Controls** - Toggle between different map types (street, satellite, terrain)
- **Custom Markers** - Use custom icons to represent different categories or types
- **GeoJSON Support** - Highlight borders, regions, or complex geographic shapes
- **Responsive Design** - Maps adapt to desktop, tablet, and mobile screen sizes

### Optimized for Textbooks

- **Minimal Margins** - Body margin/padding set to 0 for perfect iframe embedding
- **Narrow Page Layout** - Designed for pages with navbar (left) and TOC (right)
- **Fixed Height Options** - Customizable map height (default 400px)
- **Educational Metadata** - Dublin Core fields plus Bloom's taxonomy alignment
- **Accessibility** - Keyboard navigation, descriptive popups, high-contrast colors

### Map Types Supported

1. **Simple Marker Maps** - Display multiple locations with informative popups
2. **Choropleth Maps** - Color-coded regions based on data values (with GeoJSON)
3. **Route Maps** - Show paths, journeys, or connections between locations
4. **Facility Maps** - Campus buildings, museum layouts, park facilities
5. **Multi-Layer Maps** - Toggle between street, satellite, and terrain views
6. **Clustered Maps** - Handle large numbers of markers with automatic clustering

## How It Works

### Workflow

The skill follows a 10-step process:

1. **Gather Requirements** - Prompts for geographic region, markers, layers, borders, zoom level
2. **Create Directory** - Sets up `docs/sims/[map-name]/` following MicroSim pattern
3. **Generate Data File** - Creates `map-data.json` with coordinates and marker information (optional)
4. **Create HTML** - Generates `main.html` with Leaflet CDN links and map container
5. **Create CSS** - Produces `style.css` with minimal margins for iframe embedding
6. **Create JavaScript** - Generates `script.js` with map initialization and marker data
7. **Create Documentation** - Produces `index.md` with iframe embed and customization guide
8. **Create Metadata** - Generates `metadata.json` with Dublin Core and educational fields
9. **Update Navigation** - Adds entry to `mkdocs.yml` for site navigation
10. **Test and Validate** - Verifies map functionality and responsive behavior

### User Interaction

The skill prompts users for:

- **Map Purpose** - What geographic data are we visualizing?
- **Geographic Region** - Region name, coordinates, or bounding box
- **Markers** - Location data (names, coordinates, descriptions, categories)
- **Map Type** - Street map, satellite imagery, or terrain
- **Layers** - Single layer or multiple toggleable layers?
- **Borders/Regions** - Any areas that need highlighting (requires GeoJSON)?
- **Zoom Level** - Initial zoom (1 = world view, 18 = building level)
- **Interactive Features** - Custom markers, popups, controls?
- **Educational Context** - Related concepts, Bloom's level, target audience

## Example Use Cases

### 1. Historical Events Map

**Scenario**: A history textbook chapter on World War II needs a map showing major battle locations.

**Output**:
- Interactive map centered on Europe
- Markers for each major battle with dates and descriptions
- Popup links to detailed battle information
- Timeline showing chronological progression
- Educational metadata: Bloom's level = "Understand", concepts = ["World War II", "Military History", "European Geography"]

### 2. Campus Facilities Map

**Scenario**: A university orientation guide needs a campus map showing buildings and facilities.

**Output**:
- Detailed campus map with building markers
- Color-coded icons (academic buildings, residence halls, dining, recreation)
- Popups with building names, hours, and services
- Search functionality for quick location finding
- Links to building-specific information pages

### 3. Biodiversity Hotspots

**Scenario**: An ecology textbook chapter on biodiversity needs to show global biodiversity hotspots.

**Output**:
- World map with highlighted regions (GeoJSON polygons)
- Color-coded by biodiversity threat level
- Markers for specific protected areas
- Popups with species counts and conservation status
- Layer toggle between satellite and terrain views

### 4. Ancient Trade Routes

**Scenario**: A world history course needs to visualize the Silk Road trade network.

**Output**:
- Map of Asia and Europe with route polylines
- Markers for major trading cities
- Popups with historical information and trade goods
- Animated route visualization (optional advanced feature)
- Timeline integration showing route development over centuries

### 5. Climate Zones

**Scenario**: A geography textbook needs an interactive climate zone map.

**Output**:
- World map with GeoJSON climate zone boundaries
- Color-coded regions (tropical, arid, temperate, continental, polar)
- Markers for representative cities in each zone
- Popups with climate data (temperature, precipitation)
- Educational metadata: Bloom's level = "Analyze", concepts = ["Climate Classification", "Geographic Patterns"]

## Technical Details

### Technology Stack

- **Library**: Leaflet 1.9.4 (latest stable release)
- **CDN**: unpkg.com with SRI integrity checks for security
- **Base Maps**: OpenStreetMap (default), Esri satellite imagery, OpenTopoMap terrain
- **Format**: HTML5, CSS3, ES6 JavaScript
- **Dependencies**: Leaflet CSS and JavaScript (loaded from CDN, no local installation)

### File Structure

Each generated map creates:

```
docs/sims/[map-name]/
├── main.html           # Standalone HTML page with map
├── style.css           # Minimal margin styling for iframe
├── script.js           # Map initialization and data
├── index.md            # Documentation with iframe embed
└── metadata.json       # Dublin Core + educational metadata
```

### Iframe Embedding

Maps are embedded in MkDocs pages using:

```markdown
<iframe src="main.html" width="100%" height="700" frameborder="0"></iframe>

[View Fullscreen](main.html){:target="_blank"}
```

### Customization Options

Generated maps can be customized by editing:

1. **Markers** - Edit the `markers` array in `script.js`
2. **Map Type** - Change tile layer URL for different base maps
3. **Map Height** - Adjust `#map` height in `style.css`
4. **Custom Icons** - Add custom marker icons in `script.js`
5. **GeoJSON Layers** - Add highlighted regions or borders
6. **Layer Controls** - Enable toggling between map types

## Educational Framework Integration

### Bloom's Taxonomy Alignment

Maps support all six cognitive levels:

- **Remember** - Identify and locate specific places on the map
- **Understand** - Explain spatial relationships between locations
- **Apply** - Use maps to solve problems (calculate distances, plan routes)
- **Analyze** - Compare and contrast geographic patterns or distributions
- **Evaluate** - Assess the significance or strategic value of locations
- **Create** - Design custom maps for specific educational purposes

### ISO 11179 Metadata

Map metadata follows ISO 11179 standards:

- **Precise** - Exact geographic coordinates and zoom levels
- **Concise** - Focused descriptions of map purpose and content
- **Distinct** - Clear differentiation between map types and purposes
- **Non-circular** - Independent definitions of geographic concepts
- **Free of business rules** - Focus on educational value, not implementation

### Learning Objectives

Generated maps include explicit learning objectives such as:

- "Identify major cities and their locations on different continents"
- "Understand the global distribution of population centers"
- "Analyze spatial patterns in climate zone distribution"
- "Evaluate the strategic importance of geographic features"

## Accessibility Considerations

Maps are designed with accessibility in mind:

- **Keyboard Navigation** - All Leaflet controls support keyboard input
- **Descriptive Text** - Markers include detailed popup text
- **High Contrast** - Default color schemes meet WCAG guidelines
- **Screen Reader Support** - Semantic HTML and ARIA labels
- **Text Alternatives** - Geographic information provided in documentation

## Performance Optimization

For optimal performance:

- **Marker Limit** - Best performance with <100 markers
- **Marker Clustering** - Use clustering for maps with many markers (100+)
- **Lazy Loading** - Maps only load when visible in viewport
- **CDN Usage** - Leaflet served from fast, reliable CDN
- **Minimal Dependencies** - No additional libraries required for basic maps

## Advanced Features

The skill's templates include commented examples for:

### Custom Marker Icons

```javascript
const customIcon = L.icon({
    iconUrl: 'marker-icon.png',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32]
});
```

### GeoJSON Layers

```javascript
L.geoJSON(regionData, {
    style: { color: 'red', weight: 3, fillOpacity: 0.2 },
    onEachFeature: function(feature, layer) {
        layer.bindPopup(feature.properties.name);
    }
}).addTo(map);
```

### Layer Controls

```javascript
const baseMaps = {
    "Street": streetLayer,
    "Satellite": satelliteLayer,
    "Terrain": terrainLayer
};
L.control.layers(baseMaps).addTo(map);
```

### Marker Clustering

```javascript
const markers = L.markerClusterGroup();
markers.addLayer(L.marker([lat, lng]));
map.addLayer(markers);
```

## Comparison with Other MicroSim Skills

### vs. Mermaid Generator

- **Map Generator**: Geographic data visualization with real-world coordinates
- **Mermaid Generator**: Flowcharts, diagrams, and abstract visualizations

### vs. Timeline Generator

- **Map Generator**: Spatial relationships and geographic patterns
- **Timeline Generator**: Temporal relationships and chronological sequences

### vs. Chart.js Generator

- **Map Generator**: Geographic context with interactive exploration
- **Chart.js Generator**: Statistical data visualization (bar, line, pie charts)

**Complementary Use**: Combine multiple MicroSim types for rich educational content. Example: A history chapter might include a timeline (when), a map (where), and charts (quantitative data).

## Template Files

The skill includes 5 comprehensive template files:

1. **template-iframe-main.html** (35 lines)
   - HTML5 structure with Leaflet CDN links
   - Map container with fixed height requirement
   - Optional controls section
   - Placeholders: `{{TITLE}}`, `{{SUBTITLE}}`

2. **template-iframe-style.css** (180 lines)
   - Critical: `body { margin: 0; padding: 0; }`
   - Minimal margins throughout (2-5px max)
   - Responsive breakpoints (768px, 480px)
   - aliceblue background (repository standard)

3. **template-script.js** (150 lines)
   - Map initialization with configuration object
   - Tile layer setup with attribution
   - Marker creation with popups
   - Commented examples for all advanced features

4. **template-index.md** (200+ lines)
   - Complete documentation structure
   - iframe embed with fullscreen link
   - Customization guide
   - Educational applications
   - Technical details and references

5. **template-metadata.json** (30 lines)
   - Dublin Core standard fields
   - Map-specific: center_lat, center_lng, zoom_level
   - Educational: concepts, bloom_taxonomy, learning_objectives

## Best Practices

### When Creating Maps

1. **Start Simple** - Begin with basic marker maps before adding complexity
2. **Test Coordinates** - Verify latitude/longitude values before generating
3. **Limit Markers** - Keep initial marker count under 50 for quick loading
4. **Choose Appropriate Zoom** - World = 2, Country = 5, City = 10, Street = 15
5. **Provide Context** - Include descriptive popups with links to more information
6. **Consider Mobile** - Test responsive behavior on different screen sizes
7. **Add Metadata** - Complete educational metadata for searchability

### Content Design

1. **Clear Labels** - Use concise, descriptive marker titles
2. **Informative Popups** - Provide context, not just names
3. **Visual Hierarchy** - Use custom icons to distinguish marker types
4. **Color Coding** - Apply consistent color schemes for categories
5. **External Links** - Link to additional resources (Wikipedia, course content)
6. **Educational Value** - Align with specific learning objectives

## Troubleshooting

### Map Not Displaying

**Symptoms**: Blank iframe or error message

**Solutions**:
- Verify Leaflet CDN links are correct
- Ensure `#map` div has fixed height in CSS
- Check browser console for JavaScript errors
- Confirm coordinates are in decimal format (not DMS)

### Markers Not Appearing

**Symptoms**: Map displays but no markers visible

**Solutions**:
- Verify latitude range: -90 to 90
- Verify longitude range: -180 to 180
- Check marker array syntax in `script.js`
- Ensure markers added after map initialization
- Zoom to marker locations to verify they're not out of view

### Iframe Sizing Issues

**Symptoms**: Map has unwanted scrollbars or padding

**Solutions**:
- Confirm `body { margin: 0; padding: 0; }` in CSS
- Adjust iframe height in `index.md`
- Check container margins are minimal (2-5px max)
- Verify no conflicting CSS from parent page

## Version History

- **v1.0** (2025-01-16): Initial release
  - Basic marker maps with popups
  - Multiple tile layer support (street, satellite, terrain)
  - GeoJSON layer support for borders and regions
  - Layer controls for toggling map types
  - Marker clustering for large datasets
  - Complete educational metadata integration
  - Responsive design with three breakpoints
  - Accessibility features (keyboard navigation, ARIA labels)

## Related Skills

- **Timeline Generator** - Create chronological visualizations (pairs well for historical maps)
- **Chart.js Generator** - Create statistical charts (pairs well for demographic maps)
- **Mermaid Generator** - Create flowcharts and diagrams (pairs well for process maps)
- **MicroSim P5** - Create custom simulations (alternative for specialized visualizations)

## References

- [Leaflet Official Documentation](https://leafletjs.com/reference.html) - Complete API reference
- [Leaflet Tutorials](https://leafletjs.com/examples.html) - Step-by-step guides and examples
- [OpenStreetMap](https://www.openstreetmap.org/) - Default map tile provider
- [GeoJSON Format](https://geojson.org/) - Standard for encoding geographic data structures
- [Map Projections](https://en.wikipedia.org/wiki/Map_projection) - Understanding coordinate systems
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Web accessibility standards

## Quick Start Example

To generate a simple map showing three universities:

```
Input Requirements:
- Map Purpose: Show major universities in California
- Region: California, USA
- Markers:
  * Stanford University (37.4275, -122.1697)
  * UC Berkeley (37.8719, -122.2585)
  * UCLA (34.0689, -118.4452)
- Zoom Level: 7 (state view)
- Map Type: Street map (OpenStreetMap)
```

**Output**: Complete MicroSim package with:
- Interactive map centered on California
- Three markers with university information
- Popups with descriptions and links
- Documentation with customization guide
- Educational metadata aligned to higher education geography

---

*Generated maps seamlessly integrate into MkDocs Material textbooks as iframe-embedded MicroSims with minimal margins and comprehensive educational metadata.*
