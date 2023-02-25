#pip install opencv-python

import cv2

print("Press 'q' key for exit")

# взять видеопоток с 0 камеры
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('my_video.mp4')

while True:
    success, frame = cap.read() # success - успешно считан кадр или нет
                                # frame - кадр

    if not success:
        break           # выйти из цикла, если слетел поток

    cv2.imshow('Result', frame)     # показать фрейм

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 
