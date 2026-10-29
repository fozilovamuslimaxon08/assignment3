photos = ["lake", "forest", "bridge", "sunset", "beach", "garden"]
a=int(input("Enter the first photo number: "))
b=int(input("Enter the last photo number: "))

new=photos[a-1: b]
d=str(input("Enter the first photo name: "))
c=str(input("Enter the last photo name: "))
new[0]=d
new.append(c)

print(f"Original photos: {photos}")
print(f"Album: {new}")
print(f"Preview: {new[:3]}")
print(f"Remaining: {new[3:]}")