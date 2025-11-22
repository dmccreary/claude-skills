---
title: Major World Cities
description: Interactive Leaflet visualization showing major world cities
image: /sims/test-world-cities/test-world-cities.png
og:image: /sims/test-world-cities/test-world-cities.png
quality_score: 100
---


# Major World Cities

<iframe src="main.html" width="100%" height="360px"></iframe>
[Run Major World Cities in Fullscreen](main.html){ .md-button .md-button--primary }

**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/test-world-cities/main.html" width="100%" height="360px"></iframe>
```

An interactive map showcasing ten major cities across different continents, demonstrating the geographic distribution of global population centers.  Click on any marker to see the details of the city.

## Overview

This map displays major cities from around the world, representing different continents and cultural regions. Each marker can be clicked to reveal information about the city, including its significance and a link to learn more.

## Features

### Interactive Elements

- **Zoom and Pan** - Use mouse wheel or touch gestures to zoom, click and drag to pan
- **Marker Popups** - Click on markers to view detailed information about each city
- **Reset View** - Return to the initial map position and zoom level

### Visual Design

- Clean, minimalist marker design using Leaflet defaults
- Informative popups with city names, descriptions, and external links
- Responsive layout that adapts to different screen sizes
- Minimal padding optimized for textbook integration

## Map Details

**Center Coordinates**: 20°N, 0°E

**Initial Zoom Level**: 2 (world view)

**Number of Markers**: 10 cities

**Base Map**: OpenStreetMap

**Cities Featured**:

1. New York City, USA
2. London, United Kingdom
3. Tokyo, Japan
4. Sydney, Australia
5. Mexico City, Mexico
6. São Paulo, Brazil
7. Moscow, Russia
8. New Delhi, India
9. Cairo, Egypt
10. Nairobi, Kenya

## Educational Applications

This map can be used to teach:

- **Geography**: Identifying major cities and their locations on different continents
- **Demographics**: Understanding global population distribution
- **Cultural Studies**: Exploring diverse urban centers worldwide
- **Economics**: Examining major financial and trade hubs
- **History**: Studying the development of major metropolitan areas

## Bloom's Taxonomy Alignment

- **Remember**: Locate and name major world cities
- **Understand**: Explain the geographic distribution of population centers
- **Apply**: Use the map to identify cities by continent or region
- **Analyze**: Compare the locations of cities across different hemispheres
- **Evaluate**: Assess the strategic importance of city locations
- **Create**: Design additional maps showing specific themes (trade routes, climate zones, etc.)

## Technical Details

- **Library**: Leaflet 1.9.4
- **CDN**: unpkg.com (with SRI integrity checks)
- **Browser Compatibility**: All modern browsers (Chrome, Firefox, Safari, Edge)
- **Dependencies**: Leaflet CSS and JavaScript (loaded from CDN)
- **Responsive**: Yes - adapts to mobile, tablet, and desktop screens

## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Understand** (Understand) how Leaflet.js renders interactive web maps
- **Apply** (Apply) geographic coordinate systems to place markers on maps
- **Analyze** (Analyze) the trade-offs between different map tile providers
- **Create** (Create) custom interactive maps with markers and popups
- **Evaluate** (Evaluate) map visualizations for clarity and information density

### Target Audience

- **Primary**: Web developers, data visualization specialists
- **Secondary**: Geographic information systems (GIS) students, digital cartographers
- **Level**: Undergraduate computer science or professional development
- **Prerequisites**: Basic JavaScript, HTML, and CSS; understanding of latitude/longitude

### Activities

**Activity 1: Map Interaction Exploration (15 minutes)**

1. Pan across the map to view all continents
2. Zoom in to street level on 3 different cities
3. Click markers to view city information popups
4. Compare the map styles between OpenStreetMap and other tile providers (if multiple available)
5. Note: How does the map behave on mobile vs. desktop?

**Activity 2: Coordinate Analysis (20 minutes)**

1. Verify 5 city coordinates are accurate using an external source (e.g., Google Maps)
2. Calculate the distance between Tokyo (35.68°N, 139.65°E) and São Paulo (23.55°S, 46.63°W)
3. Identify which cities are in the Southern Hemisphere (latitude < 0)
4. Explain why London has negative longitude despite being far from the Prime Meridian

**Activity 3: Add Your Own Markers (35 minutes)**

1. Choose 5 cities not currently on the map
2. Look up their latitude/longitude coordinates
3. Add JavaScript code to place markers for these cities:
   ```javascript
   L.marker([latitude, longitude]).addTo(map)
     .bindPopup('<b>City Name</b><br>Country<br>Population: X');
   ```
4. Customize marker icons or colors for different continents
5. Verify all markers appear correctly when the map loads

**Activity 4: Create a Thematic Map (50 minutes)**

Design a map showing:

1. **Theme selection**: Choose a topic (e.g., capital cities, UNESCO sites, tech hubs)
2. **Data collection**: Gather 15-20 locations with coordinates
3. **Marker customization**: Use different icons/colors for categories
4. **Popup content**: Include relevant information (population, facts, images)
5. **Map bounds**: Set initial view to show all markers
6. **Deployment**: Test the map in fullscreen and iframe modes

### Assessment

**Formative Assessment:**
- During Activity 2: Can students correctly interpret latitude/longitude coordinates?
- During Activity 3: Do added markers appear in correct geographic locations?

**Summative Assessment:**

Create a complete custom interactive map:

1. **Data Quality** (25 points): Accurate coordinates for 15+ locations
2. **Visualization Design** (30 points): Effective use of markers, popups, and zoom levels
3. **Interactivity** (20 points): Smooth panning, zooming, and popup functionality
4. **Code Quality** (15 points): Clean JavaScript, proper Leaflet.js API usage
5. **Documentation** (10 points): README explaining map theme and data sources

**Success Criteria:**
- Map loads without errors and displays all markers
- Coordinate accuracy within 0.1 degrees
- Popups provide useful contextual information
- Map is responsive and works on mobile devices
- Initial view shows all markers within bounds

### Extension Activities

- **Advanced**: Implement clustering for overlapping markers at low zoom levels
- **Integration**: Load marker data from external GeoJSON file
- **Styling**: Create custom map tiles or use Mapbox for advanced styling
- **Analytics**: Add heatmap layer showing data density


## References

- [Leaflet Official Documentation](https://leafletjs.com/reference.html)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [World Cities Database](https://simplemaps.com/data/world-cities)

## Version History

- **v1.0** (2025-01-16): Initial test map with 10 major world cities

---

*Generated using the map-generator skill for intelligent textbooks*