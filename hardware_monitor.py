import threading
import time
import psutil
import os


class HardwareMonitor:
    def __init__(self, ui_object, main_window):
        self.active = True
        self.ui_object = ui_object
        main_window.closeEvent = self.exit_app

    def set_cpu_usage(self):
        try:
            usage = psutil.cpu_percent(interval=1)
            self.ui_object.cpu_usage.setText(f'Usage: {usage}%')

        except:
            pass

    def set_cpu_speed(self):
        try:
            speed = os.system()
            print(speed)
            self.ui_object.cpu_speed.setText(f'Speed: {speed} MHz')

        except:
            pass

    def exit_app(self, e):
        self.active = False

    def monitor(self):
        while self.active:
            try:
                threading.Thread(target=self.set_cpu_usage).start()

            except:
                pass

            try:
                threading.Thread(target=self.set_cpu_speed).start()

            except:
                pass