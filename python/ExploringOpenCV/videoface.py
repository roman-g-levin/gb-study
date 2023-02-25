#pip install opencv-python

import cv2

print("Press 'q' key for exit")

# объявляем обработчик для распознавания лиц
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# img = cv2.imread('face.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


# cv2.imshow('Result', img)
# cv2.waitKey(0)

# взять видеопоток с 0 камеры
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('my_video.mp4')

while True:
    success, frame = cap.read() # success - неиспользуемая переменная,
                                # успешно считан кадр или нет
                                # frame - кадр
    # конвертировать в серый цвет
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # распознать лица на сером кадре
    faces = face_cascades.detectMultiScale(img_gray)

    # перебрать все найденные лица и нарисовать прямоугольники
    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Result', frame)
    #cv2.imshow('Result gray', img_gray)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
