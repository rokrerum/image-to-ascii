import PIL #obrazki
from PIL import Image #obrazki
import pyautogui
import os

znaki = [".", ",", ":", ";", "+" , "*", "?", "%", "S", "#",  "@"] # 11 znaków | dzielenie przez 23,1 wartosci rgb i zaokrąglanie


def tworzenie_obrazka():
    with open(f"ascii/{nazwa}.txt", "+w") as file:
        for i in range(0, wysokość, 5):
            file.write("\n")
            for j in range(0, szerokość, 2):
                jasność = zdj.getpixel((j, i))
                index = int(jasność / 23.1)
                file.write(znaki[(11-index)-1] )
    print("Gotowe \n")


def sprawdza_rozmiar():
    global szerokość, wysokość
    szerokość, wysokość = zdj.size
    #print("Szerokość obrazka:", szerokość,", Wysokość obrazka:", wysokość)


dzialanie = True
while dzialanie: # aplikacja
    zdjecia = os.listdir("zdjecia")
    print("Wybierz zdjecie do przerobieni na ascii: ")
    for i in range(len(zdjecia)):
        print(f"{i+1}: {zdjecia[i]}")    
    print("\n0: Wyjście")

    a = int(input("Wybierz opcje: "))
    if a < 0 or a > len(zdjecia):
        print("Nieprawidłowy wybór")
    elif a == 0:
        dzialanie = False 
    else:
        global zdj, nazwa 
        nazwa = zdjecia[a-1]
        zdj = PIL.Image.open(f"zdjecia/{zdjecia[a-1]}").convert("L")
        sprawdza_rozmiar()
        tworzenie_obrazka()
