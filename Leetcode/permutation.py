def isSame(word: str, shuffle: str) -> bool:
    if len(word) != len(shuffle):
        return False

    wordList = list(word)

    for char in shuffle:
        if char not in wordList:
            return False

        wordList.remove(char)

    return True


print(isSame("mnbvcxzlkjhgfdsapoiuytrewq" * 2523, "qwertyuiopasdfghjklzxcvbnm" * 2523))
