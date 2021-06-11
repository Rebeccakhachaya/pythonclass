from bank import MobileMoneyAccount

user = MobileMoneyAccount("Becky","757wqt7e9","Safaricom")
user2 = MobileMoneyAccount("Vero","555587","Safaricom")

print(user.deposit(5300))
print(user.buy_airtime(40,user2))
print(user.statement())