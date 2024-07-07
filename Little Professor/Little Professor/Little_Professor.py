import random


def main():
  level = get_level()
  score = game(level)
  print(f"Score: {score}")
  


def get_level():
   x=0
   while x==0:
     level = input("Level: ")
     if level not in ["1","2","3"]:
       continue
     return level
      
    
def generate_integer(n):
  a = random.randint(10**n-1 , (10**n)-1)
  b = random.randint(10**n-1 , (10**n)-1)
  return a,b

def roundd(a,b):
  deneme = 3
  while deneme >0:
    try:
      cevap = int(input(f"{a} + {b} = "))
      if cevap == a+b:
        return True
      else:
        deneme-=1
        print("EEE")
    except:
      deneme-=1
      print("EEE")
    print(f"{a} + {b} = {a+b}")
    return False
  

def game(n):
  _round = 1
  score = 0
  while _round<=10:
    x,y = generate_integer(n)
    k = roundd(x,y)
    if k==True:
      score+=1
      _round+=1
  return score    
      
if __name__ == "__main__":
    main()