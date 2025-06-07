import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class visual:
    def __init__(self,data):
        self.data = pd.DataFrame(data)
        self.show()
    
    def show(self, bins=20, hist_color="blue", figsize=(10, 10), heatmap_cmap='coolwarm'):
            # --- Histogram ---
            axes = self.data.hist(bins=bins, figsize=figsize, grid=True)
            for ax in axes.flatten():
                for patch in ax.patches:
                    patch.set_facecolor(hist_color)
            plt.suptitle("Histogram of Dataset Features")
            plt.tight_layout()
            plt.show()

            # --- Correlation Heatmap ---
            corr = self.data.corr()
            plt.figure(figsize=(10, 8))  # Reasonable size
            sns.heatmap(corr, annot=True, fmt='.1f', cmap=heatmap_cmap)
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            plt.show()

            ### scatter 
            plt.scatter(self.data['Elevation'] , self.data['Aspect'] , c = self.data['Cover_Type'])
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
            plt.title('Scatter Plot of Classes')
            plt.show()


            plt.figure(figsize=(10, 6))
            if 'Elevation' in self.data.columns:
                plt.boxplot(self.data['Elevation'], label='Elevation')
                plt.title('Elevation')
                plt.show()
            if 'Aspect' in self.data.columns:
                plt.boxplot(self.data['Aspect'],  label='Aspect')
                plt.title('Aspect')
                plt.show()
            if 'Slope' in self.data.columns:
                plt.boxplot(self.data['Slope'],  label='Slope')
                plt.title('Slope')
                plt.show()
            if 'Horizontal_Distance_To_Hydrology' in self.data.columns:
                plt.boxplot(self.data['Horizontal_Distance_To_Hydrology'], label='Horizontal_Distance_To_Hydrology')
                plt.title('Horizontal_Distance_To_Hydrology')
                plt.show()
            if 'Vertical_Distance_To_Hydrology' in self.data.columns:
                plt.boxplot(self.data['Vertical_Distance_To_Hydrology'],  label='Vertical_Distance_To_Hydrology')
                plt.title('Vertical_Distance_To_Hydrology')
                plt.show()
            if 'Horizontal_Distance_To_Roadways' in self.data.columns:
                plt.boxplot(self.data['Horizontal_Distance_To_Roadways'],  label='Horizontal_Distance_To_Roadways')
                plt.title('Horizontal_Distance_To_Roadways')
                plt.show()
            if 'Hillshade_9am' in self.data.columns:
                plt.boxplot(self.data['Hillshade_9am'],  label='Hillshade_9am')
                plt.title('Hillshade_9am')
                plt.show()
            if 'Hillshade_Noon' in self.data.columns:
                plt.boxplot(self.data['Hillshade_Noon'],  label='Hillshade_Noon')
                plt.title('Hillshade_Noon')
                plt.show()
            if 'Hillshade_3pm' in self.data.columns:
                plt.boxplot(self.data['Hillshade_3pm'],  label='Hillshade_3pm')
                plt.title('Hillshade_3pm')
                plt.show()
            if 'Horizontal_Distance_To_Fire_Points' in self.data.columns:
                plt.boxplot(self.data['Horizontal_Distance_To_Fire_Points'],  label='Horizontal_Distance_To_Fire_Points')
                plt.title('Horizontal_Distance_To_Fire_Points')
                plt.show()
            if 'Wilderness_Area1' in self.data.columns:
                plt.boxplot(self.data['Wilderness_Area1'],  label='Wilderness_Area1')
                plt.title('Wilderness_Area1')
                plt.show()
            if 'Wilderness_Area2' in self.data.columns:
                plt.boxplot(self.data['Wilderness_Area2'],  label='Wilderness_Area2')
                plt.title('Wilderness_Area2')
                plt.show()
            if 'Wilderness_Area3' in self.data.columns:
                plt.boxplot(self.data['Wilderness_Area3'],  label='Wilderness_Area3')
                plt.title('Wilderness_Area3')
                plt.show()
            if 'Wilderness_Area4' in self.data.columns:
                plt.boxplot(self.data['Wilderness_Area4'],  label='Wilderness_Area4')
                plt.title('Wilderness_Area4')
                plt.show()
          



