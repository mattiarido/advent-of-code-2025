# Challenge https://adventofcode.com/2025/day/8

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "puzzle_input.txt")

def read_input():
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split(',') for line in lines]
        lines = [[int(coord) for coord in box] for box in lines]
    return lines

def get_distance(box1, box2):
    return sum((a - b) ** 2 for a, b in zip(box1, box2)) ** 0.5


def get_cluster(clusters, box):
    
    for cluster in clusters:
        if box in cluster:
            return cluster
    
    return None


def part_1(boxes):

    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distance = get_distance(boxes[i], boxes[j])
            distances.append((boxes[i], boxes[j], distance))

    distances.sort(key=lambda x: x[2])

    clusters = []
    for i in range(0, 1000):
        print('iteration', i)
        box1, box2 = distances[i][0: 2]
        box1, box2 = tuple(box1), tuple(box2)

        cluster1 = get_cluster(clusters, box1)
        cluster2 = get_cluster(clusters, box2)

        print(f'box1 {box1} belonging to cluster', cluster1)
        print(f'box2 {box2} belonging to cluster', cluster2)

        if cluster1 and cluster2:
            if cluster1 == cluster2:
                continue
            
            print('two different clusters, merging')
            merged_cluster = set() 
            for box in cluster1:
                merged_cluster.add(box)
            for box in cluster2:
                merged_cluster.add(box)
            clusters.append(merged_cluster)
            clusters.remove(cluster1)
            clusters.remove(cluster2)
        elif cluster1:
            print('adding one element to cluster 1')
            cluster1.add(box2)
        elif cluster2:
            print('adding one element to cluster 2')
            cluster2.add(box1)
        else:
            print('creating new cluster')
            clusters.append(set([box1, box2]))
            
    return clusters

    
def part_2(boxes):
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distance = get_distance(boxes[i], boxes[j])
            distances.append((boxes[i], boxes[j], distance))
            
    distances.sort(key=lambda x: x[2])

    clusters = []
    iteration = 0
    while sum([len(cluster) for cluster in clusters]) < len(boxes):
        if True:
            print('iteration', iteration)

        box1, box2 = distances[iteration][0: 2]
        print(f'considering {box1} and {box2}')
        box1, box2 = tuple(box1), tuple(box2)

        cluster1 = get_cluster(clusters, box1)
        cluster2 = get_cluster(clusters, box2)

        # print(f'box1 {box1} belonging to cluster', cluster1)
        # print(f'box2 {box2} belonging to cluster', cluster2)

        if cluster1 and cluster2:
            if cluster1 == cluster2:
                iteration += 1
                continue
            
            # print('two different clusters, merging')
            merged_cluster = set() 
            for box in cluster1:
                merged_cluster.add(box)
            for box in cluster2:
                merged_cluster.add(box)
            clusters.append(merged_cluster)
            clusters.remove(cluster1)
            clusters.remove(cluster2)
        elif cluster1:
            # print('adding one element to cluster 1')
            cluster1.add(box2)
        elif cluster2:
            # print('adding one element to cluster 2')
            cluster2.add(box1)
        else:
            # print('creating new cluster')
            clusters.append(set([box1, box2]))
        
        iteration += 1
    return clusters

if __name__ == "__main__":
    boxes = read_input()
    print("Part 1:")
    clusters = part_1(boxes)
    # print(f'clusters {clusters}')
    clusters_size = [len(cluster) for cluster in clusters]
    clusters_size.sort()
    print(f'clusters: {clusters}')
    print(f'three top clusters {clusters_size[-3:]} which multiplied are {clusters_size[-3]*clusters_size[-2]*clusters_size[-1]}')
    print("Part 2:")
    clusters = part_2(boxes)
    print(f'the answer is in the last print')
    
