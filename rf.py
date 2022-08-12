import cv2
import face_recognition

#img a comparar
image = cv2.imread("IMG/yo.png")
face_log = face_recognition.face_locations(image)[0]
# print("face_locations: ", face_log)
face_image_encoding = face_recognition.face_encodings(image, known_face_locations=[face_log])[0]
# print("face_encodings: ", face_image_encoding)

# cv2.rectangle(image, (face_log[3], face_log[0]), (face_log[1], face_log[2]), (0, 255, 0), 2)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == False:break
    frame = cv2.flip(frame, 1)

    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        for face_location in face_locations:
            face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
            result = face_recognition.compare_faces([face_image_encoding], face_frame_encodings)
            print("Result: ", result)
            if result[0] == True:
                text = "Reconocido"
                color = (125, 220, 0)
            else:
                text = "Desconocido"
                color = (50, 50, 255)
            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
            cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()
