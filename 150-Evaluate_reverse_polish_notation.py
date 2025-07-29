class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        def evaluate(op, num1, num2):
            match op:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '*':
                    return num1 * num2
                case '/':
                    return math.trunc(num1 / num2)
                case _:
                    return null

        for elem in tokens:
            if(elem in '+-*/'):
                num1 = stack.pop()
                num2 = stack.pop()
                val = evaluate(elem, num2, num1)
                stack.append(val)
            else:
                stack.append(int(elem))
        return stack.pop()
