def main():
    shape_areas = []
    regions = []

    # read in the file and parse the input into the shapes and regions
    with open('./puzzle-input.txt', 'r') as file:
        for line in file:
            l = line.strip()
            if l == '':
                shape_areas.append(shape_area)
                continue
            last = l[-1]
            if last == ":":
                shape_area = 0
            elif last == "#" or last == ".":
                shape_area += l.count("#")
            else:
                regions.append([list(map(int, l.split(": ")[0].split("x"))), list(map(int, l.split(": ")[1].split(" ")))])

    # check if the presents could theoretically fit in the region based on area comparison
    # note:
    #   this problem is somewhat of a troll and this approach doesn't actually work for the test input
    #   there is also no actual problem to solve in part 2
    n = 0
    for r in regions:
        region_area = r[0][0] * r[0][1]
        present_area = 0
        for i in range(len(r[1])):
            present_area += (r[1][i] * shape_areas[i])
        if present_area <= region_area:
            n += 1

    print("The number of regions that can fit all of the presents listed is:", n)
        
if __name__ == '__main__':
    main()