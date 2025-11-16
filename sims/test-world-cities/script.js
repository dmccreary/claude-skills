/**
 * Test Map: Major World Cities
 */

// Map configuration
const mapConfig = {
    center: [20, 0],  // Centered on equator
    zoom: 2,
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

// Add tile layer (OpenStreetMap)
const tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18,
    tileSize: 256
}).addTo(map);

// Define markers for major world cities
const markers = [
    {
        lat: 40.7128,
        lng: -74.0060,
        title: "New York City",
        description: "The largest city in the United States and a global financial center.",
        link: "https://en.wikipedia.org/wiki/New_York_City"
    },
    {
        lat: 51.5074,
        lng: -0.1278,
        title: "London",
        description: "The capital and largest city of England and the United Kingdom.",
        link: "https://en.wikipedia.org/wiki/London"
    },
    {
        lat: 35.6762,
        lng: 139.6503,
        title: "Tokyo",
        description: "The capital of Japan and the most populous metropolitan area in the world.",
        link: "https://en.wikipedia.org/wiki/Tokyo"
    },
    {
        lat: -33.8688,
        lng: 151.2093,
        title: "Sydney",
        description: "The largest city in Australia, known for its harbor and Opera House.",
        link: "https://en.wikipedia.org/wiki/Sydney"
    },
    {
        lat: 19.4326,
        lng: -99.1332,
        title: "Mexico City",
        description: "The capital and largest city of Mexico, one of the most populous in the Americas.",
        link: "https://en.wikipedia.org/wiki/Mexico_City"
    },
    {
        lat: -23.5505,
        lng: -46.6333,
        title: "São Paulo",
        description: "The largest city in Brazil and South America, a major financial center.",
        link: "https://en.wikipedia.org/wiki/S%C3%A3o_Paulo"
    },
    {
        lat: 55.7558,
        lng: 37.6173,
        title: "Moscow",
        description: "The capital and largest city of Russia, a major political and cultural center.",
        link: "https://en.wikipedia.org/wiki/Moscow"
    },
    {
        lat: 28.6139,
        lng: 77.2090,
        title: "New Delhi",
        description: "The capital of India, part of the National Capital Territory of Delhi.",
        link: "https://en.wikipedia.org/wiki/New_Delhi"
    },
    {
        lat: 30.0444,
        lng: 31.2357,
        title: "Cairo",
        description: "The capital of Egypt and one of the largest cities in Africa and the Middle East.",
        link: "https://en.wikipedia.org/wiki/Cairo"
    },
    {
        lat: -1.2921,
        lng: 36.8219,
        title: "Nairobi",
        description: "The capital and largest city of Kenya, a major economic hub in East Africa.",
        link: "https://en.wikipedia.org/wiki/Nairobi"
    }
];

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
