import tkinter

class interface (tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
     
    def initialize(self):
        self.grid()
        
        self.startButton = tkinter.Button(self, text="BEGIN",command=self.addInterfaces)
        self.startButton.grid(column=0,row=0,sticky="EW",padx=5,pady=5)
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        
    def addInterfaces(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.hostLabel = tkinter.Label(text="Host")
        self.hostLabel.grid(column=0,row=0,sticky="EW",padx=5,pady=5)
        
        self.hostEntry = tkinter.Entry()
        self.hostEntry.grid(column=1,row=0,sticky="EW",padx=5,pady=5)
        self.hostEntry.bind("<Return>",self.input(interface))
        interface.append = self.hostEntry.get()
        
        self.nameLabel = tkinter.Label(text="Name")
        self.nameLabel.grid(column=0,row=1,sticky="EW",padx=5,pady=5)
        
        self.nameEntry = tkinter.Entry()
        self.nameEntry.grid(column=1,row=1,sticky="EW",padx=5,pady=5)
        self.nameEntry.bind("<Return>",self.input(interface))
        interface.append = self.nameEntry.get()
        
        self.configLabel = tkinter.Label(text="Config")
        self.configLabel.grid(column=0,row=2,sticky="EW",padx=5,pady=5)
        
        self.configEntry = tkinter.Entry()
        self.configEntry.grid(column=1,row=2,sticky="EW",padx=5,pady=5)
        self.configEntry.bind("<Return>",self.input(interface))
        interface.append = self.configEntry.get()
        
        self.vFourLabel = tkinter.Label(text="IPv4")
        self.vFourLabel.grid(column=0,row=3,sticky="EW",padx=5,pady=5)
        
        self.vFourEntry = tkinter.Entry()
        self.vFourEntry.grid(column=1,row=3,sticky="EW",padx=5,pady=5)
        self.vFourEntry.bind("<Return>",self.input(interface))
        interface.append = self.vFourEntry.get()
        
        self.vSixLabel = tkinter.Label(text="IPv6")
        self.vSixLabel.grid(column=0,row=4,sticky="EW",padx=5,pady=5)
        
        self.vSixEntry = tkinter.Entry()
        self.vSixEntry.grid(column=1,row=4,sticky="EW",padx=5,pady=5)
        self.vSixEntry.bind("<Return>",self.input(interface))
        interface.append = self.vSixEntry.get()
        
        self.broadcastLabel = tkinter.Label(text="Broadcast")
        self.broadcastLabel.grid(column=0,row=5,sticky="EW",padx=5,pady=5)
        
        self.broadcastEntry = tkinter.Entry()
        self.broadcastEntry.grid(column=1,row=5,sticky="EW",padx=5,pady=5)
        self.broadcastEntry.bind("<Return>",self.input(interface))
        interface.append = self.broadcastEntry.get()
        
        self.gatewayLabel = tkinter.Label(text="Gateway")
        self.gatewayLabel.grid(column=0,row=6,sticky="EW",padx=5,pady=5)
        
        self.gatewayEntry = tkinter.Entry()
        self.gatewayEntry.grid(column=1,row=6,sticky="EW",padx=5,pady=5)
        self.gatewayEntry.bind("<Return>",self.input(interface))
        interface.append = self.gatewayEntry.get()
        
        self.netLabel = tkinter.Label(text="Network")
        self.netLabel.grid(column=0,row=7,sticky="EW",padx=5,pady=5)
        
        self.netEntry = tkinter.Entry()
        self.netEntry.grid(column=1,row=7,sticky="EW",padx=5,pady=5)
        self.netEntry.bind("<Return>",self.input(interface))
        interface.append = self.netEntry.get()
        
        self.nextPage = tkinter.Button(text="Next Page",command=self.addContent)
        self.nextPage.grid(column=0,row=8,sticky="EW",padx=5,pady=5,columnspan=2)
        
    def input(self,inputs):
        print(inputs)
    
    def addContent(self):
        print("it works")

if __name__ == "__main__":
    interface = interface(None)
    interface.title("OCCP Scenario Builder")
    interface.mainloop()
    
# def addContent():
    # clear(mainframe)
    
    # tkinter.tix.LabelEntry()
    # tkinter.Label(mainframe,text="adding content")
    # tkinter.Button(mainframe,text="Next Page",command=addTeam)
    
# def addTeam():
    # clear(mainframe)
    # tkinter.Label(mainframe,text="adding teams") 
    # tkinter.Button(mainframe,text="Next Page",command=addTeamEvent) 
    
# def addTeamEvent():
    # clear(mainframe)
    # tkinter.Label(mainframe,text="adding team events") 
    # tkinter.Button(mainframe,text="Next Page",command=addEventParams) 
    
# def addEventParams():
    # clear(mainframe)
    # tkinter.Label(mainframe,text="adding event parameters") 
    # tkinter.Button(mainframe,text="Next Page") 
    
# if __name__ == '__main__':
    # root = tkinter.tix.Tk()
    # root.title("OCCP Scenario Builder")
    # mainframe = Frame(root)
    # mainframe.grid()
    
    # #scen = ScenarioGenerator.ScenarioGen()
    
    # tkinter.Button(mainframe,text="Begin",command=addInterfaces).grid(row=0,column=0,sticky="e",columnspan=2)
        
    # root.mainloop()