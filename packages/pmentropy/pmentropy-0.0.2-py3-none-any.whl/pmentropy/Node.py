class Node:
    
    def __init__(self, path: str, visits: int, end_visits: int, parent = None):
        self.path = path
        self.key = path[path.rfind("/") + 1:]
        self.visits = visits
        self.end_visits = end_visits
        self.attributes = {"visited": False}
        self.parent = parent
    
    def get_visits(self) -> int:
        return self.visits

    def get_end_visits(self) -> int:
        return self.end_visits
    
    def increment_visits(self) -> None:
        self.visits += 1
    
    def increment_end_visits(self) -> None:
        self.end_visits += 1
    
    def is_end_node(self) -> bool:
        return self.end_visits != 0
