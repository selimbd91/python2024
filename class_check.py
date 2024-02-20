
class Myname:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_value(self):
        print(f"Name: {self.name} and Age: {self.age}")

def main():

    obj = Myname("selim", 32)
    Myname.get_value(obj)

if __name__ == "__main__":
    main()