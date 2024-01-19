#!/usr/bin/env python
# coding: utf-8

# In[1]:


ef_file = open("external_first.gcode", "r")
ef = ef_file.read()
ef_split = ef.splitlines()


# In[2]:


ef_lines = []
for index, line in enumerate(ef_split):
    if (";LAYER_CHANGE" in line):
        ef_lines.append(index)
ef_split_last_line = len(ef_split)
ef_lines_last_layer_change=ef_lines[len(ef_lines) - 1]
ef_lines_first_layer_change=ef_lines[0]


# In[3]:


ef_blocks = []
for i in range(len(ef_lines)):
    new_block = []
    if (i + 1 < len(ef_lines)):
        for j in range(ef_lines[i],ef_lines[i+1]):
            new_block.append(ef_split[j])
    else:
        for j in range(ef_lines_last_layer_change,ef_split_last_line - 1):
            new_block.append(ef_split[j])
    ef_blocks.append(new_block)


# In[4]:


#################################


# In[5]:


if_file = open("internal_first.gcode", "r")
iff = if_file.read()
if_split = iff.splitlines()


# In[6]:


if_lines = []
for index, line in enumerate(if_split):
    if (";LAYER_CHANGE" in line):
        if_lines.append(index)
if_split_last_line = len(if_split)
if_lines_last_layer_change=if_lines[len(if_lines) - 1]


# In[7]:


if_blocks = []
for i in range(len(if_lines)):
    new_block = []
    if (i + 1 < len(if_lines)):
        for j in range(if_lines[i],if_lines[i+1]):
            new_block.append(if_split[j])
    else:
        for j in range(if_lines_last_layer_change,if_split_last_line - 1):
            new_block.append(if_split[j])
    if_blocks.append(new_block)


# In[8]:


merged_blocks = []


# In[9]:


for i in range(len(ef_blocks)):
    #print (ef_blocks[i])
    if (";TYPE:Overhang perimeter" in ef_blocks[i]):
        merged_blocks.append(if_blocks[i])
    else:
        merged_blocks.append(ef_blocks[i])


# In[10]:


out_file = open("merged.gcode", "w")


# In[11]:


for i in range(0,ef_lines_first_layer_change):
    out_file.write(if_split[i] + "\n" )


# In[12]:


for block in merged_blocks:
    for line in block:
        out_file.write(line + "\n")


# In[13]:


out_file.close()


# In[ ]:




