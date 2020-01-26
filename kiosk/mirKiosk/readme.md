

* using snap (https://codeburst.io/how-to-install-and-use-snap-on-ubuntu-18-04-9fcb6e3b34f9)

## install

```
snap install mir-kiosk
#snap install --beta chromium-mir-kiosk
nap install chromium-mir-kiosk --devmode --edge

```

## config

```
snap connections chromium-mir-kiosk

snap get chromium-mir-kiosk

```

```
sudo snap start chromium-mir-kiosk

systemctl status snap.chromium-mir-kiosk.chromium-mir-kiosk.service

```


```
daemonize mir-kiosk to start after boot:
> sudo snap set mir-kiosk daemon=true

To customize the startup url for chromium use:
> sudo snap set chromium-mir-kiosk url="https://yoururl.com"

```
