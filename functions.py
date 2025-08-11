from voter import voter
from candidates import candidates
def vote(voter_now:str , candid:int  , condid_list:list ,voter_list:set  ):
      if voter_now in voter : 
            if check_candid(candid):
                  while True:
                        print(f'you are doing vote with id {voter} to {get_namecandid(candid)} are you sure ?(y , n) ')
                        order = input(': ')
                        if order == 'n' or order =="no" or order == "No" or order == "NO":
                              break
                        if order == 'y' or order =="yes" or order == "Yes" or order == "YES":
                              voter_list.add((voter,candid))
                              print('success vote')
            else:
                  print('your candid not found!!!')
      else:
            print("you can't vote!!!!")


def get_namecandid(candid:int):
      for i in candidates:
            if i.get('id') == candid:
                  return i.get('name')
      return None

def check_candid(candid:int ):
      flag = False
      for i in candidates:
            id = i.get('id')
            if id == candid:
                  flag = True
      return flag
            