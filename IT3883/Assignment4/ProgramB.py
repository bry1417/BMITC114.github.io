# Program Name: ProgramB.py
# Course: IT3883/Section W01
# Student Name: Bryson Mitchell
# Assignment Number: Assignment 4
# Due Date: 11/06/2026
# Purpose: Listen for a TCP connection from Program A and receive a string.
#          Convert the string to uppercase and send it back to Program A.
# Resources Used: Instructor-provided assignment instructions;
#                 OpenAI ChatGPT/Codex for coding assistance and testing.

import socket


# Use the same address and port as Program A.
HOST = "127.0.0.1"
PORT = 45000
BUFFER_SIZE = 4096


def main():
    try:
        # Create the TCP server socket and listen for one client.
        # The with statements close both sockets automatically.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((HOST, PORT))
            server.listen(1)
            print(f"Program B is listening on {HOST}:{PORT}", flush=True)

            # Wait until Program A connects.
            connection, address = server.accept()
            with connection:
                print(f"Connected to Program A at {address}")

                # Read all pieces until Program A signals it is done sending.
                message_parts = []
                while True:
                    data = connection.recv(BUFFER_SIZE)
                    if not data:
                        break
                    message_parts.append(data)

                # Decode the complete message, then convert it to uppercase.
                message = b"".join(message_parts).decode("utf-8")
                response = message.upper()
                print("Received:", message)

                # Send the complete uppercase response as UTF-8 bytes.
                connection.sendall(response.encode("utf-8"))
                print("Sent:", response)

        # Closing the connection tells Program A the response is complete.
        print("Program B finished.")

    except OSError as error:
        print("Network error:", error)
        print("If the port is in use, change PORT in both programs.")
        raise SystemExit(1)


# Run the server only when this file is executed directly.
if __name__ == "__main__":
    main()
