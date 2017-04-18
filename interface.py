import ScenarioGenerator
from tkinter import *
import tkinter

def clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#host, name, config=False, ipv4=False, auto=False, broadcast=False, gateway=False, network=False
def addInterfaces():
    clear(mainframe)
    mainframe.grid_rowconfigure(2,weight=1)
    mainframe.grid_columnconfigure(2,weight=1)
    tkinter.Label(mainframe,text="Host").grid(row=1,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="Name").grid(row=2,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="config").grid(row=3,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="IPv4").grid(row=4,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="IPv6").grid(row=5,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="Broadcast").grid(row=6,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="Gateway").grid(row=7,column=0,padx=5,pady=5)
    tkinter.Label(mainframe,text="Network").grid(row=8,column=0,padx=5,pady=5)
    host = tkinter.Entry().grid(row=1,column=1,padx=5,pady=5)
    name = tkinter.Entry().grid(row=2,column=1,padx=5,pady=5)
    config = tkinter.Entry().grid(row=3,column=1,padx=5,pady=5)
    vFour = tkinter.Entry().grid(row=4,column=1,padx=5,pady=5)
    vSix = tkinter.Entry().grid(row=5,column=1,padx=5,pady=5)
    bcast = tkinter.Entry().grid(row=6,column=1,padx=5,pady=5)
    gway = tkinter.Entry().grid(row=7,column=1,padx=5,pady=5)
    net = tkinter.Entry().grid(row=8,column=1,padx=5,pady=5)
    tkinter.Button(mainframe,text="Next Page",command=addContent)
    
def addContent():
    clear(mainframe)
    tkinter.Label(mainframe,text="adding content").pack()
    tkinter.Button(mainframe,text="Next Page",command=addTeam).pack()
    
def addTeam():
    clear(mainframe)
    tkinter.Label(mainframe,text="adding teams").pack()
    tkinter.Button(mainframe,text="Next Page",command=addTeamEvent).pack()
    
def addTeamEvent():
    clear(mainframe)
    tkinter.Label(mainframe,text="adding team events").pack()
    tkinter.Button(mainframe,text="Next Page",command=addEventParams).pack()
    
def addEventParams():
    clear(mainframe)
    tkinter.Label(mainframe,text="adding event parameters").pack()
    tkinter.Button(mainframe,text="Next Page").pack()
    
if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("OCCP Scenario Builder")
    mainframe = Frame(root)
    mainframe.grid(row=0)
    
    scen = ScenarioGenerator.ScenarioGen()
    
    tkinter.Button(mainframe,text="Begin",command=addInterfaces).grid(row=1)
        
    root.mainloop()