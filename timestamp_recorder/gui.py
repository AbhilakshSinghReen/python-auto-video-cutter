from json import dump as json_dump, load as json_load
from os.path import exists
from time import time
import tkinter as tk

from config import (
    SEGMENTS_JSON_FILE_PATH,
)


class TimestampRecorderGUI:
    def __init__(self) -> None:
        self.segments_json_file_path = SEGMENTS_JSON_FILE_PATH

        if not exists(self.segments_json_file_path):
            self.create_empty_segments_file()

        if self.get_num_existing_segments() > 0:
            print("One or more segments already exist in the segments file. Cannot write a START segment. Exiting...")
            exit(1)

        self.set_up_gui()

        self.start_timestamp = None
        self.current_segment_start_timestamp = None
        self.segments = []

    def create_empty_segments_file(self):
        with open(self.segments_json_file_path, 'w') as segments_json_file:
            json_dump([], segments_json_file, indent=4)

    def get_num_existing_segments(self):
        with open(self.segments_json_file_path, 'r') as segments_json_file:
            segments =  json_load(segments_json_file)
        
        return len(segments)

    def set_up_gui(self):
        self.root = tk.Tk()
        self.root.title("Timestamp Recorder")
        
        self.root.minsize(width=300, height=100)

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=5)

        self.keep_button = tk.Button(self.root, text="Keep Segment", command=self.keep_segment)
        self.keep_button.pack(pady=5)
        self.keep_button['state'] = "disabled"

        self.discard_button = tk.Button(self.root, text="Discard Segment", command=self.discard_segment)
        self.discard_button.pack(pady=5)
        self.discard_button['state'] = "disabled"

        self.log_label = tk.Label(self.root, text="Logs will appear here.")
        self.log_label.pack(pady=5)
    
    def start_mainloop(self):
        self.root.mainloop()

    def log(self, log_str):
        print(log_str)
        self.log_label.config(text=log_str)

    def get_recording_elapsed_time_from_timestamp(self, timestamp):
        if self.start_timestamp is None:
            return -1
        
        return timestamp - self.start_timestamp

    def add_segment_to_file(self, segment):
        with open(self.segments_json_file_path, 'r') as segments_json_file:
            segments =  json_load(segments_json_file)

        segments.append(segment)

        with open(self.segments_json_file_path, 'w') as segments_json_file:
            json_dump(segments, segments_json_file, indent=4)
    
    def generate_and_save_new_segment(self, segment_type):
        event_timestamp = time()

        if self.start_timestamp is None:
            self.log("Start timestamp has not been noted. Please not it first.")
            return

        segment_start_time = self.get_recording_elapsed_time_from_timestamp(self.current_segment_start_timestamp)
        segment_end_time = self.get_recording_elapsed_time_from_timestamp(event_timestamp)

        self.current_segment_start_timestamp = event_timestamp

        new_segment = {
            'type': segment_type,
            'startTime': segment_start_time,
            'endTime': segment_end_time
        }

        self.add_segment_to_file(new_segment)

        self.log(f"Segment {'kept' if segment_type == 'KEEP' else 'discarded'}.")

    def start_recording(self):
        event_timestamp = time()

        if self.start_timestamp is not None:
            self.log("Start Timestamp recording has already been noted. Cannot start again.")
            return
        
        self.start_timestamp = event_timestamp
        self.current_segment_start_timestamp = event_timestamp
        self.log("Start Timestamp noted.")

        self.start_button['state'] = "disabled"
        self.keep_button['state'] = "active"
        self.discard_button['state'] = "active"

    def keep_segment(self):
        self.generate_and_save_new_segment("KEEP")

    def discard_segment(self):
        self.generate_and_save_new_segment("DISCARD")


if __name__ == "__main__":
    timestamp_recorder_gui = TimestampRecorderGUI()
    timestamp_recorder_gui.start_mainloop()
