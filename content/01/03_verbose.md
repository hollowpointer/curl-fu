# 03 Verbosity and Debugging

So far, you typed a command, and the result just appeared. But in the real world, things break. Servers crash, firewalls block connections, and permissions get denied. When that happens, you need to see exactly what is going on.

This is where verbose mode comes in. It is one of the most useful tools in your arsenal because it turns on the lights.

By adding the `-v` (or `--verbose`) flag, curl reveals the entire lifecycle of the connection. It shows you the hidden conversation taking place between your machine and the server.

The output is coded with special characters at the start of each line to help you identify who is talking:

* **`*` (Asterisk):** This is curl talking to you. It shows internal information like IP address resolution, connection status, and handshake details.
* **`>` (Greater-than):** This is data leaving your machine. These are the request headers being sent to the server.
* **`<` (Less-than):** This is data coming back. These are the response headers sent by the server.

If you ever get stuck, your first instinct should be: make it verbose.

Run the command with the verbose flag to see the handshake in action:

```bash
curl -v http://localhost:5001/01/verbose

```

You will see the connection open, the "GET" request go out, and the HTTP 200 OK status come back before the final content is printed.