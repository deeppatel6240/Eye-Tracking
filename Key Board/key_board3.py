import cv2
import numpy as np

Keyboard = np.zeros((450, 750, 3), np.uint8)

key_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
             5: "A", 6: "S", 7: "D", 8: "F", 9: "G",
             10: "Z", 11: "X", 12: "C", 13: "V", 14: "B"}

def letter(letter_index, text, letter_light):
    # keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 150
        y = 0
    elif letter_index == 2:
        x = 300
        y = 0
    elif letter_index == 3:
        x = 450
        y = 0
    elif letter_index == 4:
        x = 600
        y = 0
        
    elif letter_index == 5:
        x = 0
        y = 150
    elif letter_index == 6:
        x = 150
        y = 150
    elif letter_index == 7:
        x = 300
        y = 150
    elif letter_index == 8:
        x = 450
        y = 150
    elif letter_index == 9:
        x = 600
        y = 150
        
    elif letter_index == 10:
        x = 0
        y = 300
    elif letter_index == 11:
        x = 150
        y = 300
    elif letter_index == 12:
        x = 300
        y = 300
    elif letter_index == 13:
        x = 450
        y = 300
    elif letter_index == 14:
        x = 600
        y = 300

        
    width = 150
    height = 150
    th = 3 #thickness
    
    if letter_light is True:
        cv2.rectangle(Keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
    else:    
        cv2.rectangle(Keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 0, 0), th)
    
    # text setting
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 10
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
     
    cv2.putText(Keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0 ,0), font_th)
       

for i in range(15):
    if i == 14:
        light = True
    else:
        light = False
    letter(i, key_set_1[i], light)

cv2.imshow("KEYBOARD", Keyboard)
cv2.waitKey(0)

cv2.destroyAllWindows()