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
    token_specification = [
        ("LPAR", r"\("),  # Identificador para abrir parênteses
        ("RPAR", r"\)"),  # Identificador para fechar parênteses
        ("QUOTE", r"'"),
        ("NUMBER", r"[-+]?\d+(\.\d+)?"),  # Integer or decimal number
        ("BOOL", r"(#t|#f)"),
        ("CHAR", r"#\\\w+"),
        ("STRING", r'"[^\n"\\]*(?:\\.[^\n"\\]*)*"'),
        ("COMMENT", r";[^\n]*"),
        ("NAME", r"[a-zA-Z\+\-\.\*\/<=>!?:$%_&~^]+"),
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'COMMENT':
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        yield Token(kind, value)


examples = [
    '(aslkdj#fsd x y)',
    '#t #f teste',
    'aqui tem uma "string"',
    r'"hello" "\"world\""'
]

for ex in examples:
    print(ex)
    for tok in lex(ex):
        print('    ', tok)
    print()
