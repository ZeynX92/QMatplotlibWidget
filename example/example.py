import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('example.ui', self)

        # create an axis
        axes = self.canvas.subplots(3, 1)

        self.canvas.set_suptitle(f"Some Plots", fontweight='bold')
        axes[0].plot([randint(1, 100) for _ in range(20)], 'r-')
        axes[0].set_ylabel('Y1, int')
        axes[0].set_xlabel('X1, int')

        axes[1].plot([randint(1, 100) for _ in range(20)], 'g-')
        axes[1].set_ylabel('Y2, int')
        axes[1].set_xlabel('X2, int')

        axes[2].plot([randint(1, 100) for _ in range(20)], 'b-')
        axes[2].set_ylabel('Y3, int')
        axes[2].set_xlabel('X3, int')

        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
