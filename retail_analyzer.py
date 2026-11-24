import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:

    def __init__(self):
        self.data = None

    def load_data(self):

        try:
            self.data = pd.read_csv("retail_sales.csv")

            print("Data Loaded Successfully!")

            return True

        except FileNotFoundError:
            print("CSV File Not Found!")

            return False

    def calculate_metrics(self):

        total_sales = self.data["Total Sales"].sum()
        average_sales = self.data["Total Sales"].mean()
        popular_products=(self.data("Product")["Quantity Sold"].sum)

        total_sales = ("Total Sales:",total_sales)
        average_sales = ("Average sales:",average_sales)
        popular_products = ("popular products:",popular_products)


    def filter_data(self):

        categaory = input("Enter Category:")

        result = self.data[self.data["Category"] == categaory]

        print(result)

    def display_summary(self):

        print("First 5 Records:")
        print(self.data.head())

        print("Last 5 Records:")
        print(self.data.tail())

        print("Total Records:")
        print(len(self.data))

        print("Sales Category:")
        print(self.data.groupby("Category")["Total Sales"].sum())

    def show_charts(self):

         self.data.groupby("Category")["Total Sales"].sum().plot(kind="bar")
    
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.show()


analyzer = RetailAnalyzer()

analyzer.load_data()


while True:

    print("\n1. Calculate Sales Metrics")
    print("2. Filter Data")
    print("3. Display Summary")
    print("4. Show Charts")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        analyzer.calculate_metrics()

    elif choice == 2:
        analyzer.filter_data()

    elif choice == 3:
        analyzer.display_summary()

    elif choice == 4:
        analyzer.show_charts()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

    
        




