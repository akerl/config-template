#!/usr/bin/env python

import os
import sys
import jinja2

if len(sys.argv) != 3:
    print("Please provide source template and desination file paths")
    sys.exit(1)

source = sys.argv[1]
target = sys.argv[2]

with open(source, 'r') as handle:
    template = jinja2.Template(handle.read())

with open(target, 'w') as handle:
    handle.write(template.render(env=os.environ))

