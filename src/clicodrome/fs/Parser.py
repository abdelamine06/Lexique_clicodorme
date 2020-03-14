from .Features import *
from .Feature import *
from .Value import *
from .ListFeatures import *
from .Atom import *

import ply.lex as lex
import ply.yacc as yacc

class Parser():
    
    def __init__(self):
        # Build the lexer and parser
        lex.lex(module=self)
        yacc.yacc(module=self, start='features', debug='true')

    # List of token names.   This is always required
    tokens = (
       'LBRACKET',
       'RBRACKET',
       'COMMA',
       'COLON',
       'PIPE',
       'IDENTIFIER',
    )

    # Regular expression rules for simple tokens
    t_LBRACKET  = r'\['
    t_RBRACKET  = r'\]'
    t_COMMA  = r','
    t_COLON  = r':'
    t_PIPE  = r'\|'
    
    precedence = (
    )

    def t_IDENTIFIER(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # [...]
    def p_features(self, p):
        '''features : LBRACKET list_feature RBRACKET
               | LBRACKET RBRACKET'''
        if len(p) > 2:
            p[0] = p[2]
        else:
            p[0] = Features()

    # attr:val, attr:val, ...
    def p_list_feature(self, p):
        '''list_feature : list_feature COMMA feature
                    | feature'''
        if len(p) > 2:
            p[0] = p[1]
            p[0].add(p[3])
        else:
            p[0] = Features(list())
            p[0].add(p[1])

    # attr:val
    def p_feature(self, p):
        '''feature : IDENTIFIER COLON atom
                |  IDENTIFIER COLON list_features'''
        p[0] = Feature(p[1], Value(p[3]))

    # attr:val
    def p_atom(self, p):
        '''atom : IDENTIFIER
                |  atom PIPE IDENTIFIER'''
        if len(p) > 2:
            p[0] = p[1]
            p[0].add(p[3])
        else:
            p[0] = Atom(list())
            p[0].add(p[1])

    # [...], [...], [...]
    def p_list_features(self, p):
        '''list_features : list_features PIPE features
               | features'''
        if len(p) > 2:
            p[0] = p[1]
            p[0].add(p[3])
        else:
            p[0] = ListFeatures(list())
            p[0].add(p[1])

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")

    def parse(self, str):
        return yacc.parse(str)
 