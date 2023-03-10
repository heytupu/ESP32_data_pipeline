"""Entrypoint"""
from json import load
import machine
import network
import time

print("\n-------------------- Started Bootloader ESP32 --------------------\n")

try:
    with open("configs/config.json", "r") as json_file:
        CFG = load(json_file)
except Exception as e:
    print("Failed to load config file.")

import ugit

def enable_garbage_collection() -> None:
    """Enabling the garbage collector."""
    import gc

    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

enable_garbage_collection()
wlan = ugit.wificonnect(CFG["Network"]["SSID"], CFG["Network"]["PASS"])
ugit.pull_all()
print("Waiting for files to settle")
time.sleep(5)

