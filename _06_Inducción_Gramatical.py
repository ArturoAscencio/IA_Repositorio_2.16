pip install nltk

import nltk
from nltk import Nonterminal, nonterminals, Production, CFG

# Ejemplos de oraciones
sentences = [
    "El gato come pescado.",
    "Los perros ladran fuerte.",
    "El p�jaro canta en la ma�ana.",
]

# Tokenizaci�n de las oraciones
tokens = [nltk.word_tokenize(sentence) for sentence in sentences]

# Creaci�n de la gram�tica inductiva
start_symbol = Nonterminal('S')
grammar = CFG(start_symbol, [])

for tokenized_sentence in tokens:
    production = Production(start_symbol, tokenized_sentence)
    grammar.productions().append(production)

# Mostrar la gram�tica resultante
print(grammar)

# Ejemplo de an�lisis sint�ctico con la gram�tica inductiva
parser = nltk.ChartParser(grammar)
for tokenized_sentence in tokens:
    for tree in parser.parse(tokenized_sentence):
        tree.pretty_print()
pip install nltk

import nltk
from nltk import Nonterminal, nonterminals, Production, CFG

# Ejemplos de oraciones
sentences = [
    "El gato come pescado.",
    "Los perros ladran fuerte.",
    "El p�jaro canta en la ma�ana.",
]

# Tokenizaci�n de las oraciones
tokens = [nltk.word_tokenize(sentence) for sentence in sentences]

# Creaci�n de la gram�tica inductiva
start_symbol = Nonterminal('S')
grammar = CFG(start_symbol, [])

for tokenized_sentence in tokens:
    production = Production(start_symbol, tokenized_sentence)
    grammar.productions().append(production)

# Mostrar la gram�tica resultante
print(grammar)

# Ejemplo de an�lisis sint�ctico con la gram�tica inductiva
parser = nltk.ChartParser(grammar)
for tokenized_sentence in tokens:
    for tree in parser.parse(tokenized_sentence):
        tree.pretty_print()