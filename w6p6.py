def first_tool_position(tools, wanted):
    for tool in range(len(tools)):
        if tools[tool]==wanted:
            return tool
    return -1

def all_tool_positions(tools, wanted):
    positions=[]
    for tool in range(len(tools)):
        if tools[tool]==wanted:
            positions.append(tool)
    return positions

tools = ["hammer", "drill", "saw", "drill", "wrench"]

for tool_name in ["drill", "tape"]:
  a=first_tool_position(tools, tool_name)
  b=all_tool_positions(tools, tool_name)
  print(f"{tool_name}: first position={a}, all positions{b}")

