from Calculator_Input import *

window = Tk()
calculator_input_screen = Label(window, text="0", width=15, height=3,
                                font="Britannic 30",
                                background="#45a6f5", anchor="e",
                                borderwidth=2, relief="solid")
window.title("Calculator")
window.config(background="#7ec4fc")
window.geometry("291x303+500+200")
window.iconbitmap("calculator_icon.ico")
window.resizable(False, False)
calculator_input_screen.place(x=0, y=0)
calculator_input = Input(window, calculator_input_screen)
calculator_input.CreateButtons()
calculator_input.KeyBoardBind()
window.mainloop()
