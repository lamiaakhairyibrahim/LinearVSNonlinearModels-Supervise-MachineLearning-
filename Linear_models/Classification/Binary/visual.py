import matplotlib.pyplot as plt

class visual:
    def __init__(self , x1 = None ,x2 = None , x3= None , x4 = None , y = None ):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y = y
        self.show()
        

    def show(self):
        plt.figure(figsize=(10, 5))  # Adjust figure size for better subplot display
        plt.subplot(1, 2, 1)
        plt.hist(self.y, bins=10)
        plt.title('Target Distribution')  # Added title for clarity
        plt.subplot(1, 2, 2)
        plt.title('Feature Relationships')
        plt.scatter(self.x1, self.y, color='red', label='sepal length')  # Corrected colorizer to color, added label
        plt.scatter(self.x2, self.y, color='green', label='sepal width')  # Corrected colorizer to color, added label
        plt.scatter(self.x3,self.y, color='yellow', label='petal length')  # Assuming 'petal width (cm)' was a typo, added label
        plt.scatter(self.x4, self.y, color='blue', label='petal width')  # Corrected colorizer to color, added label
        plt.xlabel('Feature Value')  # Added x-axis label for clarity
        plt.ylabel('Target Value')  # Added y-axis label
        plt.legend()  # Show the legend to identify the features
        plt.show()