"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, **kwargs):
        self.name = name
        self.pay_details = kwargs
        print(self.pay_details)

    def get_pay(self):
        pay = 0
        if ('salary' in self.pay_details):
            pay += self.pay_details["salary"]
        elif('hours' in self.pay_details):
            pay += (self.pay_details["hours"] *
                    self.pay_details["pay_per_hour"])
        if ('contracts' in self.pay_details):
            pay += (self.pay_details["contracts"] *
                    self.pay_details["pay_per_contract"])
        elif ('bonus' in self.pay_details):
            pay += self.pay_details["bonus"]
        return pay

    def __str__(self):
        returnString = self.name + " works on a"
        if ('salary' in self.pay_details):
            returnString += " monthly salary of " + \
                str(self.pay_details['salary'])
        elif('hours' in self.pay_details):
            returnString += " contract of " + \
                str(self.pay_details['hours']) + " hours at " + \
                str(self.pay_details['pay_per_hour'])+"/hour"
        if ('contracts' in self.pay_details):
            returnString += " and receives a commission for " + \
                str(self.pay_details['contracts'])+" contract(s) at " + \
                str(self.pay_details['pay_per_contract'])+"/contract"
        elif ('bonus' in self.pay_details):
            returnString += " and receives a bonus commission of " + \
                str(self.pay_details['bonus'])
        returnString += ".  Their total pay is "+str(self.get_pay())+"."
        return returnString


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, pay_per_hour=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contracts=4, pay_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, pay_per_hour=25,
               contracts=3, pay_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, pay_per_hour=30, bonus=600)
