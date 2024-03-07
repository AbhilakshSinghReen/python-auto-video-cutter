from moviepy.editor import concatenate_videoclips, VideoFileClip

from data_handling import (
    INPUT_VIDEO_PATH,
    OUTPUT_VIDEO_PATH,
    get_segments,
)


VIDEO_TIME_OFFSET = 5.000


def extract_video_segments(input_file_path, output_file_path, segments):
    input_video = VideoFileClip(input_file_path)

    segment_clips = []

    for segment in segments:
        start_time = segment['startTime']
        end_time = segment['endTime']
        
        segment = input_video.subclip(start_time, end_time)
        segment_clips.append(segment)

    output_video = concatenate_videoclips(segment_clips)
    output_video.write_videofile(output_file_path)

    input_video.close()


if __name__ == "__main__":
    segments = get_segments()

    for segment in segments:
        segment['startTime'] += VIDEO_TIME_OFFSET
        segment['endTime'] += VIDEO_TIME_OFFSET

    extract_video_segments(INPUT_VIDEO_PATH, OUTPUT_VIDEO_PATH, segments)
