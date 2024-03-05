from moviepy.editor import concatenate_videoclips, VideoFileClip

from data_handling import (
    INPUT_VIDEO_PATH,
    OUTPUT_VIDEO_PATH,
    SEGMENTS_JSON_FILE_PATH,
)


def extract_video_segments(input_file_path, output_file_path, segments):
    input_video = VideoFileClip(input_file_path)

    segment_clips = []

    for start_time, end_time in segments:
        segment = input_video.subclip(start_time, end_time)
        segment_clips.append(segment)

    output_video = concatenate_videoclips(segment_clips)
    output_video.write_videofile(output_file_path)

    input_video.close()


if __name__ == "__main__":
    segments = [(0.5, 10.2), (20.3, 30.7), (40.0, 50.5)]

    extract_video_segments(INPUT_VIDEO_PATH, OUTPUT_VIDEO_PATH, segments)
