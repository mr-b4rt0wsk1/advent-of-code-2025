def main():
    dial_position = 50
    zero_position_count = 0
    
    with open('./puzzle-input.txt', 'r') as document:
        instructions = document.readlines()

    for instruction in instructions:
        if instruction.startswith("L"):
            # move dial to the left
            dial_position = (dial_position - int(instruction[1:])) % 100
        else:
            # move dial to the right
            dial_position = (dial_position + int(instruction[1:])) % 100

        # count number of times the dial points at 0
        if dial_position == 0: 
            zero_position_count += 1

    print("Total number of times the dial points at 0: ", zero_position_count)

if __name__ == '__main__':
    main()