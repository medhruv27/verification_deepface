# import cv2
# import glob
# import os
# from deepface import DeepFace

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # Paths for input and output directories
# input_path = 'testimage/*.jpeg'
# output_dir = "output"
# os.makedirs(output_dir, exist_ok=True)

# verified_count = 0
# total_frames = 10
# frame_number = 1

# img_list = glob.glob(input_path)

# for file in img_list:
#     img = cv2.imread(file, 1)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
#     if len(faces) < 2:
#         print(f"Less than 2 faces detected in {file}. Skipping this frame.")
#         continue
    
#     # Extract and save the two faces from the frame
#     for i, (x, y, w, h) in enumerate(faces[:2]):
#         roi_color = img[y:y + h, x:x + w]
#         resized = cv2.resize(roi_color, (128, 128))
#         output_file = os.path.join(output_dir, f"frame_{frame_number}_face_{i+1}.jpg")
#         cv2.imwrite(output_file, resized)
#         print(f"Saved face {i+1} from frame {frame_number} as {output_file}")
    
#     # Verify the two faces in the current frame
#     img1_path = os.path.join(output_dir, f"frame_{frame_number}_face_1.jpg")
#     img2_path = os.path.join(output_dir, f"frame_{frame_number}_face_2.jpg")
    
#     if os.path.exists(img1_path) and os.path.exists(img2_path):
#         result = DeepFace.verify(img1_path=img1_path, img2_path=img2_path, detector_backend="retinaface")
#         if result['verified']:
#             verified_count += 1
#             print(f"Identity verified for frame {frame_number}.")
#         else:
#             print(f"Verification failed for frame {frame_number}.")
    
#     frame_number += 1

#     # Stop after processing 10 frames
#     if frame_number > total_frames:
#         break

# # Final result
# if verified_count >= 7:
#     print("Final Result: Identity Verified!")
# else:
#     print("Final Result: Verification failed or not determined.")


import cv2
import glob
import os
from deepface import DeepFace

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img_number =1
path = 'input/*.jpeg'


output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

img_list = glob.glob(path)

for file in img_list :
    img = cv2.imread(file, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        print(f"No faces detected in {file}")
        #exit()
    else:
        for (x, y, w, h) in faces [0:2]:
            # Extract the face
            roi_color = img[y:y + h, x:x + w]

            # Resize the extracted face
            resized = cv2.resize(roi_color, (128, 128))

            # Save the extracted face
            output_file = os.path.join(output_dir, f"{img_number}.jpg")
            cv2.imwrite(output_file, resized)
            print(f"Saved face {img_number} from {file} as {output_file}")

            # Increment the image number
            img_number += 1
        
result = DeepFace.verify(
        img1_path = "output/1.jpg",
        img2_path = "output/2.jpg", 
        detector_backend="retinaface"
    )
if result['verified'] == True:
    print ("Identity Verified!")
    
else:
    print ("Verification failed!")
print(result)