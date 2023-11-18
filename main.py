# Programa principal
from lexicalAnalysis import lexer
from syntaxAnalysis import parser


import tkinter

#INICIO CONTRIBUCION KEVIN ROLDAN
#ALGORITMOS DE PRUEBA

print("Inicio del analisis del algoritmo de prueba de Kevin Roldan\n\n")

codeRoldan = '''
//Funcion para validar contraseña
function validarContrasena($contrasena) {
    $longitud = strlen($contrasena);
    $esFuerte = false;

    if ($longitud >= 8) {
        $tieneMayuscula = preg_match('/[A-Z]/', $contrasena);
        $tieneMinuscula = preg_match('/[a-z]/', $contrasena);
        $tieneNumero = preg_match('/[0-9]/', $contrasena);
        $tieneSimbolo = preg_match('/[\W]/', $contrasena);

        if ($tieneMayuscula && $tieneMinuscula && $tieneNumero && $tieneSimbolo) {
            $esFuerte = true;
        }
    }

    return $esFuerte;
}

// Uso de la función
$clave = "ClaveSegura123!";
if (validarContrasena($clave)) {
    echo "La contraseña es fuerte.";
} else {
    echo "La contraseña es débil. Debe contener al menos 8 caracteres, incluyendo mayúsculas, minúsculas, números y símbolos.";
}

'''

lexer.input(codeRoldan)



print("Fin del analisis del algoritmo de prueba de Kevin Roldan\n\n")
# FIN DE CONTRIBUCION KEVIN ROLDAN

# INICIO CONTRIBUCION JORGE MAWYIN
print("Inicio del analisis del algoritmo de prueba de Jorge Mawyin\n\n")

# Código para validar - Jorge Mawyin
codeMawyin = ''' 
$numero = 0b1010;

if ($numero === 10) {
    echo "El número es igual a 10.\n";
} elseif ($numero > 5) {
    echo "El número es mayor que 5 pero no igual a 10.\n";
} elseif ($numero < 5) {
    echo "El número es menor que 5.\n";
}

while ($numero >= 20) {
    echo "El número es igual o mayor que 20.\n";
    $numero -= 5;
}

echo "Valor después del bucle es: " . $numero . "\n";

$texto = "Analizador Léxico";
$texto .= " en PHP.";
echo $texto . "\n";
}
'''

# Enviando el código
lexer.input(codeMawyin)


print("Fin del analisis del algoritmo de prueba de Jorge Mawyin\n\n")
# FIN DE CONTRIBUCION JORGE MAWYIN


# INICIO CONTRIBUCION JEREMY POVEDA
print("Inicio del analisis del algoritmo de prueba de Jeremy Poveda\n\n")
codePoveda =  '''
// Función para calcular el factorial de un número
function factorial($n) {
    // Inicializar el resultado a 1
    $resultado = 1;

    // Iterar desde 1 hasta $n
    for ($i = 1; $i <= $n; $i++) {
        // Multiplicar el resultado por el número actual en la iteración
        $resultado *= $i;
        
        // Comentario de una sola línea con //
    }

    /*
    Este es un comentario de bloque
    */

    // Devolver el resultado del factorial
    return $resultado;
}

// Puedes probar la función llamándola con un valor
$numero = 5;
// Esto calcula el factorial de 5 y lo imprime
echo "El factorial de $numero es " . factorial($numero);
'''

# Enviando el código
lexer.input(codePoveda)



print("Fin del analisis del algoritmo de prueba de Jeremy Poveda\n\n")
# FIN DE CONTRIBUCION JEREMY POVEDA


#Mini interfaz gráfica contribución de JEREMY POVEDA
import tkinter as tk
from tkinter import scrolledtext
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
        parser.parse(input_text)
    except Exception as e:
        print(f"Error: {e}")

    # Restaurar la salida estándar
    sys.stdout = sys.__stdout__

def play_button_clicked():
    input_text_content = input_text.get(1.0, tk.END)
    run_php(input_text_content)

root = tk.Tk()
root.title("PHP Clone - GRUPO 4")

input_text = tk.Text(root, height=30, width=100)
input_text.pack(pady=10)



# widget de texto para la consola
output_text = scrolledtext.ScrolledText(root, height=10, width=100, wrap=tk.WORD)
output_text.pack()

# botón para ejecutar el análisis lexico y semantico
play_button = tk.Button(root, text="Play", command=play_button_clicked)
play_button.pack(pady=10)

# ejecutamos la interfaz grafica
root.mainloop()
