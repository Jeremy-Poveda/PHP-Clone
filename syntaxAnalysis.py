import re

import ply.yacc as yacc

from lexicalAnalysis import tokens


## APORTACIÓN JEREMY POVEDA
# Regla para permitir más de una instrucción
def p_program_sentence_program(p):
    """program : sentence program"""


def p_program_sentence(p):
    """program : sentence"""
 

def p_sentence_print_statement(p):
    """
    sentence : print_statement SEMICOLON
             | assignment
             | types_structure
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
               | function_assignment
               | constant_assignment
    """


def p_variable_assignment(p):
    """
    variable_assignment : VARIABLE EQUALS values SEMICOLON
                        | VARIABLE EQUALS function_invocation SEMICOLON
                        | VARIABLE EQUALS expression SEMICOLON
                        | VARIABLE EQUALS types_structure
                        | VARIABLE EQUALS input SEMICOLON
    """


def p_constant_assignment(p):
    """
    constant_assignment : const_syntax
                        | define_syntax
    """


def p_const_syntax(p):
    """
     const_syntax : CONST IDENTIFIER EQUALS values SEMICOLON
    """


def p_define_syntax(p):
    """
        define_syntax : DEFINE LEFT_PAREN STRING COMMA values RIGHT_PAREN SEMICOLON
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


def p_function_assignment(p):
    """
    function_assignment : VARIABLE EQUALS special_function SEMICOLON
                        | FUNCTION IDENTIFIER LEFT_PAREN params RIGHT_PAREN codeblock
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
    """indexed_array : ARRAY LEFT_PAREN values_array_indexed RIGHT_PAREN SEMICOLON"""


def p_associative_array(p):
    """associative_array : ARRAY LEFT_PAREN structure_array RIGHT_PAREN SEMICOLON
                         | ARRAY LEFT_BRACKET structure_array RIGHT_BRACKET SEMICOLON
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
'''
parser.parse(code)


