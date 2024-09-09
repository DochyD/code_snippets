"""Construct movie using frames with opencv."""

import os
import cv2
import path_utils

def construct_movie_from_frames_opencv(frame_pattern, output_video, total_frames, fps=24):
    """Extract frames function."""
    # Read the first frame to get its width, height (this will be used to set the video size)
    first_frame = cv2.imread(frame_pattern % 1)  # Read frame_0001.png (start with first frame)
    if first_frame is None:
        print(f"Error: Could not read the first frame using the pattern {frame_pattern % 1}")
        return

    height, width, _ = first_frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (e.g., 'mp4v' for .mp4 files)
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # Write each frame to the video based on the pattern
    for i in range(1, total_frames + 1):
        frame_file = frame_pattern % i  # Generate frame filename like frame_0001.png
        frame = cv2.imread(frame_file)
        if frame is None:
            print(f"Warning: Could not read frame {frame_file}, skipping.")
            continue
        video_writer.write(frame)

    # Release the VideoWriter
    video_writer.release()
    print(f"Video created: {output_video}")

# Usage
BASE_DIR = os.path.join(path_utils.get_project_dir(),'movie_and_frames', 'frames_to_movie')
FRAMES_FOLDER = os.path.join(BASE_DIR, 'input_data', 'ffmpeg')
FRAMES_PATERN = os.path.join(BASE_DIR, 'input_data', 'ffmpeg', 'frame_%04d.png')
OUTPUT_PATH = os.path.join(BASE_DIR, 'output_data', 'output_mov_opencv.mp4')
_, _, files = next(os.walk(FRAMES_FOLDER))
NUMBER_FRAMES = len(files)
construct_movie_from_frames_opencv(FRAMES_PATERN, OUTPUT_PATH, NUMBER_FRAMES)
