def get_sources_sinks(adj_matrix):
    sources = []
    sinks = []

    for node in range(len(adj_matrix)):
        outs = 0
        ins = 0

        for other_node in range(len(adj_matrix)):
            if adj_matrix[node][other_node] == 1:
                outs += 1
            if adj_matrix[other_node][node] == 1:
                ins += 1
        
        if outs > 0 and ins > 0:
            pass
        elif outs > 0:
            sources.append(node+1)
        elif ins > 0:
            sinks.append(node+1)
        else:
            sources.append(node+1)
            sinks.append(node+1)
    
    return (sources, sinks)

def main():
    len_matrix = int(input())
    matrix = []
    for _ in range(len_matrix):
        row = list(map(int, input().split()))
        matrix.append(row)

    sources, sinks = get_sources_sinks(matrix)
    print(len(sources), *sources)
    print(len(sinks), *sinks)

main()