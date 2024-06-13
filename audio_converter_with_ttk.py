import moviepy.editor
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_video_to_audio():
  
    root = tk.Tk()
    root.withdraw()  

    
    video_file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.mkv;*.avi;*.mov")])
    
    if not video_file_path:
        print("No video file selected. Exiting...")
        return

   
    video = moviepy.editor.VideoFileClip(video_file_path)

  
    if video.audio is None:
        messagebox.showerror("Error", "The selected video does not contain an audio track.")
        return

 
    audio = video.audio

    
    audio_file_path = filedialog.asksaveasfilename(title="Save Audio File", defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    
    if not audio_file_path:
        print("No save location specified. Exiting...")
        return

   
    audio.write_audiofile(audio_file_path)
    print(f"Audio file saved to {audio_file_path}")

if __name__ == "__main__":
    convert_video_to_audio()
