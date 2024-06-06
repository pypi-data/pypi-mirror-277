# ImageLabelingTool

ImageLabelingTool is a Python package designed to facilitate the process of labeling images or video frames with bounding boxes for object detection tasks. With ImageLabelingTool, users can annotate objects with bounding boxes and save the annotations in YOLO format. The package provides a graphical user interface for interactive labeling and supports both camera input and video input.

## Installation

You can install ImageLabelingTool via pip:

```bash
pip install ImageLabelingTool
```

## Usage

To use ImageLabelingTool, follow these steps:

1. Import the `ImageLabeling` class from the package.
2. Create an instance of the `ImageLabeling` class.
3. Call the `run` method to start the labeling tool.

```python
from ImageLabelingTool import ImageLabeling

# Create an instance of the ImageLabeling class
image_labeling = ImageLabeling()

# Run the labeling tool
image_labeling.run()
```

## Features

- Annotate images or video frames with bounding boxes
- Save annotations in YOLO format
- Support for camera input and video input
- Interactive graphical user interface for labeling

## Dependencies

- OpenCV (cv2)
- Keyboard
- Time
- Random
- OS

## License

ImageLabelingTool is licensed under the MIT License. See the [LICENSE](https://github.com/Rathoreatri03/ImageLabelingTool/blob/main/LICENSE) file for details.

## Support

For support, please open an issue on our [GitHub repository](https://github.com/Rathoreatri03/ImageLabelingTool/issues).
```

