# gnome vnc

* gnome have build in vnc enabled by config::desktop sharing

* changing default port:

```
gconf-editor
  desktop -> gnome -> remote access the values of:
    alternative_port=5901
      use_alternative_port=<checked>
```
