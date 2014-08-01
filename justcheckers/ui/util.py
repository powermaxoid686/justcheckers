import os

IMAGE_ASSETS = 'images'
TEXT_ASSETS = 'assets'


def path_to_asset(filename, asset_type=IMAGE_ASSETS):
    """
    Helper utility for getting the path to an asset.

    :param filename: The filename of the asset.
    :param asset_type: The type of asset.  Defaults to images.
    :return: The path to the asset.
    """
    return os.path.join(os.path.dirname(__file__), os.pardir, asset_type.lower(), filename)
