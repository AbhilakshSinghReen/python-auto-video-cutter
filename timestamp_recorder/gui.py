import tkinter as tk

def start_recording():
    print("Start Recording")

def keep_segment():
    print("Keep Segment")

def discard_segment():
    print("Discard Segment")

# Create the main application window
root = tk.Tk()
root.title("Timestamp Recorder")

root.minsize(width=300, height=100)

# Create buttons
start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=5)

keep_button = tk.Button(root, text="Keep Segment", command=keep_segment)
keep_button.pack(pady=5)

discard_button = tk.Button(root, text="Discard Segment", command=discard_segment)
discard_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
