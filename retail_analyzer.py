
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:

    def __init__(self):
        self.df = None

    def load_data(self, file_path):

        self.df = pd.read_csv(file_path)

        required_columns = [
            "Date", "Product", "Category",
            "Price", "Quantity Sold", "Total Sales"]
        
        for column in required_columns:
            if column not in self.df.columns:
                print("Missing column:", column)
                self.df = None
                return

        self.df["Product"] = self.df["Product"].fillna("Unknown")
        self.df["Category"] = self.df["Category"].fillna("Unknown")

        numeric_columns = [
            "Price", "Quantity Sold", "Total Sales"]
        

        for column in numeric_columns:
            self.df[column] = pd.to_numeric(self.df[column], errors="coerce")
                
        self.df[numeric_columns] = self.df[numeric_columns].fillna(0)

        self.df["Date"] = pd.to_datetime(
            self.df["Date"], errors="coerce")
        

        self.df = self.df.dropna(subset=["Date"])

        sales_array = np.array(self.df["Total Sales"])

        print("Dataset Loaded Successfully!")
        print("Total Records:", len(self.df))
        print("Sales Array:", sales_array)

    def calculate_metrics(self):

        if self.df is None:
            print("Please load dataset first!")
            return

        total_sales = np.sum(self.df["Total Sales"])
        average_sales = np.mean(self.df["Total Sales"])

        popular_product = self.df.groupby("Product")["Quantity Sold"].sum().idxmax()
           
        print("\n----- Sales Metrics -----")
        print("Total Sales:", total_sales)
        print("Average Sales:", average_sales)
        print("Most Popular Product:", popular_product)

    def filter_data(self, condition):

        if self.df is None:
            print("Please load dataset first!")
            return

        if condition == "category":

            category = input("Enter Category: ")

            result = self.df[
                self.df["Category"].str.lower() == category.lower()
            ]

        elif condition == "date":

            start = pd.to_datetime(
                input("Enter Start Date (YYYY-MM-DD): "),
                errors="coerce"
            )

            end = pd.to_datetime(
                input("Enter End Date (YYYY-MM-DD): "),
                errors="coerce"
            )

            if pd.isna(start) or pd.isna(end):
                print("Invalid Date!")
                return

            result = self.df[
                (self.df["Date"] >= start) &(self.df["Date"] <= end)]
                
        else:
            print("Invalid Condition!")
            return

        if result.empty:
            print("No Records Found!")
        else:
            print(result.to_string(index=False))

    def display_summary(self):

        if self.df is None:
            print("Please load dataset first!")
            return

        print("\n----- Retail Sales Summary -----")

        print("Total Records:", len(self.df))

        print("\nFirst 5 Records:")
        print(self.df.head())

        print("\nSales By Category:")

        category_sales = self.df.groupby(
            "Category"
        )["Total Sales"].sum()

        print(category_sales)

        total = self.df["Total Sales"].sum()

        if total > 0:
            percentage = (category_sales / total) * 100

            print("\nSales Percentage:")
            print(percentage.round(2))

    def show_charts(self):

        if self.df is None:
            print("Please load dataset first!")
            return

        category_sales = self.df.groupby("Category" )["Total Sales"].sum()
           
        category_sales.plot(kind="bar")

        plt.title("Sales By Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        date_sales = self.df.groupby(
            "Date"
        )["Total Sales"].sum()

        date_sales.plot(kind="line", marker="o")

        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        correlation = self.df[
            ["Price", "Quantity Sold", "Total Sales"]
        ].corr()

        sns.heatmap(correlation, annot=True)

        plt.title("Sales Correlation Heatmap")
        plt.tight_layout()
        plt.show()


# Main Program

obj = RetailAnalyzer()

while True:

    print("\n===== RETAIL SALES DATA ANALYZER =====")
    print("1. Load Dataset")
    print("2. Calculate Metrics")
    print("3. Filter Data")
    print("4. Display Summary")
    print("5. Show Charts")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        file_path = input("Enter CSV File Path: ")

        try:
            if file_path.endswith(".csv"):
                obj.load_data(file_path)
            else:
                print("Please select CSV file!")

        except FileNotFoundError:
            print("File Not Found!")

        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        obj.calculate_metrics()

    elif choice == "3":

        print("1. Filter By Category")
        print("2. Filter By Date")

        option = input("Enter Option: ")

        if option == "1":
            obj.filter_data("category")

        elif option == "2":
            obj.filter_data("date")

        else:
            print("Invalid Option!")

    elif choice == "4":
        obj.display_summary()

    elif choice == "5":
        obj.show_charts()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")
