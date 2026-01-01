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
  #ask user for expense amount
  amount = float(input("Enter Amount: "))
  #ask user for expense category
  category = input("Enter Category: ")
  #ask user for date (example : 2025-01-01)
  date = input("Enter Date (YYYY-MM-DD): ")
  #ask user for any short note
  note = input("Enter note: ")

  #SQL query to insert data into expenses table
  insert query = """
  INSERT INTO EXPENSES (amount , category , date , note)
  VALUES (?,?,?,?)
  """

  #Execute the SQL query with user data 
  cursor.execute(insert_query, (amount, category, date, note))

  #save changes to database
  connection.commit()

  print("Expense Added Successfully.")  

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


def view_expenses():
    # SQL query to read all expense records
    cursor.execute("SELECT * FROM expenses")

    # Fetch all rows returned by query
    expenses = cursor.fetchall()

    # If database is empty
    if not expenses:
        print("No expenses found.")
        return

    # Print column headers
    print("\nID | Amount | Category | Date | Note")
    print("-" * 40)

    # Loop through each row (tuple)
    for expense in expenses:
        expense_id = expense[0]
        amount = expense[1]
        category = expense[2]
        date = expense[3]
        note = expense[4]

        print(f"{expense_id} | {amount} | {category} | {date} | {note}")


def total_expense():
    # SQL query to calculate total amount spent
    cursor.execute("SELECT SUM(amount) FROM expenses")

    # Fetch result (it returns one row)
    result = cursor.fetchone()

    # result is a tuple like (total_amount,)
    total = result[0]

    # If no expenses exist
    if total is None:
        print("No expenses found.")
    else:
        print(f"Total expense is: {total}")

def category_wise_expense():
    # Calculate total expense per category
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    results = cursor.fetchall()

    if not results:
        print("No expenses found.")
        return

    print("\nCategory | Total Amount")
    print("-" * 30)

    for row in results:
        print(f"{row[0]} | {row[1]}")
