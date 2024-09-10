

class Token:
    def __init__(self, value, t_type, line):
        self.type = t_type
        self.value = value
        self.line = line
        
    def __str__(self):
        return "Token: " + self.type + " " + str(self.value) + " " + str(self.line)
        
class Node:
    def __init__(self, type, value, child_list):
        self.type = type
        self.value = value
        self.children = child_list
        
    def add_child(self, child):
        self.children.append(child)
        
    def __str__(self):
        return "Node: " + self.type + " " + str(self.value) + " " + str(self.children)
    
class Symbol:
    """
    A class to represent a symbol in a compiler.

    Attributes
    ----------
    name : str
        The name of the symbol.
    type : str
        The type of the symbol (e.g., variable, function).
    value : any
        The value associated with the symbol.

    Methods
    -------
    __init__(name, type, value)
        Initializes the Symbol with a name, type, and value.
    
    __str__()
        Returns a string representation of the Symbol.
    """
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value 
    def __str__(self):
        return "Symbol: " + self.name + " " + self.type + " " + str(self.value)
            
            
class Scope:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol):
        self.symbols[name] = symbol

    def get_symbol(self, name):
        return self.symbols.get(name)

    def __str__(self):
        return str(self.symbols)
            
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
        character_counter += 1
        next()
    # new line
    elif char1 == "\\":
        if char2 == "n":
            line_counter += 1
            character_counter += 2
            next()
        else:
            print("Error: invalid token", char1, "at line", line_counter)
            character_counter += 1
            next()
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
            raise Exception("Error: invalid token", char1, "at line", line_counter)
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
        raise Exception("Error: invalid token", char1, "at line", line_counter)

 
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
            
    T = None
    character_counter = 0
    line_counter = 1
    
    # print("Analex done")
    # for token in list_tokens:
    #     print(token)
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


# priority, right_associative, node_type
operators = {
    "tok_*": (7, 1, "nod_multiplication"),
    "tok_div": (7, 1, "nod_division"),
    "tok_mod": (7, 1, "nod_modulo"),
    "tok_plus": (6, 1, "nod_binary_plus"),
    "tok_minus": (6, 1, "nod_binary_minus"),
    "tok_greater": (5, 1, "nod_greater"),
    "tok_less": (5, 1, "nod_less"),
    "tok_greater_equal": (5, 1, "nod_greater_equal"),
    "tok_less_equal": (5, 1, "nod_less_equal"),
    "tok_double_equal": (4, 1, "nod_double_equal"),
    "tok_different": (4, "nod_different"),
    "tok_and": (2, 1, "nod_and"),
    "tok_or": (2, 1, "nod_or"),
    "tok_assign": (1, 0, "nod_assign")
}
    
def expression():
    return expression2(0)

def expression2(pmin):
    Node1 = prefix()
    while T is not None and T.type != "tok_eof":
        op = operators.get(T.type)
        if op is None or op[0] < pmin:
            return Node1
        next()
        if T is None:
            raise Exception("Error: unexpected None token after operator")
        Node2 = expression2(op[0] + op[1]) # +1 if right associative
        # print(f"\nNode1: {Node1}\nNode2: {Node2}")
        Node1 = Node(op[2], op[2], [Node1, Node2])  # Use op[2] for the node type
    return Node1

def instruction():
    global T, L, line_counter, character_counter
    if check("tok_debug"):
        N = expression()
        accept("tok_semicolon")
        return Node("nod_debug", "debug", [N])
    elif check("tok_open_braces"):
        push_scope()
        N = Node("nod_block", "block", [])
        print("Start block")
        while not check("tok_close_braces"):
            N.add_child(instruction())
        pop_scope()
        print("End block")
        return N
    if check("tok_int"):
        accept("tok_ident")
        symbol = Symbol(L.value, "variable", None)
        current_scope().add_symbol(L.value, symbol)
        N = Node("nod_declaration", L.value, [])
        accept("tok_semicolon")
        return N
    else:
        N = expression()
        accept("tok_semicolon")
        return Node("nod_drop", "drop", [N])


def function():
    return instruction()

def anasynth():
    global T
    while T is not None and T.type != "tok_eof":
        # print("processing token ", T.type, T.value, "at line", T.line)
        N = function()
        if N is not None:
            # print(f"generated node: {N}")
            gencode(N)
        else:
            raise Exception("Error: instruction returned None")
    return Node("nod_eof", "eof", [])

def push_scope():
    var_scopes.append(Scope())

def pop_scope():
    var_scopes.pop()

def current_scope():
    return var_scopes[-1]

def gencode(N):
    def binary_operation(N, operation):
        gencode(N.children[0])
        gencode(N.children[1])
        print(operation)
        
    if N is None:
        raise Exception("Error: gencode revceived None")
    
    if N.type == "nod_eof":
        return
    # print(f"Generating code for node {N}")
    if N.type == "nod_constant":
        print("push", N.value)
    elif N.type == "nod_unary_minus":
        print("push 0")
        gencode(N.children[0])
        print("sub")
    elif N.type == "nod_binary_plus":
        binary_operation(N, "add")
    elif N.type == "nod_binary_minus":
        binary_operation(N, "sub")
    elif N.type == "nod_logical_not":
        gencode(N.children[0])
        print("not")
    elif N.type == "nod_multiplication":
        binary_operation(N, "mul")
    elif N.type == "nod_division":
        binary_operation(N, "div")
    elif N.type == "nod_modulo":
        binary_operation(N, "mod")
    elif N.type == "nod_greater":
        binary_operation(N, "cmpgt")
    elif N.type == "nod_less":
        binary_operation(N, "cmplt")
    elif N.type == "nod_greater_equal":
        binary_operation(N, "cmpge")
    elif N.type == "nod_less_equal":
        binary_operation(N, "cmple")
    elif N.type == "nod_double_equal":
        binary_operation(N, "cmpeq")
    elif N.type == "nod_different":
        binary_operation(N, "cmpne")
    elif N.type == "nod_and":
        binary_operation(N, "and")
    elif N.type == "nod_or":
        binary_operation(N, "or")
    elif N.type == "nod_block":
        for child in N.children:
            gencode(child)
    elif N.type == "nod_debug":
        gencode(N.children[0])
        print("dbg")
    elif N.type == "nod_drop":
        gencode(N.children[0])
        print("drop")
    elif N.type == "nod_declaration":
        print("push 0")
        print("pop", current_scope().get_symbol(N.value).name)
    else:
        raise Exception("Error: unknown node type", N.type)
    

  
# ---------------------------- degub ----------------------------
            
            
# for token in analex(code):
#     print(token.type, token.value, token.line)
    
    
# ---------------------------- main ----------------------------

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

# List of scopes, each scope is a list of symbols
var_scopes = [Scope()]

print(".start")


analex(code)


while (1):
    if T is not None:
        if T.type == "tok_eof":
            break
    if T is None:
        next()
    
    N = anasynth()
    
    anasem(N)
     
    N = Optim(N)
    
    gencode(N)
    
print("dbg\nhalt")