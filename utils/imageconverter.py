import os
from PIL import Image


class ImageConverter:
    """ Util class for image conversion. """
    def __init__(self, old_extension: str, new_extension: str) -> None:
        """
        Create an image converter.
        :param old_extension: the image extension to convert.
        :param new_extension: the extension of the converted image.
        """
        self._old_extension = old_extension
        self._new_extension = new_extension

    def _makedirs(self, root: str, dirs: list[str]) -> None:
        """
        Create directories to place the new images in.
        :param root:
        :param dirs: the directories to create.
        """
        for directory in dirs:
            dir_path = os.path.join(root.replace(self._old_extension, self._new_extension), directory)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

    def convert_image(self, img_src: str) -> None:
        """
        Convert a single image.
        :param img_src: the location of the image to convert.
        """
        img_target = img_src.replace(self._old_extension, self._new_extension)
        with Image.open(img_src) as img:
            img.save(img_target)

    def convert_ds(self, root: str) -> None:
        """
        Convert all images in a given folder.
        :param root: the directory containing the images.
        """
        for root, dirs, files in os.walk(root):
            self._makedirs(root, dirs)
            for file in files:
                if file.endswith(self._old_extension):
                    img_src = os.path.join(root, file)
                    self.convert_image(img_src)


converter = ImageConverter('tif', 'png')
converter.convert_ds('../data/tifimages/')
