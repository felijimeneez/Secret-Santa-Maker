import tkinter as tk
from tkinter import messagebox
from secret_santa import draw_santa

players = []

def new_player():
    inserted_player = input_text.get().strip()  # Obtiene el texto ingresado
    if inserted_player:
        if inserted_player in players:
            messagebox.showwarning("Warning", f"{inserted_player} is already in the list! You can remove it")

        players.append(inserted_player)  # Agrega a la lista
        input_text.delete(0, tk.END)  # Limpia el campo de entrada
        update_list()  # Actualiza la lista visual en la interfaz
    else:
        messagebox.showwarning("Warning", "Please put an input")

def update_list():
    list_display.config(state=tk.NORMAL)  # Habilita el campo para editar
    list_display.delete(1.0, tk.END)  # Limpia la lista mostrada
    for i, item in enumerate(players):
        list_display.insert(tk.END, f"{i+1}. {item}\n")  # Muestra cada string
    list_display.config(state=tk.DISABLED)  # Deshabilita el campo para evitar edición

def clean_list():
    players.clear()
    update_list()

def remove_last_player():
    """Función para eliminar al último jugador agregado"""
    if players:  # Verifica si hay jugadores en la lista
        players.pop()  # Elimina el último jugador
        update_list()  # Actualiza la lista visual
    else:
        messagebox.showwarning("Advertencia", "No hay jugadores para eliminar.")

def call_backend():
    """Envía la lista al back-end para procesarla"""
    if players:
        result = draw_santa(players)  # Llama a la función del back-end
        output_label.config(text=result)  # Muestra el resultado
    else:
        messagebox.showwarning("Advertencia", "La lista está vacía.")


import tkinter as tk

import tkinter as tk

#------Colores de Navidad------
xmas_darkgreen = "#173305"
xmas_midgreen = "#0b5e15"
xmas_lightgreen = "#d9ead3"
xmas_red = "#d41616"
xmas_lightred = "#f4cccc"
xmas_gold = "#FFD700"  
xmas_white = "#FFFFFF"  \

# Crear la ventana principal
window = tk.Tk()
window.title("Secret Santa")
window.geometry("900x800")
window.config(bg=xmas_darkgreen)  # Color de fondo verde oscuro

# Etiqueta de instrucciones
instructions = tk.Label(window, text="Write a player's name and press 'Add player'", 
                        font=("Times New Roman", 16, "bold"), bg = xmas_midgreen, fg=xmas_white)
instructions.pack(pady=10)

# Campo de entrada para un solo string
input_text = tk.Entry(window, width=40, font=("Times New Roman", 16, "bold"), fg = "black", bg=xmas_lightgreen, bd=3)
input_text.pack(pady=12)

# Estilo común para todos los botones
button_style = {
    'font': ("Times New Roman", 14, "bold"),
    'bg': "red",
    'fg': "black",
    'relief': "raised",
    'bd': 5,
    'width': 20
}

# Botón para agregar el string a la lista
add_button = tk.Button(window, text="Add player", command=new_player, **button_style)
add_button.pack(pady=10)

# Botón para limpiar la lista
clean_button = tk.Button(window, text="Clean list", command=clean_list, **button_style)
clean_button.config(bg=xmas_gold)  # Cambiar el color de fondo a dorado
clean_button.pack(pady=10)

# Botón para eliminar el último jugador
remove_last_button = tk.Button(window, text="Remove last player", command=remove_last_player, **button_style)
remove_last_button.config(bg=xmas_lightred)  # Cambiar el color de fondo a rojo claro
remove_last_button.pack(pady=10)

# Lista para mostrar los elementos ingresados
list_display = tk.Text(window, height=20, width=60, wrap=tk.WORD, state=tk.DISABLED, 
                       font=("Times New Roman", 18, "bold"), bg=xmas_lightred, fg="black", bd=3)
list_display.pack(pady=10)

# Botón para procesar la lista con el back-end
draw_button = tk.Button(window, text="Draw!", command=call_backend, **button_style)
draw_button.pack(pady=10)

# Etiqueta para mostrar el resultado del back-end
output_label = tk.Label(window, text="", fg=xmas_gold, font=("Times New Roman", 16), bg=xmas_darkgreen, justify="left", wraplength=350)
output_label.pack(pady=20)

# Inicia el bucle principal de la interfaz
window.mainloop()
