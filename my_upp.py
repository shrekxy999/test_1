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
