# YOLOv8 Object Detection and Tracking

This project demonstrates how to use the YOLOv8 object detection model from the Ultralytics library to process a video, perform object tracking, and save the results to an output video file.

---

## Features
- Real-time object detection and tracking using YOLOv8.
- Input: Process a given video file (e.g., test.mp4).
- Output: Save the processed video with bounding boxes into the Downloads folder.

---

## Setup Instructions
To run this project, perform the following steps:

### 1. Clone the Repository
```bash
git clone https://github.com/username/YourProject.git
cd YourProject
```

### 2. Install Dependencies
Make sure Python 3.8+ and `pip` are installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Add Your Video File
Place your video file in the project directory, or modify the `video_path` in `main.py` to set your custom path.

### 4. Run the Code
Run the following command:
```bash
python main.py
```

---

## Dependencies
This project requires the following Python packages:
- `ultralytics`
- `opencv-python`

To install the dependencies automatically, use:
```bash
pip install -r requirements.txt
```


## Output
The processed video with tracking results will be saved in your `Downloads` folder as `output.mp4`.

---

## License
This project is open source and available under the MIT License. Feel free to use, modify, and distribute this code.
