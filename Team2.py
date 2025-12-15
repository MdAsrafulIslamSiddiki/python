number_of_input=int(input("Enter the number of Members "))
team_members=[]
for i in range(1,number_of_input + 1):
  list_element=input()
  if list_element=="Borhan":
      team_members.append(list_element)
      print("Team accepted.")
      continue
  if list_element=="Imran":
      team_members.append(list_element)
      print("Team not accepted.")
      break
    
  team_members.append(list_element)
print("The team members are: ",team_members)
