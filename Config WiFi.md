1. To change WiFi connection:
- connect via USB to computer
- `ssh pi@raspberrypi.local` 
- password `raspberry`
- `nano /etc/wpa_supplicant`
- You'll see something like this, change the ssid and password (use 2.4GHz network instead of 5GHz one)

```
country=US
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
 scan_ssid=1
 ssid="StataCenter"
 psk=""
}
```

2. To change boot loop:
- SSH into the device as above
- Edit the cron job:
```crontab -e```
Scroll to the bottom, edit lines such as this:
```
*/30 * * * * python3 disp_images.py -f inky-drake.png
```
you'd likely want to change the number 30 here (currently runs every 30 minutes) and the file name inky-drake.png to your desired one.
