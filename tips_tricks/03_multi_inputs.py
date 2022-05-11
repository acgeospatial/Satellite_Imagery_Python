import skimage.io
import pandas as pd
from skimage import feature


def main(raster_file):

    img = skimage.io.imread(raster_file, 1)
    print(img.shape)
    img2 = img.reshape(-1)
    df = pd.DataFrame()
    df['Single_Image_band'] = img2


    # canny edge detection
    edges1 = feature.canny(img)
    edges2 = feature.canny(img, sigma=3)
    canny1 = edges1.reshape(-1)
    canny2 = edges2.reshape(-1)
    df['Edges1'] = canny1
    df['Edges2'] = canny2
    print(df.head(10))

    print(df.Edges1.value_counts())
    print(df.Edges2.value_counts())


if __name__ == "__main__":
    raster_path = "../Training_data/South_coast.tif"
    main(raster_path)
