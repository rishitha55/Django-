from PyQt5. QtWidgets import QApplication ,QWidgets,QPushButton,QVBoxLayout
app=QAplication([])
window=QWidget()
layout=QVBoxLayout()
layout.addWidget(QPushButton('top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()
