import cv2
import numpy as np

Keyboard = np.zeros((700, 1500, 3), np.uint8)

def letter(x, y, text):
    # keys
    width = 150
    height = 150
    th = 3 #thickness
    
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
    
letter(0, 0, "A")
letter(150, 0, "B")
letter(300, 0, "C")

cv2.imshow("KEYBOARD", Keyboard)
cv2.waitKey(0)

cv2.destroyAllWindows()