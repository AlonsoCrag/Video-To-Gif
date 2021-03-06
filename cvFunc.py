import cv2
import imageio
from pygifsicle import optimize, gifsicle

def TransformVideo(video, videoName):
    Video = cv2.VideoCapture(video)

    frames = []

    while True:
        ret, frame = Video.read()

        if not ret: break
        frame = cv2.resize(frame, (frame.shape[1] // 4, frame.shape[0] // 4))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame_rgb)

        # cv2.imshow("Video", frame)
        # if cv2.waitKey(20) == ord('q'): break

    print(len(frames))


    Video.release()

    imageio.mimsave(f"gifs/{videoName}.gif", frames, fps=50)

    gifsicle(
        sources=f"gifs/{videoName}.gif", # or a single_file.gif
        destination=f"gifs/{videoName}.gif", # or just omit it and will use the first source provided.
        optimize=True, # Whetever to add the optimize flag of not
        colors=255, # Number of colors t use
    )

    print("Success")



# TransformVideo("../astronaut_crazy.mp4", "astronaut")