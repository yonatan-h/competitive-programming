class Bank:
    
    def __has_enough(self, account, amount):
        balance = self.balances[account - 1]
        return balance >= amount
    
    def __exists(self, account):
        return account in range(1, len(self.balances)+1)
    
    def __init__(self, balances: List[int]):
        self.balances = balances
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:      
            
        if not (self.__exists(account1) and self.__exists(account2)):
            return False
        
        return self.withdraw(account1, money) and self.deposit(account2, money)

        

    def deposit(self, account: int, money: int) -> bool:
        if not self.__exists(account):
            return False
        
        self.balances[account-1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.__exists(account):
            return False
        
        if not self.__has_enough(account, money):
            return False
        
        self.balances[account-1] -= money
        return True
        
            
        
#3sub
#30min
