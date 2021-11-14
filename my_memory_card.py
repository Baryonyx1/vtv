from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QPushButton, QLabel, 
        QVBoxLayout,QHBoxLayout,
        QRadioButton,QGroupBox, QButtonGroup)
from random import shuffle,randint

class question1():
    def __init__(self,question,true_answer,no_true1,no_true2,no_true3):
        self.question = question
        self.true_answer = true_answer
        self.no_true1 = no_true1
        self.no_true2 = no_true2
        self.no_true3 = no_true3



question_list =[]
question_list.append(question1("Хто я?","зы",'л','п','н'))
question_list.append(question1('хто ты?','ds','ds','ds','ds'))
question_list.append(question1('f?','f1','f2','f3','f4'))
question_list.append(question1('Будешь кидать зигу?','да','нет','да,нет','да,нет наверное'))

app = QApplication([])

btn_ok = QPushButton('Відповісти')
lb_Question = QLabel('Коли я народився?')
RadioGroupBox = QGroupBox()

rbtn1 = QRadioButton('2008')
rbtn2 = QRadioButton('2007')
rbtn3 = QRadioButton('2009')
rbtn4 = QRadioButton('2006')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
ochki = 0


AnsGroupBox = QGroupBox('Результат')
lb_result = QLabel('Правильно чи ні')
lb_Correct = QLabel('Праивльно ответио')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Наступне питання')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Відповісти')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn1,rbtn2,rbtn3,rbtn4]
def ask(q: question1):
    shuffle(answers)
    answers[0].setText(q.true_answer)
    answers[1].setText(q.no_true1)
    answers[2].setText(q.no_true2)
    answers[3].setText(q.no_true3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.true_answer)
    question_list.remove(q)
    show_question()

 
def showw_correct(res):
    lb_result.setText(res)
    show_result()




def check_answer():
    global ochki
    if answers[0].isChecked():
        ochki += 1
        showw_correct('Молодец,ты прибавли 1 очко. теперь их количсетво равно '+ str(ochki))
        
    else:
        ochki -= 1
        showw_correct('ЛОх - 1 оЧкО,и теперь Их  у ТеБя '+str(ochki))
    

def next_question():
    window.cur_question = randint(0, len(question_list)- 1)
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    elif len(question_list) == 0

    q = question_list[window.cur_question]
    ask(q)
def resultat():

def test():

    if 'Відповісти' == btn_ok.text():
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = -1
btn_ok.clicked.connect(test)
window.show()
app.exec()