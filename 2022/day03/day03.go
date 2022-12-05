package main

import (
	"bufio"
	"fmt"
	"os"
)

func decodeCompartment(compartment string) [52]bool {
	var ret [52]bool

	for _, c := range compartment {
		if c >= 'a' && c <= 'z' {
			ret[c-'a'] = true
		} else if c >= 'A' && c <= 'Z' {
			ret[c-'A'+26] = true
		}
	}

	return ret
}

func main() {
	var scanner = bufio.NewScanner(os.Stdin)
	var line [3]string
	var total int = 0
	var total2 int = 0
	var linenum = 0

	for scanner.Scan() {
		var compartment1 string
		var compartment2 string

		line[2] = line[1]
		line[1] = line[0]
		line[0] = scanner.Text()
		linenum++

		compartment1 = line[0][:(len(line[0]) / 2)]
		compartment2 = line[0][len(line[0])/2:]

		var com1 = decodeCompartment(compartment1)
		var com2 = decodeCompartment(compartment2)

		var i int
		for i = 0; i < 52; i++ {
			if com1[i] && com2[i] {
				var priority = i + 1
				total += priority
			}
		}

		if linenum%3 == 0 {
			var rucksack1 = decodeCompartment(line[0])
			var rucksack2 = decodeCompartment(line[1])
			var rucksack3 = decodeCompartment(line[2])

			for i = 0; i < 52; i++ {
				if rucksack1[i] && rucksack2[i] && rucksack3[i] {
					total2 += (i + 1)
				}
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

	fmt.Printf("Total of priorities (part 1): %d\n", total)
	fmt.Printf("Total of priorities (part 2): %d\n", total2)
}
