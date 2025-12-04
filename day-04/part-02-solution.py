def main():
    total_accessible_rolls = 0
    search = True
    
    with open('./puzzle-input.txt', 'r') as file:
        # construct a new map with a layer of empty spaces around the border
        map = []
        
        for line in file.readlines():
            map.append("." + line.strip() + ".")

        map.insert(0, "." * (len(line) + 2))
        map.append("." * (len(line) + 2))
        
        while search == True:
            # loop through the original grid
            total_accessible_rolls_before_search = total_accessible_rolls
            for i in range(1, len(map) - 1):
                for j in range(1, len(map[0]) - 1):
                    if map[i][j] == "@":
                        # if we come across a roll of paper, check its neighbors
                        neighbors = map[i-1][j-1] + map[i-1][j] + map[i-1][j+1] + map[i][j-1] + map[i][j+1] + map[i+1][j-1] + map[i+1][j] + map[i+1][j+1]
                        if neighbors.count("@") < 4:
                            # if the roll of paper can be removed, count it and replace it with empty space
                            total_accessible_rolls += 1
                            map[i] = map[i][:j] + "." + map[i][j+1:]

            if total_accessible_rolls == total_accessible_rolls_before_search:
                # continue searching until the number of accessible rolls has not changed between searches
                search = False

    print("The number of accessible rolls of paper is: ", total_accessible_rolls)
        
if __name__ == '__main__':
    main()