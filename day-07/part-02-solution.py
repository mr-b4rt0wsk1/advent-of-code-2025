def main():
    
    with open('./puzzle-input.txt', 'r') as file:
        manifold = [line.strip() for line in file]
        # this time we keep track of the number of times a tachyon passes through a column
        tachyons = [0] * len(manifold[0])
        tachyons[manifold[0].index('S')] += 1

        for row in manifold:
            splitters = [s for s, val in enumerate(row) if val == "^"]
            for splitter in splitters:
                # if tachyons encounter a splitter, move the tachyon count to the left and right columns
                if tachyons[splitter] > 0:
                    tachyons[splitter - 1] += tachyons[splitter]
                    tachyons[splitter + 1] += tachyons[splitter]
                    tachyons[splitter] = 0

    # the number of timelines is just the sum of the number of times a tachyon travels to each column at the end of the manifold
    print("The total number of different timelines the tachyon ends up on:", sum(tachyons))
        
if __name__ == '__main__':
    main()