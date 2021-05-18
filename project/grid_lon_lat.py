from pyproj import Transformer
transformer = Transformer.from_crs(32652, 4326)
print(transformer.transform(326053, 4151242)[0])