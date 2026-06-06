from tkinter import Tk, filedialog
from pydub import AudioSegment

Tk().withdraw()

input_file = filedialog.askopenfilename(
    title = "choose mp3 file"
)

output_file = filedialog.asksaveasfilename(
    title = "save mp3",
    defaultextension= ".mp3",
    filetypes=[("MP3 files", "*.mp3")]
)

audio = AudioSegment.from_file(input_file)
audio.export(output_file, format="mp3")

print("the end")
if __name__ == "__main__"_:
    
