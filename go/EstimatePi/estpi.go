package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func estimatepi(n int) float64 {
	var k float64
	startT := time.Now()
	for i := 0; i < n; i++ {
			xr := rand.Float64() * 2
			yr := rand.Float64() * 2

			dist := math.Sqrt((xr - 1.0)*(xr - 1.0) + (yr-1.0)*(yr-1.0))
			if dist < 1 {
				k++
			}
	}

	fmt.Println("Finished in", time.Now().Sub(startT).Seconds(), "seconds")

	return (4 * k / float64(n))
}

func main() {
	ePI := estimatepi(10000000)
	fmt.Println(ePI)
}
