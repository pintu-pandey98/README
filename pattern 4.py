for i in range(1, 8):
    if(i<=4):
      for j in range(1, i+1):
        print("*", end="")
    else:
      for j in range(i, 8):
        print("*", end="") 
    print()
    