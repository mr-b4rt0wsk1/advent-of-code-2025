import pulp

def find_fewest_presses(end_joltage, buttons):
    """find the fewest button presses needed to reach the desired joltage end state"""

    # initialize a Linear Programming problem with the objective to MINIMIZE
    problem = pulp.LpProblem("FewestPresses", pulp.LpMinimize)
    
    # create a variable for each button and add them (and their sum to minimize) to the problem
    variables = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(len(buttons))]
    problem += pulp.lpSum(variables)

    # add the linear equation for each joltage value to the problem
    for j in range(len(end_joltage)):
        problem += pulp.lpSum(variables[i] for i in range(len(buttons)) if j in buttons[i]) == end_joltage[j]
    
    # solve the problem without displaying PuLP stdout
    problem.solve(pulp.PULP_CBC_CMD(msg=0))
    return int(pulp.value(problem.objective))
    
def main():
    fewest_total = 0

    with open('./puzzle-input.txt', 'r') as file:
        machines = [line.strip().split() for line in file]

    # find the fewest number of button presses needed for each machine
    for machine in machines:
        end_joltage = [int(x) for x in machine[-1][1:-1].split(",")]
        buttons = [[int(x) for x in b[1:-1].split(",")] for b in machine[1:-1]]
        fewest_total += find_fewest_presses(end_joltage, buttons)

    print("The fewest number of button presses required to configure the joltage levels is:", fewest_total)
        
if __name__ == '__main__':
    main()