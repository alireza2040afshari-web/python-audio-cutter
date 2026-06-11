import tkinter as tk 
from tkinter import filedialog

def MP3_saver():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title = "Choose MP3",
        filetypes = [("MP3 Files", "*.mp3")]
    )


def main() -> None:
    file_path = MP3_saver()
 

if __name__ == "__main__":
    main()