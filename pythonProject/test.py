from datetime import datetime
def gen_date():
    return datetime.today().strftime("%Y-%m-%d")
def print_name():
    today = gen_date()
    print(f"Hello , from functional programming {today}")
print_name()  # executing a function / function call....
class String:
    def __init__(self, value):
        self.value = value
    def upper(self):
        # self parameter : a pointer to the current object in execution
        # logical output
        self.value = self.value.upper()