def main():
    total_accessible_rolls = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        # construct a new map with a layer of empty spaces around the border
        map = []
        
        for line in file.readlines():
            map.append("." + line.strip() + ".")

        map.insert(0, "." * (len(line) + 2))
        map.append("." * (len(line) + 2))
        
        # loop through the original grid
        for i in range(1, len(map) - 1):
            for j in range(1, len(map[0]) - 1):
                if map[i][j] == "@":
                    # if we come across a roll of paper, check its neighbors
                    neighbors = map[i-1][j-1] + map[i-1][j] + map[i-1][j+1] + map[i][j-1] + map[i][j+1] + map[i+1][j-1] + map[i+1][j] + map[i+1][j+1]
                    if neighbors.count("@") < 4:
                        # if the roll of paper can be removed, count it
                        total_accessible_rolls += 1

    print("The number of accessible rolls of paper is: ", total_accessible_rolls)
        
if __name__ == '__main__':
    main()