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





tim = Student("Tim", "Junior")
julie = Student("Julie", "Senior")
# julie = Student("Julie", "Junior")

# print(f"DEBUG: Tim same rank as Julie = {tim.rank_index == julie.rank_index}")
print(f"DEBUG: Tim greater than Julie = {tim.rank_index > julie.rank_index}")
print(f"DEBUG: Julie greater than Tim = {julie.rank_index > tim.rank_index}")
