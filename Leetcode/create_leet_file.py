from sys import argv


FileName = argv[1]
FuncName = "fname"


if not FileName.endswith(".py"):
    FileName = FileName + ".py"

if FuncName := argv[2::]:
    FuncName = FuncName[0]


with open(FileName, "w") as file:
    write = file.write
    write("class Solution:\n")
    write(f"    def {FuncName}(self,)->None:\n")
    write("        return None\n\n")
    write(f"print(Solution().{FuncName}())")
