def reversed(data):
    left = 0
    right = -1

    for _ in range(len(data) // 2):
        if data[left] != data[right]:
            return False

        left += 1
        right -= 1

    return True
