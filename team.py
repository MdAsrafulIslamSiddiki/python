number_of_input=int(input("Enter the number of Members "))
team_members=[]
for i in range(1,number_of_input + 1):
  list_element=input()
  team_members.append(list_element)
print("The team members are: ",team_members)

for i in team_members:
  if team_members=="Borhan":
    break
print("Team accepted.")