import sys
import socket
import threading
import os
from tkinter import *

mGui = Tk()
mGui.geometry("800x500+220+140") # Window Geometry
mGui.title("Aquila Interface")

def DDSControl():
    DDS_Top = Toplevel()
    DDS_Top.geometry("400x200+150+150")
    DDS_Top.title("DDS Controls")    

def VCOControl():
    VCO_Top = Toplevel()
    VCO_Top.geometry("400x200+150+150")
    VCO_Top.title("VCO Controls")    

def PLLControl():
    PLL_Top = Toplevel()
    PLL_Top.geometry("400x200+150+150")
    PLL_Top.title("DDS Controls")    

def EnableAmplifiers():
    print ("Amplifiers Enabled") 

def SystemControl():
    mSC = Toplevel()
    mSC.geometry("600x200+150+150")
    mSC.title("System Control")
    mbutton = Button(mSC,text="DDS Controls",command = DDSControl).place(x=100,y=20)
    mbutton = Button(mSC,text="VCO Controls",command = VCOControl).place(x=200,y=20)
    mbutton = Button(mSC,text="PLL Controls",command = PLLControl).place(x=300,y=20)


#*********************Program Begin*************************

mlabel = Label(mGui,text="Radar Controls").place(x=100,y=20)
mlabel = Label(mGui,text="System Control").place(x=100,y=400)
mlabel = Label(mGui,text="RTI").place(x=400,y=20)
mlabel = Label(mGui,text="Spectrogram").place(x=400,y=400)

mbutton = Button(mGui,text="System Controls",command = SystemControl).place(x=100,y=420)

mRRFLabel = Label(top,text="Ramp Repition Frequency: ").place(x=10,y=220)
mRRFEntry = Entry(top,textvariable=0).place(x=10,y=240)

mConfirm = Button(top,text="Confirm",command=SyncPeriodUpdate).place(x=120,y=240)


##mbutton = Button(mGui,text="Reset PLL",command = ResetPLL).place(x=510,y=20)
##mbutton = Button(mGui,text="VCO Calibration",command = CalibrateVCO).place(x=610,y=20)
##mlabel = Label(mGui,text="PLL Information").place(x=400,y=90)
##PLL_TextBox = Text(mGui,height=8,width=45)
##PLL_TextBox.place(x=400,y=110)
##PLL_Scroll = Scrollbar(PLL_TextBox,command=PLL_TextBox.yview)
##PLL_TextBox.configure(yscrollcommand=PLL_Scroll.set)
##mLockLabel = Label(mGui,textvariable=PLLtextString).place(x=400,y=60)


mGui.mainloop() # Gui Mainloop 
