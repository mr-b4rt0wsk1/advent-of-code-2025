def calc_area(t1, t2):
    """compute the area of the rectangle using the opposite corner tiles"""
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

def get_largest_area_in_perimeter(tiles, perimeter):
    """get the area of the largest rectangle that falls within the tile polygon's perimeter"""
    largest = 0
    for i in range(0, len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = calc_area(tiles[i], tiles[j])
            # if the rectangle's area doesn't beat the current largest, skip it entirely
            if area <= largest:
                continue
            min_x, max_x = min(tiles[i][0], tiles[j][0]), max(tiles[i][0], tiles[j][0])
            min_y, max_y = min(tiles[i][1], tiles[j][1]), max(tiles[i][1], tiles[j][1])
            # check if any part of the tile polygon's perimeter is fully within the rectangle (not including on any edge)
            invalid = False
            for x, y in perimeter:
                if min_x < x < max_x and min_y < y < max_y:
                    invalid = True
                    break
            # if the rectangle is fully within the perimeter, it is now the current largest
            if not invalid:
                largest = area
    return largest

def generate_perimeter(tiles):
    """generate all coordinates of the perimeter of the tile polygon"""
    perimeter = set()
    for i in range(len(tiles)):
        (x1, y1) = tiles[i]
        (x2, y2) = tiles[(i + 1) % len(tiles)]
        if x1 == x2:
            # generate all coordinates in the horizontal line between the two tiles
            for y in range(min(y1, y2), max(y1, y2) + 1):
                perimeter.add((x1, y))
        else:
            # generate all coordinates in the vertical line between the two tiles
            for x in range(min(x1, x2), max(x1, x2) + 1):
                perimeter.add((x, y1))
    return perimeter

def main():
    # read in the file input and create the list of tile coordinates
    with open('./puzzle-input.txt', 'r') as file:
        tiles = [tuple(map(int, line.strip().split(","))) for line in file]

    largest = get_largest_area_in_perimeter(tiles, generate_perimeter(tiles))
    print("The area of the largest rectangle using only red and green tiles is:", largest)
        
if __name__ == '__main__':
    main()