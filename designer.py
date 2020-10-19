import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QApplication, QDoubleSpinBox

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

        self.nowPerFirst = QDoubleSpinBox(self)
        self.nowPerSecond = QDoubleSpinBox(self)
        self.nowMassa = QDoubleSpinBox(self)

        self.addPerFirst = QDoubleSpinBox(self)
        self.addPerSecond = QDoubleSpinBox(self)
        self.addMassa = QDoubleSpinBox(self)

        self.getPerFirst = QLineEdit(self)
        self.getPerSecond = QLineEdit(self)
        self.getMassa = QLineEdit(self)

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
        self.getPerSecond.setText(str(getPerSecond))
        self.getMassa.setText(str(getMassa))





    def calcMassa(self, percent, massa_total):

        massaElem = percent * massa_total / 100
        return massaElem

    def sumMassa(self, massa_now, massa_add):

        massaAll = massa_now + massa_add
        return massaAll

    def percent(self, massa_el, massa_total):

        per = massa_el / massa_total *100
        return per




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
