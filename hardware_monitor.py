import threading
import time
import psutil
import subprocess

class CPU:
    def __init__(self, ui):
        self.ui_object = ui

    def get_cpu_max_clock_speed(self):
        cpu_max_clock = subprocess.check_output(['powershell', 'wmic cpu get maxclockspeed']).decode('utf-8')
        cpu_max_clock = cpu_max_clock.split('MaxClockSpeed')[1].strip()

        return int(cpu_max_clock)

    def get_cpu_freq(self):
        freq_percent = subprocess.check_output(
            ["powershell", r'Get-Counter -Counter "\Processor Information(_Total)\% Processor Performance"']).decode(
            'utf-8')

        max_clock_speed = self.get_cpu_max_clock_speed()

        freq_percent = freq_percent.split('processor performance :')[1].strip()
        freq_percent = round(float(freq_percent)/100, 2)

        speed = max_clock_speed * freq_percent

        return round(speed, 2)

    def set_cpu_usage(self):
        try:
            usage = self.get_cpu_utilization()
            self.ui_object.cpu_usage.setText(f'Usage: {usage}%')

        except:
            pass

    def set_cpu_speed(self):
        try:
            speed = self.get_cpu_freq()
            self.ui_object.cpu_speed.setText(f'Speed: {speed} MHz')

        except:
            pass

    def get_cpu_utilization(self):
        utilization = subprocess.check_output(['wmic', 'cpu', 'get', 'LoadPercentage']).decode('utf-8')

        utilization = utilization.split('LoadPercentage')[1].strip()
        utilization = int(utilization)

        return utilization


class HardwareMonitor(CPU):
    def __init__(self, ui_object, main_window):
        self.active = True
        self.ui_object = ui_object

        CPU.__init__(self, ui_object)

        main_window.closeEvent = self.exit_app

    def exit_app(self, e):
        self.active = False

    def monitor(self):
        while self.active:
            if threading.active_count() < 4:
                try:
                    threading.Thread(target=self.set_cpu_usage).start()

                except:
                    pass

                try:
                    threading.Thread(target=self.set_cpu_speed).start()

                except:
                    pass

            time.sleep(1.5)
