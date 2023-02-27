import random

mineField = []
mineCount = 0
uncoveredFields = []
uncoveredFieldsCount = -1
field = []
fieldCount = 0

def createField(x,y,mines):
    global uncoveredFields
    global field
    uncoveredFields = []
    field = []

    fieldData = []
    for i in range(y):
        row = []
        visRow = []
        uncRow = []
        for e in range(x):
            row.append(0)
            visRow.append("?")
            uncRow.append(0)
        fieldData.append(row)
        field.append(visRow)
        uncoveredFields.append(uncRow)
    for b in range(mines):
        while True:
            xCoord = random.randint(0, x-1)
            yCoord = random.randint(0, y-1)
            if (fieldData[yCoord][xCoord] == 0):
                fieldData[yCoord][xCoord] = 1
                break
    return fieldData

def printField(data):
    print("-"*(len(data[0])*4+1))
    for i in data:
        print("".join(["| "," | ".join(i)," |"]))
        print("-"*(len(data[0])*4+1))

def flag(x,y):
    if (uncoveredFields[y][x] == 0):
        if (field[y][x] == "F"):
            field[y][x] = "?"
        else:
            field[y][x] = "F"
    else:
        print("Cannot flag uncovered cell.")

def check(x,y):
    if (uncoveredFields[y][x] == 0):
        if (field[y][x] == "F"):
            while True:
                res = input("Uncover flagged field (Y/N)? ").lower()
                print(res)
                if (res == "y"):
                    uncoverCell(x,y)
                    break
                elif (res == "n"):
                    break
                else:
                    print("Unexpected input")
        else:
            uncoverCell(x,y)
    else:
        print("Cell already uncovered")

def uncoverCell(x,y):
    global uncoveredFieldsCount
    uncoveredFields[y][x] == 1
    uncoveredFieldsCount += 1
    if (mineField[y][x]):
        print(f"Cell {x},{y} is a mine.")
        field[y][x] == "X"
        printField(field)
        exit()
    else:
        mineCount = getMines(x,y)
        print(f"Cell {x+1},{y+1} has {mineCount} surrounding mines.")

def getMines(x,y):
    global uncoveredFieldsCount
    print("Called for ", x, ",", y)
    mineCount = 0
    for xTest in [-1, 0, 1]:
        if (x+xTest>=0 and x+xTest<len(field[0])):
            for yTest in [-1, 0, 1]:
                if (y+yTest>=0 and y+yTest<len(field)):
                    if (uncoveredFields[y+yTest][x+xTest] == 0):
                        mineCount += mineField[y+yTest][x+xTest]
                        print(f"{x+xTest+1},{y+yTest+1}: {mineField[y+yTest][x+xTest]}")
    field[y][x] = str(mineCount)
    if(mineCount == 0):
        for xTest in [-1, 0, 1]:
            if (x+xTest>=0 and x+xTest<len(field[0])):
                for yTest in [-1, 0, 1]:
                    if (y+yTest>=0 and y+yTest<len(field)):
                        if (uncoveredFields[y+yTest][x+xTest] == 0):
                            uncoveredFields[y+yTest][x+xTest] = 1
                            uncoveredFieldsCount += 1
                            getMines(x+xTest,y+yTest)
    return mineCount

def inField(x,y):
    if (x>=0 and x<=len(field[0]) and y>=0 and y<=len(field)):
        return True
    else:
        print("Cell not in field.")
        return False

def argCount(count, argList):
    if(count<=len(argList)):
        return True
    else:
        print("Not enough arguments.")
        return False

def checkField():
    if(field!=[]):
        return True
    else:
        print("Field not created yet.")
        return False

def validateField(commandArgs):
    if(int(commandArgs[0])>0 and int(commandArgs[1])>0 and int(commandArgs[2])<(int(commandArgs[0])*int(commandArgs[1])) and int(commandArgs[2])>0):
        return True
    else:
        print("Invalid input.")
        return False

def checkComplete():
    if(uncoveredFieldsCount == fieldCount-mineCount):
        print("You win")
        exit(0)
    else:
        return False

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("    ______                                                __   __     _                 __  ___ _                                                            ")
print("   / ____/____   ____ ___   ____ ___   ____ _ ____   ____/ /  / /    (_)____   ___     /  |/  /(_)____   ___   _____ _      __ ___   ___   ____   ___   _____")
print("  / /    / __ \ / __ `__ \ / __ `__ \ / __ `// __ \ / __  /  / /    / // __ \ / _ \   / /|_/ // // __ \ / _ \ / ___/| | /| / // _ \ / _ \ / __ \ / _ \ / ___/")
print(" / /___ / /_/ // / / / / // / / / / // /_/ // / / // /_/ /  / /___ / // / / //  __/  / /  / // // / / //  __/(__  ) | |/ |/ //  __//  __// /_/ //  __// /    ")
print(" \____/ \____//_/ /_/ /_//_/ /_/ /_/ \__,_//_/ /_/ \__,_/  /_____//_//_/ /_/ \___/  /_/  /_//_//_/ /_/ \___//____/  |__/|__/ \___/ \___// .___/ \___//_/     ")
print("                                                                                                                                       /_/                   ")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Type \"help\" for help.")


while (True): 
    fullCommand = input("> ")
    command = fullCommand.split(" ")[0]
    commandArgs = fullCommand.split(" ")
    commandArgs.pop(0)

    match command:
        case "help" | "h":
            print("(h)elp: 				Displays this help page")
            print("(s)tart <width> <height> <mines>:    Create a field with the specified width, heigth and mine count")
            print("field: 					Displays the current field")
            print("(f)lag <x> <y>: 			Places a flag on the specified cell")
            print("(c)heck <x> <y>: 			Uncovers a cell")
        case "start" | "s":
            if (argCount(3, commandArgs)):
                if (validateField(commandArgs)):
                    mineField = []
                    mineField = createField(int(commandArgs[0]), int(commandArgs[1]), int(commandArgs[2]))
                    fieldCount = int(commandArgs[0])*int(commandArgs[1])
                    mineCount = int(commandArgs[2])
                    printField(field)
        case "field":
            if checkField():
                printField(field)
        case "flag" | "f":
            if checkField():
                if(argCount(2, commandArgs) and inField(int(commandArgs[0])-1, int(commandArgs[1])-1)):
                    flag(int(commandArgs[0])-1, int(commandArgs[1])-1)
                    printField(field)
                    checkComplete()
        case "check" | "c":
            if checkField():
                if(argCount(2, commandArgs) and inField(int(commandArgs[0])-1, int(commandArgs[1])-1)):
                    check(int(commandArgs[0])-1, int(commandArgs[1])-1)
                    printField(field)
                    checkComplete()