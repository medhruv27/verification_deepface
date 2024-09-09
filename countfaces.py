import cv2
import os
import dlib

# Initialize video capture
video = cv2.VideoCapture(0)

# Initialize the face detector
detector = dlib.get_frontal_face_detector()

# Create the directory if it doesn't exist
if not os.path.exists('testimage'):
    os.makedirs('testimage')

# Frame counter to give unique names to saved images
frame_counter = 0
saved_frames = 0

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    num = 0
    for face in faces:
        x, y = face.left(), face.top()
        hi, wi = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (hi, wi), (0, 0, 255), 2)
        num += 1
        cv2.putText(frame, 'face' + str(num), (x - 12, y - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # If exactly two faces are detected, save the frame
    if num == 2 and saved_frames < 10:
        frame_name = os.path.join('testimage', f'frame_{frame_counter}.jpg')
        cv2.imwrite(frame_name, frame)
        frame_counter += 1
        saved_frames += 1
        print(f'Saved: {frame_name}')
    if saved_frames >= 10:
        print("10 frames saved. Stopping further saves.")
        break
    cv2.imshow('faces', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
