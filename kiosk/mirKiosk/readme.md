# chromium-mir-kiosk on mir-kiosk

* using snap (https://codeburst.io/how-to-install-and-use-snap-on-ubuntu-18-04-9fcb6e3b34f9)

## install

```
stable
=======
snap install mir-kiosk
snap install --beta chromium-mir-kiosk


dev
====
snap install --devmode mir-kiosk
sudo snap install chromium-mir-kiosk --beta --devmode

```

## config

set connections

```
snap connect chromium-mir-kiosk:wayland mir-kiosk:wayland
```

check connection

```
snap connections chromium-mir-kiosk
====================================
wayland                   chromium-mir-kiosk:wayland                   mir-kiosk:wayland        manual

```

get settings

```
snap get chromium-mir-kiosk
snap get mir-kiosk

```

set settings

```
> sudo snap set chromium-mir-kiosk shownav=true

daemonize mir-kiosk to start after boot:
> sudo snap set mir-kiosk daemon=true

To customize the startup url for chromium use:
> sudo snap set chromium-mir-kiosk url="https://yoururl.com"


```


## run

```
sudo mir-kiosk --devmode
sudo snap start chromium-mir-kiosk
systemctl status snap.chromium-mir-kiosk.chromium-mir-kiosk.service

```

