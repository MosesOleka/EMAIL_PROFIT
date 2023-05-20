import time
import schedule

initial_balance = float(input("Enter your initial balance: "))
profit_rate = 0.1  # 10% profit rate

def calculate_investment_balance():
    global initial_balance, profit_rate
    investment_balance = initial_balance + (initial_balance * profit_rate)
    profit = investment_balance * profit_rate
    initial_balance = investment_balance
    print(f"Investment balance for the next day is: {investment_balance: .2f}")
    print(f"Profit for the next day is: {profit: .2f}")

schedule.every().day.at("00:00").do(calculate_investment_balance)

calculate_investment_balance()

while True:
    schedule.run_pending()
    time.sleep(1)
