#!/usr/bin/env python3
"""mapperT.py"""

import sys
import json

# input comes from STDIN (standard input) load into json
data = json.load(sys.stdin)
print (data["text"])
