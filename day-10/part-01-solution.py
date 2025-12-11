from itertools import permutations

def find_fewest_presses(end_lights, buttons):
    """find the fewest button presses needed to reach the desired indicator light end state"""
    presses = 1
    find = True

    while find:
        # iterate through all permutations of N button presses
        for permutation in permutations(buttons, presses):
            current = "." * len(end_lights)
            # perform the action of each button in the permutation
            for button in permutation:
                for i in button:
                    if current[i] == ".":
                        current = current[:i] + "#" + current[i + 1:]
                    else:
                        current = current[:i] + "." + current[i + 1:]
            # if the desired end state has been reached after all buttons in a permutation have been pressed
            if current == end_lights:
                return presses
        # otherwise increment the number of presses and keep searching
        presses += 1

def main():
    fewest_total = 0

    with open('./puzzle-input.txt', 'r') as file:
        machines = [line.strip().split() for line in file]

    # find the fewest number of button presses needed for each machine
    for machine in machines:
        end_lights = machine[0][1:-1]
        buttons = [[int(x) for x in b[1:-1].split(",")] for b in machine[1:-1]]
        fewest_total += find_fewest_presses(end_lights, buttons)

    print("The fewest number of button presses required to turn on all machines is:", fewest_total)
        
if __name__ == '__main__':
    main()