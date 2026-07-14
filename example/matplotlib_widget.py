from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtGui, QtWidgets
import numpy as np
import matplotlib.text as m_text


class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = Figure(facecolor='none', constrained_layout=True)
        super().__init__(self.figure)

        self.setParent(parent)
        self.setStyleSheet("background-color: palette(window);")
        self.apply_theme_colors()

    @staticmethod
    def get_text_color_hex():
        palette = QtWidgets.QApplication.palette()
        color = palette.color(QtGui.QPalette.WindowText)
        return color.name()

    def apply_theme_to_axes(self, axes):
        hex_color = self.get_text_color_hex()
        if not isinstance(axes, (list, tuple, np.ndarray)):
            axes = [axes]
        elif isinstance(axes, np.ndarray):
            axes = axes.flat

        for ax in axes:
            ax.xaxis.label.set_color(hex_color)
            ax.yaxis.label.set_color(hex_color)
            ax.tick_params(colors=hex_color)
            for spine in ax.spines.values():
                spine.set_color(hex_color)
            ax.title.set_color(hex_color)

            leg = ax.get_legend()
            if leg is not None:
                for txt in leg.get_texts():
                    txt.set_color(hex_color)

            for txt in ax.texts:
                txt.set_color(hex_color)

    def apply_theme_colors(self):
        hex_color = self.get_text_color_hex()

        axes = self.figure.get_axes()
        if axes:
            self.apply_theme_to_axes(axes)

        for txt in self.figure.texts:
            txt.set_color(hex_color)

        if hasattr(self.figure, '_suptitle') and self.figure._suptitle is not None:
            self.figure._suptitle.set_color(hex_color)

        for txt in self.figure.findobj(m_text.Text):
            txt.set_color(hex_color)

        self.draw()

    # Methods for quick setup
    def set_suptitle(self, t, **kwargs):
        """
        Set figure SuperTitle with auto theme appliance
        """
        self.figure.suptitle(t, **kwargs)
        self.apply_theme_colors()
        return self.figure._suptitle

    def add_text(self, x, y, s, **kwargs):
        """
        Add text to a figure (fig.text) with auto theme appliance
        """
        txt = self.figure.text(x, y, s, **kwargs)
        self.apply_theme_colors()
        return txt

    def add_subplot(self, *args, **kwargs):
        """
            Add sublot to a figure with auto theme appliance
        """
        ax = self.figure.add_subplot(*args, **kwargs)
        ax.set_facecolor('none')
        self.apply_theme_colors()
        return ax

    def subplots(self, nrows=1, ncols=1, **kwargs):
        """
            Add sublots to a figure with auto theme appliance
        """
        axes = self.figure.subplots(nrows=nrows, ncols=ncols, **kwargs)
        if isinstance(axes, np.ndarray):
            for ax in axes.flat:
                ax.set_facecolor('none')
        else:
            axes.set_facecolor('none')
        self.apply_theme_colors()
        return axes
