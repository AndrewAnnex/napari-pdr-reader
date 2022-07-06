import tempfile
from pathlib import Path

from napari_pdr_reader import napari_get_reader


# tmp_path is a pytest fixture
def test_reader(tmp_path):
    """An example of how you might test your plugin."""

    # write some fake data using your supported file format
    from pdr.downloaders import download_with_progress_bar

    with tempfile.TemporaryDirectory() as tdir:
        url_img = "https://pds-imaging.jpl.nasa.gov/data/mars2020/mars2020_mastcamz_sci_calibrated/data/0061/rad/ZL0_0061_0672355882_040RAD_N0032046ZCAM05036_048050A03.IMG"
        my_test_file = tdir + "/" + Path(url_img).name
        download_with_progress_bar(url_img, file_path=my_test_file)
        # try to read it back in
        reader = napari_get_reader(my_test_file)
        print(reader, my_test_file)
        assert callable(reader)

        # make sure we're delivering the right format
        layer_data_list = reader(my_test_file)
        assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
        layer_data_tuple = layer_data_list[0]
        assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None
