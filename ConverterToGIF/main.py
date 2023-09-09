from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *


def convert_mp4_to_gif(path):
    file_name = input("Write file name: ")
    clip = VideoFileClip(path)
    clip.write_gif(file_name)


if __name__ == "__main__":
    # write file name that will be converted to gif
    name = input("Write file name: ")
    convert_mp4_to_gif(name)








