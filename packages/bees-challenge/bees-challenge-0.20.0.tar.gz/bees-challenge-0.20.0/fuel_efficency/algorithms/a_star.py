import sys

import heapq
import math
from typing import List

from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class AStarStrategy(PathfindingStrategy):

    allowed_directions = [Position(-1, 0), Position(0, -1), Position(0, 1), Position(1, 0)]

    @staticmethod
    def find_path(grid:List[List[Node]], start:Node, end:Node):
        pass

    @staticmethod
    def get_neighbors(grid:List[List[Node]], node:Node) -> List[Node]:
        pass

    @staticmethod
    def calculate_distance(_:Node, node2: Node) -> float:
        pass
