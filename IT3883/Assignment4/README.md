# Python socket assignment

Bryson Mitchell | IT3883, Section W01 | Assignment 4 | Due: November 6, 2026

## Run the programs

Use Python 3. No third-party packages are required.

1. Open two terminals in the folder containing the programs.
2. In the first terminal, start the server:
   ```text
   python ProgramB.py
   ```
3. In the second terminal, start the client:
   ```text
   python ProgramA.py
   ```
4. Type a string at the client's prompt and press Enter. For example:
   ```text
   Enter a string: Hello from Program A!
   Response from Program B: HELLO FROM PROGRAM A!
   ```

Program B serves one connection and then exits. Restart Program B before each new run of Program A.

Both programs use TCP at `127.0.0.1:45000`, so run them on the same computer. Port 45000 was available during testing. If another application uses it later, change `PORT` to the same available port above 40000 in both files.

Program A sends UTF-8 bytes and shuts down only its sending side to signal the end of the string. Program B reads until that signal, converts the complete string to uppercase, sends it back, and closes the connection. Program A reads until the connection closes. Receiving in a loop avoids cutting off long messages.

## Submission

Submission folder: `IT3883/Assignment4` in `bry1417/BMITC114.github.io`.

The submission includes `ProgramA.py`, `ProgramB.py`, and `output_screenshot.jpg`. The screenshot shows a real run of the two programs, with their console output displayed in a local output viewer. The viewer is only used to capture the demonstration; the submitted programs run in ordinary terminals.
