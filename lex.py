import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    # keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ("LPAR", r"\("),  # Identificador para abrir parênteses
        ("RPAR", r"\)"),  # Identificador para fechar parênteses
        ("NUMBER", r"[-+]?\d+(\.\d+)?"),  # Integer or decimal number
        ("NAME", r"[a-zA-Z\+\-\.\*\/<=>!?:$%_&~^]+"),
        ("BOOL", r"(#t|#f)"),
        ("CHAR", r"#\\\w+"),
        # ('ASSIGN',   r'='),           # Assignment operator
        # ('COMA',      r','),            # Statement terminator
        # ('OP',       r'[+\-*/\^]'),      # Arithmetic operators
        # ('NEWLINE',  r'\n'),           # Line endings
        # ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        # ("NAME", r"[a-zA-Z_][a-zA-Z_0-9]*"),  # Variable or function names
        # ("FAT", r"!"),
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    # line_num = 1
    # line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        # column = mo.start() - line_start
        # if kind == 'NUMBER':
        #     print(f'{value!r} NUMBER')
        #     value = float(value) if '.' in value else int(value)
        # elif kind == 'ID' and value in keywords:
        #     kind = value
        # elif kind == 'NEWLINE':
        #     line_start = mo.end()
        #     line_num += 1
        #     continue
        # elif kind == 'SKIP':
        #     continue
        if kind == 'MISMATCH':
            # print(f'{value!r} unexpected')
            continue
            # raise RuntimeError(f'{value!r} unexpected')
        # print((kind, value))
        yield Token(kind, value)
        # yield Token(kind, value, line_num, column)

    # return [Token('INVALIDA', 'valor inválido')]

examples = [
    '(aslkdj#fsd x y)',
    '#t #f teste'
]

for ex in examples:
    print(ex)
    for tok in lex(ex):
        print('    ', tok)
    print()
