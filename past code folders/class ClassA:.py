# class ClassA:
#     def __init__(self):
#         self.shared_variable = "Hello from ClassA"

# class ClassB:
#     def __init__(self, class_a_instance):
#         self.class_a_instance = class_a_instance

#     def display_variable(self):
#         print(self.class_a_instance.shared_variable)

# a_instance = ClassA()
# b_instance = ClassB(a_instance)
# b_instance.display_variable()


class ClassA:
    class_variable = "Shared by all ClassA instances"

class ClassB:
    def display_class_variable(self):
        print(ClassA.class_variable)

b_instance = ClassB()
b_instance.display_class_variable()