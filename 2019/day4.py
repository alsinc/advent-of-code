#!/bin/env python

import re
import sys

regexs = {"(^|[^1])11($|[^1])", "(^|[^2])22($|[^2])", "(^|[^3])33($|[^3])",
          "(^|[^4])44($|[^4])", "(^|[^5])55($|[^5])", "(^|[^6])66($|[^6])",
          "(^|[^7])77($|[^7])", "(^|[^8])88($|[^8])", "(^|[^9])99($|[^9])"}

part1 = 0
part2 = 0

if len(sys.argv) != 2:
	print("Usage: %s lowvalue-highvalue"%sys.argv[0])
	sys.exit()

match = re.match("^([0-9]+)-([0-9]+)$", sys.argv[1])
if not match:
	print("arument error")
	sys.exit()

low = int(match.group(1))
high = int(match.group(2))

for a in range(10):
	for b in range(a, 10):
		for c in range(b, 10):
			for d in range(c, 10):
				for e in range(d, 10):
					for f in range(e, 10):
						if a == b or b == c or c == d or d == e or e == f:
							num = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
							if num > low and num < high:
								part1 += 1
								for rx in regexs:
									if re.search(rx, str(num)):
										part2 += 1
										break

print("Part 1: %d"%part1)
print("Part 2: %d"%part2)

