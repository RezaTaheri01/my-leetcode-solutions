# import re

# re_pattern = "[^{|}|\[|\]|\(|\)]"

# def check_RE(re_pattern, txt):
#     x = re.search(re_pattern, txt)

txt = '(({({()})}))'
stack = []
close_li = ')]}'
chr_map = {']': '[', ')': '(', '}': '{'}


def main():
    for char in txt:
        if char in close_li:
            # check last one in stack
            if not stack: # == len(stack) == 0
                return False
            elif chr_map[char] != stack.pop():
                return False
        else:
            stack.append(char)

    if not stack:
        return True
    return False


# if check_RE(re_pattern, txt) is None:
#     main()

print(main())
