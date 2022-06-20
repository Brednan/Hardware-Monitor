import threading
import time
import psutil


class HardwareMonitor:
    def __init__(self, ui_object, main_window):
        self.active = True
        self.ui_object = ui_object
        main_window.closeEvent = self.exit_app

    def set_cpu_usage(self):
        usage = psutil.cpu_percent(interval=1)
        self.ui_object.usage.setText(f'Usage: {usage}%')

    def exit_app(self, e):
        self.active = False

    def monitor(self):
        while self.active:
            try:
                self.set_cpu_usage()

            except:
                pass
