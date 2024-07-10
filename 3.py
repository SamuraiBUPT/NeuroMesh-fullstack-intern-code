from typing import List

# inputs = [[1, 2, 3, 4], [1, 3, 5, 9]]
inputs = [
    [1, 3, 5, 9]
    ]
res = []

def dfs(input: List[int], start: int, path: List[int]):
    global res
    res.append(path)
    for i in range(start, len(input)): 
        # 注意：组合问题，是DFS多叉树，不能重复选择自己。
        dfs(input, i + 1, path + [input[i]])


def val_S(input: List[int]) -> float:
    # 首先用dfs找出子序列
    dfs(input, 0, [])
    # print(res)
    
    max = 0
    
    res.remove([])  # 去掉空集
    
    for i in range(len(res)):
        mean = sum(res[i]) / len(res[i])
        medium = sorted(res[i])[len(res[i]) // 2]
        output = mean - medium
        if output > max:
            max = output
    
    return max

if __name__ == '__main__':
    for seq in inputs:
        print(val_S(seq))