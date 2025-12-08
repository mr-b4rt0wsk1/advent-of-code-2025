def main():
    split_total = 0
    
    with open('./puzzle-input.txt', 'r') as file:
        manifold = [line.strip() for line in file]
        beams = {manifold[0].index('S')}

        # follow the beams as they travel down through the manifold
        for row in manifold:
            splitters = [s for s, val in enumerate(row) if val == "^"]
            for splitter in splitters:
                # if a beam hits a splitter, count it and split it into two new beams
                if splitter in beams:
                    split_total += 1
                    beams.remove(splitter)
                    beams = beams | {splitter - 1, splitter + 1}
                    
    print("The tachyon beam is split this many times:", split_total)
        
if __name__ == '__main__':
    main()