// utils/mathutils/mathutils.go - @TODO Not prod ready
package mathutils
package main

func Add(a int, b int) int {
    return a + b
}


import (
    "fmt"
    "yourproject/utils/mathutils"
)

func main() {
    sum := mathutils.Add(1, 2)
    fmt.Println("Sum:", sum)
}
