# 子序列问题，一般使用滑动窗口
# 思路：滑动right指针，查找一个最大的可以匹配到的字符串，记录，然后left指针更新到right指针所在的位置，继续滑动right指针。

# "查找一个最大的可以匹配到的字符串"的定义是：这个字符串可以被source拼凑出来，比如xz就可以被xyz拼出来，而xzy不行，因为不符合顺序


source = "abc"
target = "abcbc"

source = "xyz"
target = "xzyxz"

def find_max_match_string(source: str, target: str) -> int:
    substrings = []  # 记录所有可以匹配到的子串
    left = 0

    while left < len(target):
        current_str = ""
        right = left

        while right < len(target) and check(current_str + target[right], source):
            current_str += target[right]
            right += 1

        if current_str == "":
            return -1

        substrings.append(current_str)
        left = right

    # print(substrings)
    return len(substrings)

def check(cur: str, source: str) -> bool:
    index = -1
    for char in cur:
        index = source.find(char, index + 1)    # 每次都更新开始查找的位置，因为要保持Sequence顺序
        if index == -1:
            return False
    return True


if __name__ == '__main__':
    print(find_max_match_string(source, target))