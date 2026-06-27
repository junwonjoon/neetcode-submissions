class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for elem in tokens:
            if elem == "+":
                temp = int(num_stack.pop()) + int(num_stack.pop())
                num_stack.append(temp)
            elif elem == "-":
                order_last = num_stack.pop()
                order_first = num_stack.pop()
                temp = int(order_first) - int(order_last)
                num_stack.append(temp)
            elif elem == "*":
                temp = int(num_stack.pop()) * int(num_stack.pop())
                num_stack.append(temp)
            elif elem == "/":
                order_last = num_stack.pop()
                order_first = num_stack.pop()
                temp = int(order_first) / int(order_last)
                num_stack.append(int(temp))
            else:
                num_stack.append(elem)
        return int(num_stack[0])
        