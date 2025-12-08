import math

def euclidean_distance(b1, b2):
    """compute the euclidean distance between two junction boxes"""
    return math.sqrt((b2[0] - b1[0]) ** 2 + (b2[1] - b1[1]) ** 2 + (b2[2] - b1[2]) ** 2)

def generate_pairs(boxes):
    """generate all possible pairs of junction boxes along with their euclidean distance"""
    pairs = []
    for i in range(0, len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs.append([euclidean_distance(boxes[j], boxes[i]), boxes[j], boxes[i]])
    return pairs

def main():

    # read in the file input and create the list of junction boxes
    with open('./puzzle-input.txt', 'r') as file:
        boxes = [tuple(map(int, line.strip().split(","))) for line in file]

    # find all junction box pairs and their distances, sorted from smallest to largest
    pairs = generate_pairs(boxes)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    # intialize the circuits as each junction box in its own circuit
    circuits = [{boxes[i]} for i in range(len(boxes))]
    
    # iterate through all pairs (sorted) 
    for _, b1, b2 in sorted_pairs:
        index_b1 = None
        index_b2 = None

        # find the circuit index of each junction box in the pair
        for index, c in enumerate(circuits):
            if b1 in c:
                index_b1 = index
            if b2 in c:
                index_b2 = index

        # if both junction box are not already part of the same circuit, join their circuits
        if index_b1 != index_b2:
            circuits[index_b1].update(circuits[index_b2])
            circuits.pop(index_b2)
        
        # if all junction boxes are now conencted to the same circuit, return the puzzle answer
        if len(circuits) == 1:
            print("The product of the X coordinates of the last two junction boxes is:", b1[0] * b2[0])
            break

if __name__ == '__main__':
    main()