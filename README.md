# coursera-ML
Machine Learning

## Caribbean Cruise Route Map 🚢

An interactive visualization of a Caribbean cruise route visiting beautiful islands.

### Cruise Route
1. **San Juan, Puerto Rico** (Departure)
2. **Tortola, British Virgin Islands**
3. **Antigua**
4. **Barbados**
5. **St. Lucia**
6. **St. Maarten**
7. **US Virgin Islands**
8. **San Juan, Puerto Rico** (Return)

### Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate the interactive map:
   ```bash
   python cruise_route_map.py
   ```

3. Generate the detailed coastline map:
   ```bash
   python cruise_route_detailed_map.py
   ```

4. View the maps:
   - Open `caribbean_cruise_map.html` in your browser for interactive map
   - View `cruise_route_detailed_map.png` for detailed coastlines
   - View `cruise_route_map.png` for simple route diagram

### Features

**Interactive HTML Map:**
- Multiple specialized map layers:
  - **Ocean Basemap**: Shows bathymetry (ocean floor depth) and underwater terrain
  - **Physical Map**: Displays terrain relief and elevation features
  - **Shaded Relief**: 3D-like terrain visualization
  - **Satellite View**: Real satellite imagery
  - **National Geographic**: Professional cartographic style
  - **Topographic Map**: Contour lines and elevation data
  - Plus Light/Dark themes for night viewing
- Zoom and pan controls with mini-map
- Color-coded markers for each port of call
- 17+ reference markers for other Caribbean islands
- Route line with cruise path
- Tooltips and detailed popups
- Fullscreen mode
- Distance measurement tool

**Detailed Coastline Map:**
- High-resolution (10m) coastlines of all Caribbean islands
- Ocean bathymetry showing water depth variations (light to dark blue)
- Natural Earth terrain background with realistic elevation shading
- Shows major islands: Cuba, Jamaica, Hispaniola, Puerto Rico, and Lesser Antilles
- Rivers and lakes for enhanced geographic detail
- Accurate geographic projection
- Land topography with natural terrain coloring
- Political boundaries and reference labels
- Professional cartographic styling
