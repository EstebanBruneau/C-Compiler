import sys
from colorama import init, Fore, Back, Style


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
    def __init__(self, name, type, adress, value):
        self.name = name
        self.type = type
        self.adress = adress
        self.value = value if type == "function" else None
        
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
   
# Gestion des erreurs
init(autoreset=True) # Initialize colorama
def display_error(message, line=None, character=None):
    error_prefix = f"{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL}"
    location = f" at line {line-1}" if line else ""
    location += f", character {line_character_counter}" if line_character_counter else ""
    if message == "Unexpected token 'tok_eof'":
        print(f"{error_prefix} Unexpected end of file{location}", file=sys.stderr)
    else:
        print(f"{error_prefix} {message}{location}", file=sys.stderr)
        

def display_ast(node, indent=0):
    """Recursively display the AST nodes."""
    if isinstance(node, list):
        for item in node:
            display_ast(item, indent)
    else:
        indent_str = ' ' * (indent * 2)
        print(f"{indent_str}Node(type={node.type}, value={node.value}, nbVar={node.nbVar})")
        for child in node.children:
            display_ast(child, indent + 1)

def next():
    global character_counter, T, line_counter, code, L, line_character_counter
    L = T
    
    if character_counter >= len(code):
        T = Token(0, "tok_eof", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    char1 = code[character_counter]
    char2 = code[character_counter + 1] if character_counter + 1 < len(code) else ''
    
    # spaces
    if char1 == " ":
        character_counter += 1
        line_character_counter += 1
        next()
    # new line
    elif char1 == "\\":
        if char2 == "n":
            line_counter += 1
            character_counter += 2
            line_character_counter = 0  # Reset for new line
            next()
        else:
            display_error(f"Invalid token '{char1}'", line_counter, line_character_counter)
            character_counter += 1
            line_character_counter += 1
            next()
    # signs/operations
    elif char1 == "(": 
        T = Token(0 , "tok_open_parentheses", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == ")":
        T = Token(0, "tok_close_parentheses", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "{":
        T = Token(0, "tok_open_braces", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "}":
        T = Token(0, "tok_close_braces", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "[":
        T = Token(0, "tok_open_brackets", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "]":
        T = Token(0, "tok_close_brackets", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == ";":
        T = Token(0, "tok_semicolon", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == ",":
        T = Token(0, "tok_comma", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "+":
        T = Token(0, "tok_plus", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "-":
        T = Token(0, "tok_minus", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "*":
        T = Token(0, "tok_*", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "/":
        T = Token(0, "tok_div", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "%":
        T = Token(0, "tok_mod", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "&":
        T = Token(0, "tok_&", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "!":
        T = Token(0, "tok_not", line_counter)
        character_counter += 1
        line_character_counter += 1
        return
    elif char1 == "=":
        if char2 == "=":
            T = Token(0, "tok_double_equal", line_counter)
            character_counter += 2
            line_character_counter += 2
            return
        else:
            T = Token(0, "tok_assign", line_counter)
            character_counter += 1
            line_character_counter += 1
            return
    elif char1 == ">":
        if char2 == "=":
            T = Token(0, "tok_greater_equal", line_counter)
            character_counter += 2
            line_character_counter += 2
            return
        else:
            T = Token(0, "tok_greater", line_counter)
            character_counter += 1
            line_character_counter += 1
            return
    elif char1 == "<":
        if char2 == "=":
            T = Token(0, "tok_less_equal", line_counter)
        else:
            T = Token(0, "tok_less", line_counter)
            character_counter += 1
            line_character_counter += 1
            return
    elif char1 == "|":
        if char2 == "|":
            T = Token(0, "tok_or", line_counter)
            character_counter += 2
            line_character_counter += 2
        else:
            display_error(f"Invalid token '{char1}'", line_counter, line_character_counter)
            sys.exit(1)
    elif char1 == "&":
        if char2 == "&":
            T = Token(0, "tok_and", line_counter)
            character_counter += 2
            line_character_counter += 2
        else:
            T = Token(0, "tok_&", line_counter)
            character_counter += 1
            line_character_counter += 1
    # keywords
    elif char1 == "i" and char2 == "f":
        T = Token(0, "tok_if", line_counter)
        character_counter += 2
        line_character_counter += 2
        return
    elif char1 == "e" and char2 == "l" and code[character_counter + 2] == "s" and code[character_counter + 3] == "e":
        T = Token(0, "tok_else", line_counter)
        character_counter += 4
        line_character_counter += 4
        return
    elif char1 == "w" and char2 == "h" and code[character_counter + 2] == "i" and code[character_counter + 3] == "l" and code[character_counter + 4] == "e":
        T = Token(0, "tok_while", line_counter)
        character_counter += 5
        line_character_counter += 5
        return
    elif char1 == "d" and char2 == "o":
        T = Token(0, "tok_do", line_counter)
        character_counter += 2
        line_character_counter += 2
        return
    elif char1 == "b" and char2 == "r" and code[character_counter + 2] == "e" and code[character_counter + 3] == "a" and code[character_counter + 4] == "k":
        T = Token(0, "tok_break", line_counter)
        character_counter += 5
        line_character_counter += 5
        return
    elif char1 == "c" and char2 == "o" and code[character_counter + 2] == "n" and code[character_counter + 3] == "t" and code[character_counter + 4] == "i" and code[character_counter + 5] == "n" and code[character_counter + 6] == "u" and code[character_counter + 7] == "e":
        T = Token(0, "tok_continue", line_counter)
        character_counter += 8
        line_character_counter += 8
        return
    elif char1 == "r" and char2 == "e" and code[character_counter + 2] == "t" and code[character_counter + 3] == "u" and code[character_counter + 4] == "r" and code[character_counter + 5] == "n":
        T = Token(0, "tok_return", line_counter)
        character_counter += 6
        line_character_counter += 6
        return
    elif char1 == "d" and char2 == "e" and code[character_counter + 2] == "b" and code[character_counter + 3] == "u" and code[character_counter + 4] == "g":
        T = Token(0, "tok_debug", line_counter)
        character_counter += 5
        line_character_counter += 5
        return
    elif char1 == "f" and char2 == "o" and code[character_counter + 2] == "r":
        T = Token(0, "tok_for", line_counter)
        character_counter += 3
        line_character_counter += 3
        return
    # types
    elif char1 == "i" and char2 == "n" and code[character_counter + 2] == "t":
        T = Token(0, "tok_int", line_counter)
        character_counter += 3
        line_character_counter += 3
        return
    # send and recieve
    elif char1 == "s" and char2 == "e" and code[character_counter + 2] == "n" and code[character_counter + 3] == "d":
        T = Token(0, "tok_send", line_counter)
        character_counter += 4
        line_character_counter += 4
        return
    elif char1 == "r" and char2 == "e" and code[character_counter + 2] == "c" and code[character_counter + 3] == "i" and code[character_counter + 4] == "e" and code[character_counter + 5] == "v" and code[character_counter + 6] == "e":
        T = Token(0, "tok_recieve", line_counter)
        character_counter += 7
        line_character_counter += 7
        return
    # identifiers
    elif char1.isalpha():
        ident = ""
        while code[character_counter].isalpha() or code[character_counter].isdigit():
            ident += code[character_counter]
            character_counter += 1
            line_character_counter += 1
        T = Token(ident, "tok_ident", line_counter)
        return
    # constants
    elif char1.isdigit():
        constant = ""
        while code[character_counter].isdigit():
            constant += code[character_counter]
            character_counter += 1
            line_character_counter += 1
        constant = int(constant)
        T = Token(constant, "tok_constant", line_counter)
        return
    # unrecognized token
    else:
        display_error(f"Invalid token '{char1}'", line_counter, line_character_counter)
        sys.exit(1)
 
def check(type):
    global T
    if T is not None and T.type == type:
        next()
        return True
    return False

def accept(type):
    global T
    if T is None:
        display_error("Unexpected None token", line_counter, line_character_counter)
        sys.exit(1)
    if T.type != type:
        display_error(f"Found token '{T.type}' instead of '{type}'", T.line, line_character_counter)
        sys.exit(1)
    next()

def analex(code):
    global line_counter, character_counter, T, line_character_counter
    line_counter = 1
    character_counter = 0
    line_character_counter = 0
    T = None
    list_tokens = []
    while character_counter < len(code)+1:
        next()
        if T is not None:
            list_tokens.append(T)
            
    T = None
    character_counter = 0
    line_counter = 1
    line_character_counter = 0
    
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
            display_error(f"Symbol '{N.value}' not found in the current scope")
            sys.exit(1)
    elif N.type == "nod_function":
        push_scope()
        for child in N.children:
            anasem(child)
        pop_scope()
    elif N.type == "nod_call":
        function_symbol = find_symbol(N.value)
        if function_symbol is None or function_symbol.type != "function":
            display_error(f"Function '{N.value}' not found or is not a function")
            sys.exit(1)
        if len(N.children) - 1 != len(function_symbol.value):  # -1 because the first child is the function name
            display_error(f"Incorrect number of arguments for function '{N.value}'")
            sys.exit(1)
        for child in N.children[1:]:  # Skip the first child (function name)
            anasem(child)
    else:
        for child in N.children:
            anasem(child)

def Optim(N):
    return N

def atom():
    global T, L

    if check("tok_constant"):
        value = L.value
        return Node("nod_constant", value, [])
        
    elif check("tok_open_parentheses"):
        A = expression()
        accept("tok_close_parentheses")
        return A
    
    elif check("tok_ident"):
        symbol = find_symbol(L.value)
        if symbol is None:
            display_error(f"Symbol '{L.value}' not found in the current scope", T.line, line_character_counter)
            sys.exit(1)
        return Node("nod_ident", L.value, [])
    
    display_error(f"Unexpected token '{T.type}'", T.line, line_character_counter)
    sys.exit(1)
            
def suffix():
    global T, L
    
    R = atom()
    if check("tok_open_parentheses"):
        R = Node("nod_call", R.value, [R])  # Use R.value as the function name
        if not check("tok_close_parentheses"):
            while True:
                R.add_child(expression())
                if not check("tok_comma"):
                    break
            accept("tok_close_parentheses")
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
    global T, L, line_counter, character_counter, nbVar, line_character_counter

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

    # Declaration Statement (Variable or Pointer)
    elif check("tok_int"):
        # Pointer
        if check("tok_*"):
            accept("tok_ident")
            symbol = Symbol(L.value, "pointer", nbVar, None)
            current_scope().add_symbol(L.value, symbol)
            N = Node("nod_declaration", L.value, [])
            nbVar += 1
            accept("tok_semicolon")
            return N
        # Variable
        else:
            accept("tok_ident")
            symbol = Symbol(L.value, "type_variable", nbVar, None)
            current_scope().add_symbol(L.value, symbol)
            N = Node("nod_declaration", L.value, [])
            nbVar += 1
            accept("tok_semicolon")
            return N
       
    # Variable Assignment
    elif check("tok_ident"):
        symbol = find_symbol(L.value)
        if symbol is None:
            display_error(f"Symbol '{L.value}' not found in the current scope", T.line, line_character_counter)
            sys.exit(1)
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
            display_error(f"Symbol '{L.value}' not found in the current scope", T.line, line_character_counter)
            sys.exit(1)
        N = Node("nod_assign", L.value, [])
        N.add_child(Node("nod_ident", L.value, []))
        accept("tok_assign")
        N.add_child(expression())
        accept("tok_semicolon")
        return N

    # Conditional Statement
    elif check("tok_if"):
        accept("tok_open_parentheses")
        condition = expression()
        accept("tok_close_parentheses")
        then_instr = instruction()
        if check("tok_else"):
            else_instr = instruction()
            return Node("nod_if_else", "if_else", [condition, then_instr, else_instr])
        return Node("nod_if", "if", [condition, then_instr])
    
    # While Loop
    elif check("tok_while"):
        # print("while statement")
        accept("tok_open_parentheses")
        condition = expression()
        accept("tok_close_parentheses")
        N = Node("nod_while", "while", [condition])
        while not check("tok_close_braces"):
            N.add_child(Node("nod_instructions", "instructions", []))
            N.children[-1].add_child(instruction())
        return N
    
    # For Loop
    elif check("tok_for"):
        accept("tok_open_parentheses")
        
        # Initialization
        init = expression()
        accept("tok_semicolon")
        
        # Condition
        condition = expression()
        accept("tok_semicolon")
        
        # Increment
        increment = expression()
        accept("tok_close_parentheses")
        accept("tok_open_braces")
        
        # Loop Body
        N = Node("nod_for", "for", [init, condition, increment])
        while not check("tok_close_braces"):
            N.add_child(Node("nod_instructions", "instructions", []))
            N.children[-1].add_child(instruction())
        return N

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
    global T, L, line_counter, character_counter, nbVar

    # Function Declaration
    accept("tok_int")
    accept("tok_ident")
    function_name = L.value
    N = Node("nod_function", function_name, [])
    
    accept("tok_open_parentheses")
    params = []
    while not check("tok_close_parentheses"):
        accept("tok_int")
        accept("tok_ident")
        param_name = L.value
        params.append(param_name)
        if not check("tok_comma"):
            accept("tok_close_parentheses")
            break
    
    # Add function to the global scope
    global_scope = var_scopes[0]
    global_scope.add_symbol(function_name, Symbol(function_name, "function", None, params))
    
    # Create a new scope for the function body
    push_scope()
    
    # Add parameters to the function's scope
    for i, param in enumerate(params):
        current_scope().add_symbol(param, Symbol(param, "parameter", i, None))
    
    # Function body
    N.add_child(instruction())
    
    # pop_scope() #? Ask teacher
    return N


def anasynth():
    global T, L, line_counter, character_counter, nbVar
    ast = []
    while T is not None and T.type != "tok_eof":
        N = function()
        if N is not None:
            ast.append(N)
        else:
            raise Exception("Error: Node from instruction/function is None")
    # print("Abstract Syntax Tree:")
    # display_ast(ast)
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

def generate_start():
    print(".start")
    print("  prep main")
    print("  call 0")
    print("halt")

def generate_function_prologue(function_name, param_count, var_count):
    print(f"resn {param_count}")
    print(f"  .{function_name}")
    print(f"  resn {var_count}")  # Reserve space for local variables

def generate_function_epilogue(var_count):
    print(f"  drop {var_count}")  # Clean up local variables
    print("  ret")

def count_variables(N):
    if N.type == "nod_declaration":
        return 1
    elif N.type in ["nod_block", "nod_if", "nod_if_else", "nod_while", "nod_for"]:
        count = 0
        for child in N.children:
            count += count_variables(child)
        return count
    elif N.type == "nod_function":
        return count_variables(N.children[0])  # Count variables in function body
    elif N.type == "nod_instructions":
        return sum(count_variables(child) for child in N.children)
    else:
        return 0

def gencode(N, count_only=False):
    global nbVar
    if count_only:
        return count_variables(N)
    
    def binary_operation(N, operation):
        gencode(N.children[0]) 
        gencode(N.children[1])
        print(f"{operation}")

    if N is None:
        raise Exception("Error: gencode received None")

    # Base Cases
    if N.type == "nod_eof":
        return
    elif N.type == "nod_constant":
        print(f"  push {N.value}")

    # Unary Operations
    elif N.type == "nod_unary_minus":
        print("  push 0")
        gencode(N.children[0])
        print("  sub")
    elif N.type == "nod_logical_not":
        gencode(N.children[0])
        print("  not")

    # Binary Operations
    elif N.type == "nod_binary_plus":
        binary_operation(N, "  add")
    elif N.type == "nod_binary_minus":
        binary_operation(N, "  sub")
    elif N.type == "nod_multiplication":
        binary_operation(N, "  mul")
    elif N.type == "nod_division":
        binary_operation(N, "  div")
    elif N.type == "nod_modulo":
        binary_operation(N, "  mod")

    # Comparison Operations
    elif N.type == "nod_greater":
        binary_operation(N, "  cmpgt")
    elif N.type == "nod_less":
        binary_operation(N, "  cmplt")
    elif N.type == "nod_greater_equal":
        binary_operation(N, "  cmpge")
    elif N.type == "nod_less_equal":
        binary_operation(N, "  cmple")
    elif N.type == "nod_double_equal":
        binary_operation(N, "  cmpeq")
    elif N.type == "nod_different":
        binary_operation(N, "  cmpne")

    # Logical Operations
    elif N.type == "nod_and":
        binary_operation(N, "  and")
    elif N.type == "nod_or":
        binary_operation(N, "  or")

    # Control Flow
    elif N.type == "nod_block":
        for child in N.children:
            gencode(child)
    elif N.type == "nod_if":
        label_else = generate_label()
        label_end = generate_label()
        gencode(N.children[0])
        print(f"  jumpf {label_else}")
        gencode(N.children[1])
        print(f"  jump {label_end}")
        print(f".{label_else}")
        print(f".{label_end}")
    elif N.type == "nod_if_else":
        label_else = generate_label()
        label_end = generate_label()
        gencode(N.children[0])
        print(f"  jumpf {label_else}")
        gencode(N.children[1])
        print(f"  jump {label_end}")
        print(f".{label_else}")
        gencode(N.children[2])
        print(f".{label_end}")
    elif N.type == "nod_while":
        label_start = generate_label()
        label_end = generate_label()
        print(f".{label_start}")
        gencode(N.children[0])  # Condition
        print(f"  jumpf {label_end}")
        for instruction in N.children[1].children:  # Loop through instructions
            gencode(instruction)
        print(f"  jump {label_start}")
        print(f".{label_end}")
    elif N.type == "nod_for":
        label_start = generate_label()
        label_end = generate_label()
        label_increment = generate_label()
        gencode(N.children[0])  # Initialization
        print(f".{label_start}")
        gencode(N.children[1])  # Condition
        print(f"  jumpf {label_end}")
        for instruction in N.children[3].children:  # Loop body
            gencode(instruction)
        print(f".{label_increment}")
        gencode(N.children[2])  # Increment
        print(f"  jump {label_start}")
        print(f".{label_end}")
    elif N.type == "nod_break":
        print("jump end_while")
    elif N.type == "nod_continue":
        print("jump start_while")

    # Special Operations
    elif N.type == "nod_send":
        gencode(N.children[0])
        print("  send")
    elif N.type == "nod_receive":
        print("  recv")
    elif N.type == "nod_debug":
        gencode(N.children[0])
        print("  dbg")
    elif N.type == "nod_drop":
        gencode(N.children[0])
        print("  drop 1")

    # Variable Handling
    elif N.type == "nod_declaration":
        nbVar += 1
    elif N.type == "nod_ident":
        symbol = find_symbol(N.value)
        if symbol is None:
            display_error(f"Symbol '{N.value}' not found in the current scope")
            sys.exit(1)
        print(f"  get {symbol.adress} ; {N.value}")
    elif N.type == "nod_assign":
        gencode(N.children[1])
        symbol = find_symbol(N.children[0].value)
        if symbol is None:
            display_error(f"Symbol '{N.children[0].value}' not found in the current scope")
            sys.exit(1)
        print(f"  dup")
        print(f"  set {symbol.adress}")
        print("  drop 1")
    elif N.type == "nod_address":
        symbol = find_symbol(N.children[0].value)
        if symbol is None:
            display_error(f"Symbol '{N.children[0].value}' not found in the current scope")
            sys.exit(1)
        print(f"push {symbol.adress}")
    elif N.type == "nod_dereference":
        gencode(N.children[0])
        print("  load")
        
    # Function Handling
    elif N.type == "nod_function":
        function_name = N.value
        param_count = len(find_symbol(function_name).value)
        var_count = count_variables(N.children[0])
        generate_function_prologue(function_name, param_count, var_count)
        gencode(N.children[0])
        generate_function_epilogue(var_count)
    elif N.type == "nod_call":
        print(f"  prep {N.value} ;{N.value}")
        for arg in N.children[1:]:
            gencode(arg)
        print(f"  call {len(N.children) - 1}")
    elif N.type == "nod_return":
        gencode(N.children[0])
        print("  ret")
        # Add a return flag to indicate that we've already generated a ret instruction
        return True
    
    elif N.type == "nod_instructions":
        for child in N.children:
            gencode(child)
            
    else:
        display_error(f"Unknown node type '{N.type}'")
        sys.exit(1)
  
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
line_character_counter = 0
T = None
L = None
label_counter = 0
nbVar = 0
# List of scopes, each scope is made of symbols (name, type, adress, value)
var_scopes = [Scope()]


generate_start()
tokens = analex(code)
next()
push_scope()
ast = anasynth() 
semantic_analysis(ast) 
ret_generated = False # flag to check if a return statement has been generated
for node in ast:
    node = Optim(node)
    ret_generated = gencode(node)
    if ret_generated:
        break
pop_scope()