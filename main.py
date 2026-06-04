#from pydub import AudioSegment

#audio = AudioSegment.from_file("input.flac")
#audio.export("output.mp3", format="mp3", bitrate="192k")


from tkinter import Tk, filedialog
from pydub import AudioSegment

Tk().withdraw()

input_file = filedialog.askopenfilename(
    title="انتخاب فایل صوتی"
)

output_file = filedialog.asksaveasfilename(
    title="ذخیره فایل MP3",
    defaultextension=".mp3",
    filetypes=[("MP3 files", "*.mp3")]
)

audio = AudioSegment.from_file(input_file)
audio.export(output_file, format="mp3")

print("تمام شد")