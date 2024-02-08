from random import randint
import time
ai1=[25,25,25,25]
ai2=[25,25,25,25]
ai3=[25,25,25,25]
ai4=[25,25,25,25]
lastOption1=-1
lastOption2=-1
lastOption3=-1
lastOption4=-1
runs=5000
guess=0
yn=0
smallChange=5
bigChange=10
wait=0
while runs>0:
  
  guess=randint(1,4)
  
  if guess==1:
    guess=randint(1,100)
    if guess<=ai1[0]:
      print("1")
      yn=1
      guess=0
    elif guess<=ai1[0]+ai1[1]:
      print("2")
      yn=0
      guess=1
    elif guess<=ai1[0]+ai1[1]+ai1[2]:
      print("3")
      yn=0
      guess=2
    elif guess<=ai1[0]+ai1[1]+ai1[2]+ai1[3]:
      print("4")
      yn=0
      guess=3
    if ai1[0] or ai1[1] or ai1[2] or ai1[3]!=100:
      print("5")
      if lastOption1==-1:
        lastOption1=guess
        print("6")
      elif yn==1:
        print("7")
        if ai1[guess]<100:
          print("8")
          if lastOption1!=guess:
            print("9")
            if ai1[lastOption1]!=0:
              print("10")
              ai1[lastOption1]=ai1[lastOption1]-smallChange
              ai1[guess]=ai1[guess]+smallChange
          elif lastOption1==guess:
            print("11")
            while lastOption1==guess:
              print("12")
              lastOption1=randint(0,3)
              if ai1[lastOption1]==0:
                print("13")
                lastOption1=guess
            if ai1[lastOption1]>9:
              print("14")
              if ai1[guess]<91:
                print("15")
                ai1[lastOption1]=ai1[lastOption1]-bigChange
                ai1[guess]=ai1[guess]+bigChange
              else:
                print("16")
                if ai1[lastOption1]!=0:
                  print("17")
                  if ai1[guess]!=100:
                    print("18")
                    ai1[lastOption1]=ai1[lastOption1]-smallChange
                    ai1[guess]=ai1[guess]+smallChange
            else:
              print("19")
              if ai1[lastOption1]!=0:
                print("20")
                if ai1[guess]!=100:
                  print("21")
                  ai1[lastOption1]=ai1[lastOption1]-smallChange
                  ai1[guess]=ai1[guess]+smallChange
                
      elif yn==0:
        print("22")
        if ai1[guess]>0:
          print("23")
          if lastOption1!=guess:
            print("24")
            if ai1[lastOption1]!=100:
              print("25")
              ai1[lastOption1]=ai1[lastOption1]+smallChange
              ai1[guess]=ai1[guess]-smallChange
          elif lastOption1==guess:
            print("26")
            while lastOption1==guess:
              print("27")
              lastOption1=randint(0,3)
              if ai1[lastOption1]==0:
                print("28")
                lastOption1=guess
            if ai1[lastOption1]<91:
              print("29")
              if ai1[guess]>9:
                print("30")
                ai1[lastOption1]=ai1[lastOption1]+bigChange
                ai1[guess]=ai1[guess]-bigChange
              else:
                print("31")
                if ai1[lastOption1]!=100:
                  print("32")
                  if ai1[guess]!=0:
                    print("33")
                    ai1[lastOption1]=ai1[lastOption1]+smallChange
                    ai1[guess]=ai1[guess]-smallChange
            else:
              print("34")
              if ai1[lastOption1]!=100:
                print("35")
                if ai1[guess]!=0:
                  print("36")
                  ai1[lastOption1]=ai1[lastOption1]+smallChange
                  ai1[guess]=ai1[guess]-smallChange

  elif guess==2:
    guess=randint(1,100)
    if guess<=ai2[0]:
      print("1")
      yn=0
      guess=0
    elif guess<=ai2[0]+ai2[1]:
      print("2")
      yn=1
      guess=1
    elif guess<=ai2[0]+ai2[1]+ai2[2]:
      print("3")
      yn=0
      guess=2
    elif guess<=ai2[0]+ai2[1]+ai2[2]+ai2[3]:
      print("4")
      yn=0
      guess=3
    if ai2[0] or ai2[1] or ai2[2] or ai2[3]!=100:
      print("5")
      if lastOption2==-1:
        lastOption2=guess
        print("6")
      elif yn==1:
        print("7")
        if ai2[guess]<100:
          print("8")
          if lastOption2!=guess:
            print("9")
            if ai2[lastOption2]!=0:
              print("10")
              ai2[lastOption2]=ai2[lastOption2]-smallChange
              ai2[guess]=ai2[guess]+smallChange
          elif lastOption2==guess:
            print("11")
            while lastOption2==guess:
              print("12")
              lastOption2=randint(0,3)
              if ai2[lastOption2]==0:
                print("13")
                lastOption2=guess
            if ai2[lastOption2]>9:
              print("14")
              if ai2[guess]<91:
                print("15")
                ai2[lastOption2]=ai2[lastOption2]-bigChange
                ai2[guess]=ai2[guess]+bigChange
              else:
                print("16")
                if ai2[lastOption2]!=0:
                  print("17")
                  if ai2[guess]!=100:
                    print("18")
                    ai2[lastOption2]=ai2[lastOption2]-smallChange
                    ai2[guess]=ai2[guess]+smallChange
            else:
              print("19")
              if ai2[lastOption2]!=0:
                print("20")
                if ai2[guess]!=100:
                  print("21")
                  ai2[lastOption2]=ai2[lastOption2]-smallChange
                  ai2[guess]=ai2[guess]+smallChange
                
      elif yn==0:
        print("22")
        if ai2[guess]>0:
          print("23")
          if lastOption2!=guess:
            print("24")
            if ai2[lastOption2]!=100:
              print("25")
              ai2[lastOption2]=ai2[lastOption2]+smallChange
              ai2[guess]=ai2[guess]-smallChange
          elif lastOption2==guess:
            print("26")
            while lastOption2==guess:
              print("27")
              lastOption2=randint(0,3)
              if ai2[lastOption2]==0:
                print("28")
                lastOption2=guess
            if ai2[lastOption2]<91:
              print("29")
              if ai2[guess]>9:
                print("30")
                ai2[lastOption2]=ai2[lastOption2]+bigChange
                ai2[guess]=ai2[guess]-bigChange
              else:
                print("31")
                if ai2[lastOption2]!=100:
                  print("32")
                  if ai2[guess]!=0:
                    print("33")
                    ai2[lastOption2]=ai2[lastOption2]+smallChange
                    ai2[guess]=ai2[guess]-smallChange
            else:
              print("34")
              if ai2[lastOption2]!=100:
                print("35")
                if ai2[guess]!=0:
                  print("36")
                  ai2[lastOption2]=ai2[lastOption2]+smallChange
                  ai2[guess]=ai2[guess]-smallChange

  elif guess==3:
    guess=randint(1,100)
    if guess<=ai3[0]:
      print("1")
      yn=0
      guess=0
    elif guess<=ai3[0]+ai3[1]:
      print("2")
      yn=0
      guess=1
    elif guess<=ai3[0]+ai3[1]+ai3[2]:
      print("3")
      yn=1
      guess=2
    elif guess<=ai3[0]+ai3[1]+ai3[2]+ai3[3]:
      print("4")
      yn=0
      guess=3
    if ai3[0] or ai3[1] or ai3[2] or ai3[3]!=100:
      print("5")
      if lastOption3==-1:
        lastOption3=guess
        print("6")
      elif yn==1:
        print("7")
        if ai3[guess]<100:
          print("8")
          if lastOption3!=guess:
            print("9")
            if ai3[lastOption3]!=0:
              print("10")
              ai3[lastOption3]=ai3[lastOption3]-smallChange
              ai3[guess]=ai3[guess]+smallChange
          elif lastOption3==guess:
            print("11")
            while lastOption3==guess:
              print("12")
              lastOption3=randint(0,3)
              if ai3[lastOption3]==0:
                print("13")
                lastOption3=guess
            if ai3[lastOption3]>9:
              print("14")
              if ai3[guess]<91:
                print("15")
                ai3[lastOption3]=ai3[lastOption3]-bigChange
                ai3[guess]=ai3[guess]+bigChange
              else:
                print("16")
                if ai3[lastOption3]!=0:
                  print("17")
                  if ai3[guess]!=100:
                    print("18")
                    ai3[lastOption3]=ai3[lastOption3]-smallChange
                    ai3[guess]=ai3[guess]+smallChange
            else:
              print("19")
              if ai3[lastOption3]!=0:
                print("20")
                if ai3[guess]!=100:
                  print("21")
                  ai3[lastOption3]=ai3[lastOption3]-smallChange
                  ai3[guess]=ai3[guess]+smallChange
                
      elif yn==0:
        print("22")
        if ai3[guess]>0:
          print("23")
          if lastOption3!=guess:
            print("24")
            if ai3[lastOption3]!=100:
              print("25")
              ai3[lastOption3]=ai3[lastOption3]+smallChange
              ai3[guess]=ai3[guess]-smallChange
          elif lastOption3==guess:
            print("26")
            while lastOption3==guess:
              print("27")
              lastOption3=randint(0,3)
              if ai3[lastOption3]==0:
                print("28")
                lastOption3=guess
            if ai3[lastOption3]<91:
              print("29")
              if ai3[guess]>9:
                print("30")
                ai3[lastOption3]=ai3[lastOption3]+bigChange
                ai3[guess]=ai3[guess]-bigChange
              else:
                print("31")
                if ai3[lastOption3]!=100:
                  print("32")
                  if ai3[guess]!=0:
                    print("33")
                    ai3[lastOption3]=ai3[lastOption3]+smallChange
                    ai3[guess]=ai3[guess]-smallChange
            else:
              print("34")
              if ai3[lastOption3]!=100:
                print("35")
                if ai3[guess]!=0:
                  print("36")
                  ai3[lastOption3]=ai3[lastOption3]+smallChange
                  ai3[guess]=ai3[guess]-smallChange
                    
  elif guess==4:
    guess=randint(1,100)
    if guess<=ai4[0]:
      print("1")
      yn=0
      guess=0
    elif guess<=ai4[0]+ai4[1]:
      print("2")
      yn=0
      guess=1
    elif guess<=ai4[0]+ai4[1]+ai4[2]:
      print("3")
      yn=0
      guess=2
    elif guess<=ai4[0]+ai4[1]+ai4[2]+ai4[3]:
      print("4")
      yn=1
      guess=3
    if ai4[0] or ai4[1] or ai4[2] or ai4[3]!=100:
      print("5")
      if lastOption4==-1:
        lastOption4=guess
        print("6")
      elif yn==1:
        print("7")
        if ai4[guess]<100:
          print("8")
          if lastOption4!=guess:
            print("9")
            if ai4[lastOption4]!=0:
              print("10")
              ai4[lastOption4]=ai4[lastOption4]-smallChange
              ai4[guess]=ai4[guess]+smallChange
          elif lastOption4==guess:
            print("11")
            while lastOption4==guess:
              print("12")
              lastOption4=randint(0,3)
              if ai4[lastOption4]==0:
                print("13")
                lastOption4=guess
            if ai4[lastOption4]>9:
              print("14")
              if ai4[guess]<91:
                print("15")
                ai4[lastOption4]=ai4[lastOption4]-bigChange
                ai4[guess]=ai4[guess]+bigChange
              else:
                print("16")
                if ai4[lastOption4]!=0:
                  print("17")
                  if ai4[guess]!=100:
                    print("18")
                    ai4[lastOption4]=ai4[lastOption4]-smallChange
                    ai4[guess]=ai4[guess]+smallChange
            else:
              print("19")
              if ai4[lastOption4]!=0:
                print("20")
                if ai4[guess]!=100:
                  print("21")
                  ai4[lastOption4]=ai4[lastOption4]-smallChange
                  ai4[guess]=ai4[guess]+smallChange
                
      elif yn==0:
        print("22")
        if ai4[guess]>0:
          print("23")
          if lastOption4!=guess:
            print("24")
            if ai4[lastOption4]!=100:
              print("25")
              ai4[lastOption4]=ai4[lastOption4]+smallChange
              ai4[guess]=ai4[guess]-smallChange
          elif lastOption4==guess:
            print("26")
            while lastOption4==guess:
              print("27")
              lastOption4=randint(0,3)
              if ai4[lastOption4]==0:
                print("28")
                lastOption4=guess
            if ai4[lastOption4]<91:
              print("29")
              if ai4[guess]>9:
                print("30")
                ai4[lastOption4]=ai4[lastOption4]+bigChange
                ai4[guess]=ai4[guess]-bigChange
              else:
                print("31")
                if ai4[lastOption4]!=100:
                  print("32")
                  if ai4[guess]!=0:
                    print("33")
                    ai4[lastOption4]=ai4[lastOption4]+smallChange
                    ai4[guess]=ai4[guess]-smallChange
            else:
              print("34")
              if ai4[lastOption4]!=100:
                print("35")
                if ai4[guess]!=0:
                  print("36")
                  ai4[lastOption4]=ai4[lastOption4]+smallChange
                  ai4[guess]=ai4[guess]-smallChange
                  
  print(ai1[0]," ",ai1[1]," ",ai1[2]," ",ai1[3],"\n")   
  print(ai2[0]," ",ai2[1]," ",ai2[2]," ",ai2[3],"\n")  
  print(ai3[0]," ",ai3[1]," ",ai3[2]," ",ai3[3],"\n")  
  print(ai4[0]," ",ai4[1]," ",ai4[2]," ",ai4[3],"\n")  
  time.sleep(wait)
  
  runs-=1
print("\n\n\n",ai1[0]," ",ai1[1]," ",ai1[2]," ",ai1[3],"\n")   
print(ai2[0]," ",ai2[1]," ",ai2[2]," ",ai2[3],"\n")  
print(ai3[0]," ",ai3[1]," ",ai3[2]," ",ai3[3],"\n")  
print(ai4[0]," ",ai4[1]," ",ai4[2]," ",ai4[3],"\n\n\n\n\n\n\n")  