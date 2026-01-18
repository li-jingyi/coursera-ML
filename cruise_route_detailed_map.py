#!/usr/bin/env python3
"""
Creates a detailed static map with coastlines of the Caribbean cruise route.
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

# Define cruise stops with coordinates (lat, lon)
cruise_stops = [
    {"name": "San Juan, PR", "coords": [18.4655, -66.1057], "day": "Start"},
    {"name": "Tortola, BVI", "coords": [18.4207, -64.6399], "day": "Day 2"},
    {"name": "Antigua", "coords": [17.0608, -61.7964], "day": "Day 3"},
    {"name": "Barbados", "coords": [13.1939, -59.5432], "day": "Day 4"},
    {"name": "St. Lucia", "coords": [13.9094, -60.9789], "day": "Day 5"},
    {"name": "St. Maarten", "coords": [18.0425, -63.0548], "day": "Day 6"},
    {"name": "USVI", "coords": [18.3358, -64.8963], "day": "Day 7"},
    {"name": "San Juan, PR", "coords": [18.4655, -66.1057], "day": "Return"}
]

# Other major islands for reference
other_islands = [
    {"name": "Jamaica", "coords": [18.1096, -77.2975]},
    {"name": "Haiti", "coords": [18.9712, -72.2852]},
    {"name": "Dom. Rep.", "coords": [18.7357, -70.1627]},
    {"name": "Cuba", "coords": [21.5218, -77.7812]},
    {"name": "Dominica", "coords": [15.4150, -61.3710]},
    {"name": "Martinique", "coords": [14.6415, -61.0242]},
    {"name": "Guadeloupe", "coords": [16.2650, -61.5510]},
    {"name": "Grenada", "coords": [12.1165, -61.6790]},
    {"name": "St. Vincent", "coords": [13.2528, -61.1971]},
    {"name": "Trinidad", "coords": [10.6918, -61.2225]},
]

# Extract coordinates
lats = [stop["coords"][0] for stop in cruise_stops]
lons = [stop["coords"][1] for stop in cruise_stops]

# Set up the figure with Cartopy projection
fig = plt.figure(figsize=(18, 14))
ax = plt.axes(projection=ccrs.PlateCarree())

# Set extent (lon_min, lon_max, lat_min, lat_max) - wider view to show context
ax.set_extent([-80, -58, 10, 23], crs=ccrs.PlateCarree())

# Add detailed geographic features
ax.add_feature(cfeature.LAND, facecolor='#E8D9B5', edgecolor='black', linewidth=0.5)
ax.add_feature(cfeature.OCEAN, facecolor='#A8D5E2')
ax.add_feature(cfeature.COASTLINE, linewidth=1.2, edgecolor='#2C3E50')
ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.8, edgecolor='gray')
ax.add_feature(cfeature.LAKES, facecolor='#A8D5E2', edgecolor='black', linewidth=0.5)

# Add higher resolution coastlines
ax.coastlines(resolution='10m', linewidth=1.5, color='#2C3E50')

# Plot the cruise route
ax.plot(lons, lats, 'r-', linewidth=3.5, alpha=0.8,
        transform=ccrs.PlateCarree(), zorder=5, label='Cruise Route')

# Add arrows to show direction
for i in range(len(lons)-1):
    mid_lon = (lons[i] + lons[i+1]) / 2
    mid_lat = (lats[i] + lats[i+1]) / 2
    dx = lons[i+1] - lons[i]
    dy = lats[i+1] - lats[i]
    ax.annotate('', xy=(mid_lon + dx*0.1, mid_lat + dy*0.1),
                xytext=(mid_lon - dx*0.1, mid_lat - dy*0.1),
                arrowprops=dict(arrowstyle='->', color='red', lw=2.5),
                transform=ccrs.PlateCarree(), zorder=5)

# Plot cruise stop points
for i, stop in enumerate(cruise_stops):
    if i == 0:
        # Start point
        ax.plot(stop["coords"][1], stop["coords"][0], 'go',
                markersize=20, markeredgecolor='darkgreen',
                markeredgewidth=3, transform=ccrs.PlateCarree(),
                zorder=10, label='Start Port')
    elif i == len(cruise_stops) - 1:
        # End point
        ax.plot(stop["coords"][1], stop["coords"][0], 'rs',
                markersize=20, markeredgecolor='darkred',
                markeredgewidth=3, transform=ccrs.PlateCarree(),
                zorder=10, label='Return Port')
    else:
        # Regular ports
        ax.plot(stop["coords"][1], stop["coords"][0], 'bo',
                markersize=16, markeredgecolor='darkblue',
                markeredgewidth=2.5, transform=ccrs.PlateCarree(),
                zorder=10)

# Add labels for cruise stops (skip duplicate)
for i, stop in enumerate(cruise_stops[:-1]):
    # Adjust label positions
    if stop["name"] == "San Juan, PR":
        xytext = (-25, -30)
        ha = 'right'
    elif stop["name"] == "Barbados":
        xytext = (15, -10)
        ha = 'left'
    elif stop["name"] == "St. Lucia":
        xytext = (-15, 12)
        ha = 'right'
    elif stop["name"] == "Antigua":
        xytext = (15, 5)
        ha = 'left'
    else:
        xytext = (12, 12)
        ha = 'left'

    ax.annotate(f'{stop["name"]}',
                xy=(stop["coords"][1], stop["coords"][0]),
                xytext=xytext, textcoords='offset points',
                fontsize=11, fontweight='bold', ha=ha,
                bbox=dict(boxstyle='round,pad=0.6', facecolor='yellow',
                         alpha=0.85, edgecolor='black', linewidth=1.5),
                transform=ccrs.PlateCarree(), zorder=11)

# Add small markers for other major islands
for island in other_islands:
    ax.plot(island["coords"][1], island["coords"][0], 'o',
            markersize=6, color='gray', alpha=0.6,
            transform=ccrs.PlateCarree(), zorder=3)
    ax.text(island["coords"][1], island["coords"][0],
            f'  {island["name"]}', fontsize=8, color='#555',
            alpha=0.7, style='italic', transform=ccrs.PlateCarree(),
            zorder=3)

# Add gridlines
gl = ax.gridlines(draw_labels=True, linewidth=1, color='gray',
                  alpha=0.5, linestyle='--', zorder=1)
gl.top_labels = False
gl.right_labels = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 11, 'color': '#2C3E50', 'weight': 'bold'}
gl.ylabel_style = {'size': 11, 'color': '#2C3E50', 'weight': 'bold'}

# Add title
plt.title('Caribbean Cruise Route with Detailed Island Coastlines\n' +
          'San Juan → Tortola → Antigua → Barbados → St. Lucia → St. Maarten → USVI → San Juan',
          fontsize=16, fontweight='bold', pad=20, color='#2C3E50')

# Add legend
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(),
          loc='upper left', fontsize=12, framealpha=0.95,
          edgecolor='black', fancybox=True, shadow=True)

# Add info box
info_text = "7-Day Caribbean Cruise\nRound-trip from San Juan\nVisiting 7 Tropical Islands"
props = dict(boxstyle='round', facecolor='wheat', alpha=0.9,
             edgecolor='black', linewidth=2)
ax.text(0.98, 0.02, info_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=props, zorder=12)

plt.tight_layout()
plt.savefig('cruise_route_detailed_map.png', dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("✅ Detailed coastline map saved as 'cruise_route_detailed_map.png'")
print("   This map shows high-resolution coastlines and all major Caribbean islands")
plt.close()
