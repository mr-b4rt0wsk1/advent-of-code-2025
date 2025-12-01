def main():
    dial_position = 50
    zero_position_count = 0
    
    with open('./puzzle-input.txt', 'r') as document:
        instructions = document.readlines()

    for instruction in instructions:
        clicks = int(instruction[1:])

        if instruction.startswith("L"):
            # move dial to the left
            new_position = (dial_position - clicks) % 100

            if dial_position == 0:
                # any rotation starting from 0
                zero_position_count += clicks // 100
            elif clicks > dial_position:
                # starting from a nonzero position and going past 0 at least once
                zero_position_count += ((clicks - dial_position - 1) // 100) + 1
                if new_position == 0:
                    # need to count if we also end on 0
                    zero_position_count += 1
            elif clicks == dial_position:
                # starting from a nonzero position and ending on 0 without ever passing it
                zero_position_count += 1

            dial_position = new_position
        else:
            # move dial to the right
            zero_position_count += ((dial_position + clicks) // 100)
            dial_position = (dial_position + clicks) % 100

    print("Total number of times the dial points at 0: ", zero_position_count)

if __name__ == '__main__':
    main()