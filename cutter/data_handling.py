from os.path import dirname, join


data_dir = join(dirname(dirname(__file__)), "data")

SEGMENTS_JSON_FILE_PATH = join(data_dir, "segments.json")
INPUT_VIDEO_PATH = join(data_dir, "input.mp4")
OUTPUT_VIDEO_PATH = join(data_dir, "output.mp4")
