"""split movie into frames using ffmpeg"""

import os
import path_utils
import ffmpeg

BASE_DIR = path_utils.get_project_dir()
VIDEO_PATH = os.path.join(BASE_DIR, 'input_data', 'input_video.mp4')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output_data', 'ffmpeg')

# Function to extract frames using ffmpeg
def extract_frames_ffmpeg(video_path, output_folder):
    """Extract frames from mp4"""
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Set the output file pattern (frame_%04d.png will save as frame_0001.png, frame_0002.png, etc.)
    output_pattern = os.path.join(output_folder, "frame_%04d.png")

    # Run the ffmpeg command to extract frames
    (
        ffmpeg
        .input(video_path)
        .output(output_pattern)
        .run(overwrite_output=True)
    )
    print(f"Frames extracted to {output_folder}")

extract_frames_ffmpeg(VIDEO_PATH, OUTPUT_FOLDER)
