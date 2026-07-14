# QMatplotlibWidget

## [RU] Кастомный виджет для интеграции Matplotlib в PyQt5 приложение

В файле `matplotlib_widget.py` содержится класс **MatplotlibWidget**, который наследуется
от базового **FigureCanvas** из стандартной реализации Matplotlib в Qt. Он обеспечивает
автоматическое применение текущей темы приложения и позволяет более просто и быстро создавать
графики на Figure.

В директории `example` содержится пример использования кастомного виджета, для этого необходимо
скопировать файл `matplotlib_widget.py` в директорию `example` и запустить `example.py`,
предварительно создав виртуальное окружение с установленными *PyQt5* и *matplotlib*.

## [EN] Custom widget for integrating Matplotlib into PyQt5 application

In the file `matplotlib_widget.py ` contains the **MatplotlibWidget** class, which inherits
from the base **FigureCanvas** from the standard Matplotlib implementation in Qt. It provides
automatic application of the current application theme and allows you to create
graphs on Figure more simply and quickly.

The `example` directory contains an example of using a custom widget. To do this
, copy the file `matplotlib_widget.py `to the `example` directory and run `example.py`,
by first creating a virtual environment with *PyQt5* and *matplotlib* installed.