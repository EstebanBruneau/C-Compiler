

code_line = open("code.c", 'r').read().split("\n")
code = ""
for line in code_line:
    for c in line:
        code += c
    code += "\\n"

line_counter = 1
character_counter = 0
T = None
L = None

class Token:
    def __init__(self, value, t_type, line):
        self.type = t_type
        self.value = value
        self.line = line
        
class Node:
    def __init__(self, type, value, child_list):
        self.type = type
        self.value = value
        self.children = child_list
        
    def add_child(self, child):
        self.children.append(child)
        
    def __str__(self):
        return self.type + " " + self.value + " " + str(self.children)
                
    

tok_type_list = [
    "tok_send", "tok_recieve",
    "tok_int", "tok_plus", "tok_minus", "tok_*", "tok_div", "tok_not", 
    "tok_and", "tok_or", "tok_double_equal", "tok_different", "tok_greater",
    "tok_less", "tok_greater_equal", "tok_less_equal", "tok_assign",
    "tok_semicolon", "tok_comma", "tok_open_parentheses", "tok_close_parentheses",
    "tok_open_brackets", "tok_close_brackets", "tok_open_braces", "tok_close_braces",
    "tok_mod", "tok_&", "tok_if", "tok_else", "tok_while", "tok_do", "tok_break", "tok_continue", 
    "tok_return", "tok_debug", "tok_eof", "tok_ident", "tok_constant"
]

nod_type_list = [
    "nod_unary_plus", "nod_binary_plus", "nod_unary_minus", "nod_binary_minus", "nod_logical_not"
]

def next():
    global character_counter, T, line_counter, code, L
    L = T
    
    if character_counter >= len(code):
        T = Token(0, "tok_eof", line_counter)
        character_counter += 1
        return
    char1 = code[character_counter]
    char2 = code[character_counter + 1] if character_counter + 1 < len(code) else ''
    # spaces
    if char1 == " ":
        T = None
        character_counter += 1
        return
    # new line
    elif char1 == "\\":
        if char2 == "n":
            T = None
            line_counter += 1
            character_counter += 2
            return
        else:
            print("Error: invalid token", char1, "at line", line_counter)
            T = None
            character_counter += 1
            return
    # signs/operations
    elif char1 == "(": 
        T = Token(0 , "tok_open_parentheses", line_counter)
        character_counter += 1
        return
    elif char1 == ")":
        T = Token(0, "tok_close_parentheses", line_counter)
        character_counter += 1
        return
    elif char1 == "{":
        T = Token(0, "tok_open_braces", line_counter)
        character_counter += 1
        return
    elif char1 == "}":
        T = Token(0, "tok_close_braces", line_counter)
        character_counter += 1
        return
    elif char1 == "[":
        T = Token(0, "tok_open_brackets", line_counter)
        character_counter += 1
        return
    elif char1 == "]":
        T = Token(0, "tok_close_brackets", line_counter)
        character_counter += 1
        return
    elif char1 == ";":
        T = Token(0, "tok_semicolon", line_counter)
        character_counter += 1
        return
    elif char1 == ",":
        T = Token(0, "tok_comma", line_counter)
        character_counter += 1
        return
    elif char1 == "+":
        T = Token(0, "tok_plus", line_counter)
        character_counter += 1
        return
    elif char1 == "-":
        T = Token(0, "tok_minus", line_counter)
        character_counter += 1
        return
    elif char1 == "*":
        T = Token(0, "tok_*", line_counter)
        character_counter += 1
        return
    elif char1 == "/":
        T = Token(0, "tok_div", line_counter)
        character_counter += 1
        return
    elif char1 == "%":
        T = Token(0, "tok_mod", line_counter)
        character_counter += 1
        return
    elif char1 == "&":
        T = Token(0, "tok_&", line_counter)
        character_counter += 1
        return
    elif char1 == "!":
        T = Token(0, "tok_not", line_counter)
        character_counter += 1
        return
    elif char1 == "=":
        if char2 == "=":
            T = Token(0, "tok_double_equal", line_counter)
            character_counter += 2
            return
        else:
            T = Token(0, "tok_assign", line_counter)
            character_counter += 1
            return
    elif char1 == ">":
        if char2 == "=":
            T = Token(0, "tok_greater_equal", line_counter)
            character_counter += 2
            return
        else:
            T = Token(0, "tok_greater", line_counter)
            character_counter += 1
            return
    elif char1 == "<":
        if char2 == "=":
            T = Token(0, "tok_less_equal", line_counter)
        else:
            T = Token(0, "tok_less", line_counter)
            character_counter += 1
            return
    elif char1 == "|":
        if char2 == "|":
            T = Token(0, "tok_or", line_counter)
            character_counter += 2
        else:
            print("Error: invalid token", char1, "at line", line_counter)
            T = None
            character_counter += 1
            return
    elif char1 == "&":
        if char2 == "&":
            T = Token(0, "tok_and", line_counter)
            character_counter += 2
        else:
            T = Token(0, "tok_&", line_counter)
            character_counter += 1
    # keywords
    elif char1 == "i" and char2 == "f":
        T = Token(0, "tok_if", line_counter)
        character_counter += 2
        return
    elif char1 == "e" and char2 == "l" and code[character_counter + 2] == "s" and code[character_counter + 3] == "e":
        T = Token(0, "tok_else", line_counter)
        character_counter += 4
        return
    elif char1 == "w" and char2 == "h" and code[character_counter + 2] == "i" and code[character_counter + 3] == "l" and code[character_counter + 4] == "e":
        T = Token(0, "tok_while", line_counter)
        character_counter += 5
        return
    elif char1 == "d" and char2 == "o":
        T = Token(0, "tok_do", line_counter)
        character_counter += 2
        return
    elif char1 == "b" and char2 == "r" and code[character_counter + 2] == "e" and code[character_counter + 3] == "a" and code[character_counter + 4] == "k":
        T = Token(0, "tok_break", line_counter)
        character_counter += 5
        return
    elif char1 == "c" and char2 == "o" and code[character_counter + 2] == "n" and code[character_counter + 3] == "t" and code[character_counter + 4] == "i" and code[character_counter + 5] == "n" and code[character_counter + 6] == "u" and code[character_counter + 7] == "e":
        T = Token(0, "tok_continue", line_counter)
        character_counter += 8
        return
    elif char1 == "r" and char2 == "e" and code[character_counter + 2] == "t" and code[character_counter + 3] == "u" and code[character_counter + 4] == "r" and code[character_counter + 5] == "n":
        T = Token(0, "tok_return", line_counter)
        character_counter += 6
        return
    elif char1 == "d" and char2 == "e" and code[character_counter + 2] == "b" and code[character_counter + 3] == "u" and code[character_counter + 4] == "g":
        T = Token(0, "tok_debug", line_counter)
        character_counter += 5
        return
    # types
    elif char1 == "i" and char2 == "n" and code[character_counter + 2] == "t":
        T = Token(0, "tok_int", line_counter)
        character_counter += 3
        return
    # send and recieve
    elif char1 == "s" and char2 == "e" and code[character_counter + 2] == "n" and code[character_counter + 3] == "d":
        T = Token(0, "tok_send", line_counter)
        character_counter += 4
        return
    elif char1 == "r" and char2 == "e" and code[character_counter + 2] == "c" and code[character_counter + 3] == "i" and code[character_counter + 4] == "e" and code[character_counter + 5] == "v" and code[character_counter + 6] == "e":
        T = Token(0, "tok_recieve", line_counter)
        character_counter += 7
        return
    # identifiers
    elif char1.isalpha():
        ident = ""
        while code[character_counter].isalpha() or code[character_counter].isdigit():
            ident += code[character_counter]
            character_counter += 1
        T = Token(ident, "tok_ident", line_counter)
        return
    # constants
    elif char1.isdigit():
        constant = ""
        while code[character_counter].isdigit():
            constant += code[character_counter]
            character_counter += 1
        constant = int(constant)
        T = Token(constant, "tok_constant", line_counter)
        return
    # unrecognized token
    else:
        print("Error: invalid token", char1, "at line", line_counter)
        T = None
        character_counter += 1
        return

    
def check(type):
    global T
    if T is not None and T.type == type:
        next()
        return True
    return False

def accept(type):
    global T
    if T is None:
        raise Exception("Error: unexpected None token at line", line_counter, character_counter)
    if T.type != type:
        raise Exception("Error: Found token", T.type, "instead of", type, "at line", T.line, character_counter)
    next()

def analex(code):
    global line_counter, character_counter, T
    line_counter = 1
    character_counter = 0
    T = None
    list_tokens = []
    while character_counter < len(code)+1:
        next()
        if T is not None:
            list_tokens.append(T)
            
    T = list_tokens[0]
    character_counter = 1
    line_counter = 1
    
    return list_tokens

def anasem(N):
    pass

def Optim(N):
    return N

def atom():
    global T, L

    if check("tok_constant"):
        value = L.value  # Capture the value of the constant token
        return Node("nod_constant", value, [])
        
    elif check("tok_open_parentheses"):
        A = expression()
        accept("tok_close_parentheses")
        return A
    raise Exception("Error: unexpected token", T.type, "at line", T.line)
            
def suffix():
    return atom()

def prefix():
    global T, L
    if check("tok_plus"):
        A = prefix()
        return A
    elif check("tok_minus"):
        A = prefix()
        return Node("nod_unary_minus", "-", [A])
    elif check("tok_not"):
        A = prefix()
        return Node("nod_logical_not", "!", [A])
    else:
        return suffix()

def expression():
    return prefix()

def instruction():
    return expression()

def function():
    return instruction()

def anasynth():
    global T
    while T is not None and T.type != "tok_eof":
        return instruction()
        
def gencode(N):
    if N.type == "nod_constant":
        print("push", N.value)
    elif N.type == "nod_unary_minus":
        print("push 0")
        gencode(N.children[0])
        print("sub")
    elif N.type == "nod_binary_plus":
        gencode(N.children[0])
        gencode(N.children[1])
        print("add")
    elif N.type == "nod_binary_minus":
        gencode(N.children[0])
        gencode(N.children[1])
        print("sub")
    elif N.type == "nod_logical_not":
        gencode(N.children[0])
        print("not")
  
# ---------------------------- degub ----------------------------
            
            
# for token in analex(code):
#     print(token.type, token.value, token.line)
    
    
# ---------------------------- main ----------------------------

print(".start")


analex(code)


while T is not None and T.type != "tok_eof":
    
    N = anasynth()
    
    anasem(N)
     
    N = Optim(N)
    
    gencode(N)
    
    print("dbg\nhalt")