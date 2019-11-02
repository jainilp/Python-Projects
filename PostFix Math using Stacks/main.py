from Stack import Stack

def postfix(exp):
    stack = Stack()
    numbers = '0123456789'
    listN = exp.split()
    for i in listN:
        if i != '+' and i != '-' and i != '*' and i != '/':
            if type(int(i)) == int:
                stack.push(int(i))
        if i == '+':
            one = stack.top()
            stack.pop()
            two = stack.top()
            stack.pop()
            stack.push(two + one)
        elif i == '-':
            one = stack.top()
            stack.pop()
            two = stack.top()
            stack.pop()
            stack.push(two - one)
        elif i == '*':
            one = stack.top()
            stack.pop()
            two = stack.top()
            stack.pop()
            stack.push(two * one)
        elif i == '/':
            one = stack.top()
            stack.pop()
            two = stack.top()
            stack.pop()
            stack.push(two / one)
            
    return float(stack.top())

if __name__ == "__main__":
    while True:
        userInput = input("Enter Expression:\n")
        if userInput.lower() == 'exit':
            break
        print(postfix(userInput))
