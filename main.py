import re
from classes import *


path = 'src/lib_sample.lef'

macro_list = []

with open(file=path, mode='rt') as file:
    lines = file.read().split('\n')
    lines = list(filter(None, lines))  # deleting '' lines
    section_macro = False

    for line in lines:
        # print(line)
        if 'MACRO' in line:
            macro = Macro()
            macro_name = line.replace('MACRO ', '')
            macro.name = macro_name
            print(macro.name)

            section_macro = True
            continue

        if section_macro and 'SIZE' in line:
            size = line.replace('SIZE ', '')
            size = re.sub("[;| ]", "", size)
            size = size.split('BY')
            macro.size = size
            continue

        if section_macro and 'END' in line and macro_name in line:
            macro_list.append(macro)

            section_macro = False
            continue

    del lines

    area = float(macro_list[0].size[0]) * float(macro_list[0].size[1])

    print(area)

    print('end')