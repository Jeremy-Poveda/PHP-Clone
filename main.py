# Programa principal
from lexicalAnalysis import lexer
from syntaxAnalysis import parser


import tkinter


#Mini interfaz gráfica contribución de JEREMY POVEDA
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from io import StringIO
import sys
import ply.yacc as yacc

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

def run_php(input_text):
    output_text.delete(1.0, tk.END)  # Limpiamos contenido actual
    sys.stdout = RedirectText(output_text) # Mandamos el texto de stdout del programa a la interfaz grafica
    lexer.input(input_text)
    try:
        for token in lexer: 
            print(token)
        lexer.lineno = 1
        parser.parse(input_text)
        lexer.lineno = 1
    except Exception as e:
        print(f"Error: {e}")

    # Restaurar la salida estándar
    sys.stdout = sys.__stdout__

def play_button_clicked():
    input_text_content = input_text.get(1.0, tk.END)
    run_php(input_text_content)

root = tk.Tk()
root.title("PHP Clone - GRUPO 4")

# Cambia el color de fondo y del texto
root.configure(bg='#444444')
input_text = tk.Text(root, height=30, width=200, bg='#222222', fg='white')
input_text.pack(pady=10)



# widget de texto para la consola
output_text = scrolledtext.ScrolledText(root, height=15, width=200, wrap=tk.WORD, bg='#333333', fg='white')
output_text.pack()

# botón para ejecutar el análisis lexico y semantico
style = ttk.Style()
style.configure('TButton', background='#666666', foreground='#333333', padding=(10, 5))
play_button = ttk.Button(root, text="Play", command=play_button_clicked, style='TButton')
play_button.pack(pady=10)

# ejecutamos la interfaz grafica
root.mainloop()
