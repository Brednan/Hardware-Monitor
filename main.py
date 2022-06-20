from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
from hardware_monitor import HardwareMonitor
import threading

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    monitor = HardwareMonitor(ui, MainWindow)
    threading.Thread(target=monitor.monitor).start()

    MainWindow.show()
    sys.exit(app.exec_())
