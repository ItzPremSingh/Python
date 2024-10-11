from random import randint
from subprocess import run
from time import sleep

# Changeable Variable: Yes
Hint = True
Sleep = True
Speak = True
sleepTime = 0.6
start = randint(1, 100)
end = randint(900, 1000)
# (life) Only Can Be False Or Natural Number =! 0
# False: You Get Unlimted Life
# Number: You Get (Number) Life
life = False


# Changeable Variable: No
guessTime = 1
guessed = False
forcelyQuit = False
OutOfRange = False
hint = [start, end]

# Swaping Number
if start > end:
    temp = end
    end = start
    start = temp

# Random Variable
randomNumber = randint(start, end)

# Printing Intro
print(f"🤖: I Am Guessing A Number Between {start} ~ {end}")
if life:
    print(f"🤖: Tell Me The Number You Have {life}⚡")
else:
    print("🤖: Tell Me The Number")

# Speak If True
if Speak:
    print("🤖: Speaking So Lets Begin\n\n\n")
    run("espeak 'so lets'", shell=True)
    sleep(0.1)
    run("espeak 'begin'", shell=True)

else:
    print("🤖: So Lets Begin\n\n\n")

# Sleep If True
if Sleep:
    sleep(float(sleepTime))


# Game Loop
while True:
    if life and guessTime - 1 == life:
        break

    if life:
        print(f"🤖: {(life - guessTime) + 1}⚡ Left ", end="")
    else:
        print("🤖: ∞ ⚡ ", end="")

    if Hint:
        print(f"[HINT({hint[0]} ~ {hint[1]})]")
    else:
        print()

    inputStr = "🧒: Number? "
    wrongInputStr = "🧒: Number [INTEGER]? "

    number = ""

    while True:
        try:
            number = input(inputStr)

        except (EOFError, KeyboardInterrupt):
            Sleep = False
            forcelyQuit = True
            break

        if number.isdigit():
            break

        else:
            inputStr = wrongInputStr

    if forcelyQuit:
        break

    number = int(number)

    if number < hint[0] or number > hint[1]:
        OutOfRange = True

    if number == randomNumber:
        print(f"\n\n🤖: Congratulations You Have Guessed The In {guessTime}")
        guessed = True
        break

    elif number < randomNumber:
        if not OutOfRange:
            print("🤖: Your Guess Is Smaller")
            hint[0] = number

        else:
            print("🤖: Your Guess Is Too Smaller")

    else:
        if not OutOfRange:
            print("🤖: Your Guess Is Greater")
            hint[1] = number

        else:
            print("🤖: Your Guess Is Too Greater")

    guessTime += 1
    OutOfRange = False
    print()


# When Player Lose Or Quit
if not guessed:
    if forcelyQuit:
        print("\n\n🤖: You Quit The Game 😞")
    else:
        print("\n\n🤖: You Lose The Game 😞")

    print("🤖: The Number Was ", end="", flush=True)
    if Sleep:
        sleep(sleepTime)
    print(randomNumber)
