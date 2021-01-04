from satsearch import Search
# script uses the selected feature in the toc of QGIS
# tested in qgis 3.10 ltr

layer = iface.activeLayer()
feats = layer.getFeatures()
for feat in feats:
   geom = feat.geometry().boundingBox()
bounds = [geom.xMinimum(), geom.yMinimum(), geom.xMaximum(), geom.yMaximum()]
search = Search(bbox=bounds, datetime='2020-05-01/2020-07-30', collections=['sentinel-s2-l2a-cogs'], url='https://earth-search.aws.element84.com/v0')
items = search.items()
file_url = items[0].asset('red')['href']
rlayer = iface.addRasterLayer(file_url, 'S2_cog')