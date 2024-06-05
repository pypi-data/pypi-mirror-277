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
        priority_queue = [(0, start)]
        visited_nodes = set()
        cum_distance = {node: sys.maxsize if node is not start else 0 for row in grid for node in row}
        previous_node = {node: None for row in grid for node in row}

        while priority_queue:
            current_cum_distance, current_node = heapq.heappop(priority_queue)
            visited_nodes.add(current_node)

            if current_node == end:
                path = []
                while current_node:
                    path.insert(0, current_node)
                    current_node = previous_node[current_node]
                return path[1:]

            if current_cum_distance > cum_distance[current_node]:
                continue

            for neighbor in DijkstraStrategy.get_neighbors(grid, current_node):
                inc_distance = DijkstraStrategy.calculate_distance(current_node, neighbor)
                new_cum_distance = current_cum_distance + inc_distance
                if neighbor not in visited_nodes and new_cum_distance < cum_distance[neighbor]:
                    cum_distance[neighbor] = new_cum_distance
                    previous_node[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_cum_distance, neighbor))

        return None

    @staticmethod
    def get_neighbors(grid:List[List[Node]], node:Node) -> List[Node]:
        row_qty = len(grid)
        col_qty = len(grid[0])

        neighbors = []
        for offset in DijkstraStrategy.cardinal_directions:
            neighbor_position = node.position - offset
            if 0 <= neighbor_position.x < row_qty and 0 <= neighbor_position.y < col_qty:
                neightbor = grid[neighbor_position.x][neighbor_position.y]
                neighbors.append(neightbor)

        return neighbors

    @staticmethod
    def calculate_distance(node1:Node, node2: Node) -> float:
        if node1.position.x == node2.position.x or node1.position.y == node2.position.y:
            return node2.weight
        return math.sqrt(2) * node2.weight
