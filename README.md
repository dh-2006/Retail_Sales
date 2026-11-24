# 📊 Retail Sales Data Analyzer

An interactive **Command Line Interface (CLI)** application built using **Python**, **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**. This beginner-friendly project uses Object-Oriented Programming (OOP) to load retail sales records, calculate useful sales metrics, filter data, display summaries, and create charts.

---

## 🚀 Features

- 📂 **CSV Data Loading**: Load retail sales records from `retail_sales.csv`.
- 🧮 **Sales Metrics**: Calculate total sales and average sales.
- 🏆 **Popular Product**: Find the product with the highest quantity sold.
- 🔎 **Category Filtering**: Display records for a selected product category.
- 📋 **Data Summary**: View the first five records, total record count, and sales by category.
- 📈 **Data Visualization**: Create a bar chart showing total sales by category.
- 🛡️ **Basic Error Handling**: Display a helpful message if the CSV file is missing or data has not been loaded.

---

## 🏗️ Object-Oriented Programming (OOP) Highlights

- **Class**: `RetailAnalyzer` groups the project's data and operations.
- **Constructor (`__init__`)**: Initializes the data attribute.
- **Instance Methods**: Separate methods handle loading, calculations, filtering, summaries, and charts.
- **Object**: An instance of `RetailAnalyzer` is used to run the application.

---

---

## 💻 Source Code

Click below to open the Python source file:

[![View Source Code](https://img.shields.io/badge/💻_View_Source_Code-green?style=for-the-badge)](retail_analyzer.py)

---

## 📂 Dataset (CSV File)

Click below to view the retail sales dataset:

[![View CSV Dataset](https://img.shields.io/badge/📊_View_CSV_Dataset-blue?style=for-the-badge)](retail_sales.csv)

---

## 🛠️ Prerequisites & Installation

### Requirements

- **Python 3.x**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

### Installation Steps

1. Keep `retail_analyzer.py` and `retail_sales.csv` in the same folder.
2. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. Run the application:

   ```bash
   python retail_analyzer.py
   ```

---

## 📖 How to Use

1. Run the program. It will automatically try to load `retail_sales.csv`.
2. Select **Option 1** to calculate sales metrics.
3. Select **Option 2** to filter records by category.
4. Select **Option 3** to display the data summary.
5. Select **Option 4** to show the sales chart.
6. Select **Option 5** to exit the application.

---

## 🗂️ Dataset Information

The `retail_sales.csv` file contains 15 sample records and the following six columns:

| Column | Description |
|---|---|
| `Date` | Date of the sale |
| `Product` | Product name |
| `Category` | Product category |
| `Price` | Price per item |
| `Quantity Sold` | Number of items sold |
| `Total Sales` | Price multiplied by quantity sold |

---

## 📜 License

This project is created for educational and learning purposes. You may use and modify it for your own practice.
