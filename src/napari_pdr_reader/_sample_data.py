"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/guides.html?#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations

import tempfile


def get_m2020_data():
    """Generates an image"""
    import pdr
    from pdr.downloaders import download_data_and_label

    with tempfile.TemporaryDirectory() as dir:
        url_img = "https://pds-imaging.jpl.nasa.gov/data/mars2020/mars2020_mastcamz_sci_calibrated/data/0061/rad/ZL0_0061_0672355882_040RAD_N0032046ZCAM05036_048050A03.IMG"
        img_path = download_data_and_label(url_img, data_dir=dir)
        data = pdr.read(img_path)["IMAGE"]

    return [(data, {"name": "Ingenuity from Mastcam-Z aboard the NASA Perseverance Mars Rover"})]
