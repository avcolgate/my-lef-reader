import re
from classes import *


path = 'src/sky130_sram_1kbyte_1rw1r_8x1024_8.lef'

macro_list = []

with open(file=path, mode='rt') as file:
    lines = file.read().split('\n')
    lines = list(filter(None, lines))  # deleting '' lines
    section_macro = False
    section_pin = False
    section_port = False
    for line in lines:
        # print(line)
        if 'MACRO' in line:
            macro = Macro()
            macro_name = line.replace('MACRO ', '')
            macro.name = macro_name
            print(macro.name)

            section_macro = True
            continue

        if section_macro and 'CLASS' in line:
            class_type = line.replace('CLASS ', '')
            class_type = re.sub("[;| ]", "", class_type)
            macro.class_type = class_type
            continue

        if section_macro and 'SIZE' in line:
            size = line.replace('SIZE ', '')
            size = re.sub("[;| ]", "", size)
            size = size.split('BY')
            macro.size = size
            continue

        if section_macro and 'SYMMETRY' in line:
            symmetry = line.replace('SYMMETRY ', '')
            symmetry = re.sub("[;]", "", symmetry)
            macro.symmetry = symmetry.strip()
            continue

        if section_macro and 'PIN' in line:
            pin = Pin()
            pin_name = line.replace('PIN ', '')
            pin_name = re.sub("[;| ]", "", pin_name)
            pin.name = pin_name

            section_pin = True
            continue

        if section_macro and section_pin and 'DIRECTION' in line:
            direction = line.replace('DIRECTION ', '')
            direction = re.sub("[;| ]", "", direction)
            pin.direction = direction
            continue

        if section_macro and section_pin and 'PORT' in line:

            section_port = True
            continue

        if section_macro and section_pin and section_port and 'LAYER' in line:
            layer = line.replace('LAYER ', '')
            layer = re.sub("[;| ]", "", layer)
            pin.layers.append(layer)
            continue    

        if section_macro and 'END' in line and macro_name in line:
            macro_list.append(macro)

            section_macro = False
            continue

        if section_pin and 'END' in line and pin_name in line:
            macro.pins.append(pin)

            section_pin = False
            continue

        if section_port and 'END' in line:
            
            section_port = False
            continue

    del lines
    print('end')