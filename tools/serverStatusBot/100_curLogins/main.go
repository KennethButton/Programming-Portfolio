// Main file for the Size McMonitoring Bot for BigRedPaws Servers
package main

import (
	"database/sql"	// Used to save data to the database
	_ "github.com/go-sql-driver/mysql"
	"log"
	"os/exec"	// Used to grab a linux system
)

var db *sql.DB
var err error

func main() {
	// Database information
	db, err = sql.Open("mysql", "gs_api:Kyrodo-Is-The-1@/webAdmin?interpolateParams=true")
	if err != nil {
		panic(err.Error())	// TODO: Replace with actual handling
	}
	defer db.Close()

	// Verify handle
	err = db.Ping()
	if err != nil {
		panic(err.Error())	// TODO: Replace with actual handling
	}

	// Run Linux PS command
	cmd := exec.Command("sleep", "1")
	log.Printf("Running command and waiting for it to finish...")
	err := cmd.Run()
	log.Printf("Command finished with error: %v", err)

	// Break apart returned values
	// TODO: Create loop that saves each entry to the database

	// Save to database
	_, err = db.Exec("INSERT INTO usersActive(username, accessVia, accessTime) VALUES(?, ?, NOW())", who, where)
	if err != nil {
		panic(err.Error())	// TODO: Replace with actual handling
	}
}
