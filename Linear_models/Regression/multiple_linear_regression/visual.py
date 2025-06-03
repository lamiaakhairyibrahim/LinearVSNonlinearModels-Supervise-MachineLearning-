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

            # --- Scatter Plots ---
            plt.figure(figsize=(10, 6))
            if 'area' in self.data.columns:
                plt.scatter(self.data['area'], self.data['price'], color='red', label='Area vs Price')
            if 'bedrooms' in self.data.columns:
                plt.scatter(self.data['bedrooms'], self.data['price'], color='green', label='Bedrooms vs Price')
            if 'bathrooms' in self.data.columns:
                plt.scatter(self.data['bathrooms'], self.data['price'], color='blue', label='Bathrooms vs Price')
            if 'stories' in self.data.columns:
                plt.scatter(self.data['stories'], self.data['price'], color='yellow', label='stories vs Price')
            if 'parking' in self.data.columns:
                plt.scatter(self.data['parking'], self.data['price'], color='black', label='parking vs Price')

            plt.xlabel('Feature Value')
            plt.ylabel('Price')
            plt.title('Feature vs Price Scatter Plots')
            plt.legend()
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(10, 6))
            if 'area' in self.data.columns:
                plt.boxplot(self.data['area'], label='Area vs Price')
                plt.title('area')
                plt.show()
            if 'bedrooms' in self.data.columns:
                plt.boxplot(self.data['bedrooms'],  label='Bedrooms vs Price')
                plt.title('bedrooms')
                plt.show()
            if 'bathrooms' in self.data.columns:
                plt.boxplot(self.data['bathrooms'],  label='Bathrooms vs Price')
                plt.title('bathrooms')
                plt.show()
            if 'stories' in self.data.columns:
                plt.boxplot(self.data['stories'], label='stories vs Price')
                plt.title('stories')
                plt.show()
            if 'parking' in self.data.columns:
                plt.boxplot(self.data['parking'],  label='parking vs Price')
                plt.title('parking')
                plt.show()
            if 'price' in self.data.columns:
                plt.boxplot(self.data['price'],  label='parking vs Price')
                plt.title('price')
                plt.show()


     