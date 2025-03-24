class User:
    def __init__(self, username):
        self.username = username
        self.goals = {'water_goal': 0, 'electricity_goal': 0}
        self.consumption = {'water': 0, 'electricity': 0}

    def set_water_goal(self, goal):
        self.goals['water_goal'] = goal

    def set_electricity_goal(self, goal):
        self.goals['electricity_goal'] = goal

    def update_water_consumption(self, amount):
        self.consumption['water'] += amount

    def update_electricity_consumption(self, amount):
        self.consumption['electricity'] += amount

    def check_goal_completion(self):
        if self.consumption['water'] <= self.goals['water_goal'] and self.consumption['electricity'] <= self.goals['electricity_goal']:
            return True
        else:
            return False

# Example usage:
user1 = User("john_doe")
user1.set_water_goal(100)
user1.set_electricity_goal(500)
user1.update_water_consumption(80)
user1.update_electricity_consumption(450)

if user1.check_goal_completion():
    print(f"{user1.username}'s consumption goals are met!")
else:
    print(f"{user1.username}'s consumption goals are not met.")
