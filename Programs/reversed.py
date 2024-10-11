def reversed(data):
    """
    Checks if given data is reversed or not.

    Args:
        data (list): list of data to be checked

    Returns:
        bool: True if reversed, False if not
    """
    left = 0
    right = -1

    for _ in range(len(data) // 2):
        if data[left] != data[right]:
            return False

        left += 1
        right -= 1

    return True
