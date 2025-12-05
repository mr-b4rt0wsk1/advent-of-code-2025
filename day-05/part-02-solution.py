def merge_intervals(intervals):
    '''algorithm to merge a list of intervals
    input: list of unsorted and unmerged intervals
    output: list of sorted and merged intervals
    '''

    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]
    
    for current in sorted_intervals[1:]:
            previous = merged[-1]
            if current[0] <= previous[1]:
                merged[-1] = [previous[0], max(previous[1], current[1])]
            else:
                merged.append(current)
                
    return merged

def main():
    total_ids = 0

    with open('./puzzle-input.txt', 'r') as file:
        database = [line.strip() for line in file]
        id_ranges = database[:database.index('')]
        intervals = []

        # create a list of intervals from the ID range inputs
        for id_range in id_ranges:
            intervals.append([int(id_range.split("-")[0]), int(id_range.split("-")[1])])

        merged = merge_intervals(intervals)

        # count the unique number of IDs using the start and end of each interval
        for x in merged:
            total_ids += (x[1] - x[0] + 1)
            
    print("The total number of fresh ingredient IDs is:", total_ids)
        
if __name__ == '__main__':
    main()