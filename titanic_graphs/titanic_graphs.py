import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class GraphBuilder:
    def __init__(self, file_path):
        self.file_path = file_path

    def survival_rate_by_gender(self):
        data = pd.read_csv(self.file_path)
        survival_by_gender = data.groupby("Sex")["Survived"].mean()
        survival_by_gender = survival_by_gender.reindex(['female', 'male'])
        plt.figure(figsize=(10, 6))
        plt.bar(survival_by_gender.index, survival_by_gender.values, color=['blue', 'pink'])
        plt.title("Survival Rate by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Survival Rate")
        plt.grid(axis='y', linestyle='-', alpha=0.7)
        plt.show()
    
    def age_distribution(self):
        data = pd.read_csv(self.file_path)
        ages = data["Age"]

        plt.figure(figsize=(10, 6))
        plt.hist(ages, bins=80, color='green', alpha=0.7)
        plt.title("Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Number of Passengers")
        plt.grid(True)
        plt.show()

    def survival_rate_by_class(self):

        data = pd.read_csv(self.file_path)
        survival_by_class = data.groupby("Pclass")["Survived"].mean()

        plt.figure(figsize=(10, 6))
        plt.bar(survival_by_class.index, survival_by_class.values, color='skyblue')
        plt.title("Survival Rate by Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")
        plt.xticks([1, 2, 3], labels=["First Class", "Second Class", "Third Class"])
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def fare_by_class(self):

        data = pd.read_csv(self.file_path)
        fare_by_class = data.groupby("Pclass")["Fare"].mean()

        plt.figure(figsize=(10, 6))
        sns.boxplot(x="Pclass", y="Fare", data=data, palette="pastel")
        plt.title("Fare Distribution by Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Fare")
        plt.show()

    def survival_by_age_group(self):

        data = pd.read_csv(self.file_path)
        data['AgeGroup'] = pd.cut(data['Age'], bins=[0, 18, 35, 50, 80], labels=['Child', 'Young Adult', 'Middle Age', 'Senior'])
        survival_by_age_group = data.groupby("AgeGroup")["Survived"].mean()

        plt.figure(figsize=(10, 6))
        plt.bar(survival_by_age_group.index, survival_by_age_group.values, color='purple')
        plt.title("Survival Rate by Age Group")
        plt.xlabel("Age Group")
        plt.ylabel("Survival Rate")  
        plt.grid(axis='y', linestyle='--', alpha=0.7) 
        plt.show()

    def survival_heatmap(self):

        data = pd.read_csv(self.file_path)
        heatmap_data = data.pivot_table(index='Pclass', columns='Sex', values='Survived', aggfunc='mean')

        plt.figure(figsize=(10, 6))
        sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True)
        plt.title("Survival Heatmap by Class and Gender") 
        plt.xlabel("Gender") 
        plt.ylabel("Passenger Class")
        plt.show()

    def class_gender_survival_countplot(self):

        data = pd.read_csv(self.file_path)

        plt.figure(figsize=(12, 6))
        sns.countplot(x="Pclass", hue="Sex", data=data, palette="coolwarm")
        plt.title("Count of Passengers by Class and Gender")
        plt.xlabel("Passenger Class")
        plt.ylabel("Count") 
        plt.legend(title="Gender") 
        plt.show()

if __name__ == "__main__":
    titanic_csv_path = "titanic.csv"
    builder = GraphBuilder(titanic_csv_path)
    
    builder.survival_rate_by_gender()
    builder.age_distribution()
    builder.survival_rate_by_class()
    builder.survival_by_age_group()
    builder.fare_by_class()
    builder.survival_heatmap()
    builder.class_gender_survival_countplot()