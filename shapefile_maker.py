import geopandas as gpd

# Load the 'Admin 1 – States, Provinces' dataset from the local file
states_provinces = gpd.read_file("./110m_cultural/ne_110m_admin_1_states_provinces.shp")

# Check the column names to identify the correct columns
print(states_provinces.columns)

# Once you identify the columns representing country and state names (assuming they are 'admin' and 'name' as previously),
# Adjust the below filtering if needed based on the column names:
california_baja = states_provinces[
    (states_provinces['admin'] == 'United States of America') & 
    (states_provinces['name'] == 'California') |
    (states_provinces['admin'] == 'Mexico') & 
    ((states_provinces['name'] == 'Baja California') | 
     (states_provinces['name'] == 'Baja California Sur'))
]

# Save to a new shapefile
california_baja.to_file("california_baja_shapefile.shp")

print("Shapefile created!")