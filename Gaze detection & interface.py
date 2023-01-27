import cv2
import mediapipe as mp
import pyautogui
import math
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
font = cv2.FONT_HERSHEY_PLAIN


while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    #print(landmark_points)
    frame_h, frame_w, _ = frame.shape


    if landmark_points:
        landmarks = landmark_points[0].landmark
        pupil = landmarks[473:478]
        eye = landmarks[374],landmarks[263],landmarks[362],landmarks[386],
        whole_eye= landmarks[473],landmarks[474],landmarks[475],landmarks[476],landmarks[477],landmarks[374], landmarks[263], landmarks[362], landmarks[386],

        
        #263,249,390,373,374,380,381,382,362
        for id, landmark in enumerate(whole_eye):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            #print(x,y)
            cv2.circle(frame, (x, y), 1, (0, 255, 0))
            #p1=landmarks[473]
            #p2=landmarks[362]
            #print(p1)
           # xx=math.dist(p1,p2)
           # print(xx)


        horizontal = [ landmarks[362], landmarks[473], landmarks[263]]
        vertical = [landmarks[374], landmarks[473], landmarks[386]]
        for landmark in horizontal:


            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            print(x,y)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

            w = landmarks[363].x* frame_w - landmarks[362].x* frame_w
            h = landmarks[374].y* frame_h - landmarks[386].y* frame_h
            x1, y1 = (int(landmarks[362].x* frame_w), int(landmarks[362].y* frame_h - h))
            print(x1,y1)
            # Ending coordinate, here (220, 220)
            # represents the bottom right corner of rectangle
            x2, y2 = (int(landmarks[263].x* frame_w), int(landmarks[263].y* frame_h + h))
            print(x2, y2)
            # Using cv2.rectangle() method
            # Draw a rectangle with blue line borders of thickness of 2 px
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
            roi = frame[y1:y2,x1:x2]
            roi=cv2.resize(roi,None,fx=10,fy=10)
            cv2.imshow("Roi",roi)
            cv2.waitKey(1)



    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)