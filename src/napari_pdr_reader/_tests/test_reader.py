import tempfile

import pdr
import pdr.downloaders

from napari_pdr_reader import napari_get_reader


def get_test_data():
    with tempfile.TemporaryDirectory() as dir:
        url_img = "https://pds-imaging.jpl.nasa.gov/data/mars2020/mars2020_mastcamz_sci_calibrated/data/0061/rad/ZL0_0061_0672355882_040RAD_N0032046ZCAM05036_048050A03.IMG"
        img_path = pdr.downloaders.download_data_and_label(url_img, data_dir=dir)
        return img_path


# tmp_path is a pytest fixture
def test_reader(tmp_path):
    """An example of how you might test your plugin."""

    # write some fake data using your supported file format
    my_test_file = get_test_data()

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_tuple = layer_data_list[0]
    assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None
