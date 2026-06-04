from pydub import AudioSegment

audio = AudioSegment.from_file("input.flac")
audio.export("output.mp3", format="mp3", bitrate="192k")