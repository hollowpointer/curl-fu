# 05 Output Redirection

Dumping raw data to your terminal is usually a mess. If you accidentally curl a binary file (like an image or an executable), it will flood your screen with garbage characters and might even crash your shell.

You need to capture that output and save it to a disk.

Curl provides two ways to do this:

1. **`-o` (lowercase):** You specify the filename. Great for renaming files on the fly.
2. **`-O` (uppercase):** It saves the file using the exact filename it has on the server.

Lets say you found a sensitive file on the server and you want to exfiltrate it to your local machine for analysis.

Run this command to download the data and save it as `image.jpg`:

```bash
curl -o image.jpg http://{{address}}/mystery_file

```

If you see no output, that is good news. It means the data went into the file instead of your screen. Check your folder to see what you stole.