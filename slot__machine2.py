import random

things = [ "🍉" ,  "🍋" , "🍒"]



print("""
-------Welcome to the vending machine game-------
                   🍋 🍉 🍒
""")

i = 0


try:
  balance = int(input('enter your balance: '))
  
  
except ValueError:
  print(" you have an error enter a valid input")
  

  

  
while True:
 

  try:
    bet = int(input(' enter  your bet amount:'))
  
 
  
  
    if balance < bet or bet <= 0:
            
              print(" your balance is not enough for the  bet amount that you entered or maybe you entered negative or zero bet amount , you can't play! set your bet amount again")
                
              while True:
                
                
                try:
                    bet = int(input(' set  your bet amount:'))
                    
                except Exception:
                      print(" can not do any work ")
                      break
                    
                if bet <= balance and bet > 0:
                      break
  
  except (ValueError , NameError):
    print(" you have an error ")
    break             
  
  
  
  
  


  i+=1
  
  a = random.choice(things)
  b = random.choice(things)
  c = random.choice(things)
  


  
 
            
    
 
  if a == b == c :
      print(f"""{a} | {b} | {c} 
  Congratulations
  you win !!!          
  """)
    
      
      print()
      
      balance =  balance + bet
      print(f"""your balance after bet: {balance}$ 
  your bet count : {i}
            """)
      
      if balance == 0:
                print(" you don't have any money ")
                break
                
      else:
      
        q = input(" do you want to play again?(just  type y/n  hint: if you type y or anything else except no(n) game will continue ) ").lower()
          
        if q == "n":
            print(" ok have a nice day bye ")
            print(f" your balance : {balance} ")
            break
  
        
      
          
          

  else :
        print(f""" {a} | {b} | {c} 
    you lose
    """)
      
        balance = balance - bet
    
        
        print(f""" your balance after bet: {balance}$ 
    your bet count : {i}      
              """)
        
        if balance == 0:
          print(" you don't have any money ")
          break
        
          
        else:
          q = input(" do you want to play again?(just  type y/n  hint: if you type y or anything else except no(n) game will continue ) ").lower()
          

          if q == "n":
            print(" ok bye have a nice day ")
            print(f" your balance : {balance} ")
            break
        
