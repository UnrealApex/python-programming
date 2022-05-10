class Account:
    def __init__(self, id = 0, balance = 100, annual_interest_rate = 0):
        self.__id = id
        self.__balance = balance
        self.annual_interest_rate = annual_interest_rate
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id
        
    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate
    
    def set_annual_interest_rate(self, new_annual_interest_rate):
        self.__annual_interest_rate = new_annual_interest_rate

    def get_monthly_interest(self):
        self.__balance * (annual_interest_rate / 0.12)
    
    def get_monthly_interest_rate(self):
        pass
    
    def withdraw(self):
        pass

    def deposit(self):
        pass
