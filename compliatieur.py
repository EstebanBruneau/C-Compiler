class Token:
    def __init__(self, value, t_type, line):
        self.type = t_type
        self.value = value
        self.line = line
        
    def __str__(self):
        return "Token: " + self.type + " " + str(self.value) + " " + str(self.line)
        
class Node:
    def __init__(self, type, value, children, nbVar = 0):
        self.type = type
        self.value = value
        self.children = children
        self.nbVar = nbVar

    def add_child(self, child):
        self.children.append(child)
        
    def count_children(self):
        return len(self.children)
        
    def __str__(self):
        return f"Node(type={self.type}, value={self.value}, children={self.children})"
    
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
    def __init__(self, name, type, adress, value):
        self.name = name
        self.type = type
        self.adress = adress
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

def semantic_analysis(ast):
    for node in ast:
        anasem(node)

def anasem(N):
    if N.type == "nod_ident":
        symbol = find_symbol(N.value)
        if symbol is None:
            raise Exception(f"Error: symbol '{N.value}' not found in the current scope")
    
    for child in N.children:
        anasem(child)

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
    
    elif check("tok_ident"):
        symbol = find_symbol(L.value)
        if symbol is None:
            print("Scope:", current_scope())
            raise Exception(f"Error: symbol '{L.value}' not found in the current scope")
        return Node("nod_ident", L.value, [])
    
    raise Exception("Error: unexpected token", T.type, "at line", T.line)
            
def suffix():
    global T, L
    
    R = atom()
    if check("tok_open_parentheses"):
        R = Node("nod_call", "call", [R])
        while not check("tok_close_parentheses"):
            R.add_child(expression())
            if not check("tok_comma"):
                break
    return R   

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
    elif check("tok_&"):
        A = prefix()
        return Node("nod_address", "&", [A])
    elif check("tok_*"):
        A = prefix()
        return Node("nod_dereference", "*", [A])
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
        Node1 = Node(op[2], op[2], [Node1, Node2])
    return Node1

def instruction():
    global T, L, line_counter, character_counter, nbVar

    # Debug Statement
    if check("tok_debug"):
        N = expression()
        accept("tok_semicolon")
        return Node("nod_debug", "debug", [N])

    # Block Statement
    elif check("tok_open_braces"):
        # push_scope()
        N = Node("nod_block", "block", [])
        while not check("tok_close_braces"):
            N.add_child(instruction())
        # pop_scope()
        return N

   # Variable Declaration
    elif check("tok_int"):
        pointer_level = 0
        while check("tok_*"):
            pointer_level += 1
            
        accept("tok_ident")
        var_type = "int" + "*" * pointer_level
        symbol = Symbol(L.value, var_type, nbVar, None)
        current_scope().add_symbol(L.value, symbol)
        N = Node("nod_declaration", L.value, [])
        nbVar += 1
        accept("tok_semicolon")
        return N
    
    # Assignment Statement
    elif check("tok_ident"):
        symbol = find_symbol(L.value)
        if symbol is None:
            raise Exception(f"Error: symbol '{L.value}' not found in the current scope")
        N = Node("nod_assign", L.value, [])
        N.add_child(Node("nod_ident", L.value, []))
        accept("tok_assign")
        N.add_child(expression())
        accept("tok_semicolon")
        return N
    elif check("tok_*"):
        accept("tok_ident")
        symbol = find_symbol(L.value)
        if symbol is None:
            raise Exception(f"Error: symbol '{L.value}' not found in the current scope")
        N = Node("nod_assign", L.value, [])
        N.add_child(Node("nod_ident", L.value, []))
        accept("tok_assign")
        N.add_child(expression())
        accept("tok_semicolon")
        return N

    # Conditional Statement
    elif check("tok_if"):
        print("if statement")
        accept("tok_open_parentheses")
        condition = expression()
        print("condition:", condition)
        accept("tok_close_parentheses")
        print("if instruction")
        then_instr = instruction()
        print("then instruction:", then_instr)
        if check("tok_else"):
            else_instr = instruction()
            return Node("nod_if_else", "if_else", [condition, then_instr, else_instr])
        return Node("nod_if", "if", [condition, then_instr])
    
    # While Loop
    elif check("tok_while"):
        print("while statement")
        accept("tok_open_parentheses")
        condition = expression()
        print("condition:", condition)
        accept("tok_close_parentheses")
        print("while instruction")
        loop_instr = instruction()
        print("loop instruction:", loop_instr)
        return Node("nod_while", "while", [condition, loop_instr])

    # Break Statement
    elif check("tok_break"):
        accept("tok_semicolon")
        return Node("nod_break", "break", [])
    
    # return statement
    elif check("tok_return"):
        N = expression()
        accept("tok_semicolon")
        return Node("nod_return", "return", [N])
    
    # Expression Handling
    else:
        N = expression()
        accept("tok_semicolon")
        return Node("nod_drop", "drop", [N])

def function():    
    global T, L, line_counter, character_counter, nbVar, funcMode

    # Function Declaration
    if check("tok_int"):
        accept("tok_ident")
        S = Symbol(L.value, "type_function", None, None)
        push_scope()
        N = Node("nod_function", L.value, [])
        accept("tok_open_parentheses")
        while not check("tok_close_parentheses"):
            accept("tok_int")
            accept("tok_ident")
            symbol = Symbol(L.value, "type_variable", nbVar, None)
            current_scope().add_symbol(L.value, symbol)
            # print("Adding parameter to scope : ", L.value)
            if not check("tok_comma"):
                accept("tok_close_parentheses")
                break
        for child in N.children:
            anasem(child)
        # pop_scope()   # PROF
        N.nbVar = nbVar - (N.count_children()-1)
        funcMode = False  
        return N

    # Function Call
    if check("tok_ident"):
        func_name = L.value
        accept("tok_ident")
        accept("tok_open_parentheses")
        call_node = Node("nod_call", func_name, [])
        while not check("tok_close_parentheses"):
            call_node.add_child(expression())
            if not check("tok_comma"):
                break
        accept("tok_close_parentheses")
        return call_node
                    
def anasynth():
    global T, L, line_counter, character_counter, nbVar, funcMode
    ast = []
    while T is not None and T.type != "tok_eof":
        if funcMode:
            N = function()
        else:
            N = instruction()
        if N is not None:
            ast.append(N)
        else:
            raise Exception("Error: Node from instruction/function is None")
    # for node in ast:
    #     print(node)
    return ast

def push_scope():
    # print("pushing scope : ")
    global nbVar, var_scopes
    var_scopes.append(Scope())
    nbVar = 0
    # print_scopes()
    # print("scope pushed")
        
def pop_scope():
    # print("popping scope : ")
    global nbVar, var_scopes
    var_scopes.pop()
    nbVar = 0
    # print_scopes()
    # print("scope popped")
    
def current_scope():
    return var_scopes[-1]

def print_scopes():
    for scope in var_scopes:
        print(scope)

def generate_label():
    global label_counter
    label = f"l{label_counter}"
    label_counter += 1
    return label

def find_symbol(name):
    """
    Searches for a symbol by name in the current scope stack. If the symbol is not found in the current scope,
    the search continues to the parent scopes.

    Args:
        name (str): The name of the symbol to search for.

    Returns:
        Optional[Symbol]: The symbol if found, otherwise None.
    """
    for scope in reversed(var_scopes):
        symbol = scope.get_symbol(name)
        if symbol is not None:
            return symbol
    return None

def gencode(N):
    def binary_operation(N, operation):
        gencode(N.children[0]) 
        gencode(N.children[1])
        print(operation)

    if N is None:
        raise Exception("Error: gencode received None")

    # Base Cases
    if N.type == "nod_eof":
        return
    elif N.type == "nod_constant":
        print(f"push {N.value}")

    # Unary Operations
    elif N.type == "nod_unary_minus":
        print("push 0")
        gencode(N.children[0])
        print("sub")
    elif N.type == "nod_logical_not":
        gencode(N.children[0])
        print("not")

    # Binary Operations
    elif N.type == "nod_binary_plus":
        binary_operation(N, "add")
    elif N.type == "nod_binary_minus":
        binary_operation(N, "sub")
    elif N.type == "nod_multiplication":
        binary_operation(N, "mul")
    elif N.type == "nod_division":
        binary_operation(N, "div")
    elif N.type == "nod_modulo":
        binary_operation(N, "mod")

    # Comparison Operations
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

    # Logical Operations
    elif N.type == "nod_and":
        binary_operation(N, "and")
    elif N.type == "nod_or":
        binary_operation(N, "or")

    # Control Flow
    elif N.type == "nod_block":
        for child in N.children:
            gencode(child)
    elif N.type == "nod_if":
        label_else = generate_label()
        label_end = generate_label()
        gencode(N.children[0])
        print("jz", label_else)
        gencode(N.children[1])
        print("jmp", label_end)
        print(label_else + ":")
        print(label_end + ":")
    elif N.type == "nod_if_else":
        label_else = generate_label()
        label_end = generate_label()
        gencode(N.children[0])
        print("jz", label_else)
        gencode(N.children[1])
        print("jmp", label_end)
        print(label_else + ":")
        gencode(N.children[2])
        print(label_end + ":")
    elif N.type == "nod_while":
        label_start = generate_label()
        label_end = generate_label()
        print(label_start + ":")
        gencode(N.children[0])
        print("jz", label_end)
        gencode(N.children[1])
        print("jmp", label_start)
        print(label_end + ":")
    elif N.type == "nod_break":
        print("jmp", "end_while")
    elif N.type == "nod_continue":
        print("jmp", "start_while")

    # Special Operations
    elif N.type == "nod_send":
        gencode(N.children[0])
        print("send")
    elif N.type == "nod_receive":
        print("receive")
    elif N.type == "nod_drop":
        print("drop")

    # Variable Handling
    elif N.type == "nod_declaration":
        symbol = Symbol(N.value, "type_variable", nbVar, None)
        current_scope().add_symbol(N.value, symbol)
    elif N.type == "nod_ident":
        symbol = find_symbol(N.value)
        if symbol is None:
            raise Exception(f"Error: symbol '{N.value}' not found in the current scope")
        print(f"load {symbol.adress} ({N.value})")
    elif N.type == "nod_assign":
        gencode(N.children[0])
        gencode(N.children[1])
        print("store")

    # Function Handling
    elif N.type == "nod_function":
        print(f"{N.value}:")
        for i in range(1, len(N.children)):
            gencode(N.children[i])
    elif N.type == "nod_return":
        gencode(N.children[0])
        print("ret")
    
    
    else:
        raise Exception("Error: unknown node type", N.type)

  
# ---------------------------- degub ----------------------------
            
            
# for token in analex(code):
#     print(token.type, token.value, token.line)
    
    
# ---------------------------- main ----------------------------

funcMode = True


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
label_counter = 0
nbVar = 0

# List of scopes, each scope is a list of symbols
var_scopes = [Scope()]



print(".start")
print("prep main")
print("call 0")
# print("halt") #?

tokens = analex(code)
next()
push_scope()
ast = anasynth()
semantic_analysis(ast)
for node in ast:
    node = Optim(node)
    gencode(node)
print("dbg")
pop_scope()