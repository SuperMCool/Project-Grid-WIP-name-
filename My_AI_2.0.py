from random import randint
import time
ac1=[25,25,25,25]
ac2=[25,25,25,25]
ac3=[25,25,25,25]
ac4=[25,25,25,25]
lastGuess=[0,0,0,0]
runs=30
action=0
event=0
percent=0
change=25
plus=0
minus=0
cancel=0
wait=0
min=1
max=4
user="0"
def calcChangeSame():
  global cancel
  global plus
  global minus
  if lastGuess[event-1]!=0:
    #print("1")
    if lastGuess[event-1]==1:
      #print("2")
      ac1[event-1]=ac1[event-1]-change
      minus=1
      if ac1[event-1]<0:
        cancel=1
    elif lastGuess[event-1]==2:
      #print("3")
      ac2[event-1]=ac2[event-1]-change
      minus=2
      if ac2[event-1]<0:
        cancel=1
    elif lastGuess[event-1]==3:
      #print("4")
      ac3[event-1]=ac3[event-1]-change
      minus=3
      if ac3[event-1]<0:
        cancel=1
    elif lastGuess[event-1]==4:
      #print("5")
      ac4[event-1]=ac4[event-1]-change
      minus=4
      if ac4[event-1]<0:
        cancel=1
    #print("6")
    if action==1:
      #print("7")
      ac1[event-1]=ac1[event-1]+change
      plus=1
      if ac1[event-1]>100:
        cancel=1
    elif action==2:
      #print("8")
      ac2[event-1]=ac2[event-1]+change
      plus=2
      if ac2[event-1]>100:
        cancel=1
    elif action==3:
      #print("9")
      ac3[event-1]=ac3[event-1]+change
      plus=3
      if ac3[event-1]>100:
        cancel=1
    elif action==4:
      #print("10")
      ac4[event-1]=ac4[event-1]+change
      plus=4
      if ac4[event-1]>100:
        cancel=1
    if cancel==1:
      if plus==1:
        ac1[event-1]=ac1[event-1]-change
      elif plus==2:
        ac2[event-1]=ac2[event-1]-change
      elif plus==3:
        ac3[event-1]=ac3[event-1]-change
      elif plus==4:
        ac4[event-1]=ac4[event-1]-change
      if minus==1:
        ac1[event-1]=ac1[event-1]+change
      elif minus==2:
        ac2[event-1]=ac2[event-1]+change
      elif minus==3:
        ac3[event-1]=ac3[event-1]+change
      elif minus==4:
        ac4[event-1]=ac4[event-1]+change
  #print("11")
  cancel=0
  lastGuess[event-1]=action
def calcChangeDif():
  global cancel
  global plus
  global minus
  if lastGuess[event-1]!=0:
    #print("12")
    if lastGuess[event-1]==1:
      #print("13")
      ac1[event-1]=ac1[event-1]+change
      plus=1
      if ac1[event-1]>100:
        cancel=1
    elif lastGuess[event-1]==2:
      #print("14")
      ac2[event-1]=ac2[event-1]+change
      plus=2
      if ac2[event-1]>100:
        cancel=1
    elif lastGuess[event-1]==3:
      #print("15")
      ac3[event-1]=ac3[event-1]+change
      plus=3
      if ac3[event-1]>100:
        cancel=1
    elif lastGuess[event-1]==4:
      #print("16")
      ac4[event-1]=ac4[event-1]+change
      plus=4
      if ac4[event-1]>100:
        cancel=1
    #print("17")
    if action==1:
      #print("18")
      ac1[event-1]=ac1[event-1]-change
      minus=1
      if ac1[event-1]<0:
        cancel=1
    elif action==2:
      #print("19")
      ac2[event-1]=ac2[event-1]-change
      minus=2
      if ac2[event-1]<0:
        cancel=1
    elif action==3:
      #print("20")
      ac3[event-1]=ac3[event-1]-change
      minus=3
      if ac3[event-1]<0:
        cancel=1
    elif action==4:
      #print("21")
      ac4[event-1]=ac4[event-1]-change
      minus=4
      if ac4[event-1]<0:
        cancel=1
    if cancel==1:
      if plus==1:
        ac1[event-1]=ac1[event-1]-change
      elif plus==2:
        ac2[event-1]=ac2[event-1]-change
      elif plus==3:
        ac3[event-1]=ac3[event-1]-change
      elif plus==4:
        ac4[event-1]=ac4[event-1]-change
      if minus==1:
        ac1[event-1]=ac1[event-1]+change
      elif minus==2:
        ac2[event-1]=ac2[event-1]+change
      elif minus==3:
        ac3[event-1]=ac3[event-1]+change
      elif minus==4:
        ac4[event-1]=ac4[event-1]+change
  #print("22")
  cancel=0
  lastGuess[event-1]=action
while True:
  if runs>0:
    event=randint(min,max)
  else:
    user=input("do you want an apple, orange, banana, or grape?\n")
    if user=="apple":
      event=1
    elif user=="orange":
      event=2
    elif user=="banana":
      event=3
    elif user=="grape":
      event=4
  percent=randint(1,100)
  if event == 1:
    print("I want an apple")
  elif event == 2:
    print("I want a orange")
  elif event == 3:
    print("I want a banana")
  else:
    print("I want a grape")
  #print(event,"\n",percent,"\n")
  if percent<=ac1[event-1]:
    #print("23")
    action=1
    print("Here's a apple")
  elif percent<=ac2[event-1]+ac1[event-1]:
    #print("24")
    action=2
    print("Here's a orange")
  elif percent<=ac3[event-1]+ac2[event-1]+ac1[event-1]:
    #print("25")
    action=3
    print("Here's a banana")
  elif percent<=ac4[event-1]+ac3[event-1]+ac2[event-1]+ac1[event-1]:
    #print("26")
    action=4
    print("Here's a grape")
  #print("27")
  #print( action, ", ", event, "\n")
  if event==action:
    #print("28")
    calcChangeSame()
  else:
    #print("29")
    calcChangeDif()
  runs=runs-1
  print("\n",ac1,"\n",ac2,"\n",ac3,"\n",ac4,"\n",lastGuess,"\n\n")
  time.sleep(wait)