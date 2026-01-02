# 04 HTTP Response Headers

Every HTTP response is split into two distinct parts: the **Headers** and the **Body**.

The Body is what a normal user sees: the HTML, the images, the text.

But as a security researcher, you are often more interested in the Headers. This is where the server reveals its identity. Headers can leak critical information, such as what software the server is running (Apache, Nginx, IIS), what version it is on, and sometimes even the operating system or backend language (PHP, Python).

This process is called "Banner Grabbing" or fingerprinting. Before you can look for vulnerabilities, you need to know exactly what you are attacking.

You want to grab this information quickly and efficiently, without dragging down the entire page content.

The `-I` flag (that is a capital i) allows you to do exactly this. It switches the request method from GET to **HEAD**. This tells the server: "Send me your metadata, but keep the body."

Try fingerprinting with this command:

```bash
curl -I http://{{address}}/headers.txt

```

You will see the server declaration and content type, but the actual text of the page will be missing.