import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arduino = serial.Serial("COM5", 9600)
grafico = plt.figure()
ax = grafico.add_subplot(1, 1, 1)

# Listas para almacenar los valores en el tiempo
valorx = []
valory_humedad = []
valory_temperatura = []

def graficar(_, valorx, valory_humedad, valory_temperatura):
    if arduino.in_waiting > 0:
        lecturaArduino = arduino.readline().decode("utf-8").strip()
        try:
            # Divide los datos de humedad y temperatura
            humedad, temperatura = map(float, lecturaArduino.split(","))
            valorx.append(len(valorx))  # Incrementa el tiempo

            # Agrega los valores a las listas de humedad y temperatura
            valory_humedad.append(humedad)
            valory_temperatura.append(temperatura)
            ax.clear()

            # Graficar humedad y temperatura
            ax.plot(valorx, valory_humedad, color="blue", linestyle="-", marker="o", label="Humedad (%)")
            ax.plot(valorx, valory_temperatura, color="red", linestyle="-", marker="x", label="Temperatura (°C)")

            # Establece detalles de la gráfica
            ax.legend(loc="upper right")
            ax.set_title("Humedad y Temperatura DHT11", fontsize=14, color="black")
            ax.set_xlabel("Tiempo (s)", fontsize=12)
            ax.set_ylabel("Valor", fontsize=12)
            ax.grid(True, color="gray", linestyle="--", linewidth=0.5)

        except ValueError:
            print(f"Dato no válido recibido: {lecturaArduino}")

# Configuración de animación de la gráfica
graficoAnimado = animation.FuncAnimation(
    grafico, graficar, fargs=(valorx, valory_humedad, valory_temperatura), interval=1000
)

plt.show()
