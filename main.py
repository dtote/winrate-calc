import tkinter as tk
import json
import os

# Archivo donde se almacenan los datos
DATA_FILE = "data.json"

# Variables globales
successes = 0
mistakes = 0
attempts = 0

def load_data():
  """Carga los datos desde el archivo JSON"""
  global successes, mistakes, attempts
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
      data = json.load(file)
      successes = data.get("successes", 0)
      mistakes = data.get("mistakes", 0)
      attempts = data.get("attempts", 0)
  else:
    save_data() # Crear el archivo si no existe

def save_data():
  """Guarda los datos en el archivo JSON"""
  data = {
    "successes": successes,
    "mistakes": mistakes,
    "attempts": attempts
  }
  with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4)

def update_from_entries(event: None):
  global successes, mistakes, attempts
  try:
    successes = int(successes_entry.get())
    mistakes = int(mistakes_entry.get())
    attempts = successes + mistakes
    update_success_rate()
    save_data()
  except ValueError:
    success_rate_label.config(text="Entrada inválida")

def increase_successes():
  global successes, attempts
  successes += 1
  attempts += 1
  successes_entry.delete(0, tk.END)
  successes_entry.insert(0, str(successes))
  update_success_rate()
  save_data()

def increase_mistakes():
  global mistakes, attempts
  mistakes += 1
  attempts += 1
  mistakes_entry.delete(0, tk.END)
  mistakes_entry.insert(0, str(mistakes))
  update_success_rate()
  save_data()

def update_success_rate():
  global successes, attempts
  ratio = (successes / attempts) * 100
  success_rate_label.config(text=f"Ratio acierto: {ratio:.2f} %")

def main():
    # Cargar los datos al inicio+
    load_data()

    # Crear ventana principal
    root = tk.Tk()
    root.title("Calculadora de winratio")
    root.geometry("600x300")

    # Frame principal para distribuir las columnas
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame para columna de aciertos
    successes_frame = tk.Frame(main_frame)
    successes_frame.grid(row=0, column=0, padx=20)

    # Etiqueta para los aciertos
    tk.Label(successes_frame, text="Aciertos: ", font=("Arial", 14), fg="green").pack(pady=5)
    global successes_entry
    successes_entry = tk.Entry(successes_frame, font=("Arial", 14), justify="center")
    successes_entry.insert(0, str(successes))
    successes_entry.pack(pady=5)
    successes_entry.bind("<FocusOut>", update_from_entries)  # Detecta cambios al perder el foco

    # Botón para incrementar los aciertos
    increase_successes_button = tk.Button(successes_frame, text="Incrementar", font=("Arial", 12), command=increase_successes)
    increase_successes_button.pack(pady=5)

    # Frame para columna de errores
    mistakes_frame = tk.Frame(main_frame)
    mistakes_frame.grid(row=0, column=1, padx=20)

    # Etiqueta para los errores
    tk.Label(mistakes_frame, text="Errores:", font=("Arial", 14), fg="red").pack(pady=5)
    global mistakes_entry
    mistakes_entry = tk.Entry(mistakes_frame, font=("Arial", 14), justify="center")
    mistakes_entry.insert(0, str(mistakes))
    mistakes_entry.pack(pady=5)
    mistakes_entry.bind("<FocusOut>", update_from_entries)  # Detecta cambios al perder el foco

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

    update_success_rate()  # Actualizar el ratio de éxito inicial

    # Botón para cerrar la app
    exit_button = tk.Button(root, text="Salir", font=("Arial", 12), command=root.quit)
    exit_button.pack(pady=20)

    # Iniciar el loop principal
    root.mainloop()


if __name__ == "__main__":
  main()