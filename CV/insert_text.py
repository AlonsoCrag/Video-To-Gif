import cv2
import numpy
import random
import os

def TextIntoGif(user):
    randomVideo = random.choice(os.listdir('./delta'))

    video = cv2.VideoCapture(f'./delta/{randomVideo}')

    frame_width = int(video.get(3)) 
    frame_height = int(video.get(4))    
    size = (frame_width, frame_height)

    writer = cv2.VideoWriter(f'./Output_Img/{user}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 60, (1440, 480))

    font = cv2.FONT_HERSHEY_DUPLEX
    text = user.upper()
    textsize = cv2.getTextSize(text, font, 2, 2)[0]
    textX = (frame_width - textsize[0]) // 2
    textY = (frame_height + textsize[1]) // 2


    font = cv2.FONT_HERSHEY_DUPLEX
    text_2 = "Welcome to La Logia".upper()
    textsize_2 = cv2.getTextSize(text_2, font, 2, 2)[0]
    text_2X = (frame_width - textsize_2[0]) // 2
    text_2Y = (frame_height + textsize_2[1]) // 2

    font = cv2.FONT_HERSHEY_DUPLEX
    text_3 = "Enjoy your stay".upper()
    textsize_3 = cv2.getTextSize(text_3, font, 1, 2)[0]
    text_3X = (frame_width - textsize_3[0]) // 2
    text_3Y = (frame_height + textsize_3[1]) // 2


    scale_choosed = 2
    canBlur = True
    first_frame = True

    while True:
        ret, frame = video.read()
        
        if not ret: break

        if scale_choosed <= 1.9:
            scale_choosed += 0.02
        else:
            scale_choosed -= 0.025
        

        if canBlur:
            cv2.putText(frame, text, ((textX + 4) * int(scale_choosed) + 2, ((textY) + 4) * int(scale_choosed)), font, scale_choosed, (245, 135, 66), 4)
            cv2.putText(frame, text, ((textX + 4) * int(scale_choosed), ((textY) + 3) * int(scale_choosed)), font, scale_choosed, (163, 85, 26), 6)
            cv2.putText(frame, text, ((textX + 4) * int(scale_choosed), ((textY) + 3) * int(scale_choosed)), font, scale_choosed, (163, 23, 168), 3)
            cv2.putText(frame, text, (textX, textY), font, scale_choosed, (255, 255, 255), 7)

            cv2.putText(frame, text_2, (text_2X + 5, text_2Y - 70), font, scale_choosed, (163, 85, 26), 7)
            cv2.putText(frame, text_2, (text_2X, text_2Y - 70), font, scale_choosed, (255, 255, 255), 7)

            cv2.putText(frame, text_3, (text_3X + 5, text_3Y + 70), font, 1, (163, 85, 26), 4)
            cv2.putText(frame, text_3, (text_3X, text_3Y + 70), font, 1, (255, 255, 255), 4)

            blured = cv2.GaussianBlur(frame, (35, 35), cv2.BORDER_REFLECT)
            canBlur = False
            # cv2.imshow("Video", blured)
            # cv2.waitKey(20)
            writer.write(blured)
        else:
            cv2.putText(frame, text, ((textX + 4) * int(scale_choosed), ((textY) + 3) * int(scale_choosed)), font, scale_choosed, (163, 23, 168), 4)
            cv2.putText(frame, text, (textX, textY), font, scale_choosed, (255, 255, 255), 6)
            cv2.putText(frame, text_2, (text_2X + 1, text_2Y - 71), font, scale_choosed, (255, 255, 255), 7)
            cv2.putText(frame, text_3, (text_3X + 5, text_3Y + 70), font, 1, (163, 85, 26), 2)
            cv2.putText(frame, text_3, (text_3X, text_3Y + 70), font, 1, (255, 255, 255), 2)
            canBlur = True
        
        if first_frame:
            first_frame = False
            continue
        writer.write(frame)

        # cv2.imshow("Video", frame)
        # cv2.waitKey(20)

    video.release()
    writer.release()
