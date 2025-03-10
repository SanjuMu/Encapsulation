
input = input("Enter a string: ")
class Reverse:
    def __init__(self, s= "default"):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]
    
reversed = Reverse(input)
print("Reversed string:",reversed.reverse_string())