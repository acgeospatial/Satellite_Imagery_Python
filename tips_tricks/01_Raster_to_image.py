import rasterio
from rasterio.plot import reshape_as_raster, reshape_as_image
import numpy as np


def main(raster_file):
    """
    Reads a raster and prints the dimensions and adds a new dimension to single band rasters.
    """
    with rasterio.open(raster_file) as src:
        data = src.read() # gets ALL the data
        single_band = data[0] # gets the first band OR src.read(1

    print (f'Normally expect this shape from rasterio: {data.shape}')
    # https://rasterio.readthedocs.io/en/latest/topics/image_processing.html

    image = reshape_as_image(data)

    print(f'After reshaping as image: {image.shape}')

    reshaped_to_raster = reshape_as_raster(image)

    print(f'After reshaping as raster: {reshaped_to_raster.shape}')

    print('---------------')

    print(f'first band, or a single band image: {single_band.shape}')

    added_dimension = np.expand_dims(single_band, axis=2)

    print(f'After adding a dimension: {added_dimension.shape}')
    print('---------------')
    print(added_dimension[:,:,0])

if __name__ == "__main__":
    raster_path = "../Training_data/South_coast.tif"
    main(raster_path)