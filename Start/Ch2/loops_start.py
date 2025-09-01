# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops

x = 0

# define a while loop
# while x < 5:
#   print(x)
#   x = x +1

# ans = input("Should I stop?")
# while ans != "yes":
#   print(ans)
#   ans = input("Should I stop?")

# define a for loop
days = ["M","T","W","Th","Fri"]
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
# for d in days:
#   if d == "W":
#     break
#   print(d)

# for d in days:
#   if d == "W":
#     continue
#   print(d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
  print(i,d)