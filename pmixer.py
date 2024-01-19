import sys

def create_blocks(splitted_gcode):
    
    lines = []
    blocks = []

    for index, line in enumerate(splitted_gcode):
        if (";LAYER_CHANGE" in line):
            lines.append(index)
        
    last_line = len(splitted_gcode)
    last_layer_change = lines[len(lines) - 1]
    first_layer_change = lines[0]
    
    for i in range(len(lines)):
        new_block = []
        if (i + 1 < len(lines)):
            for j in range(lines[i],lines[i+1]):
                new_block.append(splitted_gcode[j])
        else:
            for j in range(last_layer_change,last_line - 1):
                new_block.append(splitted_gcode[j])
        blocks.append(new_block)

    return (blocks, first_layer_change, last_line, last_layer_change)

ep_filename = sys.argv[1] #"external_first.gcode"
ip_filename = sys.argv[2] #"internal_first.gcode"
out_filename = sys.argv[3] #"merged.gcode"

ep = open(ep_filename, "r").read().splitlines()
ip = open(ip_filename, "r").read().splitlines()

ep_blocks, ep_first_layer_change, ep_last_line, ep_last_layer_change = create_blocks(ep)
ip_blocks, ip_first_layer_change, ip_last_line, ip_last_layer_change = create_blocks(ip)

merged_blocks = []
for i in range(len(ep_blocks)):
    if (";TYPE:Overhang perimeter" in ep_blocks[i]):
        merged_blocks.append(ip_blocks[i])
    else:
        merged_blocks.append(ep_blocks[i])

out_file = open(out_filename, "w")
for i in range(0,ep_first_layer_change):
    out_file.write(ep[i] + "\n")
for block in merged_blocks:
    for line in block:
        out_file.write(line + "\n")
out_file.close()
