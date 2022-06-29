def DeleteZeroes(string):
    if string[-1] == '0' and string[-2] == '0':
        return string[0:len(string) - 3]
    elif string[-1] == '0':
        return string[0:len(string) - 1]
    return string


class Clicks:
    def Clear(self, t=0):
        self.lbl.config(text="0")

    def ChangeSign(self):
        num = self.lbl.cget("text")
        if num == '0':
            return
        if num[0] == '-':
            self.lbl.config(text=num[1:len(num)])
        else:
            self.lbl.config(text='-' + num)

    def ToPercent(self):
        num = self.lbl.cget("text")
        if num == '0':
            return
        val = float(num) / float(100)
        self.lbl.config(text=str(round(val + 10 ** (-len(str(val)) - 1),
                                       len(num[
                                           num.index('.') + 1:len(num)]) + 2)))

    def KeyWordClickNums(self, event, t=0):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = event.char
        else:
            text_of_label += event.char
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Set(self):
        self.Click_eq()
        num = self.lbl.cget("text")
        if num.__contains__('.'):
            self.temp_num = float(num)
        else:
            self.temp_num = int(num)
        self.lbl.config(text="0")

    def Click1(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '1'
        else:
            text_of_label += '1'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click2(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '2'
        else:
            text_of_label += '2'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click3(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '3'
        else:
            text_of_label += '3'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click4(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '4'
        else:
            text_of_label += '4'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click5(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '5'
        else:
            text_of_label += '5'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click6(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '6'
        else:
            text_of_label += '6'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click7(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '7'
        else:
            text_of_label += '7'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click8(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '8'
        else:
            text_of_label += '8'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click9(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '9'
        else:
            text_of_label += '9'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click_dot(self):
        text_of_label = self.lbl.cget("text")
        if not text_of_label.__contains__('.'):
            text_of_label += '.'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click0(self):
        text_of_label = self.lbl.cget("text")
        if text_of_label == '0':
            text_of_label = '0'
        else:
            text_of_label += '0'
        if len(text_of_label) <= 15:
            self.lbl.config(text=text_of_label)

    def Click_plus(self):
        self.Set()
        self.bool_dict['plus_clicked_button'] = True

    def Click_minus(self):
        self.Set()
        self.bool_dict['minus_clicked_button'] = True

    def Click_plus_keyboard(self, t=1):
        self.Set()
        self.bool_dict['plus_clicked_keyword'] = True

    def Click_minus_keyboard(self, t=1):
        self.Set()
        self.bool_dict['minus_clicked_keyword'] = True

    def Click_multiplication(self):
        self.Set()
        self.bool_dict['multiplication_clicked_button'] = True

    def Click_division(self):
        self.Set()
        self.bool_dict['division_clicked_button'] = True

    def Click_division_keyboard(self, t=1):
        self.Set()
        self.bool_dict['division_clicked_keyword'] = True

    def Click_eq(self, t=1):
        if self.bool_dict['plus_clicked_button'] or self.bool_dict[
            'plus_clicked_keyword']:
            num = self.lbl.cget("text")
            if num.__contains__('.'):
                self.temp_num += float(num)
            else:
                self.temp_num += int(num)
        elif self.bool_dict['minus_clicked_button'] or self.bool_dict[
            'minus_clicked_keyword']:
            num = self.lbl.cget("text")
            if num.__contains__('.'):
                self.temp_num -= float(num)
            else:
                self.temp_num -= int(num)
        elif self.bool_dict['multiplication_clicked_button'] or self.bool_dict[
            'multiplication_clicked_keyword']:
            num = self.lbl.cget("text")
            if num.__contains__('.'):
                self.temp_num *= float(num)
            else:
                self.temp_num *= int(num)
        elif self.bool_dict['division_clicked_button'] or self.bool_dict[
            'division_clicked_keyword']:
            num = self.lbl.cget("text")
            if num.__contains__('.'):
                self.temp_num /= float(num)
            else:
                self.temp_num /= int(num)
        else:
            return
        self.Reset('2')
        ans = str(self.temp_num)
        if len(ans) > 15:
            ans = ans[0:15]
        self.lbl.config(text=ans)
        self.temp_num = 0

    def __init__(self, label):
        self.lbl = label
        self.bool_dict = {'plus_clicked_button': False,
                          'minus_clicked_button': False,
                          'multiplication_clicked_button': False,
                          'division_clicked_button': False,
                          'plus_clicked_keyword': False,
                          'minus_clicked_keyword': False,
                          'multiplication_clicked_keyword': False,
                          'division_clicked_keyword': False}
        self.temp_num = 0

    def Reset(self, key_not_to_reset):
        for key in self.bool_dict.keys():
            if key != key_not_to_reset:
                self.bool_dict[key] = False
