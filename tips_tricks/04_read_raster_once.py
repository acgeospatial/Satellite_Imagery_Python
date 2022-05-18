import rasterio
import numpy as np
import pandas as pd
import geopandas as gpd


def main(raster_file):

    with rasterio.open(raster_file) as src:
        band1 = src.read(1)
        print(src.crs)

    # create a list random points in the raster
    x = np.random.randint(0, src.width, size=10)
    y = np.random.randint(0, src.height, size=10)

    # extract the values of the raster at the random points
    values = band1[y, x]
    print(type(values))
    print (values)

    # create a dataframe with the random points and the values
    df = pd.DataFrame({'x': x, 'y': y, 'values': values})

    # convert row and column to x coord and y coord
    df['xcoord'] = df['x'] * src.res[0] + src.bounds.left
    df['ycoord'] = df['y'] * src.res[1] + src.bounds.bottom

    # convert dataframe to geopandas
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.xcoord, df.ycoord))
    # set crs
    gdf.crs = src.crs

    # save to shapefile
    gdf.to_file(raster_file.replace('.tif', '.shp'))


if __name__ == '__main__':
    raster_path = "../Training_data/South_coast.tif"
    main(raster_path)
