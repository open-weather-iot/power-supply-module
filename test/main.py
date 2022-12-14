from machine import Pin
from src.power_supply import PowerSupply
import time

def has_method(o, name):
    return callable(getattr(o, name, None))

# TODO: fazer o tratamento de erros
# TODO: suportar um botão de reset e calibração dos sensores

def main():
    # ---------------------------------------
    # ------------- SETUP    ----------------
    # ---------------------------------------
    led_internal = Pin(25, Pin.OUT)

    led_internal.value(1)

    read_interval = 1

    sensors = {
        # nome do sensor: nome da classe()
        "power_supply_sensor": PowerSupply()
    }

    # inicialização de cada sensor (se o método setup existe)
    for sensor in sensors.values():
        if has_method(sensor, 'setup'):
            sensor.setup()

    # ---------------------------------------
    # -------------   LOOP   ----------------
    # ---------------------------------------
    while True:
        read_map = { name: sensor.read() for (name, sensor) in sensors.items() }
        print(read_map)

        led_internal.toggle() # internal led toggle
        time.sleep(read_interval)

if __name__ == "__main__":
    main()
