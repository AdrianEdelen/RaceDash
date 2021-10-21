import os

class connection:
    def start_can_interface():
        os.system('sudo ip link set can0 type can bitrate 500000')
        os.system('sudo ifconfig can0 up')
        return

    def shutdown_can_interface():
        os.system('sudo ifconfig can0 down')
        return

        