import ply.yacc as yacc

from lexicalAnalysis import tokens


## APORTACIÓN JEREMY POVEDA
# Regla para permitir más de una instrucción
def p_program_sentence_program(p):
    'program : sentence program'


def p_program_sentence(p):
    'program : sentence'
 

def p_sentence_print_statement(p):
    '''
    sentence : print_statement SEMICOLON
             | assignment SEMICOLON
    '''

def p_print_statement(p):
    '''
    print_statement : ECHO LEFT_PAREN values RIGHT_PAREN
                    | PRINT LEFT_PAREN values RIGHT_PAREN
                    | ECHO values
                    | PRINT values
    '''

def p_string_values(p):
    '''
    values : value 
           | value COMMA values
    '''

# Tipos de dato
def p_value(p):
    '''
    value : INTEGER 
          | STRING
          | FLOAT
          | boolean
    '''

def p_boolean(p):
    '''
    boolean : TRUE 
            | FALSE
    '''


def p_assignment(p):
    'assignment : VARIABLE EQUALS expression'

def p_expression(p):
    '''
    expression : term
               | term PLUS expression
               | term MINUS expression
    '''

def p_term(p):
    '''
    term : factor
         | factor MULTIPLY term
         | factor DIVIDE term
         | factor MODULE term
         | factor POW term
    '''

def p_factor(p):
    '''
    factor : INTEGER
           | VARIABLE
           | LEFT_PAREN expression RIGHT_PAREN
    '''

#FIN DE APORTACIÓN JEREMY POVEDA

# Regla para los errores de sintáxis
def p_error(p):
    print(f"Error de sintaxis en la entrada.")


# Creamos el parser
parser = yacc.yacc()



"""
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
"""