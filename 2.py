char_set = []

inputs = ["bge)))))))))", "((IIII))))))", "()()()()(uuu", "))))UUUU((()"]

def check(input_str: str):
    char_set.clear()
    for i in range(len(input_str)):
        char_set.append(input_str[i])  # 先入队
        if input_str[i] == ")":
            # 查找char_set里面有无左括号，如果有，标记为1，如果没有，入队，什么也不做
            if '(' in char_set:
                char_set[char_set.index('(')] = 'a'
                char_set[-1] = 'b'
            
    # 现在开始检查整个char_set, 有"("打印x，有")"打印?
    # print(char_set)
    
    for i in range(len(char_set)):
        if char_set[i] == '(':
            print('x', end='')
        elif char_set[i] == ')':
            print("?", end='')
        else:
            print(" ", end='')
    print()

if __name__ == "__main__":
    for input_str in inputs:
        check(input_str)