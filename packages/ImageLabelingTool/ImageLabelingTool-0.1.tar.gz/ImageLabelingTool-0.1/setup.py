from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Simplify the process of labeling images or video frames with bounding boxes for object detection tasks.'
LONG_DESCRIPTION = """
ImageLabelingTool is a Python package designed to facilitate the process of labeling images or video frames with bounding boxes for object detection tasks. With ImageLabelingTool, users can annotate objects with bounding boxes and save the annotations in YOLO format. The package provides a graphical user interface for interactive labeling and supports both camera input and video input.
"""

# Setting up
setup(
    name="ImageLabelingTool",
    version=VERSION,
    author="Atri Rathore",
    author_email="<rathoreatri@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Rathoreatri03/Model_Trainer",
    packages=find_packages(),
    install_requires=['opencv-python', 'keyboard'],
    keywords=['python', 'image labeling', 'object detection', 'bounding box annotation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)