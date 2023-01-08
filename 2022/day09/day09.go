package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type CoOrdinate struct {
	X, Y int
}

func main() {
	var scanner = bufio.NewScanner(os.Stdin)
	var line string
	var head CoOrdinate
	var tailsize int = 1

	if len(os.Args) == 2 {
		tailsize, _ = strconv.Atoi(os.Args[1])
	}

	m := make(map[CoOrdinate]bool)
	tail := make([]CoOrdinate, tailsize)

	head.X = 0
	head.Y = 0

	for i := 0; i < len(tail); i++ {
		tail[i].X = head.X
		tail[i].Y = head.Y
	}

	m[tail[tailsize-1]] = true

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

			for t := 0; t < tailsize; t++ {
				if t == 0 {
					dx = head.X - tail[0].X
					dy = head.Y - tail[0].Y
				} else {
					dx = tail[t-1].X - tail[t].X
					dy = tail[t-1].Y - tail[t].Y
				}

				if dx < -1 || dx > 1 || dy < -1 || dy > 1 {
					if dx < 0 {
						tail[t].X = tail[t].X - 1
					}

					if dx > 0 {
						tail[t].X = tail[t].X + 1
					}

					if dy < 0 {
						tail[t].Y = tail[t].Y - 1
					}

					if dy > 0 {
						tail[t].Y = tail[t].Y + 1
					}
					m[tail[tailsize-1]] = true
				}
			}
		}
	}
	fmt.Printf("Tail visited %d co-ordinates\n", len(m))
}
