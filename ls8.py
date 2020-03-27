"""Main"""

import sys
import os
from cpu import CPU

if len(sys.argv) != 2:
    print("ERR: No file given:\t python ls8.py examples/file_name")
    
cpu = CPU()
cpu.load(file_name)
cpu.run()