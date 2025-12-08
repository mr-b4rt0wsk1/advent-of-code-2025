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
    # change to 10 if using test-input.txt
    connections = 1000

    # read in the file input and create the list of junction boxes
    with open('./puzzle-input.txt', 'r') as file:
        boxes = [tuple(map(int, line.strip().split(","))) for line in file]

    # find the N shortest pairs of all of the junction boxes, sorted from smallest to largest
    pairs = generate_pairs(boxes)
    n_shortest_pairs = sorted(pairs, key=lambda x: x[0])[:connections:]
    # intialize the circuits as each junction box in its own circuit
    circuits = [{boxes[i]} for i in range(len(boxes))]
    
    # iterate through the N shortest pairs
    for _, b1, b2 in n_shortest_pairs:
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

    sorted_circuits = sorted([len(c) for c in circuits], reverse=True)
    print("The product of the 3 largest circuits is:", sorted_circuits[0] * sorted_circuits[1] * sorted_circuits[2])
        
if __name__ == '__main__':
    main()