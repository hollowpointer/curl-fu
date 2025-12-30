# Introduction to cURL

Welcome to the White Belt tier. Before we start firing off commands, we need to agree on what we are actually using.

cURL stands for "Client for URLs". It is a command-line tool used to transfer data to or from a server. You may think of it as a web browser without the graphical interface. When you type `google.com` into Chrome or Firefox, the browser does a lot of lifting to make the page look pretty for you. It renders images, executes JavaScript, and styles the text.

cURL does none of that. It connects to a server, performs a handshake, and shows you the raw data exactly as the server sent it.

This is why it is the industry standard for developers and security professionals. If you want to debug an API, download a file automatically, or test a server for vulnerabilities, you use cURL.

In this sandbox, you will act as the client. I'm the web server, your target. You will use cURL to talk to me, manipulate me, and eventually break me.

Let's get started.