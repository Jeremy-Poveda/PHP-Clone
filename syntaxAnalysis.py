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
    """


# Tipos de dato
def p__values(p):
    """
    values : INTEGER
           | STRING
           | FLOAT
           | VARIABLE
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
    """


def p_variable_assignment(p):
    """
    variable_assignment : VARIABLE EQUALS values SEMICOLON
                        | VARIABLE EQUALS function_invocation SEMICOLON
                        | VARIABLE EQUALS expression SEMICOLON
    """


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
                | real_params COMMA VARIABLE
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

#FIN DE APORTACIÓN KEVIN ROLDAN


# Regla para los errores de sintáxis
def p_error(p):
    if p:
        print(f"Error semántico en línea {p.lineno}, posición {p.lexpos}: Token inesperado '{p.value}' \n'{p}'")
    else:
        print("Error semántico: Fin de archivo inesperado")



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
$op = function($nombre) {};
$ko = 23+5;
'''
parser.parse(code)


