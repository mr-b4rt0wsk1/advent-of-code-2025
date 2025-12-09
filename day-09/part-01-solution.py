def calc_area(t1, t2):
    """compute the area of the rectangle using the opposite corner tiles"""
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

def generate_pairs(tiles):
    """generate all possible pairs of tiles along with their rectangle area"""
    pairs = []
    for i in range(0, len(tiles)):
        for j in range(i + 1, len(tiles)):
            pairs.append([calc_area(tiles[i], tiles[j]), tiles[i], tiles[j]])
    return pairs

def main():
    # read in the file input and create the list of tile coordinates
    with open('./puzzle-input.txt', 'r') as file:
        tiles = [tuple(map(int, line.strip().split(","))) for line in file]

    largest = sorted(generate_pairs(tiles), key=lambda x: x[0], reverse=True)[0][0]
    print("The area of the largest rectangle is:", largest)
        
if __name__ == '__main__':
    main()