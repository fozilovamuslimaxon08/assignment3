quantities = [200, 100, 50]

factor1=int(input("Enter the factor: "))
factor2=int(input("Enter the factor: "))
def scale_in_place(quantities, factor):
  for index in range(len(quantities)):
        quantities[index] = quantities[index]*factor
  
    
def scaled_copy(quantities, factor):
    new2=quantities[:]
    scale_in_place(new2, factor)
    return new2
  

first = scaled_copy(quantities, factor1)
second = scaled_copy(quantities, factor2)


print(f"Original quantities: {quantities}")
print(f"First version: {first}")
print(f"Second version: {second}")