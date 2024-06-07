import requests

class RoverControl:
    def __init__(self, ip):
        self.esp32_ip = f'http://{ip}'

    def send_command(self, cmd, spd):
        url = f"{self.esp32_ip}/command"
        params = {'cmd': cmd, 'spd': spd}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"Failed to send command: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def move_forward(self, speed):
        self.send_command('f', speed)

    def move_backward(self, speed):
        self.send_command('b', speed)

    def turn_left(self, speed):
        self.send_command('l', speed)

    def turn_right(self, speed):
        self.send_command('r', speed)

    def stop(self):
        self.send_command('s', 0)

    def control_rover(self, direction, speed):
        if not 0 <= speed <= 255:
            raise ValueError("Speed must be between 0 and 255.")
        if direction == 'f':
            self.move_forward(speed)
        elif direction == 'b':
            self.move_backward(speed)
        elif direction == 'l':
            self.turn_left(speed)
        elif direction == 'r':
            self.turn_right(speed)
        elif direction == 's':
            self.stop()
        else:
            print("Invalid direction. Use 'f', 'b', 'l', 'r', or 's'.")
