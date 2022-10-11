package main

import "fmt"

func main() {

	var conferenceName string = "Go Conference"
	//const conferenceTickets int = 50
	var remainingTickets uint = 50

	fmt.Printf("Welcome to %v booking application\n", conferenceName)
	fmt.Printf("we have total %v tickets remaining\n", remainingTickets)
	fmt.Println("Get your tickets here to attend")

	var firstName string
	var lastName string
	var email string
	var userTickets uint

	fmt.Printf("Enter your First Name :")
	fmt.Scan(&firstName)
	fmt.Printf("Enter your Last Name :")
	fmt.Scan(&lastName)
	fmt.Printf("Enter your Email :")
	fmt.Scan(&email)
	fmt.Printf("Enter number of Tickets :")
	fmt.Scan(&userTickets)

	remainingTickets = remainingTickets - userTickets

	//userName = "Tom"
	//userTickets = 2
	fmt.Printf("User %v booked %v tickets\n", firstName, userTickets)

	fmt.Printf("Remaining Tickets : %v", remainingTickets)

}
