import matplotlib.pyplot as plt 

class visual:
    def __init__(self, x , y):
        self.x = x
        self.y = y 

    def show(self):
        plt.scatter(self.x , self.y)
        plt.show()