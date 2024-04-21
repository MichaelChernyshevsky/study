package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type User struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
	Car  bool   `json:"car"`
}

func main() {
	user := User{Name: "John Doe", Age: 30, Car: true}
	json.NewEncoder(os.Stdout).Encode(user)
	var n User
	json.NewDecoder(os.Stdin).Decode(&n)
	fmt.Println(n.Name, n.Age, n.Car)

	// jsonData, err := json.Marshal(user)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }

	// fmt.Println(string(jsonData))
}
