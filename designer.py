import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QApplication, QDoubleSpinBox

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

        self.nowPerFirst = QDoubleSpinBox(self, decimals=1)
        self.nowPerSecond = QDoubleSpinBox(self, decimals=1)
        self.nowMassa = QDoubleSpinBox(self, decimals=1, maximum=9999)

        self.addPerFirst = QDoubleSpinBox(self, decimals=1)
        self.addPerSecond = QDoubleSpinBox(self, decimals=1)
        self.addMassa = QDoubleSpinBox(self, decimals=1, maximum=9999)

        self.getPerFirst = QLabel(self)
        self.getPerSecond = QLabel(self)
        self.getMassa = QLabel(self)

        self.btn = QPushButton('Расчет', self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(perFirst, 1, 0)
        grid.addWidget(perSecond, 2, 0)
        grid.addWidget(massa, 3, 0)

        grid.addWidget(nowAlloy, 0, 1)
        grid.addWidget(self.nowPerFirst, 1, 1)
        grid.addWidget(self.nowPerSecond, 2, 1)
        grid.addWidget(self.nowMassa, 3, 1)

        grid.addWidget(addAlloy, 0, 2)
        grid.addWidget(self.addPerFirst, 1, 2)
        grid.addWidget(self.addPerSecond, 2, 2)
        grid.addWidget(self.addMassa, 3, 2)

        grid.addWidget(getAlloy, 0, 3)
        grid.addWidget(self.getPerFirst, 1, 3)
        grid.addWidget(self.getPerSecond, 2, 3)
        grid.addWidget(self.getMassa, 3, 3)

        grid.addWidget(self.btn, 4, 3)

        self.setLayout(grid)

        self.btn.clicked.connect(self.calcMetal)

        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Расчет сплавов')
        self.show()

    def calcMetal(self):

        nowPerFirst = self.nowPerFirst.value()
        nowPerSecond = self.nowPerSecond.value()
        nowMassa = self.nowMassa.value()

        addPerFirst = self.addPerFirst.value()
        addPerSecond = self.addPerSecond.value()
        addMassa = self.addMassa.value()

        nowMassaFirst = self.calcMassa(nowPerFirst, nowMassa)
        nowMassaSecond = self.calcMassa(nowPerSecond, nowMassa)

        addMassaFirst = self.calcMassa(addPerFirst, addMassa)
        addMassaSecond = self.calcMassa(addPerSecond, addMassa)

        getMassaFirst = self.sumMassa(nowMassaFirst, addMassaFirst)
        getMassaSecond = self.sumMassa(nowMassaSecond, addMassaSecond)
        getMassa = self.sumMassa(nowMassa, addMassa)

        getPerFirst = self.percent(getMassaFirst, getMassa)
        getPerSecond = self.percent(getMassaSecond, getMassa)

        self.getPerFirst.setText(str(getPerFirst))
        self.getPerFirst.adjustSize()
        self.getPerSecond.setText(str(getPerSecond))
        self.getPerSecond.adjustSize()
        self.getMassa.setText(str(getMassa))
        self.getMassa.adjustSize()





    def calcMassa(self, percent, massa_total):

        massaElem = percent * massa_total / 100
        return massaElem

    def sumMassa(self, massa_now, massa_add):

        massaAll = massa_now + massa_add
        return massaAll

    def percent(self, massa_el, massa_total):

        per = round(massa_el / massa_total *100, 1)
        return per




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
