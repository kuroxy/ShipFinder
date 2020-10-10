import os

class window():
    def __init__(self,winsize):
        self.winsize=tuple(winsize)
        self.buffer = None
        self.clearbuffer("")
        self.clear = "clear"
        if os.name=="nt":
            self.clear="cls"


    def drawscreen(self):
        #clear terminal then draw screen
        os.system(self.clear)

        for i in range(self.winsize[1]):
            print("".join(self.buffer[i]))


    def setpixel(self,pos ,chararcter):
        if pos[0] >= 0 and pos[0] < self.winsize[0] and pos[1] >= 0 and pos[1] < self.winsize[1]:
            self.buffer[pos[1]][pos[0]] = chararcter


    def setpixels(self,pos1,pos2,chararcter):

        if pos1[0] == pos2[0]:
            for y in range(pos1[1],pos2[1]+1):
                self.setpixel((pos1[0],y), chararcter)
        elif pos1[1]==pos2[1]:

            for x in range(pos1[0],pos2[0]+1):
                self.setpixel((x,pos1[1]), chararcter)
        else:
            for y in range(pos1[1],pos2[1]+1):
                for x in range(pos1[0],pos2[0]+1):
                    self.setpixel((x,y), chararcter)


    def clearbuffer(self, chararcter):
        self.buffer = [[chararcter for _ in range(self.winsize[0])] for _ in range(self.winsize[1])]
