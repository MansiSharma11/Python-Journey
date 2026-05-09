class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate spending per category (withdrawals only)
    spent = []
    for cat in categories:
        s = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(s)

    total_spent = sum(spent)
    # Calculate percentages rounded down to nearest 10
    percentages = [(s / total_spent * 100) // 10 * 10 for s in spent]

    # Build the chart
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{str(i).rjust(3)}| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    # Separator line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical names
    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names)
    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += f"{name[i]}  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res
# Create categories
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Add some data
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
clothing.deposit(500, "initial deposit")
food.transfer(50, clothing)
auto.deposit(1000, "initial deposit")
auto.withdraw(150, "fuel and oil")

# Print the ledger for one category
print(food)

# Print the spend chart
print(create_spend_chart([food, clothing, auto]))
