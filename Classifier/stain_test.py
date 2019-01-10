import staintools
from matplotlib import pyplot as plt
# # Read data
# target = staintools.read_image("from.png")
# to_transform = staintools.read_image("test.png")
#
# # Standardize brightness (This step is optional but can improve the tissue mask calculation)
# standardizer = staintools.BrightnessStandardizer()
# target = standardizer.transform(target)
# to_transform = standardizer.transform(to_transform)
#
# # Stain normalize
# normalizer = staintools.StainNormalizer(method='vahadane')
# normalizer.fit(target)
# transformed = normalizer.transform(to_transform)
#
# plt.imshow(transformed)
# plt.show()
#
# colorizer = staintools.ReinhardColorNormalizer()
# colorizer.fit(target)

def transform(image, target_im):
    # Read data
    target = staintools.read_image(image)
    to_transform = staintools.read_image(target_im)

    # Standardize brightness (This step is optional but can improve the tissue mask calculation)
    standardizer = staintools.BrightnessStandardizer()
    target = standardizer.transform(target)
    to_transform = standardizer.transform(to_transform)

    # Stain normalize
    normalizer = staintools.StainNormalizer(method='vahadane')
    normalizer.fit(target)
    transformed = normalizer.transform(to_transform)
    return transformed

if __name__ == '__main__':
    transformed = transform("from.png", "test.png")
    print(type(transformed))
    plt.imshow(transformed)
    plt.show()



