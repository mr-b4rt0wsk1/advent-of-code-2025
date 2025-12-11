def dfs(src, dest, devices):
    """depth-first search (DFS) algorithm to find the number of paths from src to dest in a graph"""
    # if we have reached dest, count the path
    if src == dest:
        return 1
    # otherwise, continue DFS from the adjacent nodes
    total_paths = 0
    for adj_node in devices[src]:
        total_paths += dfs(adj_node, dest, devices)
    return total_paths    

def main():
    devices = {}
    # read in the file and create a dictionary to represent the graph
    with open('./puzzle-input.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            devices[key] = value.split()

    # use depth-first search to find all paths from 'you' to 'out' in the graph
    total_paths = dfs('you', 'out', devices)

    print("The number of paths that lead from 'you' to 'out' is:", total_paths)
        
if __name__ == '__main__':
    main()