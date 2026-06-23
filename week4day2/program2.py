# ============================================================
#  BALANCED PARENTHESES CHECKER
# ============================================================
class Stack:
    def __init__(self):
        self._items = []

    def push(self, v): self._items.append(v)
    def pop(self): return self._items.pop() if self._items else None
    def is_empty(self): return len(self._items) == 0
    def size(self): return len(self._items)
    def __repr__(self): return repr(self._items)
    
def is_balanced(expr):
    """
    Returns True if all brackets in expr are balanced.
    Handles: () [] {} and ignores other characters.
    """
    stack = Stack()   # Reuse our Stack class
    opening = set('({[')
    match   = {')':'(', '}':'{', ']':'['}
 
    for ch in expr:
        if ch in opening:
            stack.push(ch)           # Push every opening bracket
        elif ch in match:             # It's a closing bracket
            if stack.is_empty():
                return False          # Nothing to match against
            top = stack.pop()
            if top != match[ch]:
                return False          # Wrong pair e.g. ( closed by ]
 
    return stack.is_empty()           # Extra opens → not balanced
 
 
# ---- Comprehensive Test Cases ----
test_cases = [
    ("({[]})",    True,  "Correctly nested"),
    ("()[]{}", True,  "Sequential — all correct"),
    ("([)]",     False, "Wrong close order"),
    ("((((",     False, "Only opens, no close"),
    ("}}}}",     False, "Only closes, no open"),
    ("{[()]}",   True,  "Triple nested"),
    ("",         True,  "Empty string"),
    ("a+(b*c)",  True,  "Embedded in expression"),
    ("{[(])}",   False, "Interleaved wrong order"),
]
 
print(f'{"Expression":<16} {"Expected":<10} {"Got":<10} {"Status":<6}')
print('-' * 55)
for expr, expected, desc in test_cases:
    result = is_balanced(expr)
    status = 'PASS' if result == expected else 'FAIL'
    print(f'{expr!r:<16} {str(expected):<10} {str(result):<10} [{status}] {desc}')
