## Kasa KP115 streamer

To find out the Plug ip addres go to the BT smart hub manager and check the plug wireless connection at 192.168.1.254


To build the image do this:
```
docker build . -t kasa-estream:dev
```

To run the streaming use this:
```
docker run -it -e KP115_IP=<PLUG_IP_ADDRESS> kasa-estream:dev
```