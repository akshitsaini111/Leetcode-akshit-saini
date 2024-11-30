class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"

class Expense:
    def __init__(self, payer, amount, participants, split):
        """
        :param payer: User who paid the amount
        :param amount: Total expense amount
        :param participants: List of users sharing the expense
        :param split: Dictionary with {user: share_amount}
        """
        self.payer = payer
        self.amount = amount
        self.participants = participants
        self.split = split

class ExpenseManager:
    def __init__(self):
        self.users = {}
        self.expenses = []
        self.balances = {}

    def add_user(self, user_id, name):
        """Adds a new user to the system."""
        if user_id in self.users:
            print(f"User {user_id} already exists!")
        else:
            self.users[user_id] = User(user_id, name)
            self.balances[user_id] = {}

    def add_expense(self, payer_id, amount, participant_ids, split):
        """
        Adds an expense to the system.
        :param payer_id: ID of the user who paid
        :param amount: Total expense amount
        :param participant_ids: List of user IDs participating
        :param split: Dictionary with {user_id: share_amount}
        """
        if payer_id not in self.users:
            print("Payer not found!")
            return
        
        for uid in participant_ids:
            if uid not in self.users:
                print(f"Participant {uid} not found!")
                return
        
        # Add expense
        payer = self.users[payer_id]
        participants = [self.users[uid] for uid in participant_ids]
        expense = Expense(payer, amount, participants, split)
        self.expenses.append(expense)

        # Update balances
        for uid, share in split.items():
            if uid == payer_id:
                continue
            # Payer gets credited
            self.balances[payer_id][uid] = self.balances[payer_id].get(uid, 0) + share
            # Participants get debited
            self.balances[uid][payer_id] = self.balances[uid].get(payer_id, 0) - share

    def show_balances(self):
        """Displays all balances."""
        print("Balances:")
        for user_id, debts in self.balances.items():
            for debtor_id, amount in debts.items():
                if amount > 0:
                    print(f"{self.users[user_id].name} owes {self.users[debtor_id].name}: {amount:.2f}")

    def simplify_debts(self):
        """Simplifies the debt structure."""
        print("Simplifying debts...")
        # Implementation of debt simplification can use algorithms like min-cost flow,
        # but for simplicity, we are not implementing this here.
        pass

# Example usage
if __name__ == "__main__":
    manager = ExpenseManager()

    # Add users
    manager.add_user("u1", "Alice")
    manager.add_user("u2", "Bob")
    manager.add_user("u3", "Charlie")

    # Add expenses
    manager.add_expense("u1", 100, ["u1", "u2", "u3"], {"u1": 33.33, "u2": 33.33, "u3": 33.34})
    manager.add_expense("u2", 60, ["u2", "u3"], {"u2": 30, "u3": 30})

    # Show balances
    manager.show_balances()

    # Simplify debts (to be implemented)
    manager.simplify_debts()
