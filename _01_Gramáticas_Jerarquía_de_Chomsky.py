grammar_type_0 = {
    "S -> aSb | ab": 1
}

# Gramática de Tipo 1
grammar_type_1 = {
    "aAb -> aaB": 1,
    "aAa -> aa": 1,
    "Ba -> aB": 1,
    "Ba -> ab": 1,
    "Ba -> bB": 1,
    "Ba -> bb": 1
}

# Gramática de Tipo 2
grammar_type_2 = {
    "S -> aS | bS | ?": 1
}

# Gramática de Tipo 3
grammar_type_3 = {
    "S -> aA | bB": 1,
    "A -> a | ?": 1,
    "B -> b | ?": 1
}
