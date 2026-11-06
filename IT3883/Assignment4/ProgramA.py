# Program Name: ProgramA.py
# Course: IT3883/Section W01
# Student Name: Bryson Mitchell
# Assignment Number: Assignment 4
# Due Date: 11/06/2026
# Purpose: Ask the user for a string and send it to Program B using TCP.
#          Receive Program B's response and display it on the console.
# Resources Used: Instructor-provided assignment instructions;
#                 OpenAI ChatGPT/Codex for coding assistance and testing.

import socket


# Both programs use the same address and port on this computer.
HOST = "127.0.0.1"
PORT = 45000
BUFFER_SIZE = 4096


def main():
    # Get the string that will be sent to Program B.
    message = input("Enter a string: ")

    try:
        # Create a TCP socket and connect to Program B.
        # The with statement closes the socket automatically.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))

            # Encode text as bytes and send the entire message.
            client.sendall(message.encode("utf-8"))

            # Signal the end of the request while still allowing a response.
            client.shutdown(socket.SHUT_WR)

            # TCP may deliver the response in several pieces.
            # Read until Program B closes its connection.
            response_parts = []
            while True:
                data = client.recv(BUFFER_SIZE)
                if not data:
                    break
                response_parts.append(data)

        # Combine all bytes before decoding so UTF-8 characters stay intact.
        response = b"".join(response_parts).decode("utf-8")
        print("Response from Program B:", response)

    except OSError as error:
        print("Network error:", error)
        print("Start ProgramB.py first and check that HOST and PORT match.")
        raise SystemExit(1)


# Run the client only when this file is executed directly.
if __name__ == "__main__":
    main()
