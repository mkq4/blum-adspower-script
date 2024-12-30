class Account:
    def __init__(self, tikets: int = 0, blum_balance: int = 0, meme_balance: int = 0, checkin_days: int = 0, account_number: int = 0):
        self.tikets = tikets
        self.blum_balance = blum_balance
        self.meme_balance = meme_balance
        self.checkin_days = checkin_days
        self.account_number = account_number
        
    def __str__(self):
        return f"""
                Account {self.account_number}\n
                Blum balance = {self.blum_balance} | Meme balance = {self.meme_balance} | check in = {self.checkin_days} days | tikets = {self.tikets}
                """
                
def read_accounts(): #читаем акки
    with open('accounts.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def rewrite_accounts(accounts): #перезаписываем акки
    with open('accounts.txt', 'w') as file:
        for account in accounts:
            file.write(f"{account}\n")
            
def get_numbers(text):
    result = ''
    for i in range(len(text)):
        if(text[i] != '-') and (text[i] != ' '):
            result += text[i]
        else:
            return result