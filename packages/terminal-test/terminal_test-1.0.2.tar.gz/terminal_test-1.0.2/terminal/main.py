class terminal:
    def __init__(self):
        self.display_list = {}
    def add(self,name,str):
        self.display_list[name] = str
    def delete(self,name):
        del self.display_list[name]
    def display(self):
        print("\033c")
        print("\033[H\033[2J",end="")
        keys = self.display_list.keys()
        for key in keys:
            print(self.display_list[key])

def hello():
    print("吵啥?")