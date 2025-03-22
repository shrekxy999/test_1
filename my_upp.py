from instr import *
class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_apper()#устанавливает как будет выглядеть окно
    self.initUI()
    self.connects()
    self.show()
  
  def set_appear(self): 
        pass
    def initUI(self): 
        pass
    def connects(self): 
        pass
  def set_appear(self):
    
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
    def initUI(self):
self.hello_text = QLabel( txt_hello )
self. instruction = QLabel( txt_instruction)
self. button = PushButton( txt_next )
self.layout = QVBoxLayout()
self.layout .addWidget(self.hello_text)
self. layout.addWidget(self instruction)
self. layout.addWidget(self.button)

from instr import * class MainWin(QWidget) :
def initUI(self):
self.hello_text = Label(txt_hello)
self. instruction = QLabel(txt_instruction)
self.button = PushButton(txt_next)

def connects (self) :
self.btn_next.clicked.connect(self.next_click)
def next_click(self) :
