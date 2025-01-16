import tkinter as tk

successes = 0
mistakes = 0
attempts = 0

def increase_successes():
  global successes, attempts
  successes += 1
  attempts += 1
  successes_label.config(text=f"Aciertos: {successes}")
  update_success_rate()

def increase_mistakes():
  global mistakes, attempts
  mistakes += 1
  attempts += 1
  mistakes_label.config(text=f"Errores: {mistakes}")
  update_success_rate()

def update_success_rate():
  global successes, attempts
  ratio = (successes / attempts) * 100
  success_rate_label.config(text=f"Ratio acierto: {ratio:.2f} %")

def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Calculadora de winratio")
    root.geometry("400x300")

    # Frame principal para distribuir las columnas
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame para columna de aciertos
    successes_frame = tk.Frame(main_frame)
    successes_frame.grid(row=0, column=0, padx=20)

    # Etiqueta para los aciertos
    global successes_label
    successes_label = tk.Label(successes_frame, text=f"Aciertos: {successes}", font=("Arial", 14), fg="green")
    successes_label.pack(pady=10)

    # Botón para incrementar los aciertos
    increase_successes_button = tk.Button(successes_frame, text="Incrementar", font=("Arial", 12), command=increase_successes)
    increase_successes_button.pack(pady=5)

    # Frame para columna de errores
    mistakes_frame = tk.Frame(main_frame)
    mistakes_frame.grid(row=0, column=1, padx=20)

    # Etiqueta para los errores
    global mistakes_label
    mistakes_label = tk.Label(mistakes_frame, text=f"Errores: {mistakes}", font=("Arial", 14), fg="red")
    mistakes_label.pack(pady=10)

    # Botón para incrementar los errores
    increase_mistakes_button = tk.Button(mistakes_frame, text="Incrementar", font=("Arial", 12), command=increase_mistakes)
    increase_mistakes_button.pack(pady=5)

    # Frame para columna de porcentaje
    success_rate_frame = tk.Frame(root)
    success_rate_frame.pack(pady=10)

    # Etiqueta porcentaje de acierto
    global success_rate_label
    success_rate_label = tk.Label(success_rate_frame, text=f"Ratio acierto: 0.00 %" , font=("Arial", 16))
    success_rate_label.pack()

    # Botón para cerrar la app
    exit_button = tk.Button(root, text="Salir", font=("Arial", 12), command=root.quit)
    exit_button.pack(pady=20)

    # Iniciar el loop principal
    root.mainloop()


if __name__ == "__main__":
  main()