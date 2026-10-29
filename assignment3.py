def replace_value(values, index, new_value):
    for i in range(len(values)):
        if i==index:
            values[i]=new_value
            break
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i]==target:
            return i
        
    return -1
def summarize(values):
    stats_record=(min(values), max(values), sum(values))
    return stats_record

days=int(input("Enter the number of days: "))
original=[]
for day in range(1, days+1):
    dayy=int(input("Enter sleep time in hours: "))
    original.append(dayy)

updated=original[:]

index=int(input("Enter the index to correct: "))
new_time=int(input("Enter the new sleep time: "))
replace_value(updated, index, new_time)

target=int(input("Enter the sleep time to search for: "))

rindex=find_first(updated, target)
times=updated.count(target)

stats_method=summarize(updated)
minimum, maximum, total=stats_method
sorted_list=sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum sleep time: {minimum} hours")
print(f"Maximum sleep time: {maximum} hours")
print(f"Total sleep time: {total} hours")
if rindex==-1:
 print("Target not found")
else:
 print(f"First matching index: {rindex}")
print(f"Matching values: {times}")




        
        