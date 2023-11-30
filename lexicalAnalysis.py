# Grupo: 4
# Componentes lexicos con libreria ply lex
import ply.lex as lex

# INICIO CONTRIBUCION KEVIN ROLDAN

reserved = {
    'array': 'ARRAY',
    'and': 'LOGIC_AND',
    'or': 'LOGIC_OR',
    'xor': 'LOGIC_XOR',
    'break': 'BREAK',
    'class': 'CLASS',
    'const': 'CONST',
    'echo': 'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'extends': 'EXTENDS',
    'fn': 'FN',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'implements': 'IMPLEMENTS',
    'interface': 'INTERFACE',
    'new': 'NEW',
    'print': 'PRINT',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'public': 'PUBLIC',
    'return': 'RETURN',
    'static': 'STATIC',
    'while': 'WHILE'
}

# FIN DE CONTRIBUCION KEVIN ROLDAN

essential_functions = {
    'fgets': 'FEGTS',
    'readline': 'READLINE',
    'STDIN': 'STDIN',
    'define': 'DEFINE',
    'strlen' : 'STRLEN',
    'substr' : 'SUBSTR'
}
# Tokens
tokens = (
             # CONTRIBUCION JEREMY POVEDA
             'STRING',
             'FLOAT',
             'COMMENT',
             # FIN DE LA CONTRIBUCION JEREMY POVEDA


             # CONTRIBUCION JORGE MAWYIN
             'INTEGER',
             'NULL',
             # OPERADORES ARITMÉTICOS
             'PLUS',
             'MINUS',
             'MULTIPLY',
             'DIVIDE',
             'MODULE',
             'POW',
             # OPERADORES DE ASIGNACION
             'EQUALS',
             'PLUS_EQUALS',
             # OPERADORES DE COMPARACION
             'EQUALS_EQUALS',
             'IDENTICAL',
             'NOT_EQUALS',
             'NOT_IDENTICAL',
             'SMALL_THAN',
             'GREATER_THAN',
             'SMALL_EQUALS_TO',
             'GREATER_EQUALS_TO',
             'SPACECRAFT',
             'NULL_FUSION',


             # OPERADORES DE INCREMENTO/DECREMENTO
             'INCREASE',
             'DECREMENT',
             # OPERADORES LOGICOS
             'LOGIC_AND',
             'LOGIC_OR',


             'LOGIC_NOT',
             # OPERADOR PARA STRING
             'STRING_CONCATENATION',

             # FIN DE CONTRIBUCION JORGE MAWYIN

             # INICIO CONTRIBUCION KEVIN ROLDAN
             'IDENTIFIER',
             'VARIABLE',
             'TRUE',
             'FALSE',
             'LEFT_PAREN',
             'RIGHT_PAREN',
             'LEFT_BRACE',
             'RIGHT_BRACE',
             'LEFT_BRACKET',
             'RIGHT_BRACKET',
             'COMMA',
             'SEMICOLON',
             'COLON',

             # FIN DE CONTRIBUCION KEVIN ROLDAN
         ) + tuple(reserved.values()) + tuple(essential_functions.values())

# INICIO CONTRIBUCION JORGE MAWYIN

def t_NULL(t):
    r'[Nn][Uu][Ll][Ll]'
    return t

# Expresiones Regulares simples para símbolos
# OPERADORES ARITMÉTICOS
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'\%'
t_POW = r'\*\*'
# OPERADORES DE ASIGNACION
t_EQUALS = r'='
t_PLUS_EQUALS = r'\+='

# OPERADORES DE COMPARACION
t_EQUALS_EQUALS = r'=='
t_IDENTICAL = r'==='
t_NOT_EQUALS = r'!=|<>'
t_NOT_IDENTICAL = r'!=='
t_SMALL_THAN = r'<'
t_GREATER_THAN = r'>'
t_SMALL_EQUALS_TO = r'<='
t_GREATER_EQUALS_TO = r'>='
t_SPACECRAFT = r'<=>'
t_NULL_FUSION = r'\?\?'

# OPERADORES DE INCREMENTO/DECREMENTO
t_INCREASE = r'\+\+'
t_DECREMENT = r'--'
# OPERADORES LOGICOS
t_LOGIC_AND = r'and|&&'
t_LOGIC_OR = r'or|\|\|'

t_LOGIC_NOT = r'!'

# FIN DE CONTRIBUCION JORGE MAWYIN
# INICIO DE CONTRIBUCION JEREMY POVEDA
# OPERADOR PARA STRING
t_STRING_CONCATENATION = r'\.'

t_STRING = r'\'[^\']*\'|"[^"]*"'



def t_FLOAT(t):
    r'([0-9]+\.[0-9])([eE][+-]?[0-9]+)?'
    t.value = float(t.value)
    return t


def t_COMMENT(t):
    r'(\#.*|\/\/.*|/\*(.|\n)*?\*/)'
    pass


# Expresión regular para números enteros, con casting para las 4 bases
def t_INTEGER(t):
    r'[+-]?([1-9][0-9]*|0|0[xX][0-9a-fA-F]+|0[0-7]+|0b[01]+)'
    base = 10
    if t.value.startswith("0x") or t.value.startswith("0X"):
        base = 16  # Hexadecimal
    elif t.value.startswith("0"):
        base = 8  # Octal
    if t.value.startswith("0b") or t.value.startswith("0B"):
        base = 2  # BInaria
    t.value = int(t.value, base)
    return t


# FIN DE LA CONTRIBUCION JEREMY POVEDA


# INICIO CONTRIBUCION KEVIN ROLDAN
t_VARIABLE = r'\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'


def t_TRUE(t):
    r'[Tt][Rr][Uu][Ee]'
    return t


def t_FALSE(t):
    r'[Ff][Aa][Ll][Ss][Ee]'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*'
    t.type = essential_functions.get(t.value, 'IDENTIFIER')
    if t.type == 'IDENTIFIER':
        t.type = reserved.get(t.value, 'IDENTIFIER')
    return t
    # FIN DE CONTRIBUCION KEVIN ROLDAN


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}")
    t.lexer.skip(1)


# Construccion de los lexers
lexer = lex.lex()
