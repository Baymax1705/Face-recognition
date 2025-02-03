Here is the `.md` code for your README file:

```md
# Face Detection using OpenCV

## Overview
This project utilizes OpenCV's Haar cascade classifier to detect faces in real-time using a webcam. The script captures video frames, converts them to grayscale, and detects faces using a pre-trained Haar cascade model. Detected faces are highlighted with rectangles.

## Requirements
Ensure you have the following installed:
- Python 3.x
- OpenCV (`cv2` library)

Install OpenCV if not already installed:
```sh
pip install opencv-python
```

## Files Included
- `face_reco.py` - The main script for face detection.
- `haarcascade_frontalface_default.xml` - Pre-trained Haar cascade model for face detection.

## How to Run
1. Connect a webcam to your computer.
2. Run the script using the command:
   ```sh
   python face_reco.py
   ```
3. The webcam window will open and detect faces in real time.
4. Press `d` to exit the program.

## How It Works
1. The script initializes the Haar cascade model for face detection.
2. Captures frames from the webcam.
3. Converts frames to grayscale for better detection accuracy.
4. Detects faces using the `detectMultiScale` function.
5. Draws rectangles around detected faces.
6. Displays the video feed with detected faces in real time.

## Configuration
You can tweak the detection parameters in `face_reco.py`:
- `scaleFactor=1.2`: Adjusts how much the image is reduced at each scale.
- `minNeighbors=5`: Defines how many neighbors each candidate rectangle should have.

## Troubleshooting
- **Webcam not opening?** Ensure that another application is not using the webcam.
- **No faces detected?** Try adjusting `scaleFactor` and `minNeighbors`.

## License
The Haar cascade model is part of OpenCV and follows its license agreement. Ensure you comply with OpenCV's licensing terms before redistribution.
```

Save this as `README.md`, and it will be ready for use. Let me know if you need any modifications! 🚀
