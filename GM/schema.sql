PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Categories (
  CategoryID INTEGER PRIMARY KEY,
  CategoryName TEXT
);

CREATE TABLE IF NOT EXISTS Suppliers (
  SupplierID INTEGER PRIMARY KEY,
  SupplierName TEXT,
  Address TEXT
);

CREATE TABLE IF NOT EXISTS Products (
  ProductID INTEGER PRIMARY KEY,
  Name TEXT,
  SupplierID INTEGER,
  CategoryID INTEGER,
  Price REAL,
  FOREIGN KEY(SupplierID) REFERENCES Suppliers(SupplierID),
  FOREIGN KEY(CategoryID) REFERENCES Categories(CategoryID)
);

CREATE TABLE IF NOT EXISTS Customers (
  CustomerID INTEGER PRIMARY KEY,
  Name TEXT,
  Address TEXT
);

CREATE TABLE IF NOT EXISTS Store_Employees (
  EmployeeID INTEGER PRIMARY KEY,
  Name TEXT,
  HireDate TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
  OrderID INTEGER PRIMARY KEY,
  CustomerID INTEGER,
  EmployeeID INTEGER,
  OrderDate TEXT,
  FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY(EmployeeID) REFERENCES Store_Employees(EmployeeID)
);

CREATE TABLE IF NOT EXISTS OrderDetails (
  OrderDetailID INTEGER PRIMARY KEY,
  OrderID INTEGER,
  ProductID INTEGER,
  Quantity INTEGER,
  PriceEach REAL,
  TotalPrice REAL,
  FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
  FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);
