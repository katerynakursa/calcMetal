import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QApplication

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        perFirst = QLabel('% элемент 1')
        perSecond = QLabel('% элемент 2')
        massa = QLabel('Вес')

        nowAlloy = QLabel('Имеем')
        addAlloy = QLabel('Добавим')
        getAlloy = QLabel('Получим')

        nowPerFirst = QLineEdit()
        nowPerSecond = QLineEdit()
        nowMassa = QLineEdit()

        addPerFirst = QLineEdit()
        addPerSecond = QLineEdit()
        addMassa = QLineEdit()

        getPerFirst = QLineEdit()
        getPerSecond = QLineEdit()
        getMassa = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(perFirst, 1, 0)
        grid.addWidget(perSecond, 2, 0)
        grid.addWidget(massa, 3, 0)

        grid.addWidget(nowAlloy, 0, 1)
        grid.addWidget(nowPerFirst, 1, 1)
        grid.addWidget(nowPerSecond, 2, 1)
        grid.addWidget(nowMassa, 3, 1)

        grid.addWidget(addAlloy, 0, 2)
        grid.addWidget(addPerFirst, 1, 2)
        grid.addWidget(addPerSecond, 2, 2)
        grid.addWidget(addMassa, 3, 2)

        grid.addWidget(getAlloy, 0, 3)
        grid.addWidget(getPerFirst, 1, 3)
        grid.addWidget(getPerSecond, 2, 3)
        grid.addWidget(getMassa, 3, 3)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 100)
        self.setWindowTitle('Расчет сплавов')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
