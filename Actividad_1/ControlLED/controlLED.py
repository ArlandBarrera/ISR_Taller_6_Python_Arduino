import tkinter as tk
import serial

arduino = serial.Serial("COM5", 9600)


def close_window(event):
    window.quit()


def encender_LED(event):
    arduino.write(b"1")


def apagar_LED(event):
    arduino.write(b"0")


window = tk.Tk()
window.geometry("530x260")
window.title("Control LED Python-Arduino")
window["background"] = "#dddddd"

window.bind("1", encender_LED)
window.bind("0", apagar_LED)
window.bind("<space>q", close_window)

frame_titulo = tk.Frame(window)
frame_titulo.pack()

lbl_titulo = tk.Label(
    frame_titulo,
    text="Control LED Python - Arduino",
    fg="#aa0000",
    bg="light yellow",
    font=("Ink free", 18),
)
lbl_titulo.grid(row=0, column=0)

frame_opciones = tk.Frame(window)
frame_opciones.pack(pady=10)

img_encendido = tk.PhotoImage(file="img\\led_encendido.png")
img_encendido = img_encendido.subsample(3)
lbl_encendido = tk.Label(frame_opciones, image=img_encendido)
lbl_encendido.grid(row=0, column=0)

img_apagado = tk.PhotoImage(file="img\\led_apagado.png")
img_apagado = img_apagado.subsample(3)
lbl_apagado = tk.Label(frame_opciones, image=img_apagado)
lbl_apagado.grid(row=0, column=1)

img_exit = tk.PhotoImage(file="img\\exit.png")
img_exit = img_exit.subsample(3)
lbl_exit = tk.Label(frame_opciones, image=img_exit)
lbl_exit.grid(row=0, column=2)

lbl_encender = tk.Label(
    frame_opciones,
    text="Boton 1",
    fg="red",
    bg="light blue",
    font=("Consolas", 12),
)
lbl_encender.grid(row=1, column=0)

lbl_apagar = tk.Label(
    frame_opciones,
    text="Boton 0",
    fg="blue",
    bg="light green",
    font=("Consolas", 12),
)
lbl_apagar.grid(row=1, column=1)

lbl_salir = tk.Label(
    frame_opciones,
    text="space + q",
    fg="yellow",
    bg="purple",
    font=("Consolas", 12),
)
lbl_salir.grid(row=1, column=2)

window.mainloop()
