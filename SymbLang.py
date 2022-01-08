# SymbLang

try:
    hl_file = open(input("Symblang file name... (file.sl)"), "r")
except:
    print("Error: error in open file")
    quit(0)
hl_loaded = hl_file.read()
hl_file.close()

cursor_position = 0
array = []
for i in range(30000):
    array.append(0)

functs = [[], []]
execute_code = False


def executeFunctions(lines: str):
    global cursor_position, array
    for i in range(len(lines)):
        match lines[i]:
            case ">":
                cursor_position += 1
            case "<":
                if cursor_position == 0:
                    print(
                        f"Error: cursor position < 0 (error in symbol {i + 1})")
                    break
                else:
                    cursor_position -= 1
            case "+":
                array[cursor_position] += 1
            case ".":
                try:
                    print(chr(array[cursor_position]))
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case "-":
                if array[cursor_position] < 0 or array[cursor_position] == 0:
                    print(f"Error: error in symbol {i + 1}")

                else:
                    array[cursor_position] -= 1
            case "*":
                try:
                    array[cursor_position] = int(
                        array[cursor_position] * lines[i+1])
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case "/":
                try:
                    array[cursor_position] = int(
                        array[cursor_position]) / lines[i+1]
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case ",":
                try:
                    array[cursor_position] = int(input("> "))
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case ";":
                try:
                    for u in range(30000):
                        array[u] = 0
                    cursor_position = 0
                except:
                    print(f"Error: unknown error in symbol {i + 1}")
            case "?":
                print(array[cursor_position])


for i in range(len(hl_loaded)):
    if hl_loaded[i] == "&":
        execute_code = True
    if hl_loaded[i] == "@":
        functs[0].append(int(hl_loaded[i+1]))
        line = ""
        for p in range(i+2, 1000):

            if hl_loaded[p] == ":":
                break
            else:
                line += hl_loaded[p]

        functs[1].append(line)
        line = ""

    if execute_code == True:
        match hl_loaded[i]:

            case ">":
                cursor_position += 1
            case "<":
                if cursor_position == 0:
                    print(
                        f"Error: cursor position < 0 (error in symbol {i + 1})")
                    break
                else:
                    cursor_position -= 1
            case "+":
                array[cursor_position] += 1
            case ".":
                try:
                    print(chr(array[cursor_position]))
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case "-":
                if array[cursor_position] < 0 or array[cursor_position] == 0:
                    print(f"Error: error in symbol {i + 1}")

                else:
                    array[cursor_position] -= 1
            case "*":
                try:
                    array[cursor_position] = int(
                        array[cursor_position] * hl_loaded[i+1])
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case "/":
                try:
                    array[cursor_position] = int(
                        array[cursor_position]) / hl_loaded[i+1]
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case ",":
                try:
                    array[cursor_position] = int(input("> "))
                except:
                    print(f"Error: error in symbol {i + 1}")
                    break
            case ";":
                try:
                    for u in range(30000):
                        array[u] = 0
                    cursor_position = 0
                except:
                    print(f"Error: unknown error in symbol {i + 1}")
            case "%":
                print("Line ended!")
                break
            case "$":
                try:
                    if int(hl_loaded[i+1]) in functs[0]:
                        executeFunctions(functs[1][int(hl_loaded[i+1])])

                except:
                    print(f"Error: error in symbol {i + 1}")
            case "?":
                print(array[cursor_position])
