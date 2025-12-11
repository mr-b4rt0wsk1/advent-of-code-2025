def dfs(src, dest, devices, cache):
    """depth-first search (DFS) algorithm to find the number of paths from src to dest in a graph
    improvements from part 1: dead end checks and caching for performance
    """
    # if we have reached dest, count the path
    if src == dest:
        return 1
    # if we have reached a dead end, do not count the path
    elif src not in devices:
        return 0
    # if we have already counted the paths from the current node to dest, get it from the cache
    elif src in cache:
        return cache[src]
    # otherwise, continue DFS from the adjacent nodes
    total_paths = 0
    for adj_node in devices[src]:
        total_paths += dfs(adj_node, dest, devices, cache)
    # update the cache with a new entry of the total paths from the current node to dest
    cache[src] = total_paths
    return total_paths

def main():
    devices = {}
    # read in the file and create a dictionary to represent the graph
    with open('./puzzle-input.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            devices[key] = value.split()

    # use depth-first search to find:
    # -  the number of paths from 'svr' to 'fft' in the graph 
    # -  the number of paths from 'fft' to 'dac' in the graph
    # -  the number of paths from 'dac' to 'out' in the graph
    # then multiply those numbers to find the total paths from 'svr' to 'out' that include 'fft' and 'dac'

    total_paths = dfs('svr', 'fft', devices, {}) * dfs('fft', 'dac', devices, {}) * dfs('dac', 'out', devices, {})

    print("The number of paths that lead from 'srv' to 'out' that include 'fft' and 'dac' is:", total_paths)
        
if __name__ == '__main__':
    main()