CLASS_RANKS = ["Freshman", "Sophomore", "Junior", "Senior"]

class Student:
    def __init__(self, name, class_rank):
        self.name = name
        self.class_rank = class_rank
        self.rank_index = CLASS_RANKS.index(self.class_rank)



tim = Student("Tim", "Junior")
print(f"DEBUG: Name = {tim.name}")
print(f"DEBUG: Class rank = {tim.class_rank}")
print(f"DEBUG: Rank index = {tim.rank_index}")
