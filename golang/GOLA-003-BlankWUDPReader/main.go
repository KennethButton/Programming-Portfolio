package main

import(
	"log";
	"net";
)

func main() {
	pc, err := net.ListenPacket("udp", ":400")
	if err != nil {
		log.Fatal(err)
	}
	defer pc.Close()

	for {
		// TODO: Make handle all incomes, not just one.
		buffer := make([]byte, 1024)
		_, addr, _ := pc.ReadFrom(buffer)

		println(string(buffer));
		// TODO: Fix dumb reply
		pc.WriteTo([]byte("Stomped you flat"), addr)
	}
}
