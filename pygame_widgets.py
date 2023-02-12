from time import sleep

import pygame as p

class DisplayHolo():
    def __init__(self,WIDTH_SCREEN,HEIGHT_SCREEN,BORDER_SCREEN, color='cyan'):
        self.surf = p.surface.Surface((WIDTH_SCREEN-BORDER_SCREEN*2,HEIGHT_SCREEN-BORDER_SCREEN*2))
        self.color=color
        self.surf.fill('black')
        self.lb = Label(self.surf,"test",0,0,color,)
        self.new = p.transform.flip(self.lb.get_self(), True, True)
        # self.textrect = self.lb.get_self().get_rect()
        # self.textrect.centerx = display.get_rect().centerx
        # self.textrect.centery = display.get_rect().centery
    def set_text(self, text):
        # self.lb.set_text(text)
        self.surf.fill('black')
        self.lb = Label(self.surf, text, 0, 0, self.color, )
        self.new = p.transform.flip(self.lb.get_self(), False, True)

class LabelBg():
    def __init__(self, master, text, x,y,width, height,colorText,colorBg,fontsize=18):
        self.master, self.text, self.x, self.y, self.width, self.height = master, text, x, y, width, height
        font = p.font.SysFont('Consolas',fontsize)
        testStr = font.render(self.text,1,colorText)
        wgt = p.draw.rect(self.master,colorBg,(x,y,width,height))
        master.blit(testStr,(x,y))
    def set_text(self,text):
        self.text = text
        testStr = font.render(text,1,colorText)


class Label():
    def __init__(self, master, text, x,y,colorText,fontsize=38):
        self.colorText = colorText
        self.master, self.text, self.x, self.y = master, text, x, y,
        self.font = p.font.SysFont('Consolas',fontsize)
        self.testStr = self.font.render(self.text,1,colorText)
        master.blit(self.testStr,(x,y))
    def get_self(self):
        return self.testStr
    def set_text(self,text):
        self.text = text
        testStr = self.font.render(text,1,self.colorText)


class Button():
    def __init__(self, master, text, x, y, xt=0,yt=0, width=200, height=70, colorText=(255,255,255), colorBg=(50,50,50),colorBgOk=(0,255,0),command=False):
        self.master, self.text, self.x, self.y, self.width, self.height = master, text, x, y, width, height
        self.colorText,self.colorBg, self.colorBgOk = colorText, colorBg, colorBgOk
        self.xt,self.yt = xt,yt
        self.command = command
        self.activeBtn = False
        font = p.font.SysFont('Consolas', 20)
        self.testStr = font.render(self.text, 1, colorText)
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        master.blit(self.testStr, (xt, yt))

    def getValue(self):
        mx, my = p.mouse.get_pos()
        # print(f"""{self.x} < {mx} < {self.width} and {self.y} < {my} < {self.height}""")
        if self.x < mx < self.width and self.y < my < self.height and p.mouse.get_pressed()[0] == True:
            print(p.mouse.get_pressed())
            if self.activeBtn == False:
                self.wgt = p.draw.rect(self.master, self.colorBgOk, (self.x, self.y, self.width, self.height))
                self.master.blit(self.testStr, (self.xt, self.yt))
                # print("CLICK")
                if self.command != False:
                    self.command()
                self.activeBtn = True
                # sleep(0.5)
            if self.activeBtn == True:
                self.activeBtn = False
                self.wgt = p.draw.rect(self.master, self.colorBg, (self.x, self.y, self.width, self.height))
                self.master.blit(self.testStr, (self.xt, self.yt))

            return True
        else:
            return False

    def wait(self):
        self.getValue()


class ButtonImage():
    def __init__(self, master, text, x, y, width, height, colorText, colorBg):
        self.master, self.text, self.x, self.y, self.width, self.height = master, text, x, y, width, height
        font = p.font.SysFont('Consolas', 20)
        testStr = font.render(self.text, 1, colorText)
        wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        master.blit(testStr, (0, 0))

    def getValue(self):
        mx, my = p.mouse.get_pos()
        # print(f"""{self.x} < {mx} < {self.width} and {self.y} < {my} < {self.height}""")
        if self.x < mx < self.width and self.y < my < self.height:
            return True
        else:
            return False


class ButtonPick():
    def __init__(self, master, text, x, y, xt=0,yt=0, width=200, height=70, colorText=(255,255,255), colorBg=(50,50,50),colorBgOk=(0,255,0),command=False):
        self.master, self.text, self.x, self.y, self.width, self.height = master, text, x, y, width, height
        self.colorText,self.colorBg, self.colorBgOk = colorText, colorBg, colorBgOk
        self.xt,self.yt = xt,yt
        self.command = command
        self.activeBtn = False
        font = p.font.SysFont('Consolas', 20)
        self.testStr = font.render(self.text, 1, colorText)
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        master.blit(self.testStr, (xt, yt))

    def getValue(self):
        mx, my = p.mouse.get_pos()
        # print(f"""{self.x} < {mx} < {self.width} and {self.y} < {my} < {self.height}""")
        if self.x < mx < self.width and self.y < my < self.height and p.mouse.get_pressed()[0]:
            if self.activeBtn == False:
                self.wgt = p.draw.rect(self.master, self.colorBgOk, (self.x, self.y, self.width, self.height))
                self.master.blit(self.testStr, (self.xt, self.yt))
                if self.command != False:
                    self.command()
                self.activeBtn = None
            if self.activeBtn == True:
                self.activeBtn = False
                self.wgt = p.draw.rect(self.master, self.colorBg, (self.x, self.y, self.width, self.height))
                self.master.blit(self.testStr, (self.xt, self.yt))
            if self.activeBtn == None:
                self.activeBtn = True

        return self.activeBtn




class Histogram():
    def __init__(self, master,x, y,width, height, colorBg, colorProgress, percent ):
        self.master, self.x, self.y, self.width, self.height = master, x, y, width, height
        self.colorBg, self.colorProcess = colorBg, colorProgress
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        self.progress = p.draw.rect(self.master, colorProgress, (x, height-percent, width, percent))


class HistogramPercentVertical():
    def __init__(self, master,x, y,width, height, colorBg, colorProgress, percent ):
        self.master, self.x, self.y, self.width, self.height = master, x, y, width, height
        self.colorBg, self.colorProcess = colorBg, colorProgress
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        px1 = int(height / 100)
        # print(height, px1)
        self.progress = p.draw.rect(self.master, colorProgress, (x, height-(px1*percent), width, (px1*percent)))


class HistogramPercentHorizontal():
    def __init__(self, master,x, y,width, height, colorBg, colorProgress, percent ):
        self.master, self.x, self.y, self.width, self.height = master, x, y, width, height
        self.colorBg, self.colorProcess = colorBg, colorProgress
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        px1 = int(width / 100)
        # print(height, px1)
        self.progress = p.draw.rect(self.master, colorProgress, (x, y, (px1*percent),height))

class HistogramPercentVerticalData():
    def __init__(self, master,x, y,width, height, colorBg, colorProgress, percent, allnum):
        self.master, self.x, self.y, self.width, self.height = master, x, y, width, height
        self.colorBg, self.colorProcess = colorBg, colorProgress
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        px1 = int(height / allnum)
        # print(height, px1)
        self.progress = p.draw.rect(self.master, colorProgress, (x, y+height-(px1*percent), width, (px1*percent)))


class HistogramPercentHorizontalData():
    def __init__(self, master,x, y,width, height, colorBg, colorProgress, percent ,allnum):
        self.master, self.x, self.y, self.width, self.height = master, x, y, width, height
        self.colorBg, self.colorProcess = colorBg, colorProgress
        self.wgt = p.draw.rect(self.master, colorBg, (x, y, width, height))
        px1 = int(width / allnum)
        # print(height, px1)
        self.progress = p.draw.rect(self.master, colorProgress, (x, y, (px1*percent),height))

