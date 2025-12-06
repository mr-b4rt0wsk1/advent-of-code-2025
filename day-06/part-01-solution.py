import math

def main():
    grand_total = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        homework = [line.strip().split() for line in file]
        # transpose the homework matrix for easier computation
        homework_t = list(map(list, zip(*homework)))

        # compute the answer for each math problem and add to the grand total
        for problem in homework_t:
            numbers = [int(x) for x in problem[:-1]]
            if problem[-1] == '*':
                grand_total += math.prod(numbers)
            elif problem[-1] == '+':
                grand_total += sum(numbers)

    print("The grand total of all of the math problems is:", grand_total)
        
if __name__ == '__main__':
    main()