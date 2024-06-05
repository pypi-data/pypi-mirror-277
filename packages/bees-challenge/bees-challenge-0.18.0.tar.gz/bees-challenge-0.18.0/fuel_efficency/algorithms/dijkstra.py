import sys

import heapq
import math
from typing import List

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class DijkstraStrategy(PathfindingStrategy):

    cardinal_directions = [
        Position(-1, -1),
        Position(-1, 0),
        Position(-1, 1),
        Position(0, -1),
        Position(0, 1),
        Position(1, -1),
        Position(1, 0),
        Position(1, 1),
    ]

    @staticmethod
    def find_path(grid:List[List[Node]], start:Node, end:Node):
        distances = {node: sys.maxsize for row in grid for node in row}
        distances[start] = 0
        previous_nodes = {node: None for row in grid for node in row}
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                path = []
                while current_node:
                    path.insert(0, current_node)
                    current_node = previous_nodes[current_node]
                return path[1:]

            if current_distance > distances[current_node]:
                continue

            for neighbor in DijkstraStrategy.get_neighbors(grid, current_node):
                distance = DijkstraStrategy.calculate_distance(current_node, neighbor)
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        return None

    @staticmethod
    def get_neighbors(grid:List[List[Node]], node:Node) -> List[Node]:
        rows = len(grid)
        cols = len(grid[0])

        neighbors = []
        for offset in DijkstraStrategy.cardinal_directions:
            neighbor_position = node.position - offset
            if 0 <= neighbor_position.x < rows and 0 <= neighbor_position.y < cols:
                neightbor = grid[neighbor_position.x][neighbor_position.y]
                neighbors.append(neightbor)

        return neighbors

    @staticmethod
    def calculate_distance(node1:Node, node2: Node) -> float:
        offset = node1.position - node2.position
        row_dist = abs(offset.x)
        col_dist = abs(offset.y)
        diagonals = math.sqrt(2) * min(row_dist, col_dist)
        orthogonals = abs(row_dist - col_dist)
        return diagonals + orthogonals
