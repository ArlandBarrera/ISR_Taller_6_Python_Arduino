import tkinter as tk
from pyfirmata import Arduino, SERVO

LED = 13
servomotor = 3

placa = Arduino("COM5")
placa.digital[servomotor].mode = SERVO


def servo(posicion):
    placa.digital[servomotor].write(posicion)


def led_encerder():
    placa.digital[LED].write(1)


def led_apagar():
    placa.digital[LED].write(0)


def cerrar_ventana():
    window.quit()


def salir_bind(event):
    window.quit()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Control de Servomotor")
    window.minsize(300, 150)
    window["background"] = "#dddddd"

    window.bind("<space>q", salir_bind)

    angulo = tk.Scale(
        window,
        command=servo,
        from_=50,
        to=100,
        orient=tk.HORIZONTAL,
        length=300,
        troughcolor="gold",
        width=30,
        label="Angulo Servo",
        bg="light yellow",
        fg="magenta2",
        font=("Open Sans", 12),
    )
    angulo.pack()

    frame_buttons = tk.Frame(window)
    frame_buttons.pack(pady=20)

    btn_encender = tk.Button(
        frame_buttons,
        text="Encender LED",
        command=led_encerder,
        font=("Consolas", 12),
        bg="lawn green",
        fg="red",
        activebackground="red",
        activeforeground="lawn green",
    )
    btn_encender.grid(row=0, column=0)

    btn_apagar = tk.Button(
        frame_buttons,
        text="Apagar LED",
        command=led_apagar,
        font=("Consolas", 12),
        bg="dim gray",
        fg="navajo white",
        activebackground="navajo white",
        activeforeground="dim gray",
    )
    btn_apagar.grid(row=0, column=1)

    btn_salir = tk.Button(
        frame_buttons,
        text="Cerrar App",
        command=cerrar_ventana,
        font=("Consolas", 12),
        bg="turquoise",
        fg="deep pink",
        activebackground="deep pink",
        activeforeground="turquoise",
    )
    btn_salir.grid(row=0, column=2)

    window.tk.mainloop()
