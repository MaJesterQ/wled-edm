1. Install VSCODE
      - Install PlatformIO IDE plugin
      - Install C/C++ Plugin
      - Install Python plugin
2. Install Python 3.12q
3. (Optionally) Might need to download esp32 com port drivers


For build:
1. Go to PlatformIO plugin panel
2. (Optionally) Refresh Project Tasks on the top
3. Find your configuration (my custom seeed_xiao_esp32s3_v2, esp32s3dev_8MB_PSRAM_opi or custom) that is currently active in platformio.ini
4. Build (sometimes it fails for whatever reason, build multiple times if needed. You can also use Default -> Build All)
5. The build can be found under .pio/build/{yourConfig}/firmware.bin

For every flash I do
1. Disconnect the ESP
2. Hold "BOOT" button (has small B button next to it) and connect the usb, release the "BOOT" button
3. Go to https://web.esphome.io/ and press Connect -> Prepare for First use
4. Reconnect ESP
5. Wifi espHome-web should come up
6. Connect and go to 192.168.4.1
7. Scroll down to OTA Update, Choose the bin and Update. NB! Wait till the Wifi WLED comes up, default password is wled1234.
8. Go to 4.3.2.1
9. ???
10. Profit


