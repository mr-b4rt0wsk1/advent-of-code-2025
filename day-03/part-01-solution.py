def main():
    total_joltage = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        banks = file.readlines()

        for bank in banks:
            bank = bank.strip()
            # the first battery is the max of the entire bank, excluding the end battery
            first_battery = max(bank[:-1])
            # the second battery is the max of the remaining batteries in the bank that come after the first battery
            second_battery = max(bank[bank.index(first_battery)+1:])
            total_joltage += int(first_battery + second_battery)

    print("The total output joltage is: ", total_joltage)
        
if __name__ == '__main__':
    main()