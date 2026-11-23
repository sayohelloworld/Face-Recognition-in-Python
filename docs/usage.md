# Usage Guide

## Reference Images

Place reference images inside the `faces/` directory.

Supported formats:

- JPG
- JPEG
- PNG

The filename of each image is used as the corresponding person's name.

Example:

```text
faces/
├── obama.jpg
├── person_2.jpg
└── person_3.png
```

## Running FaceRec

Start the application:

```bash
python src/face_rec.py
```

Enter the path to the image you want to analyze when prompted.

## Results

FaceRec displays the analyzed image with bounding boxes around detected faces.

Recognized faces are labeled with their corresponding names. Unknown faces are labeled as `Unknown`.