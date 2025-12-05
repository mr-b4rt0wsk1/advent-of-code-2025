def main():
    total_fresh_ingredients = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        database = [line.strip() for line in file]
        id_ranges = database[:database.index('')]
        ingredients = database[database.index('') + 1:]

        # check each ingredient to see if it falls within a fresh ingredient ID range
        for ingredient in ingredients:
            for id_range in id_ranges:
                if int(ingredient) >= int(id_range.split("-")[0]) and int(ingredient) <= int(id_range.split("-")[1]):
                    total_fresh_ingredients += 1
                    break

    print("The number of available ingredient IDs that are fresh is:", total_fresh_ingredients)
        
if __name__ == '__main__':
    main()