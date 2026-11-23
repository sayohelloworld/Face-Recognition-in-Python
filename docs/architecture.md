# Architecture

## Overview

FaceRec is built around facial encoding extraction and face comparison.

## Processing Pipeline

1. Load reference images from the `faces/` directory.
2. Extract facial encodings from each reference image.
3. Load the test image.
4. Detect faces and extract their encodings.
5. Compare detected faces against known encodings.
6. Identify matching faces.
7. Display the results using OpenCV.

## Main Components

| Component | Responsibility |
|---|---|
| Reference loader | Loads known faces and their names |
| Face encoder | Extracts facial encodings |
| Recognition function | Compares faces |
| OpenCV | Displays the analyzed image |