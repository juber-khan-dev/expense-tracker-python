import sqlite3
connection = sqlite3.connect("expense.db")
cursor = connection.cursor()
cursor.execute("""
CREATE A TABLE IF NOT EXIST expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT,
    note TEXT
)
""")
connection.commit()

def add_expense():
  # This function will take input and store expense in database 
  pass

def view_expenses():
  # This function will fetch and display all expenses
  pass

def total_expense():
  # This function will calculate total expense
  pass

while true:
  print("\n1. Add Expense")
  print("2. View Expenses")
  print("3. Total Expense")
  print("4. Exit")

  choice = input("Choose An Option: ")

  if choice == "1":
    add_expense()
  elif choice == "2":
    view_expenses()
  elif choice == "3":
    total_expense()
  elif choice == "4":
    break
  else:
    print("Invalid Choice")

connection.close()
