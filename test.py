import tkinter as tk 
from tkinter import filedialog
from pydub import AudioSegment


def MP3_saver():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title = "Choose MP3",
        filetypes = [("MP3 Files", "*.mp3")]
    )

    return file_path

def cut(audio = ""):
    audio = AudioSegment.from_file(audio)
    start = int(input("Start second: "))
    end = int(input("End second: "))
    clip = audio[start * 1000:end * 1000]
    clip.export("output.mp3", format="mp3")
    clip = cut(clip)

    save_path = filedialog.asksaveasfilename(
    title="Save MP3",
    defaultextension=".mp3",
    filetypes=[("MP3 Files", "*.mp3")])

    clip.export(save_path, format="mp3")


def main() -> None:
    file_path = MP3_saver()
    file_path = cut(file_path)
 

if __name__ == "__main__":
    main()
