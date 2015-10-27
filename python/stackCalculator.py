#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("stackCalculator.py", "8/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from ADT.stack import Stack

compute_stack = Stack()

# print(re.split("([^0-9])", "123+456*/"))


def eval_postfix(stack, expr):
    from re import split
    token_list = split("([^0-9])", expr)

    for token in token_list:
        # Commutative operands
        if token in ["", " "]:
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*" or token.lower() == 'x':
            product = stack.pop() * stack.pop()
            stack.push(product)
        # Non-commutative operands
        elif token == "-":
            oper1 = stack.pop()
            oper2 = stack.pop()
            diff = oper2 - oper1
            stack.push(diff)
        elif token == "/":
            oper1 = stack.pop()
            oper2 = stack.pop()
            div = oper2 / float(oper1)
            stack.push(div)
        elif token == '^':
            oper1 = stack.pop()
            oper2 = stack.pop()
            expon = oper2**oper1
            stack.push(expon)
        else:
            stack.push(float(token))

    result = stack.pop()

    if not stack.is_empty():
        raise ValueError("Too many input values")

    return result

print(eval_postfix(compute_stack, input("Enter postfix expression\n>>>")))