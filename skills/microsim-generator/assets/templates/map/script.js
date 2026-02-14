/* Leaflet Map MicroSim Script Template
 * =====================================
 * Provides core functionality for Leaflet.js map visualizations:
 * - Loads data from data.json
 * - Creates and configures Leaflet map
 * - Supports choropleth maps with GeoJSON
 * - Supports marker-based maps
 * - Handles hover interactions with info panel
 *
 * CUSTOMIZATION POINTS (marked with TODO):
 * - Map center and zoom level
 * - Color scales for choropleth
 * - Info panel content
 * - Feature styling
 */

// ===========================================
// CONFIGURATION - Customize these values
// ===========================================

// TODO: Set your map's initial view
const MAP_CONFIG = {
    center: [39.5, -98.5],  // [lat, lng] - Center of continental US
    zoom: 4,                 // Initial zoom level
    minZoom: 2,
    maxZoom: 18
};

// TODO: GeoJSON source for boundaries (choropleth maps)
// Set to null for marker-only maps
const GEOJSON_URL = 'https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json';

// Local data file
const DATA_URL = 'data.json';

// TODO: Define color scale for choropleth
const colorScale = {
    high: '#1a5e1a',    // Best/highest values
    medHigh: '#4CAF50',
    medium: '#FFC107',
    medLow: '#FF9800',
    low: '#8B0000'      // Worst/lowest values
};

// ===========================================
// STATE VARIABLES
// ===========================================
let map;
let geojsonLayer;
let mapData = {};
let infoControl;

// ===========================================
// UTILITY FUNCTIONS
// ===========================================

/**
 * Format number as currency
 */
function formatCurrency(value) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        maximumFractionDigits: 0
    }).format(value);
}

/**
 * Format number with commas
 */
function formatNumber(value) {
    return new Intl.NumberFormat('en-US').format(value);
}

/**
 * Get color based on value
 * TODO: Customize thresholds for your data
 */
function getColor(value) {
    return value > 80 ? colorScale.high :
           value > 60 ? colorScale.medHigh :
           value > 40 ? colorScale.medium :
           value > 20 ? colorScale.medLow :
                        colorScale.low;
}

// ===========================================
// DATA LOADING
// ===========================================

/**
 * Load map data from data.json
 */
async function loadMapData() {
    try {
        const response = await fetch(DATA_URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        mapData = await response.json();
        return true;
    } catch (error) {
        console.error('Error loading map data:', error);
        document.getElementById('map').innerHTML =
            '<div class="error">Error loading map data. Please refresh the page.</div>';
        return false;
    }
}

/**
 * Load GeoJSON boundaries (for choropleth maps)
 */
async function loadGeoJSON() {
    if (!GEOJSON_URL) return null;

    try {
        const response = await fetch(GEOJSON_URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error loading GeoJSON:', error);
        return null;
    }
}

// ===========================================
// MAP INITIALIZATION
// ===========================================

/**
 * Initialize the Leaflet map
 */
function initializeMap() {
    map = L.map('map', {
        zoomControl: true,
        // Prevent iframe scroll hijacking in chapter pages; enable only if explicitly required.
        scrollWheelZoom: false
    }).setView(MAP_CONFIG.center, MAP_CONFIG.zoom);

    // Add tile layer (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: MAP_CONFIG.maxZoom
    }).addTo(map);

    // Initialize info control
    initInfoControl();
}

/**
 * Initialize the info panel control
 */
function initInfoControl() {
    infoControl = L.control({ position: 'topright' });

    infoControl.onAdd = function(map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    infoControl.update = function(props) {
        // TODO: Customize default and hover content
        if (!props) {
            this._div.innerHTML = '<h4>Map Title</h4>' +
                '<p>Hover over a feature for details</p>';
            return;
        }

        // TODO: Customize info panel content for your data
        let html = `<h4>${props.name}</h4>`;
        html += `<p>Value: ${props.value || 'N/A'}</p>`;
        this._div.innerHTML = html;
    };

    infoControl.addTo(map);
}

// ===========================================
// CHOROPLETH MAP FUNCTIONS
// ===========================================

/**
 * Style function for GeoJSON features
 */
function styleFeature(feature) {
    const name = feature.properties.name;
    const data = mapData.features ? mapData.features[name] : null;
    const value = data ? data.value : 0;

    return {
        fillColor: getColor(value),
        weight: 1,
        opacity: 1,
        color: 'white',
        fillOpacity: 0.7
    };
}

/**
 * Highlight feature on hover
 */
function highlightFeature(e) {
    const layer = e.target;

    layer.setStyle({
        weight: 3,
        color: '#333',
        fillOpacity: 0.9
    });

    layer.bringToFront();

    // Update info panel
    const name = layer.feature.properties.name;
    const data = mapData.features ? mapData.features[name] : null;
    infoControl.update({ name: name, ...data });
}

/**
 * Reset feature style on mouse out
 */
function resetHighlight(e) {
    geojsonLayer.resetStyle(e.target);
    infoControl.update();
}

/**
 * Zoom to feature on click
 */
function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

/**
 * Set up event handlers for each feature
 */
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

/**
 * Add GeoJSON layer to map
 */
function addGeoJSONLayer(geoData) {
    geojsonLayer = L.geoJSON(geoData, {
        style: styleFeature,
        onEachFeature: onEachFeature
    }).addTo(map);
}

// ===========================================
// MARKER MAP FUNCTIONS
// ===========================================

/**
 * Add markers to map from data
 * TODO: Customize for your data structure
 */
function addMarkers() {
    if (!mapData.markers) return;

    mapData.markers.forEach(marker => {
        const m = L.marker([marker.lat, marker.lng])
            .addTo(map)
            .bindPopup(`
                <div class="popup-title">${marker.name}</div>
                <div class="popup-content">${marker.description || ''}</div>
            `);

        // Optional: Add hover effect
        m.on('mouseover', function() {
            this.openPopup();
        });
    });
}

// ===========================================
// INITIALIZATION
// ===========================================

/**
 * Main initialization function
 */
async function init() {
    // Load map data
    const dataLoaded = await loadMapData();
    if (!dataLoaded) return;

    // Initialize map
    initializeMap();

    // Load and add GeoJSON if configured (choropleth)
    if (GEOJSON_URL) {
        const geoData = await loadGeoJSON();
        if (geoData) {
            addGeoJSONLayer(geoData);
        }
    }

    // Add markers if present in data
    addMarkers();
}

// Start initialization when DOM is ready
document.addEventListener('DOMContentLoaded', init);
