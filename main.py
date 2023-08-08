import requests
import customtkinter as ct
from PIL import Image, ImageTk

#CREATE: Copy QR to clipboard button
#CREATE: Downloar QR button

WIDTH = 250
HEIGHT = 250

#FUNCTION
def generate_qr():
    global QR_IMAGE

    data = url_entry.get()
    data_file_name = 'QR_log'
    image = requests.get(f"https://chart.googleapis.com/chart?chs={WIDTH}x{HEIGHT}&cht=qr&chl={data}")
    image.raise_for_status()
    
    with open(f"ScanForge/logs/{data_file_name}.png", "wb") as qr:
        qr.write(image.content)

    QR_IMAGE = ImageTk.PhotoImage(Image.open(f"ScanForge/logs/{data_file_name}.png"))
    qr_placeholder.create_image(100,100, image=QR_IMAGE)

#GUI
COLOR = '#03001C'
QR_PLACEHOLDER_COLOR = '#301E67'

ct.set_appearance_mode('dark')
ct.set_default_color_theme("dark-blue")

window = ct.CTk()
window.title('ScanForge - A QR Code Generator')
window.resizable(False, False)
window.config(padx=50, pady=25, bg=COLOR)

canvas = ct.CTkCanvas(width=362, height=74, bg=COLOR, highlightthickness=0)
scanforge_logo = ImageTk.PhotoImage(Image.open('ScanForge/resources/logo.png'))
canvas.create_image(181, 37, image=scanforge_logo)
canvas.pack()

QR_IMAGE = ImageTk.PhotoImage(Image.open(f"ScanForge/resources/clout.png"))

qr_placeholder = ct.CTkCanvas(width=200, height=200, bg=QR_PLACEHOLDER_COLOR, highlightbackground='black')
qr_placeholder.create_image(100,100, image=QR_IMAGE)
qr_placeholder.pack()

url_entry = ct.CTkEntry(master=window, width=300,fg_color=COLOR, placeholder_text='Enter Link Here...')
url_entry.pack(pady=25)

generate_button = ct.CTkButton(master=window, text='Generate', command=generate_qr)
generate_button.pack()

url_label = ct.CTkLabel(master=window, text='Created by Fynn (2023)', bg_color=COLOR)
url_label.pack()

window.mainloop()