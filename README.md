# gpio-to-keyboard-emulater-python

Make sure to install the python evdev driver and that the evdev module is loaded.

```
lsmod | grep 'evdev'
```
should return 'evdev', meaning that it has been loaded.

Else
```
modprobe evdev
```

