#!/usr/bin/env python3
import re
import sys
from statistics import median_low

def tokenize(expr):
    # Split into parentheses, operators, and integer literals
    return re.findall(r'\(|\)|[A-Z]+|-?\d+', expr)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def next(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse(self):
        tok = self.next()
        if tok == '(':
            op = self.next()
            args = []
            while self.peek() != ')':
                args.append(self.parse())
            self.next()  # consume ')'
            return self.apply_op(op, args)
        else:
            # integer literal
            return int(tok)

    def apply_op(self, op, args):
        if op == 'SUM':
            return sum(args)
        elif op == 'MIN':
            return min(args)
        elif op == 'MAX':
            return max(args)
        elif op == 'AVG':
            return sum(args) // len(args)
        elif op == 'MED':
            # lower median for even-length lists
            return int(median_low(args))
        elif op == 'SM':
            return sum(args) % 10
        else:
            raise ValueError(f'Unknown operator: {op}')

def evaluate(expr):
    tokens = tokenize(expr)
    parser = Parser(tokens)
    return parser.parse()

def main():
    # Read expression from the user
    expr = input("Enter ListOps expression: ").strip()
    try:
        result = evaluate(expr)
        print("Result:", result)
    except Exception as e:
        print("Error evaluating expression:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import re
import sys
from statistics import median_low

def tokenize(expr):
    # Split into parentheses, operators, and integer literals
    return re.findall(r'\(|\)|[A-Z]+|-?\d+', expr)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def next(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse(self):
        tok = self.next()
        if tok == '(':
            op = self.next()
            args = []
            while self.peek() != ')':
                args.append(self.parse())
            self.next()  # consume ')'
            return self.apply_op(op, args)
        else:
            # integer literal
            return int(tok)

    def apply_op(self, op, args):
        if op == 'SUM':
            return sum(args)
        elif op == 'MIN':
            return min(args)
        elif op == 'MAX':
            return max(args)
        elif op == 'AVG':
            return sum(args) // len(args)
        elif op == 'MED':
            # lower median for even-length lists
            return int(median_low(args))
        elif op == 'SM':
            return sum(args) % 10
        else:
            raise ValueError(f'Unknown operator: {op}')

def evaluate(expr):
    tokens = tokenize(expr)
    parser = Parser(tokens)
    return parser.parse()

def main():
    # Read expression from the user
    expr = input("Enter ListOps expression: ").strip()
    try:
        result = evaluate(expr)
        print("Result:", result)
    except Exception as e:
        print("Error evaluating expression:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()