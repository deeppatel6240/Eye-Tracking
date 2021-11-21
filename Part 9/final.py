import cv2
import dlib
import numpy as np
from math import hypot
from playsound import playsound
import time


cap = cv2.VideoCapture(0)
board = np.zeros((700, 1500), np.uint8)
board[:] = 255


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# key board settings
Keyboard = np.zeros((150, 500, 3), np.uint8)
key_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T", 5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",
             10: "A", 11: "S", 12: "D", 13: "F", 14: "G", 15: "H", 16: "J", 17: "K", 18: "L", 19: ";",
             20: "Z", 21: "X", 22: "C", 23: "V", 24: "B", 25: "N", 26: "M", 27: ",", 28: ".", 29: "/"}


def letter(letter_index, text, letter_light):
    # keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 50
        y = 0
    elif letter_index == 2:
        x = 100
        y = 0
    elif letter_index == 3:
        x = 150
        y = 0
    elif letter_index == 4:
        x = 200
        y = 0
    elif letter_index == 5:
        x = 250
        y = 0
    elif letter_index == 6:
        x = 300
        y = 0
    elif letter_index == 7:
        x = 350
        y = 0
    elif letter_index == 8:
        x = 400
        y = 0
    elif letter_index == 9:
        x = 450
        y = 0
        
    elif letter_index == 10:
        x = 0
        y = 50
    elif letter_index == 11:
        x = 50
        y = 50
    elif letter_index == 12:
        x = 100
        y = 50
    elif letter_index == 13:
        x = 150
        y = 50
    elif letter_index == 14:
        x = 200
        y = 50
    elif letter_index == 15:
        x = 250
        y = 50
    elif letter_index == 16:
        x = 300
        y = 50
    elif letter_index == 17:
        x = 350
        y = 50
    elif letter_index == 18:
        x = 400
        y = 50
    elif letter_index == 19:
        x = 450
        y = 50
        
    elif letter_index == 20:
        x = 0
        y = 100
    elif letter_index == 21:
        x = 50
        y = 100
    elif letter_index == 22:
        x = 100
        y = 100
    elif letter_index == 23:
        x = 150
        y = 100
    elif letter_index == 24:
        x = 200
        y = 100
    elif letter_index == 25:
        x = 250
        y = 100
    elif letter_index == 26:
        x = 300
        y = 100
    elif letter_index == 27:
        x = 350
        y = 100
    elif letter_index == 28:
        x = 400
        y = 100
    elif letter_index == 29:
        x = 450
        y = 100
        
    
        
    width = 50
    height = 50
    th = 3 #thickness
    
    if letter_light is True:
        cv2.rectangle(Keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
    else:    
        cv2.rectangle(Keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 0, 0), th)
    
    # text setting
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 3
    font_th = 2
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
     
    cv2.putText(Keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0 ,0), font_th)

def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_SIMPLEX

def get_eye_blinking_ratio(eye_points, facial_landmarks):
    
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
        
    # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)
        
    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    # print("horizontal lenght:", hor_line_lenght)
    
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    # print("vertical lenght", ver_line_length)
        
    ratio = hor_line_lenght/ver_line_length
    return ratio

def get_gaze_Ratio(eye_points, facial_landmarks):
    
     left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                 (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                 (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                 (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                 (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                 (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
     # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)
        
     height, width, _ = frame.shape
     mask = np.zeros((height, width), np.uint8)
       
     cv2.polylines(mask, [left_eye_region], True, 255, 2)
     cv2.fillPoly(mask, [left_eye_region], 255)
       
     eye = cv2.bitwise_and(gray, gray, mask = mask)
        
        
        
     min_x = np.min(left_eye_region[:, 0])
     max_x = np.max(left_eye_region[:, 0])
     min_y = np.min(left_eye_region[:, 1])
     max_y = np.max(left_eye_region[:, 1])
        
     gray_eye = eye[min_y: max_y, min_x: max_x]
     _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY_INV)

     height, width = threshold_eye.shape
        
     left_side_threshold = threshold_eye[0: height, 0: int(width/2)]
     left_side_white = cv2.countNonZero(left_side_threshold)
        
     right_side_threshold = threshold_eye[0: height, int(width/2): width]
     right_side_white = cv2.countNonZero(right_side_threshold)
     
     if left_side_white == 0:
         gaze_ratio = 1
     elif right_side_white == 0:
         gaze_ratio = 5
     else:
         gaze_ratio = left_side_white/right_side_white
     return gaze_ratio   
   
# Counters
frames = 0
letter_index = 0
blinking_frames = 0
text = ""
    
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5)
    Keyboard[:] = (0, 0, 0)
    frames += 1
    new_frame = np.zeros((500, 500, 3), np.uint8)    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    active_letter = key_set_1[letter_index]    
    
    faces = detector(gray)
    for face in faces:
        # print(face)
        # x, y = face.left(), face.top()
        # x1, y1 = face.right(), face.bottom()
        # cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        
        landmarks = predictor(gray, face)
        
        # eye-blinking
        left_eye_ratio = get_eye_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_eye_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        print(blinking_ratio)
        
        
        if blinking_ratio > 5.5:
            #cv2.putText(frame, "BLINKING", (50,100), font, 2, (255, 0 ,0), thickness = 3)
            blinking_frames += 1
            frames -= 1
            
            if blinking_frames == 6:
                text += active_letter
                sound = playsound("sound.wav")
                time.sleep(1)
            
        else:
            blinking_frames = 0
            

        """    
        # gaze detection
        gaze_ratio_left_eye = get_gaze_Ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_Ratio([42, 43, 44, 45, 46, 47], landmarks)
        
        gaze_ratio = (gaze_ratio_left_eye + gaze_ratio_right_eye) / 2
        
        if gaze_ratio < 0.5:
             cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
             new_frame[:] = (0, 0, 255)
        elif gaze_ratio <= 2:
             cv2.putText(frame, "CENTER", (50, 100), font, 2, (0, 0, 255), 3)
        else:
             cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
             new_frame[:] = (255, 0, 0)
        """
    
    
    #Letters 
    if frames == 30:
        letter_index += 1
        frames = 0
    if letter_index == 30:
        letter_index = 0
    
    for i in range(30):
        if i == letter_index:
            light = True
        else:
            light = False
        letter(i, key_set_1[i], light)        
             
    cv2.putText(board, text, (10, 100), font, 4, 0, 3)

    # cv2.imshow("New Frame", new_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("Virtual Keyboard", Keyboard)
    cv2.imshow("Board", board)
 
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release() 
cv2.destroyAllWindows() 