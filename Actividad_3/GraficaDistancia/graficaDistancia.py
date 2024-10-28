import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arduino = serial.Serial("COM5", 9600)

grafico = plt.figure()
ax = grafico.add_subplot(1, 1, 1)
valorx, valory = [], []


def graficar(_, valorx, valory):
    if arduino.in_waiting > 0:
        lecturaArduino = arduino.readline().decode("utf-8").strip()
        try:
            datoRecibido = float(lecturaArduino)
            valorx.append(len(valorx))
            valory.append(datoRecibido)
            ax.clear()

            ax.plot(
                valorx,
                valory,
                color="purple",
                linestyle="-",
                marker="o",
                label="Distancia (cm)",
            )
            ax.legend(loc="upper right")
            ax.set_title("Distancia Sensor HC-SR04", fontsize=14, color="blue")
            ax.set_xlabel("Tiempo (us)", fontsize=12, color="green")
            ax.set_ylabel("Distancia (cm)", fontsize=12, color="green")
            ax.grid(True, color="gray", linestyle="--", linewidth=0.5)

        except ValueError:
            print(f"Dato no valido recibido: {lecturaArduino}")


graficoAnimado = animation.FuncAnimation(
    grafico, graficar, fargs=(valorx, valory), interval=100
)

plt.show()
