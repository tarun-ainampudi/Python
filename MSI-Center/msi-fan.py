# pseudo-code (concept only)
import sys
from ec_driver import ec_read_byte, ec_write_byte  # wrapper for WinRing0 / InpOut

def set_fan_mode(mode_name):
    modes = {"auto": 0x0D, "silent": 0x1D, "advanced": 0x8D}
    if mode_name not in modes:
        print("mode must be one of:", ", ".join(modes))
        return
    value = modes[mode_name]
    ec_write_byte(0xD4, value)
    print(f"wrote 0x{value:02X} to 0xD4 (fan_mode)")

def read_temp_and_fan():
    cpu_temp = ec_read_byte(0x68)
    cpu_fan = ec_read_byte(0x71)
    gpu_temp = ec_read_byte(0x80)
    gpu_fan = ec_read_byte(0x89)
    print(f"CPU temp: {cpu_temp}, CPU fan: {cpu_fan}")
    print(f"GPU temp: {gpu_temp}, GPU fan: {gpu_fan}")

if __name__ == "__main__":
    if sys.argv[1] == "setmode":
        set_fan_mode(sys.argv[2])
    elif sys.argv[1] == "status":
        read_temp_and_fan()
