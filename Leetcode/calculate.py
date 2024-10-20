class Solution:
    def calculate(self, expression: str) -> list[int]:
        operators = ["+", "-", "*", "/"]
        operator = []
        number = []

        tokens = expression.replace(" ", "")

        for token in tokens:
            if token in operators:
                operator.append(token)

            else:
                number.append(int(token))

        operatorIndex = 0
        numberIndex = 1

        lastNumber = number[0]

        while numberIndex < len(number) - 1:
            print(lastNumber)
            operatorSign = operator[operatorIndex]
            num = number[numberIndex]

            if operatorSign == "+":
                result = lastNumber + num

            elif operatorSign == "-":
                result = lastNumber - num

            elif operatorSign == "*":
                result = lastNumber * num

            else:
                result = lastNumber / num

            print(number.pop(1))

            number[0] = result

            numberIndex += 2
            operatorIndex += 1

            lastNumber = num

        return number


print(Solution().calculate("4-8+8-2"))


def calculate(expression):
    try:
        operators = {"+": 1, "-": 1, "*": 2, "/": 2}
        output = []
        operator_stack = []

        def apply_operator():
            operator = operator_stack.pop()
            num2 = output.pop()
            num1 = output.pop()
            if operator == "+":
                output.append(num1 + num2)
            elif operator == "-":
                output.append(num1 - num2)
            elif operator == "*":
                output.append(num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                output.append(num1 / num2)

        for token in expression.split():
            if token.isnumeric():
                output.append(float(token))
            elif token in operators:
                while operator_stack and operators.get(token, 0) <= operators.get(
                    operator_stack[-1], 0
                ):
                    apply_operator()
                operator_stack.append(token)
            else:
                raise ValueError("Invalid token: " + token)

        while operator_stack:
            apply_operator()

        if len(output) == 1:
            return output[0]
        else:
            raise ValueError("Invalid expression")

    except (ValueError, IndexError, ZeroDivisionError):
        return "Invalid input"


# Input expression
expression = "10 * 4 / 2"

# Calculate the result
result = calculate(expression)
# print("Result:", result)
