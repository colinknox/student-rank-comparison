CLASS_RANKS = ["Freshman", "Sophomore", "Junior", "Senior"]

class Student:
    def __init__(self, name, class_rank):
        self.name = name
        self.class_rank = class_rank
        self.rank_index = CLASS_RANKS.index(self.class_rank)

    def __eq__(self, other):
        return self.rank_index == other.rank_index

    def __gt__(self, other):
        return self.rank_index > other.rank_index
    
    def __lt__(self, other):
        return self.rank_index < other.rank_index

    def __str__(self):
        return f"{self.name} {self.class_rank}"