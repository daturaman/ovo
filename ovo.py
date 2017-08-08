#!/usr/bin/python
import json
x = json.loads(open('prices.json').read())
print(isinstance(x, dict))
