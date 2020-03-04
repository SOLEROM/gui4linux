# x11vnc
* This assumes screen :0 represents your monitor and binds x11vnc to that monitor instead of a session
* not to ask for an additional password (-nopw)

* install
```
apt install x11vnc
```

* /lib/systemd/system/x11vnc.service
```
# Description: Custom Service Unit file
# File: /lib/systemd/system/x11vnc.service
[Unit]
Description="x11vnc"
Requires=display-manager.service
After=display-manager.service

[Service]
ExecStart=/usr/bin/x11vnc -loop -nopw -xkb -repeat -noxrecord -noxfixes -noxdamage -forever -rfbport 5900 -display :0 -auth guess
ExecStop=/usr/bin/killall x11vnc
Restart=on-failure
Restart-sec=2

[Install]
WantedBy=multi-user.target
```


```
systemctl enable x11vnc.service
```
