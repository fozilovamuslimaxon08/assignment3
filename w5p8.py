route = ["forward", "left", "forward"]
a=int(input("Enter the position: "))
b=str(input("Enter the insruction: "))
def make_route(route, position, instruction):
    copy=route[:]
    copy[position-1]=instruction
    s="stop"
    copy.append(s)
    return copy
def reset_route():
    copyy=route[:]
    for i in range(0,len(copyy)+1):
        copyy.pop(i)
        return copyy
revised=make_route(route, a, b)
after=reset_route()
print(f"Original route: {route}")
print(f"Revised route: {revised}")
print(f"After reset: {after}")