# {{TITLE}}

{{DESCRIPTION}}

## Interactive Map

<iframe src="main.html" width="100%" height="700" frameborder="0"></iframe>

[View Fullscreen](main.html){:target="_blank"}

## Overview

{{OVERVIEW_TEXT}}

## Features

### Interactive Elements

- **Zoom and Pan** - Use mouse wheel or touch gestures to zoom, click and drag to pan
- **Marker Popups** - Click on markers to view detailed information
- **Layer Controls** - Toggle between different map views (street, satellite, terrain)
- **Reset View** - Return to the initial map position and zoom level

### Visual Design

- Color-coded markers for different categories
- Clear, informative popups with titles and descriptions
- Responsive layout that adapts to different screen sizes
- Minimal padding optimized for textbook integration

## Map Details

**Center Coordinates**: {{CENTER_LAT}}, {{CENTER_LNG}}

**Initial Zoom Level**: {{ZOOM}}

**Number of Markers**: {{MARKER_COUNT}}

**Base Map**: {{BASE_MAP_TYPE}}

## Customization Guide

This map can be customized by editing the files in the `sims/{{MAP_NAME}}/` directory.

### Adding Markers

To add new markers, edit the `markers` array in `script.js`:

```javascript
const markers = [
    {
        lat: 40.7128,
        lng: -74.0060,
        title: "New York City",
        description: "The largest city in the United States",
        link: "https://en.wikipedia.org/wiki/New_York_City"
    },
    // Add more markers here
];
```

**Fields**:

- `lat` - Latitude (-90 to 90)
- `lng` - Longitude (-180 to 180)
- `title` - Marker title (shown in popup)
- `description` - Detailed description (optional)
- `link` - External link for more information (optional)

### Changing the Base Map

Modify the tile layer URL in `script.js`:

**OpenStreetMap** (default):
```javascript
const tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
});
```

**Satellite Imagery**:
```javascript
const tileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: '&copy; Esri'
});
```

**Terrain Map**:
```javascript
const tileLayer = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenTopoMap contributors'
});
```

### Adjusting Map Height

Edit `style.css` to change the map container height:

```css
#map {
    height: 500px;  /* Change this value */
    width: 100%;
}
```

Also update the iframe height in this `index.md` file to match.

### Custom Marker Icons

Replace the default marker icons by adding custom icons in `script.js`:

```javascript
const customIcon = L.icon({
    iconUrl: 'custom-marker.png',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32]
});

L.marker([lat, lng], { icon: customIcon }).addTo(map);
```

### Adding GeoJSON Layers

To highlight regions or borders, add GeoJSON data:

```javascript
const regionData = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[...]]
    },
    "properties": {
        "name": "Region Name"
    }
};

L.geoJSON(regionData, {
    style: { color: 'red', weight: 3, fillOpacity: 0.2 }
}).addTo(map);
```

## Technical Details

- **Library**: Leaflet 1.9.4
- **CDN**: unpkg.com (with SRI integrity checks)
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Leaflet CSS and JavaScript (loaded from CDN)
- **Responsive**: Yes - adapts to mobile, tablet, and desktop screens
- **Performance**: Optimized for up to 100 markers (use clustering for more)

## Educational Applications

This map pattern can be adapted for various educational contexts:

### Geography and History

- Historical event locations and timelines
- Ancient civilization sites
- Exploration routes and trade networks
- Geographic feature identification

### Science

- Biodiversity hotspots
- Climate zones and weather patterns
- Geological formations
- Ecological regions

### Social Studies

- Cultural landmarks
- Population centers
- Economic activity zones
- Political boundaries

### Campus and Facility Maps

- University campus buildings
- Museum floor plans
- Park trails and facilities
- City infrastructure

## Bloom's Taxonomy Alignment

This map supports multiple cognitive levels:

- **Remember**: Identify and locate specific places on the map
- **Understand**: Explain spatial relationships between locations
- **Apply**: Use the map to solve problems (distances, routes)
- **Analyze**: Compare and contrast geographic patterns
- **Evaluate**: Assess the significance of location-based data
- **Create**: Design custom maps for specific educational purposes

## Accessibility Considerations

- All markers include descriptive text in popups
- Keyboard navigation supported through Leaflet controls
- High-contrast colors used for visibility
- Text alternatives provided for geographic information

## References

- [Leaflet Official Documentation](https://leafletjs.com/reference.html) - Complete API reference
- [Leaflet Tutorials](https://leafletjs.com/examples.html) - Step-by-step guides
- [OpenStreetMap Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/) - Terms of service
- [GeoJSON Format Specification](https://geojson.org/) - Standard for geographic data
- [Map Projections](https://en.wikipedia.org/wiki/Map_projection) - Understanding coordinate systems

## Version History

- **v1.0** ({{DATE}}): Initial map created with {{MARKER_COUNT}} markers

---

*Generated using the map-generator skill for intelligent textbooks*
