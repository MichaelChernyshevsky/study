package beginner

import (
	"fmt"
	"strconv"
)

func SquaringEachOne(number string) {
	var finalNumber string = ""
	for _, char := range number {
		num := int(char - '0')
		num2 := strconv.Itoa(num * num)
		finalNumber = finalNumber + num2
	}
	fmt.Println(finalNumber)

}
