from http.server import HTTPServer,BaseHTTPRequestHandler
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
