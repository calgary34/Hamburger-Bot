import json
import random
import bot_data
def create_account(id):    
    bank=get_data()
    have_id = str(id) in bank
    if not have_id:
        print('Account created with id '+str(id))
        save({
            "user": str(id),
            "wallet": 0,
            "bank": 0,
            "job": None,
        })
def cleanup(data):
  data = data.replace('\\\"', '\"')
  data = data.replace('\\n', '\n')
  data = data.replace('{,\"', '{\"')
  if data[0]=='\"':
    data=data[1:]
  if data[-1]=='\"':
    data=data[:-1]
  numbers=[1,2,3,4,5,6,7,8,9,0]
  for n in numbers:
    data=data.replace(f',{str(n)}',f',\"{str(n)}')
    data=data.replace(f'{str(n)}:',f'{str(n)}\":')
  with open('economy.json', 'w') as file:
    file.write(data)
  return data
def get_data():
    with open('economy.json', 'r') as file :
      filedata = file.read()
    filedata=cleanup(filedata)
    return json.loads(filedata)
def save(account:dict):
  print("The account saved")
  try:
    filedata=get_data()
    filedata=cleanup(json.dumps(filedata))
    myjson=open('economy.json')
    mynewjson=myjson.read()[:-1]+','+account['user']+':'+json.dumps(account)+'}'
    with open('economy.json', 'w') as outfile:
      json.dump(mynewjson, outfile)  
    myjson.close()
  except Exception as e:
    print(type(e))
    print(e)
  
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
  
def subtract_wallet(econ:Economy,amount):    
    if amount>get_data()[econ.account.user]['wallet']:
      raise EconomyError("You don't have enough money in your wallet.")
    else:
      get_data()[econ.account.user]['wallet']-=amount
def subtract_bank(econ,amount):
    if amount>get_data()[econ.account.user]['bank']:
      raise EconomyError("You don't have enough money in the bank.")
    else:
      get_data()[econ.account.user]['bank']-=amount

def work(user):
  user=str(user)
  myecon=get_data()[user]
  job=myecon['job']
  for x in bot_data.jobs:
    if x==job:
      print(job)
      print(bot_data.job_data[job])
      myecon['wallet']+=bot_data.job_data[job]
  save(myecon)
  return bot_data.job_data[job]
  '''except Exception as e:
    print(type(e))
    print(e)
    create_account(str(user))
    print(get_data()[user]['job'])
    return "0 dollars because you don't have a job haha"'''
  
def applyjob(econ,job):
  if job in bot_data.jobs:
    econ.account['job']=job
    save(econ.account)
  else:
    raise EconomyError("That job is not possible")
def deposit(econ,amount):
      try:
        econ.subtract_wallet(amount)
        econ.account['bank']+=amount
        save(econ.account)
      except EconomyError:
        raise EconomyError("You don't have enough money in your wallet!")
def withdraw(econ,amount):
      try:
        econ.account+=amount
        econ.subtract_bank(amount)
        save(econ.account)
      except EconomyError:
        raise EconomyError("You don't have enough money in the bank!")
def lottery(econ):
    try:
      x1=random.randint(1,10)
      x2=random.randint(1,100)
      econ.subtract_wallet(10)
      if x1==random.randint(1,10):
        econ.account+=100
      if x2==random.randint(1,100):
        econ.account+=10000
      save(econ.account)
    except EconomyError:
      raise EconomyError("You don't have enough money in your wallet to buy a lottery ticket.")
def getAccount(user):
  user=str(user)
  raw=get_data()
  acc=raw[user]
  bank=acc['bank']
  wallet=acc['wallet']
  job=acc['job']
  return Economy(user,wallet,bank,job)

