import json
import random
def get_data(self):
    with open('economy.json') as f:
      g=json.loads(f)
    return g
def save(account:dict):
  with open('economy.json', 'r') as file :
    filedata = file.read()
  filedata = filedata.replace('\\\"', '\"')

  with open('file.txt', 'w') as file:
    file.write(filedata)
  myjson=open('economy.json').read()[2:-2]
  mynewjson=myjson+','+account['user']+':'+json.dumps(account)+'}'
  with open('economy.json', 'w') as outfile:
    json.dump(mynewjson, outfile)
  
class EconomyError(Exception):
  pass
class Economy:	
  def __init__(self,user,wallet=0,bank=0,job=None):
    self.account={
      'user':user,
      'wallet':wallet,
      'bank':bank,
      'job':job,
    }
  
  def subtract_wallet(self,amount):    
    if amount>get_data()[self.account.user]['wallet']:
      raise EconomyError("You don't have enough money in your wallet.")
    else:
      get_data()[self.account.user]['wallet']-=amount
  def subtract_bank(self,amount):
    if amount>get_data()[self.account.user]['bank']:
      raise EconomyError("You don't have enough money in the bank.")
    else:
      get_data()[self.account.user]['bank']-=amount
  def work(self):
    job=get_data()[self.account.user]['job']
    money=get_data()[self.account.user]['money']
    if job=="McDonald's":
      money+=1
  
  def applyjob(self,job):
    self.account['job']=job
    save(self.account)
  def deposit(self,amount):
      try:
        self.subtract_wallet(amount)
        self.account['bank']+=amount
        save(self.account)
      except EconomyError:
        raise EconomyError("You don't have enough money in your wallet!")
  def withdraw(self,amount):
      try:
        self.account+=amount
        self.subtract_bank(amount)
        save(self.account)
      except EconomyError:
        raise EconomyError("You don't have enough money in the bank!")
  def lottery(self):
    try:
      x1=random.randint(1,10)
      x2=random.randint(1,100)
      self.subtract_wallet(10)
      if x1==random.randint(1,10):
        self.account+=100
      if x2==random.randint(1,100):
        self.account+=10000
      save(self.account)
    except EconomyError:
      raise EconomyError("You don't have enough money in your wallet to buy a lottery ticket.")
def getAccount(user):
  with open('economy.json') as f:
    raw = json.load(f)
  acc=raw[user]
  bank=acc['bank']
  wallet=acc['wallet']
  job=acc['job']
  return Economy(user,wallet,bank,job)



