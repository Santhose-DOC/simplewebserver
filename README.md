# EX01 Developing a Simple Webserver
## Date: 15/04/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body align="center">
    <style>
        table,th,td{border: 1px solid black;}
    </style>
    <table cellpadding="30" align="center" style="font-size:30px;">
        <tr>
            <th>Layer</th>
            <th>Protocol</th>
            
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP,DNS,DHCP,FTP</td>
            
            
        </tr>
        <tr>
            <td>Transport Protocol</td>
            <td>TCP,UDP</td>
            
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>IPv4,IPv6</td>
            
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>PPP,Ethernet</td>
            
        </tr>

    </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request Received")
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(content.encode())

server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("My webserver is running...")
httpd.serve_forever()
```

## OUTPUT:

![alt text](<Screenshot 2025-04-15 084435.png>)

![alt text](<Screenshot 2025-04-12 083424.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
