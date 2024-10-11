def onlyNumber():
    while True:
        try:
            _input = float(input("Enter choice: "))
            return _input

        except ValueError:
            pass