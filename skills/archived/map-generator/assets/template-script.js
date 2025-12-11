/**
 * Leaflet Map Script Template
 * Replace placeholders with actual values when generating a map
 */

// Map configuration
const mapConfig = {
    center: [{{CENTER_LAT}}, {{CENTER_LNG}}],  // [latitude, longitude]
    zoom: {{ZOOM}},  // Zoom level (1-18)
    minZoom: 2,
    maxZoom: 18
};

// Initialize the map
const map = L.map('map', {
    center: mapConfig.center,
    zoom: mapConfig.zoom,
    minZoom: mapConfig.minZoom,
    maxZoom: mapConfig.maxZoom,
    zoomControl: true,
    scrollWheelZoom: true
});

// Add tile layer (base map)
// Options: OpenStreetMap, Satellite, Terrain
const tileLayer = L.tileLayer('{{TILE_LAYER_URL}}', {
    attribution: '{{ATTRIBUTION}}',
    maxZoom: 18,
    tileSize: 256
}).addTo(map);

// ===== MARKERS =====
// Define markers with popups
const markers = {{MARKERS_JSON}};

// Add markers to the map
markers.forEach(markerData => {
    const marker = L.marker([markerData.lat, markerData.lng]);

    // Create popup content
    let popupContent = `<h3>${markerData.title}</h3>`;
    if (markerData.description) {
        popupContent += `<p>${markerData.description}</p>`;
    }
    if (markerData.link) {
        popupContent += `<p><a href="${markerData.link}" target="_blank">Learn more</a></p>`;
    }

    marker.bindPopup(popupContent);
    marker.addTo(map);
});

// ===== OPTIONAL: CUSTOM MARKER ICONS =====
// Uncomment and modify to use custom icons
/*
const customIcon = L.icon({
    iconUrl: 'marker-icon.png',
    iconSize: [32, 32],
    iconAnchor: [16, 32],
    popupAnchor: [0, -32]
});

L.marker([lat, lng], { icon: customIcon }).addTo(map);
*/

// ===== OPTIONAL: GEOJSON LAYERS =====
// Uncomment to add GeoJSON polygons (borders, regions, etc.)
/*
const geoJsonData = {{GEOJSON_DATA}};

L.geoJSON(geoJsonData, {
    style: {
        color: '#ff0000',
        weight: 3,
        opacity: 0.8,
        fillOpacity: 0.2
    },
    onEachFeature: function(feature, layer) {
        if (feature.properties && feature.properties.name) {
            layer.bindPopup(`<h3>${feature.properties.name}</h3>`);
        }
    }
}).addTo(map);
*/

// ===== OPTIONAL: LAYER CONTROLS =====
// Uncomment to add multiple base layers with toggle controls
/*
const streetMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
});

const satelliteMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: '&copy; Esri'
});

const terrainMap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenTopoMap contributors'
});

const baseMaps = {
    "Street": streetMap,
    "Satellite": satelliteMap,
    "Terrain": terrainMap
};

// Add the first layer by default
streetMap.addTo(map);

// Add layer control
L.control.layers(baseMaps).addTo(map);
*/

// ===== OPTIONAL: MARKER CLUSTERING =====
// For maps with many markers, use clustering for better performance
// Requires: https://unpkg.com/leaflet.markercluster/dist/leaflet.markercluster.js
/*
const markerCluster = L.markerClusterGroup();

markers.forEach(markerData => {
    const marker = L.marker([markerData.lat, markerData.lng]);
    marker.bindPopup(`<b>${markerData.title}</b><br>${markerData.description}`);
    markerCluster.addLayer(marker);
});

map.addLayer(markerCluster);
*/

// ===== OPTIONAL: CUSTOM CONTROLS =====
// Add custom buttons for user interactions
/*
function addCustomControl(label, onClick) {
    const button = document.createElement('button');
    button.textContent = label;
    button.onclick = onClick;
    document.querySelector('.controls').appendChild(button);
}

// Example: Add a "Reset View" button
addCustomControl('Reset View', function() {
    map.setView(mapConfig.center, mapConfig.zoom);
});

// Example: Add a "Toggle Markers" button
let markersVisible = true;
addCustomControl('Toggle Markers', function() {
    if (markersVisible) {
        map.eachLayer(layer => {
            if (layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });
        markersVisible = false;
    } else {
        markers.forEach(markerData => {
            L.marker([markerData.lat, markerData.lng])
                .bindPopup(`<b>${markerData.title}</b><br>${markerData.description}`)
                .addTo(map);
        });
        markersVisible = true;
    }
});
*/

// ===== OPTIONAL: FIT BOUNDS =====
// Automatically adjust zoom to fit all markers
/*
if (markers.length > 0) {
    const bounds = L.latLngBounds(markers.map(m => [m.lat, m.lng]));
    map.fitBounds(bounds, { padding: [50, 50] });
}
*/

// ===== EVENT LISTENERS =====
// Add custom event handlers
/*
map.on('click', function(e) {
    console.log('Map clicked at:', e.latlng);
});

map.on('zoomend', function() {
    console.log('Current zoom level:', map.getZoom());
});
*/
