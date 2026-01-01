# 02 Basic HTTP GET

To communicate with a web server, you need two things: a location (the URL) and an action. In the HTTP protocol, these actions are called "verbs" or "methods". They tell the server exactly what you want to do with the resource you are visiting.

You might want to read a file, delete a user or upload a photo. There is a specific verb for each of these.

The most fundamental verb is **GET**.

GET is used solely to retrieve data. It is a read only request. When you type an address into your web browser, the browser sends a GET request to that server asking for the page content. It is the equivalent of asking "Can you show me what is on this page?"

Because fetching data is the most common task, curl uses GET as its default behavior. If you provide a URL without specifying a method, curl assumes you just want to look at it.

You (hopefully) have been using the GET request with curl simply by typing:

```bash
curl http://localhost:5001/01/02

```

This fetched the specific data for this stage of the training and printed it to your terminal.