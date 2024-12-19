import math

class Node:
    def __init__(self, row_index, column_index, direction):
        self.row = row_index
        self.column = column_index
        self.distance = math.inf
        self.previous_nodes = []
        self.direction = direction
        self.discovered = False

def get_nodes(filepath):
    # node = row, column, distance, previous node, direction
    unvisited_nodes = list()
    end_node = None
    with open(filepath) as file:
        for row_index, row in enumerate(file.readlines()):
            for column_index, column in enumerate(row):
                if row[column_index] == "S":
                    starting_node = Node(row_index, column_index,  [0, 1])
                    starting_node.distance = 0
                    unvisited_nodes.append(starting_node)
                elif row[column_index] == "E":
                    end_node = Node(row_index, column_index,  None)
                    unvisited_nodes.append(end_node)
                elif row[column_index] == ".":
                    unvisited_nodes.append(Node(row_index, column_index,  None))

    return sorted(unvisited_nodes, key = lambda x: x.distance), end_node

def rotate(actual_direction, next_direction):
    if actual_direction[0] == -1 * next_direction[0] and actual_direction[1] == next_direction[1]:
        return 2
    elif actual_direction[1] == -1 * next_direction[1] and actual_direction[0] == next_direction[0]:
        return 2
    else:
        return 1


def part_one():
    unvisited_nodes, end_node = get_nodes("sample.txt")
    visited_nodes = list()

    while len(unvisited_nodes) > 0:
        # We start by selecting the node with the minimal distance
        node_with_minimum_distance = unvisited_nodes[0]

        # For each neighbor, check the direction needed
        for node in unvisited_nodes:
            if node.row == node_with_minimum_distance.row + 1 and node.column == node_with_minimum_distance.column:
                node.direction = [1, 0]
            elif node.row == node_with_minimum_distance.row - 1 and node.column == node_with_minimum_distance.column:
                node.direction = [-1, 0]
            elif node.row == node_with_minimum_distance.row and node.column == node_with_minimum_distance.column + 1:
                node.direction = [0, 1]
            elif node.row == node_with_minimum_distance.row and node.column == node_with_minimum_distance.column - 1:
                node.direction = [0, -1]
            else:
                continue

            # Calculate how many turns are necessary to reach this neighbor
            rotation = 0
            if node_with_minimum_distance.direction != node.direction:
                rotation = rotate(node_with_minimum_distance.direction, node.direction)

            # Set the previous node as the node with the actual minumum distance
            actual_distance = 1000 * rotation + 1 + node_with_minimum_distance.distance
            if actual_distance < node.distance:
                node.previous_nodes.append(node_with_minimum_distance)
                node.distance = actual_distance
            elif actual_distance == node.distance:
                node.previous_nodes.append(node_with_minimum_distance)
            # print(f"row: {node.row}, column: {node.column}, distance: {node.distance}")

        # Once all his neighbors are scanned, we remove this node from the list and sort it again to have the
        unvisited_nodes.remove(node_with_minimum_distance)
        unvisited_nodes = sorted(unvisited_nodes, key=lambda x: x.distance)
        visited_nodes.append(node_with_minimum_distance)

    for node in visited_nodes:
        if node.row == end_node.row and node.column == end_node.column:
            print(f"[PART ONE] - The shortest path length is: {node.distance}")

    return visited_nodes, end_node

def part_two():
    unvisited_nodes, end_node = get_nodes("sample.txt")
    visited_nodes = list()

    while len(unvisited_nodes) > 0:
        # We start by selecting the node with the minimal distance
        node_with_minimum_distance = unvisited_nodes[0]

        # For each neighbor, check the direction needed
        for node in unvisited_nodes:
            if node.row == node_with_minimum_distance.row + 1 and node.column == node_with_minimum_distance.column:
                node.direction = [1, 0]
            elif node.row == node_with_minimum_distance.row - 1 and node.column == node_with_minimum_distance.column:
                node.direction = [-1, 0]
            elif node.row == node_with_minimum_distance.row and node.column == node_with_minimum_distance.column + 1:
                node.direction = [0, 1]
            elif node.row == node_with_minimum_distance.row and node.column == node_with_minimum_distance.column - 1:
                node.direction = [0, -1]
            else:
                continue

            # Calculate how many turns are necessary to reach this neighbor
            rotation = 0
            if node_with_minimum_distance.direction != node.direction:
                rotation = rotate(node_with_minimum_distance.direction, node.direction)

            # Set the previous node as the node with the actual minumum distance
            actual_distance = 1000 * rotation + 1 + node_with_minimum_distance.distance
            if actual_distance < node.distance:
                node.previous_nodes.append(node_with_minimum_distance)
                node.distance = actual_distance
            elif actual_distance == node.distance:
                node.previous_nodes.append(node_with_minimum_distance)
            # print(f"row: {node.row}, column: {node.column}, distance: {node.distance}")

        # Once all his neighbors are scanned, we remove this node from the list and sort it again to have the
        unvisited_nodes.remove(node_with_minimum_distance)
        unvisited_nodes = sorted(unvisited_nodes, key=lambda x: x.distance)
        visited_nodes.append(node_with_minimum_distance)

    for node in visited_nodes:
        if node.row == end_node.row and node.column == end_node.column:
            print(f"[PART TWO] - There are {"Waiting on solution"} good places to sit")



if __name__ == "__main__":
    #part_one()
    part_two()
