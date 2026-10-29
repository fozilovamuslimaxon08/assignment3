days=int(input("Enter the number of days: "))
heights=[]
for day in range(1,days+1):
    b=int(input(f"Day {day}: "))
    heights.append(b)

print(f"First height: {heights[0]}")
print(f"Last height: {heights[-1]}")
print(f"Change: {heights[-1]-heights[0]}")