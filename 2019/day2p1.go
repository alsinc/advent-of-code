package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	program := GetProgram()
	program[1] = 12
	program[2] = 2

	result := Run(program)
	fmt.Println(result[0])
}


func Run(memory []int) []int {
	ip := 0
	program := make([]int, len(memory))
	copy(program, memory)

	for program[ip] != 99 {	
		if program[ip] == 1 {
			res := program[program[ip + 1]] + program[program[ip + 2]]
			program[program[ip + 3]] = res
		} else if program[ip] == 2 {
			program[program[ip + 3]] = program[program[ip  +1]] * program[program[ip + 2]]
		}

		ip = ip + 4	
	}
	return program
}

func GetProgram() []int {
	var input string
	var program []int
	scanner := bufio.NewScanner(os.Stdin)

	onComma := func(data []byte, atEOF bool) (advance int, token []byte, err error) {
		for i := 0; i < len(data); i++ {
			if data[i] == ',' {
				return i + 1, data[:i], nil
			}
		}
		if !atEOF {
			return 0, nil, nil
		}
		// There is one final token to be delivered, which may be the empty string.
		// Returning bufio.ErrFinalToken here tells Scan there are no more tokens after this
		// but does not trigger an error to be returned from Scan itself.
		return 0, data, bufio.ErrFinalToken
	}

	scanner.Split(onComma)

	for	scanner.Scan() {
		input = strings.TrimRight(scanner.Text(), "\n")

		i, err := strconv.Atoi(input)
		if err == nil {
			program = append(program, i)
		}
	}

	return program
}
