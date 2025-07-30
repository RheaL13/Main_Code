class Question:
    def __init__(self):
        print("Method A called")

    def method_a(self):
        print("Method B called")
        self.instance_a.method_a()  # Call method_a of ClassA

class LevelQuiz:
    def method_b(self):
        self.instance_a = Question()  # Instantiate ClassA

# Example usage
instance_b = LevelQuiz()
instance_b.method_b()