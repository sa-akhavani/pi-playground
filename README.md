# pi-playground



## NFC
Reading from and Writing on the RC522 NFC reader.
Thanks to: https://pimylifeup.com/raspberry-pi-rfid-rc522/

#### Enabling SPI on the Raspberry Pi
```
sudo raspi-config
# 3 Interface Options -> I$ SPI -> Enable -> Finish
sudo reboot
```

Setup:
```bash
python -m venv venv
source /venv/bin/activate
pip install spidev
pip install mfrc522
```

