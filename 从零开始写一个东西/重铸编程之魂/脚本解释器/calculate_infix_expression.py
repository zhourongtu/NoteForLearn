# -*- coding: utf-8 -*-


def calculate(expression):
    operators = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b,
                 '/': lambda a, b: a / b}

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_operation():
        operator = stack_operators.pop()
        operand2 = stack_operands.pop()
        operand1 = stack_operands.pop()
        result = operators[operator](operand1, operand2)
        stack_operands.append(result)

    def has_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    stack_operands = []
    stack_operators = []

    expression = expression.replace(" ", "")

    i = 0
    while i < len(expression):
        token = expression[i]

        if token.isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            number = int(expression[i:j])
            stack_operands.append(number)
            i = j - 1

        elif token in operators:
            while stack_operators and stack_operators[-1] != '(' and has_precedence(stack_operators[-1], token):
                apply_operation()
            stack_operators.append(token)

        elif token == '(':
            stack_operators.append(token)

        elif token == ')':
            while stack_operators and stack_operators[-1] != '(':
                apply_operation()
            if stack_operators and stack_operators[-1] == '(':
                stack_operators.pop()

        else:
            raise ValueError("Invalid token: " + token)

        i += 1

    while stack_operators:
        apply_operation()

    return stack_operands[0] if stack_operands else None


# 测试
expression = "(3 + 4) * (2 - 5) / 2"
result = calculate(expression)
print(result)  # 输出: -6.0
