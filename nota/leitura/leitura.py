import cv2
#import pandas as pd
from bs4 import BeautifulSoup
from pyzbar import pyzbar

#from selenium import webdriver
#from selenium.webdriver.common.by import By


# Initialize webcam // abre a wecam
cap = cv2.VideoCapture(0)

while True:
    # Get webcam frame // obtem o frame da webcam
    ret, frame = cap.read()

    # Find QR codes in the frame // busca um RQCode em cada framde
    decoded_objects = pyzbar.decode(frame)

    # Draw a bounding box around each QR code / desenha uma caixa vermelha em volta do QRCode quando encontrar ele
    for obj in decoded_objects:
        # Extract the bounding box coordinates / extrei as coordenadas da caixa delimitadora
        x, y, w, h = obj.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

        # Extract the QR code data as a string / extrai o dado do QRCode em formato string
        qr_data = obj.data.decode("utf-8")
        print("Aguarde alguns segundos")
        break

    # Show the webcam frame
    cv2.imshow("Webcam", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if len(decoded_objects) > 0:
        break

# Release webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()