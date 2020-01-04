package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: %s filename\n", os.Args[0])
		os.Exit(0)
	}
	program := getProgram(os.Args[1])
	run(program)
}

func decodeOpCode(value int) (int, []int) {
	var ret []int
	var opCode = value % 100

	value = value / 100
	for i:=0 ; i < 4; i++ {
		ret = append(ret, value % 10)
		value = value / 10
	}

	return opCode, ret
}

func read(memory []int, parameterMode int, parameter int, relativeBase int) int {
	if parameterMode == 0 {
		return memory[parameter]
	} else if parameterMode == 1 {
		return parameter
	} else if parameterMode == 2 {
		return memory[relativeBase + parameter]
	} else {
		log.Fatal("Unknown parameterMode")
	}
	return 0
}

func write(memory []int, parameterMode int, parameter int, relativeBase int, value int) {
	if parameterMode == 0 {
		memory[parameter] = value
	} else if parameterMode == 1 {
		log.Fatal("Mode 1 not alowed for Write")
	} else if parameterMode == 2 {
		memory[relativeBase + parameter] = value
	} else {
		log.Fatal("Unknown parameterMode")
	}
}

func run(memory []int) []int {
	ip := 0
	rb := 0
	var opcode int
	var parameterModes []int

	program := make([]int, 64*1024*1024)

	copy(program, memory)

	for program[ip] != 99 {
		opcode, parameterModes = decodeOpCode(program[ip])

		switch opcode {
		case 1: //add
			res := read(program, parameterModes[0], program[ip + 1], rb)
			res = res + read(program, parameterModes[1], program[ip + 2], rb)
			write(program, parameterModes[2], program[ip + 3], rb, res)
			ip = ip + 4
		case 2: //multiply
			res := read(program, parameterModes[0], program[ip + 1], rb)
			res = res * read(program, parameterModes[1], program[ip + 2], rb)
			write(program, parameterModes[2], program[ip + 3], rb, res)
			ip = ip + 4
		case 3: //read int
			var input int
			fmt.Scanln(&input)
			write(program, parameterModes[0], program[ip + 1], rb, input)
			ip = ip + 2
		case 4: //print int
			val := read(program, parameterModes[0], program[ip + 1], rb)
			fmt.Println(val)
			ip = ip + 2
		case 5: //jump-if-true
			val := read(program, parameterModes[0], program[ip + 1], rb)
			if val != 0 {
				ip = read(program, parameterModes[1], program[ip + 2], rb)
			} else {
				ip = ip + 3
			}
		case 6: //jump-if-false
			val := read(program, parameterModes[0], program[ip + 1], rb)
			if val == 0 {
				ip = read(program, parameterModes[1], program[ip + 2], rb)
			} else {
				ip = ip + 3
			}
		case 7: //less than
			val1 := read(program, parameterModes[0], program[ip + 1], rb)
			val2 := read(program, parameterModes[1], program[ip + 2], rb)
			if val1 < val2 {
				write(program, parameterModes[2], program[ip + 3], rb, 1)
			} else {
				write(program, parameterModes[2], program[ip + 3], rb, 0)
			}

			ip = ip + 4
		case 8: //equals
			val1 := read(program, parameterModes[0], program[ip + 1], rb)
			val2 := read(program, parameterModes[1], program[ip + 2], rb)
			if val1 == val2 {
				write(program, parameterModes[2], program[ip + 3], rb, 1)
			} else {
				write(program, parameterModes[2], program[ip + 3], rb, 0)
			}

			ip = ip + 4
		case 9: //adjust relative base
			rb = rb + read(program, parameterModes[0], program[ip + 1], rb)
			ip = ip + 2
		default:
			log.Fatalf("Unknown opcode %d\n", opcode)
		}
	}
	return program
}

func getProgram(filename string) []int {
	var input string
	var program []int

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)

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
