#!/usr/bin/env python3
"""
Creates a static image of the Caribbean cruise route map.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Define cruise stops with coordinates (lat, lon)
cruise_stops = [
    {"name": "San Juan, PR", "coords": [18.4655, -66.1057], "day": "Start/End"},
    {"name": "Tortola, BVI", "coords": [18.4207, -64.6399], "day": "Day 2"},
    {"name": "Antigua", "coords": [17.0608, -61.7964], "day": "Day 3"},
    {"name": "Barbados", "coords": [13.1939, -59.5432], "day": "Day 4"},
    {"name": "St. Lucia", "coords": [13.9094, -60.9789], "day": "Day 5"},
    {"name": "St. Maarten", "coords": [18.0425, -63.0548], "day": "Day 6"},
    {"name": "USVI", "coords": [18.3358, -64.8963], "day": "Day 7"},
    {"name": "San Juan, PR", "coords": [18.4655, -66.1057], "day": "Return"}
]

# Create figure with a nice size
fig, ax = plt.subplots(figsize=(14, 10))
fig.patch.set_facecolor('#E8F4F8')
ax.set_facecolor('#B8E6F5')

# Extract coordinates for plotting
lats = [stop["coords"][0] for stop in cruise_stops]
lons = [stop["coords"][1] for stop in cruise_stops]

# Plot the route line
ax.plot(lons, lats, 'r-', linewidth=2.5, alpha=0.7, zorder=1, label='Cruise Route')

# Add arrow annotations along the route to show direction
for i in range(len(lons)-1):
    dx = lons[i+1] - lons[i]
    dy = lats[i+1] - lats[i]
    ax.annotate('', xy=(lons[i+1], lats[i+1]), xytext=(lons[i], lats[i]),
                arrowprops=dict(arrowstyle='->', color='red', lw=2, alpha=0.6))

# Plot points with different colors for start/end vs ports
for i, stop in enumerate(cruise_stops):
    if i == 0:
        # Start point - green
        ax.plot(stop["coords"][1], stop["coords"][0], 'go',
                markersize=18, markeredgecolor='darkgreen',
                markeredgewidth=2, zorder=3, label='Start Port')
    elif i == len(cruise_stops) - 1:
        # End point - red
        ax.plot(stop["coords"][1], stop["coords"][0], 'rs',
                markersize=18, markeredgecolor='darkred',
                markeredgewidth=2, zorder=3, label='Return Port')
    else:
        # Regular ports - blue
        ax.plot(stop["coords"][1], stop["coords"][0], 'bo',
                markersize=15, markeredgecolor='darkblue',
                markeredgewidth=2, zorder=3)

# Add labels for each stop
for i, stop in enumerate(cruise_stops[:-1]):  # Skip last since it's same as first
    # Adjust label positions to avoid overlap
    if stop["name"] == "San Juan, PR":
        xytext = (-20, -25)
    elif stop["name"] == "Barbados":
        xytext = (10, -15)
    elif stop["name"] == "St. Lucia":
        xytext = (-15, 10)
    else:
        xytext = (10, 10)

    ax.annotate(f'{stop["name"]}\n({stop["day"]})',
                xy=(stop["coords"][1], stop["coords"][0]),
                xytext=xytext, textcoords='offset points',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow',
                         alpha=0.8, edgecolor='black'),
                zorder=4)

# Set axis labels and title
ax.set_xlabel('Longitude', fontsize=12, fontweight='bold')
ax.set_ylabel('Latitude', fontsize=12, fontweight='bold')
ax.set_title('🚢 Caribbean Cruise Route Map 🚢\n' +
             'San Juan → Tortola → Antigua → Barbados → St. Lucia → St. Maarten → USVI → San Juan',
             fontsize=16, fontweight='bold', pad=20, color='#2C3E50')

# Add grid
ax.grid(True, linestyle='--', alpha=0.4, color='gray')

# Set axis limits with some padding
lat_min, lat_max = min(lats), max(lats)
lon_min, lon_max = min(lons), max(lons)
lat_padding = (lat_max - lat_min) * 0.15
lon_padding = (lon_max - lon_min) * 0.15

ax.set_xlim(lon_min - lon_padding, lon_max + lon_padding)
ax.set_ylim(lat_min - lat_padding, lat_max + lat_padding)

# Add legend
handles, labels = ax.get_legend_handles_labels()
# Remove duplicate labels
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),
          loc='upper right', fontsize=11, framealpha=0.9)

# Add a text box with route summary
route_text = "🏝️ Island Paradise Tour 🏝️\n\n" + \
             "7 Amazing Caribbean Islands\n" + \
             "Round-trip from San Juan, PR"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.02, 0.98, route_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('cruise_route_map.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print("✅ Static map image saved as 'cruise_route_map.png'")
plt.close()
