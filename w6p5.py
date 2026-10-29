def prepare_boards(lengths, needed):
    copy=sorted(lengths)
    selected=copy[0:needed]
    if needed>len(lengths)+1:
        needed=len(lengths)+1
    return selected
lengths = [60, 20, 50, 20, 35]
needed = 3

a=prepare_boards(lengths, needed)
print(f"Original: {lengths}")
print(f"Sorted: {sorted(lengths)}")
print(f"Selected: {a}")
print(f"Total: {sum(a)}")