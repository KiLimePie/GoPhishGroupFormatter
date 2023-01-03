f=open("list.csv", "r")

try:
  while True:
    
    contents=f.readline().strip().split(",")
    
    with open("names.csv", "a+") as b:
      b.write(f"{contents[3]},{contents[2]},{contents[4]},{contents[1]}\n")
      
    if contents=="":
      break
  f.close()
  b.close()
  
except:
  print("The script has completed. Check file for results.")
