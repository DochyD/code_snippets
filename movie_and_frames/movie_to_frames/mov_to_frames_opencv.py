"""split movie into frames using opencv"""

import os
import cv2
import path_utils

def extract_frames_opencv(video_path, output_folder):
    """Extract frames function."""
    # Open the video file
    vidcap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not vidcap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read and save frames
    success, frame = vidcap.read()
    count = 0

    while success:
        # Save frame as JPEG file
        frame_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        print(f"Saved frame {count}")

        # Read next frame
        success, frame = vidcap.read()
        count += 1

    # Release the video capture object
    vidcap.release()
    print("Finished extracting frames")

# Usage
BASE_DIR = path_utils.get_project_dir()
VIDEO_PATH = os.path.join(BASE_DIR, 'input_data', 'input_video.mp4')  # Specify the path to your video file
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output_data', 'opencv')   # Specify the output folder for saving frames

extract_frames_opencv(VIDEO_PATH, OUTPUT_FOLDER)
