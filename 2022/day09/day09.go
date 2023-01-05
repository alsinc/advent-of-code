package main

import (
	"bufio"
	"fmt"
	"os"
)

type CoOrdinate struct {
	X, Y int
}

func main() {
	var scanner = bufio.NewScanner(os.Stdin)
	var line string
	var head CoOrdinate
	var tail CoOrdinate
	var m map[CoOrdinate]bool

	m = make(map[CoOrdinate]bool)

	head.X = 0
	head.Y = 0
	tail.X = 0
	tail.Y = 0

	m[tail] = true

	for scanner.Scan() {
		var direction string
		var distance int
		var vx int
		var vy int

		line = scanner.Text()

		fmt.Sscanf(line, "%s %d", &direction, &distance)

		if direction == "D" {
			vx = 0
			vy = -1
		} else if direction == "U" {
			vx = 0
			vy = 1
		} else if direction == "R" {
			vx = 1
			vy = 0
		} else if direction == "L" {
			vx = -1
			vy = 0
		} else {
			fmt.Printf("OOPS, unknown direction %s", direction)
		}

		for d := 0; d < distance; d++ {
			var dx int
			var dy int

			head.X += vx
			head.Y += vy

			dx = head.X - tail.X
			dy = head.Y - tail.Y

			if dx < -1 || dx > 1 || dy < -1 || dy > 1 {
				//fmt.Printf("move tail: head(%d, %d), tail(%d, %d) dx(%d,%d)\n", headx, heady, tailx, taily, dx, dy)

				if dx < 0 {
					tail.X = tail.X - 1
				}

				if dx > 0 {
					tail.X = tail.X + 1
				}

				if dy < 0 {
					tail.Y = tail.Y - 1
				}

				if dy > 0 {
					tail.Y = tail.Y + 1
				}
				m[tail] = true
			}
		}
	}
	fmt.Printf("Tail visited %d co-ordinates\n", len(m))
}
