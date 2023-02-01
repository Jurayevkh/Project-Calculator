from PyQt5.QtWidgets import QLabel

class func:
    def __init__(self,label):
        self.label=label
        self.text=""

    def func_bir(self):
        self.text+="1"
        self.label.setText(self.text)


    def func_ikki(self):
        self.text+="2"
        self.label.setText(self.text)

    def func_uch(self):
        self.text+="3"
        self.label.setText(self.text)

    def func_tort(self):
        self.text+="4"
        self.label.setText(self.text)

    def func_besh(self):
        self.text+="5"
        self.label.setText(self.text)

    def func_olti(self):
        self.text+="6"
        self.label.setText(self.text)

    def func_yetti(self):
        self.text+="7"
        self.label.setText(self.text)

    def func_sakkiz(self):
        self.text+="8"
        self.label.setText(self.text)

    def func_toqqiz(self):
        self.text+="9"
        self.label.setText(self.text)


    def func_nol(self):
        self.text+="0"
        self.label.setText(self.text)

    def func_clear(self):
        self.text=""
        self.label.setText("")

    def func_kopaytiruv(self):
        self.text+="*"
        self.label.setText(self.text)

    def func_boluv(self):
        self.text+="//"
        self.label.setText(self.text)

    def func_plus(self):
        self.text+="+"
        self.label.setText(self.text)

    def func_minus(self):
        self.text+="-"
        self.label.setText(self.text)

    def func_foiz(self):
        self.text+="%"
        self.label.setText(self.text)

    def func_nuqta(self):
        self.text+="."
        self.label.setText(self.text)

    def func_equal(self):
        self.label.setText(str(eval(self.text)))