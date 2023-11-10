# Programa principal
from lexicalAnalysis import lexerJM,lexerJP,lexerKR

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

lexerKR.input(codeRoldan)

for token in lexerKR:
    print(token)


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
lexerJM.input(codeMawyin)

for token in lexerJM:
    print(token)

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
lexerJP.input(codePoveda)

for token in lexerJP:
    print(token)

print("Fin del analisis del algoritmo de prueba de Jeremy Poveda\n\n")
# FIN DE CONTRIBUCION JEREMY POVEDA