import re

def main():
    invalid_id_sum = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        ranges = file.readlines()[0].strip().split(",")

        for r in ranges:
            start = r.split("-")[0]
            end = r.split("-")[1]
            range_r = range(int(start), int(end) + 1)

            for i in range_r:
                # use regex to check if an ID is fully made up of a repetitive sequence
                if bool(re.fullmatch(r'(.+)\1+', str(i))):
                    invalid_id_sum += i

    print("The sum of all the invalid IDs in the ranges is: ", invalid_id_sum)
        

if __name__ == '__main__':
    main()