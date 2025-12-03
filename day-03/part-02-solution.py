def main():
    total_joltage = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        banks = file.readlines()

        for bank in banks:
            bank = bank.strip()
            joltage = ""

            for i in range(11, -1, -1):
                if i == 0:
                    # if there is only one battery left to pick, it will be the max of the remaining batteries in the bank
                    max_battery = max(bank)
                else:
                    # pick the max battery in the bank while ensuring there are still enough batteries left to pick a total of 12 batteries
                    max_battery = max(bank[:-i])
                joltage += max_battery
                # after picking a battery, the remaining bank of batteries to choose from becomes all batteries after the most recently picked battery
                bank = bank[bank.index(max_battery)+1:]

            total_joltage += int(joltage)

    print("The total output joltage is: ", total_joltage)
        
if __name__ == '__main__':
    main()