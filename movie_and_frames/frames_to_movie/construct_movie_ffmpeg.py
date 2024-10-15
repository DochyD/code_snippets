"""Construct movie using frames with ffmpeg."""

import os
import path_utils
import ffmpeg

BASE_DIR = path_utils.get_project_dir()
INPUT_PATERN = os.path.join(BASE_DIR, 'input_data', 'ffmpeg', 'frame_%04d.png')
OUTPUT_PATH = os.path.join(BASE_DIR, 'output_data', 'output_mov_ffmpeg.mp4')

# Function to create a video from frames using ffmpeg-python
def construct_movie_from_frames_ffmpeg(input_pattern, output_video, fps=24):
    """Create mp4 from frames using ffmpeg."""
    try:
        # Use ffmpeg to create a video from the image sequence
        (
            ffmpeg
            .input(input_pattern, framerate=fps)  # input pattern and framerate
            .output(output_video, pix_fmt='yuv420p')  # output video file
            .run(overwrite_output=True)  # overwrite if output file exists
        )
        print(f"Video created: {output_video}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr}")

construct_movie_from_frames_ffmpeg(INPUT_PATERN, OUTPUT_PATH)
