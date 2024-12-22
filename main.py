from ultralytics import YOLO
import cv2
import os

# Load YOLO model
model = YOLO('yolov8n.pt')

# Video input
video_path = 'test.mp4'
cap = cv2.VideoCapture(video_path)

# Check if video is successfully opened
if not cap.isOpened():
    print(f"Error: Cannot open video file {video_path}")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second

# Define output path (Downloads folder)
downloads_path = os.path.expanduser('~/Downloads')
output_video_path = os.path.join(downloads_path, 'output.mp4')

# Define VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))


ret = True
while ret:
    ret, frame = cap.read()

    if not ret:
        print("End of video or unable to read frame.")
        break

    # Perform object tracking
    res = model.track(frame, persist=True)

    # Plotting results
    frame_ = res[0].plot()

    # Write the processed frame to output video
    out.write(frame_)

    # Display frame (optional)
    cv2.imshow('frame', frame_)

    # Quit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()  # Save the video file
cv2.destroyAllWindows()

print(f"Output video saved to: {output_video_path}")
