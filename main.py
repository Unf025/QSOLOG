from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType("pa.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def clean_window():
    form.lineEdit.clear()
     

def inform_check():
    callsign = str(form.lineEdit.text())
    RSTR = str(form.lineEdit_2.text())
    RSTS = str(form.lineEdit_3.text())

    if callsign and RSTR and RSTS:
        print('Date: ' + form.dateEdit.dateTime().toString('yyyy-MM-dd') + ' Time: ' + form.timeEdit.dateTime().toString('hh:mm') + ' CALL: ' +
            form.lineEdit.text().upper() + ' BAND: ' + str(form.comboBox.currentText() + ' MODE: ' + form.comboBox_2.currentText())
            + ' RSTr: ' + str(form.lineEdit_2.text() + ' RSTs: ' + form.lineEdit_3.text()))
        file = open('log.txt' , 'a')
        file.write('Date: ' + form.dateEdit.dateTime().toString('yyyy-MM-dd') + ' Time: ' + form.timeEdit.dateTime().toString('hh:mm') + ' CALL: ' +
            form.lineEdit.text().upper() + ' BAND: ' + str(form.comboBox.currentText() + ' MODE: ' + form.comboBox_2.currentText())
            + ' RSTr: ' + str(form.lineEdit_2.text() + ' RSTs: ' + form.lineEdit_3.text()))
        file.close
        clean_window()
        form.lineEdit.clear()
    elif RSTR and RSTS and not callsign:
        form.lineEdit.setText('Введите позывной!')
    elif callsign and not RSTS and not RSTR:
        form.lineEdit.setText('Введите рапорты!')
    elif not callsign and not RSTS and not RSTR:
        form.lineEdit.setText('Введите данные!')
    elif callsign and RSTR and not RSTS:
        form.lineEdit.setText('Введите переданный рапорт!')
    elif callsign and RSTS and not RSTR:
        form.lineEdit.setText('Введите принятый рапорт!')





form.pushButton.clicked.connect(inform_check)



app.exec_()