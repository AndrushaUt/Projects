import sys

from Click_functions import Clicks
from tkinter import *


class Input:
    def __init__(self, win, cis):
        self.window = win
        self.calculator_input_screen = cis
        self.click_button = Clicks(self.calculator_input_screen)

    def CreateButtons(self):
        button_clear = Button(self.window, text='C', width=7, height=2,
                              command=self.click_button.Clear)
        button_clear.place(x=1, y=112)
        button_change_sign = Button(self.window, text='+/-', width=7, height=2,
                                    command=self.click_button.ChangeSign)
        button_change_sign.place(x=73, y=112)
        button_percent = Button(self.window, text='%', width=7, height=2,
                                command=self.click_button.ToPercent)
        button_percent.place(x=145, y=112)
        button_1 = Button(self.window, text="1", width=7, height=2,
                          command=self.click_button.Click1)
        button_1.place(x=1, y=150)
        button_2 = Button(self.window, text="2", width=7, height=2,
                          command=self.click_button.Click2)
        button_2.place(x=73, y=150)
        button_3 = Button(self.window, text="3", width=7, height=2,
                          command=self.click_button.Click3)
        button_3.place(x=145, y=150)
        button_4 = Button(self.window, text="4", width=7, height=2,
                          command=self.click_button.Click4)
        button_4.place(x=1, y=188)
        button_5 = Button(self.window, text="5", width=7, height=2,
                          command=self.click_button.Click5)
        button_5.place(x=73, y=188)
        button_6 = Button(self.window, text="6", width=7, height=2,
                          command=self.click_button.Click6)
        button_6.place(x=145, y=188)
        button_9 = Button(self.window, text="9", width=7, height=2,
                          command=self.click_button.Click9)
        button_9.place(x=145, y=226)
        button_7 = Button(self.window, text="7", width=7, height=2,
                          command=self.click_button.Click7)
        button_7.place(x=1, y=226)
        button_8 = Button(self.window, text="8", width=7, height=2,
                          command=self.click_button.Click8)
        button_8.place(x=73, y=226)
        button_division = Button(self.window, text="÷", width=7, height=2,
                          command=self.click_button.Click_division)
        button_division.place(x=217, y=226)
        button_0 = Button(self.window, text="0", width=15, height=2,
                          command=self.click_button.Click0)
        button_0.place(x=1, y=264)
        button_dot = Button(self.window, text='.', width=7, height=2,
                            command=self.click_button.Click_dot)
        button_dot.place(x=145, y=264)
        button_plus = Button(self.window, text="+", width=7, height=2,
                             command=self.click_button.Click_plus)
        button_plus.place(y=112, x=217)
        button_minus = Button(self.window, text="-", width=7, height=2,
                              command=self.click_button.Click_minus)
        button_minus.place(y=150, x=217)
        button_multiplication = Button(self.window, text="x", width=7,
                                       height=2,
                                       command=self.click_button.Click_multiplication)
        button_multiplication.place(y=188, x=217)
        button_eq = Button(self.window, text="=", width=7, height=2,
                           command=self.click_button.Click_eq)
        button_eq.place(y=264, x=217)

    def KeyBoardBind(self):
        self.window.bind('0', self.click_button.KeyWordClickNums)
        self.window.bind('1', self.click_button.KeyWordClickNums)
        self.window.bind('2', self.click_button.KeyWordClickNums)
        self.window.bind('3', self.click_button.KeyWordClickNums)
        self.window.bind('4', self.click_button.KeyWordClickNums)
        self.window.bind('5', self.click_button.KeyWordClickNums)
        self.window.bind('6', self.click_button.KeyWordClickNums)
        self.window.bind('7', self.click_button.KeyWordClickNums)
        self.window.bind('8', self.click_button.KeyWordClickNums)
        self.window.bind('9', self.click_button.KeyWordClickNums)
        self.window.bind('+', self.click_button.Click_plus_keyboard)
        self.window.bind('-', self.click_button.Click_minus_keyboard)
        self.window.bind("<BackSpace>", self.click_button.Clear)
        self.window.bind("<Escape>", sys.exit)
        self.window.bind('<Return>', self.click_button.Click_eq)
        self.window.bind('/', self.click_button.Click_division_keyboard)
