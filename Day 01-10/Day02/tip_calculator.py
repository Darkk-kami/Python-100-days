print("This is a bid calculator!\nFollow the prompts below to calculate each person\'s tip")

total_bill = float(input("what is the total bill?\n$"))

total_users = int(input("How many are splitting the bill?\n"))

tip = int(input("What is the percentage of Tip?\n%"))

print("calculating....")

tip_users = (total_bill/total_users) * (tip / 100 + 1)
ans = round(tip_users, 2)

print(f"Each person should pay: ${ans}")
