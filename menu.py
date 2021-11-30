"""Provide user with a list of options."""

import runpy
import pyinputplus as pyip

options_map = {
    1: ["drill protocols and administrative distances", \
        "drill_protocols_and_admin_distances.py",],
    2: ["binary and decimal conversion", "binary_and_decimal_conversion.py",],
}

NUM_OPTIONS = len(options_map)

while True:
    print("\nplease select an option below or enter nothing to quit.")
    for number, options in options_map.items():
        print(f"{number}. {options[0]}")
    response = pyip.inputInt("> ", min=1, max=len(options_map), blank=True)
    if response != "":
        runpy.run_path(path_name=options_map[response][1])
    else:
        print("session complete")
        break
