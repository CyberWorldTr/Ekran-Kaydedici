#Gerekli Paketler
import pyautogui
import cv2
import numpy as np
import datetime
import time

#Oluşturucu
print(
"""
 .o88b. db    db d8888b. d88888b d8888b.   db   d8b   db  .d88b.  d8888b. db      d8888b. 
d8P  Y8 `8b  d8' 88  `8D 88'     88  `8D   88   I8I   88 .8P  Y8. 88  `8D 88      88  `8D 
8P       `8bd8'  88oooY' 88ooooo 88oobY'   88   I8I   88 88    88 88oobY' 88      88   88 
8b         88    88~~~b. 88~~~~~ 88`8b     Y8   I8I   88 88    88 88`8b   88      88   88 
Y8b  d8    88    88   8D 88.     88 `88.   `8b d8'8b d8' `8b  d8' 88 `88. 88booo. 88  .8D 
 `Y88P'    YP    Y8888P' Y88888P 88   YD    `8b8' `8d8'   `Y88P'  88   YD Y88888P Y8888D' 


d88888b db   dD d8888b.  .d8b.  d8b   db   db   dD  .d8b.  db    db d8888b. d88888b d888888b 
88'     88 ,8P' 88  `8D d8' `8b 888o  88   88 ,8P' d8' `8b `8b  d8' 88  `8D 88'     `~~88~~' 
88ooooo 88,8P   88oobY' 88ooo88 88V8o 88   88,8P   88ooo88  `8bd8'  88   88 88ooooo    88    
88~~~~~ 88`8b   88`8b   88~~~88 88 V8o88   88`8b   88~~~88    88    88   88 88~~~~~    88    
88.     88 `88. 88 `88. 88   88 88  V888   88 `88. 88   88    88    88  .8D 88.        88    
Y88888P YP   YD 88   YD YP   YP VP   V8P   YP   YD YP   YP    YP    Y8888D' Y88888P    YP    
"""
)

time.sleep(4)

# Ekran Çözünürlüğü
resolution = (1920, 1080)

# Bileşen Belirtme
codec = cv2.VideoWriter_fourcc(*"XVID")

# Dosya İsmi Oluşturma
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # Getting the exact time the screen is being recorded
filename = f'{time_stamp}.mp4'

# Fps Değeri Atama
fps = 20.0

# Video Okuyucu değerleri alma
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Boş Ekran Oluşturma
cv2.namedWindow("VideoKaydedici", cv2.WINDOW_NORMAL)

# Ekran Boyutu Ayarlama Video Kaydedici İçin!!
cv2.resizeWindow("VideoKaydedici", 480, 270)

while True:

    img = pyautogui.screenshot()
    frame = np.array(img)
    # BGR dan RGBye Dönüştürme
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Çıktı Dosyası Yazma
    out.write(frame)
    # Opsiyonel: Ekranda Görünecekler
    cv2.imshow('VideoKaydedici', frame)
    # 'q' tuşu ile görüntü almayı bitirme
    if cv2.waitKey(1) == ord('q'):
        break
#Video Kaydını durdurma
out.release()
# Tüm Ekranları Kapama
cv2.destroyAllWindows()
