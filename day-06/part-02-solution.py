def main():
    grand_total = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        # this time we transpose each character instead of each number, still for easier processing
        homework = [list(line.strip("\n")) for line in file]
        operands = [x for x in homework[-1] if x != ' ']
        homework_t = list(map(list, zip(*homework[:-1])))

        total = 0
        for row in homework_t:
            operand = operands[0]
            item = ''.join(row).strip()
            if item != "":
                # if the item is a number, we need to either add it to or multiply by the running total
                if operand == "*":
                    if total == 0:
                        total = int(item)
                    else:
                        total *= int(item)
                elif operand == "+":
                    total += int(item)
            else:
                # if the item is empty, our current math problem is done and we need to add it to the grand total
                operands.pop(0)
                grand_total += total
                total = 0
        grand_total += total
            
    print("The grand total of all of the math problems is:", grand_total)
        
if __name__ == '__main__':
    main()