#!/usr/bin/env python3
"""
Caribbean Cruise Route Map Visualizer
Creates an interactive map showing the cruise route through the Caribbean islands.
"""

import folium
from folium import plugins


def create_cruise_map():
    """Create an interactive map of the Caribbean cruise route."""

    # Define cruise stops with coordinates (lat, lon)
    cruise_stops = [
        {"name": "San Juan, Puerto Rico", "coords": [18.4655, -66.1057], "day": "Start/End"},
        {"name": "Tortola, British Virgin Islands", "coords": [18.4207, -64.6399], "day": "Day 2"},
        {"name": "Antigua", "coords": [17.0608, -61.7964], "day": "Day 3"},
        {"name": "Barbados", "coords": [13.1939, -59.5432], "day": "Day 4"},
        {"name": "St. Lucia", "coords": [13.9094, -60.9789], "day": "Day 5"},
        {"name": "St. Maarten", "coords": [18.0425, -63.0548], "day": "Day 6"},
        {"name": "US Virgin Islands", "coords": [18.3358, -64.8963], "day": "Day 7"},
        {"name": "San Juan, Puerto Rico", "coords": [18.4655, -66.1057], "day": "Return"}
    ]

    # Other major Caribbean islands for reference
    other_islands = [
        {"name": "Jamaica", "coords": [18.1096, -77.2975]},
        {"name": "Haiti", "coords": [18.9712, -72.2852]},
        {"name": "Dominican Republic", "coords": [18.7357, -70.1627]},
        {"name": "Cuba", "coords": [21.5218, -77.7812]},
        {"name": "Dominica", "coords": [15.4150, -61.3710]},
        {"name": "Martinique", "coords": [14.6415, -61.0242]},
        {"name": "Guadeloupe", "coords": [16.2650, -61.5510]},
        {"name": "Grenada", "coords": [12.1165, -61.6790]},
        {"name": "St. Vincent", "coords": [13.2528, -61.1971]},
        {"name": "Trinidad", "coords": [10.6918, -61.2225]},
        {"name": "Tobago", "coords": [11.1870, -60.7260]},
        {"name": "Aruba", "coords": [12.5211, -69.9683]},
        {"name": "Curaçao", "coords": [12.1696, -68.9900]},
        {"name": "St. Kitts", "coords": [17.3578, -62.7830]},
        {"name": "Nevis", "coords": [17.1508, -62.5789]},
        {"name": "Montserrat", "coords": [16.7425, -62.1874]},
        {"name": "Anguilla", "coords": [18.2206, -63.0686]},
    ]

    # Calculate center point for map (average of all coordinates)
    center_lat = sum(stop["coords"][0] for stop in cruise_stops) / len(cruise_stops)
    center_lon = sum(stop["coords"][1] for stop in cruise_stops) / len(cruise_stops)

    # Create base map centered on the Caribbean with terrain view
    cruise_map = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=7,
        tiles='OpenStreetMap'
    )

    # Add alternative tile layers with detailed coastlines and terrain
    folium.TileLayer('OpenTopoMap', name='Topographic Map').add_to(cruise_map)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Satellite View',
        overlay=False,
        control=True
    ).add_to(cruise_map)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Terrain View',
        overlay=False,
        control=True
    ).add_to(cruise_map)
    folium.TileLayer('CartoDB positron', name='Light Map').add_to(cruise_map)
    folium.TileLayer('CartoDB dark_matter', name='Dark Map').add_to(cruise_map)

    # Draw the route line
    route_coords = [stop["coords"] for stop in cruise_stops]
    folium.PolyLine(
        route_coords,
        color='#FF6B6B',
        weight=3,
        opacity=0.8,
        popup='Cruise Route'
    ).add_to(cruise_map)

    # Add markers for each stop
    for i, stop in enumerate(cruise_stops):
        # Use different icons for start/end vs regular stops
        if i == 0:
            icon = folium.Icon(color='green', icon='play', prefix='fa')
            popup_text = f"<b>{stop['name']}</b><br>{stop['day']}<br>🚢 Departure Port"
        elif i == len(cruise_stops) - 1:
            icon = folium.Icon(color='red', icon='stop', prefix='fa')
            popup_text = f"<b>{stop['name']}</b><br>{stop['day']}<br>🏁 Return Port"
        else:
            icon = folium.Icon(color='blue', icon='anchor', prefix='fa')
            popup_text = f"<b>{stop['name']}</b><br>{stop['day']}<br>⚓ Port of Call"

        # Add marker with popup
        folium.Marker(
            location=stop["coords"],
            popup=folium.Popup(popup_text, max_width=200),
            tooltip=stop["name"],
            icon=icon
        ).add_to(cruise_map)

        # Add circle markers for visual emphasis
        folium.CircleMarker(
            location=stop["coords"],
            radius=8,
            color='white',
            fillColor='#FF6B6B' if i in [0, len(cruise_stops)-1] else '#4A90E2',
            fillOpacity=0.7,
            weight=2
        ).add_to(cruise_map)

    # Add a title using HTML
    title_html = '''
    <div style="position: fixed;
                top: 10px;
                left: 50px;
                width: 400px;
                height: 90px;
                background-color: white;
                border:2px solid grey;
                border-radius: 5px;
                z-index:9999;
                font-size:14px;
                padding: 10px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
                ">
    <h4 style="margin:0; color:#2C3E50;">🚢 Caribbean Cruise Route Map</h4>
    <p style="margin:5px 0 0 0; color:#555;">
        <b>Route:</b> San Juan → Tortola → Antigua → Barbados →
        St. Lucia → St. Maarten → USVI → San Juan
    </p>
    </div>
    '''
    cruise_map.get_root().html.add_child(folium.Element(title_html))

    # Add fullscreen button
    plugins.Fullscreen(
        position='topright',
        title='Fullscreen',
        title_cancel='Exit Fullscreen',
        force_separate_button=True
    ).add_to(cruise_map)

    # Add layer control
    folium.LayerControl().add_to(cruise_map)

    # Add measure control for distances
    plugins.MeasureControl(position='bottomleft').add_to(cruise_map)

    # Add markers for other Caribbean islands (reference points)
    for island in other_islands:
        folium.CircleMarker(
            location=island["coords"],
            radius=4,
            color='gray',
            fillColor='lightgray',
            fillOpacity=0.5,
            weight=1,
            popup=folium.Popup(f"<b>{island['name']}</b><br>Reference Island", max_width=150),
            tooltip=island["name"]
        ).add_to(cruise_map)

    # Add minimap for context
    minimap = plugins.MiniMap(toggle_display=True, position='bottomright')
    cruise_map.add_child(minimap)

    return cruise_map


def main():
    """Main function to generate and save the cruise map."""
    print("🗺️  Generating Caribbean cruise route map...")

    cruise_map = create_cruise_map()
    output_file = "caribbean_cruise_map.html"
    cruise_map.save(output_file)

    print(f"✅ Map successfully created and saved as '{output_file}'")
    print(f"📍 Open the file in your web browser to view the interactive map!")

    # Print route summary
    print("\n🚢 Cruise Route Summary:")
    print("=" * 50)
    stops = [
        "San Juan, Puerto Rico (Start)",
        "Tortola, British Virgin Islands",
        "Antigua",
        "Barbados",
        "St. Lucia",
        "St. Maarten",
        "US Virgin Islands",
        "San Juan, Puerto Rico (Return)"
    ]
    for i, stop in enumerate(stops, 1):
        print(f"  {i}. {stop}")
    print("=" * 50)


if __name__ == "__main__":
    main()
