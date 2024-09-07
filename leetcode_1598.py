def minOperationsSecond(logs: list[str]) -> int:
    depth = 0

    for log in logs:
        if log == '../':
            depth -= 1 if depth > 0 else 0
        elif log != './':
            depth += 1

    return depth

print(minOperationsSecond(["d1/","d2/","../","d21/","./"]))