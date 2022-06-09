from moviepy.editor import *
import random

def BorderVideo(user):
    colors = [
        (92, 36, 181),
        (181, 36, 55),
        (36, 181, 99),
        (181, 82, 36)
    ]

    color = random.choice(colors)

    video = VideoFileClip(f"./Output_Img/{user}.avi")
    # print(vfx.margin)
    marg = vfx.margin(video, mar=40, color=(18, 18, 18))
    marg.write_videofile(f'./Output_Img/{user}.mp4')