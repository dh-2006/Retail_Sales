
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

        if self.data is None:
            print("Please Load Data First!")
            return

        print("\n----- SALES -----")

        total_sales = self.data["Total Sales"].sum()
        average_sales = self.data["Total Sales"].mean()

        popular_products = (self.data.groupby("Product")["Quantity Sold"].sum())
            
        print("Total Sales:", total_sales)
        print("Average Sales:", average_sales)
        print("Popular Product:", popular_products)

    def filter_data(self):

        if self.data is None:
            print("Please Load Data First!")
            return

        category = input("Enter Category: ")

        result = self.data[self.data["Category"] == category]

        print(result)

    def display_summary(self):

        if self.data is None:
            print("Please Load Data First!")
            return

        print("\nFirst 5 Records:")
        print(self.data.head())

        print("\nLast 5 Records:")
        print(self.data.tail())

        print("\nTotal Records:")
        print(len(self.data))

        print("\nSales by Category:")
        print(self.data.groupby("Category")["Total Sales"].sum())

   
def show_charts(self):

    if self.data is None:
        print("Please Load Data First!")
        return

    while True:
        print("\nSelect Chart Option:")
        print("1. Bar Chart")
        print("2. Line Chart")
        

        choice = int(input("Enter Your Choice: "))

        if choice == 1:

            self.data.groupby("Category")["Total Sales"].sum().plot(kind="bar")

            plt.title("Sales by Category")
            plt.xlabel("Category")
            plt.ylabel("Total Sales")
            plt.show()

        elif choice == 2:

            sales_by_date = self.data.groupby("Date")["Total Sales"].sum()

            sales_by_date.plot(kind="line", marker="o")

            plt.title("Sales Trend Over Time")
            plt.xlabel("Date")
            plt.ylabel("Total Sales")
            plt.xticks(rotation=45)
            

        else:
            print("Invalid Choice!")



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
