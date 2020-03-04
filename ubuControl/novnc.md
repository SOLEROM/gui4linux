# novnc


* Install
```
apt -y install novnc websockify python-numpy
```

* config

```
>   cd /etc/ssl

>   openssl req -x509 -nodes -newkey rsa:2048 -keyout novnc.pem -out novnc.pem -days 365

Generating a 2048 bit RSA private key
....+++
........................................................+++
writing new private key to 'novnc.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:JP   # country
State or Province Name (full name) [Some-State]:Hiroshima    # state
Locality Name (eg, city) []:Hiroshima  # city
Organization Name (eg, company) [Internet Widgits Pty Ltd]:GTS  # company
Organizational Unit Name (eg, section) []:Server World     # department
Common Name (e.g. server FQDN or YOUR name) []:www.srv.world  # server's FQDN
Email Address []:root@srv.world   # admin email

>   chmod 644 novnc.pem
```

* run

```
websockify -D --web=/usr/share/novnc/ --cert=/etc/ssl/novnc.pem 6080 localhost:5901

WebSocket server settings:
  - Listen on :6080
  - Flash security policy server
  - Web server. Web root: /usr/share/novnc
  - SSL/TLS support
  - Backgrounding (daemon)

```

* use

```
http://(server's hostname or IP address):6080/vnc.htm
```
