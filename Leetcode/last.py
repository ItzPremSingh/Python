def lengthOfLast(string: str) -> int:
    string = string.strip()
    return len(string.split(" ")[-1])
