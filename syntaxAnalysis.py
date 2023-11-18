import re

import ply.yacc as yacc

from lexicalAnalysis import tokens


## APORTACIÓN JEREMY POVEDA
# Regla para permitir más de una instrucción
def p_program_sentence_program(p):
    """program : sentence program"""


def p_program_sentence(p):
    """program : sentence"""
 

# Sentencias para impresión de valores, asignaciones, estructuras de datos, declaración de funciones y estructuras de control.
def p_sentence_print_statement(p):
    """
    sentence : print_statement SEMICOLON
             | assignment SEMICOLON
             | types_structure
             | control_structures
             | function_declaration
    """

# Estructuras de control
def p_control_structures(p):
    """
    control_structures : if_statement
                       | while_statement
    """
def p_while_statement(p):
    """
    while_statement : WHILE LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
    """

def p_if_statement(p):
    """
    if_statement : IF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
                 | IF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE elseif_statement
                 | IF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE else_statement
    """

def p_elseif_statement(p):
    """
    elseif_statement : ELSEIF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE
                 | ELSEIF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE elseif_statement
                 | ELSEIF LEFT_PAREN conditional RIGHT_PAREN LEFT_BRACE body_statement RIGHT_BRACE else_statement
    """

def p_else_statement(p):
    """
    else_statement : ELSE LEFT_BRACE body_statement RIGHT_BRACE
    """

def p_body_statement(p):
    """
    body_statement : sentence
            | sentence RETURN values SEMICOLON
            | sentence RETURN SEMICOLON
            | sentence BREAK SEMICOLON
            | sentence body_statement
    """

# Sentencias que pueden ser condicionales, preprosiciones lógicas y combinaciones de estas comparaciones

def p_conditional(p):
    """
    conditional  : boolean_expression
                 | boolean_expression logic_operator boolean_expression
    """

def p_logic_operator(p):
    """
    logic_operator  : LOGIC_AND
                    | LOGIC_OR
                    | LOGIC_XOR 
    """

def p_boolean_expression(p):
    """
    boolean_expression  : comparation
                        | LEFT_PAREN conditional RIGHT_PAREN
                        | LOGIC_NOT conditional
    """

def p_comparation(p):
    """
    comparation : values comparator_operator values
                | values comparator_operator expression
                | expression comparator_operator expression
    """

def p_comparator_operator(p):
    """
    comparator_operator : EQUALS_EQUALS
                         | IDENTICAL
                         | NOT_EQUALS
                         | NOT_IDENTICAL
                         | SMALL_THAN
                         | GREATER_THAN
                         | SMALL_EQUALS_TO
                         | GREATER_EQUALS_TO
                         | SPACECRAFT
                         | NULL_FUSION
    """

def p_print_statement(p):
    """
    print_statement : ECHO LEFT_PAREN printable_values RIGHT_PAREN
                    | PRINT LEFT_PAREN printable_values RIGHT_PAREN
                    | ECHO printable_values
                    | PRINT printable_values
    """


def p_printable_values(p):
    """
    printable_values : values
                     | values COMMA printable_values
                     | VARIABLE
                     | VARIABLE COMMA printable_values
                     | conditional
                     | conditional COMMA printable_values
    """


# Tipos de dato
def p_values(p):
    """
    values : INTEGER
           | STRING
           | FLOAT
           | boolean
    """


def p_boolean(p):
    """
    boolean : TRUE
            | FALSE
    """


def p_expression(p):
    """
    expression : term
               | term PLUS expression
               | term MINUS expression
    """


def p_term(p):
    """
    term : factor
         | factor MULTIPLY term
         | factor DIVIDE term
         | factor MODULE term
         | factor POW term
    """


def p_factor(p):
    """
    factor : INTEGER
           | VARIABLE
           | LEFT_PAREN expression RIGHT_PAREN
    """

#FIN DE APORTACIÓN JEREMY POVEDA

#APORTACIÓN KEVIN ROLDAN


def p_assignment(p):
    """
    assignment : variable_assignment
               | constant_assignment
    """


def p_variable_assignment(p):
    """
    variable_assignment : VARIABLE assignment_operator values
                        | VARIABLE assignment_operator expression 
                        | VARIABLE assignment_operator function_invocation
                        | VARIABLE assignment_operator types_structure 
                        | VARIABLE assignment_operator input 
                        | VARIABLE assignment_operator special_function
                        | VARIABLE INCREASE 
                        | VARIABLE DECREMENT 
                        | INCREASE VARIABLE 
                        | DECREMENT VARIABLE 
    """

# Aportación Jeremy Poveda, Para que se apliquen más operadores de asignación
def p_assignment_operator(p):
    """
    assignment_operator : EQUALS
                        | PLUS_EQUALS
    """
#Nota para el resto, hay que hacer en el semantico la diferenciacion entre asignacion de strings para poder usar la operacion de .=

def p_constant_assignment(p):
    """
    constant_assignment : const_syntax
                        | define_syntax
    """


def p_const_syntax(p):
    """
     const_syntax : CONST IDENTIFIER EQUALS values 
    """


def p_define_syntax(p):
    """
        define_syntax : DEFINE LEFT_PAREN STRING COMMA values RIGHT_PAREN 
    """
    constant_name = p[3][1:-1]

    if re.match(r'[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*', constant_name) is None:
        print(f"Error de sintaxis: nombre de constante '{constant_name}' no permitido")
        raise SyntaxError(f"Error de sintaxis: nombre de constante '{constant_name}' no permitido")


def p_function_invocation(p):
    """
    function_invocation : IDENTIFIER LEFT_PAREN params RIGHT_PAREN SEMICOLON
    """


def p_params(p):
    """
    params : real_params
           | empty
    """


def p_real_params(p):
    """
    real_params : VARIABLE
                | values
                | real_params COMMA VARIABLE
                | real_params COMMA values
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) > 2:
        p[0] = p[1] + [p[3]]


def p_empty(p):
    """
    empty :
    """
    pass

# Creado por Jeremy Poveda, separando la declaración de la función con su asignación a una variable
def p_function_declaration(p):
    """
    function_declaration : FUNCTION IDENTIFIER LEFT_PAREN params RIGHT_PAREN codeblock
    """


def p_special_function(p):
    """
    special_function : arrow_function
                     | anonymous_functions
    """


def p_arrow_function(p):
    """
    arrow_function : FN LEFT_PAREN params RIGHT_PAREN EQUALS GREATER_THAN codeblock
    """


def p_anonymous_functions(p):
    """
    anonymous_functions : FUNCTION LEFT_PAREN params RIGHT_PAREN codeblock
    """


def p_codeblock(p):
    """
    codeblock : LEFT_BRACE RIGHT_BRACE
    """


def p_input(p):
    """
    input : FEGTS LEFT_PAREN STDIN RIGHT_PAREN
          | READLINE LEFT_PAREN STRING RIGHT_PAREN
    """


#FIN DE APORTACIÓN KEVIN ROLDAN
#INICIO DE APORTACIÓN JORGE MAWYIN
#ESTRUCTURAS DE DATOS


def p_types_structure(p):
    """
    types_structure : structure_array_principal
                    | structure_matrix_principal
                    | structure_object_principal
    """


#ARRAY
def p_structure_array_principal(p):
    """
    structure_array_principal : indexed_array
                              | associative_array
    """


def p_indexed_array(p):
    """indexed_array : ARRAY LEFT_PAREN values_array_indexed RIGHT_PAREN"""


def p_associative_array(p):
    """associative_array : ARRAY LEFT_PAREN structure_array RIGHT_PAREN 
                         | ARRAY LEFT_BRACKET structure_array RIGHT_BRACKET
    """


def p_structure_array(p):
    """
    structure_array : key EQUALS GREATER_THAN values
                    | key EQUALS GREATER_THAN values COMMA structure_array
    """


def p_key(p):
    """
    key : INTEGER
        | STRING
    """


def p_values_array_indexed(p):
    """values_array_indexed : values
                            | values COMMA values_array_indexed
    """


#MATRIX
def p_structure_matrix_principal(p):
    """
    structure_matrix_principal : matrix_firstform
                               | matrix_secondform
                               | access_element_matrix
                               | modify_element_matrix
                               | add_element_matrix
    """


def p_matrix_firstform(p):
    """matrix_firstform : ARRAY LEFT_PAREN structure_matrix_first RIGHT_PAREN SEMICOLON"""


def p_matrix_secondform(p):
    """matrix_secondform : LEFT_BRACKET structure_matrix_second RIGHT_BRACKET SEMICOLON"""


def p_structure_matrix_second(p):
    """
    structure_matrix_second : LEFT_BRACKET values RIGHT_BRACKET
                            | LEFT_BRACKET values RIGHT_BRACKET COMMA structure_matrix_second
    """


def p_structure_matrix_first(p):
    """
    structure_matrix_first : ARRAY LEFT_PAREN values RIGHT_PAREN
                           | ARRAY LEFT_PAREN values RIGHT_PAREN COMMA structure_matrix_first
    """


def p_access_element_matrix(p):
    """access_element_matrix : VARIABLE LEFT_BRACKET INTEGER RIGHT_BRACKET LEFT_BRACKET INTEGER RIGHT_BRACKET SEMICOLON"""


def p_modify_element_matrix(p):
    'modify_element_matrix : VARIABLE LEFT_BRACKET INTEGER RIGHT_BRACKET LEFT_BRACKET INTEGER RIGHT_BRACKET EQUALS values SEMICOLON'


def p_add_element_matrix(p):
    """add_element_matrix : VARIABLE LEFT_BRACKET RIGHT_BRACKET EQUALS indexed_array"""


#OBJECT
def p_structure_object_principal(p):
    """
    structure_object_principal : object_creation
                               | access_method_object
    """


def p_object_creation(p):
    """object_creation : NEW class_name SEMICOLON"""


def p_class_name(p):
    """class_name : IDENTIFIER"""


def p_access_method_object(p):
    """access_method_object : VARIABLE MINUS GREATER_THAN IDENTIFIER LEFT_PAREN RIGHT_PAREN SEMICOLON"""

#FIN DE APORTACIÓN JORGE MAWYIN


# Regla para los errores de sintáxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}' \n'{p}'")
    else:
        print("Error de sintaxis: Fin de archivo inesperado")



# Creamos el parser
parser = yacc.yacc()


parser.error = 0

code = '''
print 56;
$clave = 34;
$rtr = $ft;
echo "asjos", 34, "2";
function validarContrasena($contrasena) {}
$clave = "ClaveSegura123!";
$_cla = fn($a) => {};
$op = function($nombre,$rrr, 2, true, "hola") {};
$ko = 23;
define("hola",29);
const HOLA = "xd";
$hola = array(4,5);
$input = fgets(STDIN);
$input2 = readline("escriba una linea");
$a--;
--$a;
'''

algorith_Poveda = '''
$numero = 7;

// Bucle while y estructura if anidada
while (!($numero == 0) and $numero > 1) { // Ejemplo de negacion
    echo "El número actual es: $numero ";

    if ($numero % 2 == 0) {
        echo "(par)\n";
    } else {
        echo "(impar)\n";
        return "Hola mundo";
    }

    $numero--;

    if ($numero == 4) {
        echo "¡El número llegó a 4! Terminando el bucle.\n";
        break;
    }
}

echo "Fin del programa.";
'''
parser.parse(code)
parser.parse(algorith_Poveda)


