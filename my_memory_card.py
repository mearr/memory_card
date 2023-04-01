from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle


class Question:
    def __init__(self, quest,right,wrong1,wrong2,wrong3):
        self.quest = quest
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#app = QApplication Приложение
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
 
#
lb_question = QLabel('Какой национальности не существует?')
layout_label = QVBoxLayout()
layout_label.addWidget(lb_question)
 
#Ответы
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
 
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат теста")
lb_result = QLabel('Вы Правы')
lb_correct = QLabel('Ответ будет здесь')
lb_question = QLabel('Консистенси')
ans_layout = QVBoxLayout()
ans_layout.addWidget(lb_correct)
ans_layout.addWidget(lb_result)
AnsGroupBox.setLayout(ans_layout)
 

 
#pre konec
layout_end = QVBoxLayout()
layout_end.addLayout(layout_label)
layout_end.addWidget(RadioGroupBox)
layout_end.addWidget(AnsGroupBox)
AnsGroupBox.hide()
btn_ok = QPushButton('Ответить')
layout_end.addWidget(btn_ok, stretch=2)
window.setLayout(layout_end)
 
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
 
RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

#KONEC
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')
 
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.quest)
    lb_correct.setText(q.right)
    show_question()
 
def show_correct(result):
    lb_result.setText(result)
    show_result()
 
def check_ok():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')


def next_question():
    window.cur_question += 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_ok.text() == 'Ответить':
        check_ok()
    else:
        next_question()

btn_ok.clicked.connect(click_ok)
window.cur_question = -1
window.show()
app.exec()