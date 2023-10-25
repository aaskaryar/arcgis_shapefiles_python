import os
import pandas as pd
import geopandas as gpd
# from shapely.geometry import Point
path = "C:\\Users\\Gisuser\\SCCWRP\\Staff - P Drive\\Data\\PartTimers\\Aria\\EMPA"
combined_shapefile = "C:\\Users\\Gisuser\\SCCWRP\\Staff - P Drive\\Data\\PartTimers\\Aria\\Lat-long_isin_California\\combined\\california_combined.shp"
combined_gdf = gpd.read_file(combined_shapefile)

path = r"C:\Users\GisUser\SCCWRP\Staff - P Drive\Data\PartTimers\Aria\EMPA\macroalgae\clean\macroalgae_testdata.xlsx"

excel_file = pd.ExcelFile(path)
all_dfs = {}

for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    all_dfs[sheet_name] = df

crosswalk = {
    'transectbeginlongitude': 'longitude',
    'transectbeginlatitude': 'latitude',
}

for key in all_dfs.keys():
    # print(key)
    df = all_dfs[key]
    df.rename(columns=crosswalk, inplace=True)
    # print(df.columns)

# for key, df in all_dfs.items():
#     if ('longitude' in df.columns) and ('latitude' in df.columns):
#         df = df.dropna(subset=['longitude', 'latitude'])        
#         gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude),crs=combined_gdf.crs)  
        
#         within_shapefile = gdf.within(combined_gdf.unary_union)        
#         outside_points = gdf[~within_shapefile]        
#         if not outside_points.empty:
#             print(f"Columns 'longitude' and 'latitude' from the sheet '{key}' have values outside the shapefile bounds.")
#             for _, row in outside_points.iterrows():
#                 print(f"Row: {row.name + 2}, Latitude: {row['latitude']}, Longitude: {row['longitude']}")
# # print(gdf)

for key, df in all_dfs.items():
    if ('longitude' in df.columns) and ('latitude' in df.columns):
        df = df.dropna(subset=['longitude', 'latitude'])        
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude),crs=combined_gdf.crs)  
        
        within_shapefile = gdf.within(combined_gdf.unary_union)        
        outside_points = gdf[~within_shapefile]        
        if not outside_points.empty:
            print(f"Rows from the sheet '{key}' outside the shapefile bounds:")
            for index in outside_points.index:
                # Assuming that the dataframe's index starts at 0, and you want Excel-style row numbers.
                # If the header is included, then we add 2 (1 for the header row and 1 because Excel is 1-based).
                print(index + 2)
