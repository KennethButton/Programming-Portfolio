// GOLA-002-17Q1.go
// 3/3/17
// Start 0300
// End 0354

// FAILURE: Failed to use Regex

package main

import (
	"fmt"		// Formatting for display
	"strconv"	// Take advantage of String to Int conversion
)

func main() {
	// Display intent
	fmt.Print("\n\n\n\n\nThis program is intended to validate an IPv4 address.\n\n")
	fmt.Print("-- For the prompts that follow, please press enter after each octet in decimal notation.\n\n\n")

	// prep variables
	userInput := 0
	toValidate := [4]int{0,0,0,0}

	//////////////////////////////////////////////// FIRST PROMPT
	fmt.Print("First Octet (###.   .   .   ) : ")

	// Get Input, catch error
	_, err := fmt.Scanf("%d", &userInput)
	if err != nil {
		panic(">>> ERR <<< -" + err.Error())
	} else {
		toValidate[0] = userInput
	}

	//////////////////////////////////////////////// SECOND PROMPT
	fmt.Print("Second Octet (   .###.   .   ) : ")

	// Get Input, catch error
	_, err = fmt.Scanf("%d", &userInput)
	if err != nil {
		panic(">>> ERR <<< - " + err.Error())
	} else {
		toValidate[1] = userInput
	}

	//////////////////////////////////////////////// THIRD PROMPT
	fmt.Print("Third Octet (   .   .###.   ) : ")

	// Get Input, catch error
	_, err = fmt.Scanf("%d", &userInput)
	if err != nil {
		panic(">>> ERR <<< - " + err.Error())
	} else {
		toValidate[2] = userInput
	}

	//////////////////////////////////////////////// FIRST PROMPT
	fmt.Print("Final Octet (   .   .   .###) : ")

	// Get Input, catch error
	_, err = fmt.Scanf("%d", &userInput)
	if err != nil {
		panic(">>> ERR <<< - " + err.Error())
	} else {
		toValidate[3] = userInput
	}

	//////////////////////////////////////////////// OUTPUT RESULT
	fmt.Println("You Input: " + strconv.Itoa(toValidate[0]) + "." + strconv.Itoa(toValidate[1]) + "." + strconv.Itoa(toValidate[2]) + "." + strconv.Itoa(toValidate[3]) + " ")




	//////////////////////////////////////////////// OUTPUT ANALYSIS
	addressValid := true

	for i := range toValidate {
		fmt.Print("\n\nNow testing octet " + strconv.Itoa(i+1) + "...")

		// Test limits
		if toValidate[i] < 0 {
			fmt.Print("\n INVALID OCTET FOUND -- Octet " + strconv.Itoa(i+1) + " contained # <0")
			addressValid = false
		}
		if toValidate[i] > 255 {
			fmt.Print("\n INVALID OCTET FOUND -- Octet " + strconv.Itoa(i+1) + " contained # > 255")
			addressValid = false
		} else if i == 0 && toValidate[i] >= 240 {
			fmt.Print("\n INVALID OCTET FOUND -- Octet " + strconv.Itoa(i+1) + " is in experimental/reserved range")
			addressValid = false
		}
	}

	if addressValid {
		fmt.Print("\n\n\n\n >>> Your IPv4 ADDRESS is VALID <<<\n\n")
	} else {
		fmt.Print("\n\n\n\n >>> Your IPv4 ADDRESS is INVALID <<< !!!!!!!\n\n")
	}
}
