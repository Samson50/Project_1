import tkinter
from tkinter import ttk

class RootDNS:
    def __init__(self):
        self.entries = []
        #self.entries.append(DNSEntry("tempName","tempType","tempVal"))
        #self.entries.append(DNSEntry("tempName2","tempType2","tempVal2"))
        
    def addEntry(self,name,type,value,parent):
        self.entries.append(DNSEntry(name,type,value))
        updateDisplayFrame(parent,self.entries)

class DNSEntry:
    def __init__(self,name,type,value):
        self.name = name
        self.type = type
        self.value = value
        
class Network:
    def __init__(self):
        self.entries = []
        #self.entries.append("temp")
        #self.entries.append("temp2")
     
    def addEntry(self,label,parent):
        self.entries.append(label)
        updateDisplayFrame(parent,self.entries)
        
class EventHandlers:
    def __init__(self):
        self.entries = []
        self.entries.append(Handler("testClass","testName","testServerHost","testServerIP","testServerPort"))
        self.entries.append(Handler("testClass2","testName2","testServerHost2","testServerIP2","testServerPort2"))
    
    def addEntry(self,classHandler,name,serverHostname,serverIP,serverPort,parent):
        self.entries.append(Handler(classHandler,name,serverHostname,serverIP,serverPort))
        updateDisplayFrame(parent,self.entries)

class Handler:
    def __init__(self,classHandler,name,serverHostname,serverIP,serverPort):
        self.classHandler = classHandler
        self.name = name
        self.serverHostname = serverHostname
        self.serverIP = serverIP
        self.serverPort = serverPort
        
def updateDisplayFrame(frame,data):
    row = 0
    for entry in data:
        if (isinstance(entry,DNSEntry)):
            name = tkinter.Label(frame,text=entry.name)
            name.grid(column=0,row=row,sticky="EW",padx=5,pady=5)
            type = tkinter.Label(frame,text=entry.type)
            type.grid(column=1,row=row,sticky="EW",padx=5,pady=5)
            value = tkinter.Label(frame,text=entry.value)
            value.grid(column=2,row=row,sticky="EW",padx=5,pady=5)
        if (isinstance(entry,Handler)):
            classHandler = tkinter.Label(frame,text=entry.classHandler)
            classHandler.grid(column=0,row=row,sticky="EW",padx=5,pady=5)
            name = tkinter.Label(frame,text=entry.name)
            name.grid(column=1,row=row,sticky="EW",padx=5,pady=5)
            serverHostname = tkinter.Label(frame,text=entry.serverHostname)
            serverHostname.grid(column=2,row=row,sticky="EW",padx=5,pady=5)
            serverIP = tkinter.Label(frame,text=entry.serverIP)
            serverIP.grid(column=3,row=row,sticky="EW",padx=5,pady=5)
            serverPort = tkinter.Label(frame,text=entry.serverPort)
            serverPort.grid(column=4,row=row,sticky="EW",padx=5,pady=5)
        else: 
            label = tkinter.Label(frame,text=entry)
            label.grid(column=0,row=row,sticky="EW",padx=5,pady=5)
        row += 1

if __name__ == "__main__":
    root = tkinter.Tk()
    note = tkinter.ttk.Notebook(root)
    
    root.title("OCCP Scenario Builder")
    
    # Tabs
    networkTab = tkinter.Frame(note)
    hostsTab = tkinter.Frame(note)
    scenarioTab = tkinter.Frame(note)
    ipPoolsTab = tkinter.Frame(note)
    eventHandlersTab = tkinter.Frame(note)
    teamsTab = tkinter.Frame(note)
    
    # NETWORK TAB
    dnsFrame = tkinter.Frame(networkTab)
    dnsFrame.grid()
    dnsFrame.grid(column=0,row=0)
    netFrame = tkinter.Frame(networkTab)
    netFrame.grid()
    netFrame.grid(column=0,row=1)
    
    dnsTitle = tkinter.Label(dnsFrame,text="DNS Records")
    dnsTitle.grid(column=0,row=0,sticky="EW",padx=5,pady=5,columnspan=4)
    
    nameLabel = tkinter.Label(dnsFrame,text="Name")
    nameLabel.grid(column=0,row=1,sticky="EW",padx=5,pady=5)
    typeLabel = tkinter.Label(dnsFrame,text="Type")
    typeLabel.grid(column=1,row=1,sticky="EW",padx=5,pady=5)
    valueLabel = tkinter.Label(dnsFrame,text="Value")
    valueLabel.grid(column=2,row=1,sticky="EW",padx=5,pady=5)
    
    rootDNS = RootDNS()
    recordsFrame = tkinter.Frame(dnsFrame)
    recordsFrame.grid()
    recordsFrame.grid(column=0,row=3,columnspan=4)
    
    nameEntry = tkinter.Entry(dnsFrame)
    nameEntry.grid(column=0,row=2,sticky="EW",padx=5,pady=5)
    typeEntry = tkinter.Entry(dnsFrame)
    typeEntry.grid(column=1,row=2,sticky="EW",padx=5,pady=5)
    valueEntry = tkinter.Entry(dnsFrame)
    valueEntry.grid(column=2,row=2,sticky="EW",padx=5,pady=5)
    addButton = tkinter.Button(dnsFrame,text="Add",command= lambda:rootDNS.addEntry(nameEntry.get(),typeEntry.get(),valueEntry.get(),recordsFrame))
    addButton.grid(column=3,row=2,sticky="EW",padx=5,pady=5)
    updateDisplayFrame(recordsFrame,rootDNS.entries)
    
    entryFrame = tkinter.Frame(dnsFrame)
    
    netTitle = tkinter.Label(netFrame,text="Network Labels")
    netTitle.grid(column=0,row=0,sticky="EW",padx=5,pady=5,columnspan=3)
    
    net = Network()
    labelsFrame = tkinter.Frame(netFrame)
    labelsFrame.grid()
    labelsFrame.grid(column=0,row=2,columnspan=3)
    
    label = tkinter.Label(netFrame,text="Label")
    label.grid(column=0,row=1,sticky="EW",padx=5,pady=5)
    entry = tkinter.Entry(netFrame)
    entry.grid(column=1,row=1,sticky="EW",padx=5,pady=5)
    addButton = tkinter.Button(netFrame,text="Add",command = lambda:net.addEntry(entry.get(),labelsFrame))
    addButton.grid(column=2,row=1,sticky="EW",padx=5,pady=5)
    updateDisplayFrame(labelsFrame,net.entries)
    
    #EVENT HANDLERS TAB
    
    addFrame = tkinter.Frame(eventHandlersTab)
    addFrame.grid()
    addFrame.grid(column=0,row=0,columnspan=5)
    entriesFrame = tkinter.Frame(eventHandlersTab)
    entriesFrame.grid()
    entriesFrame.grid(column=0,row=1,columnspan=5)
    
    eventHandlers = EventHandlers()
    
    title = tkinter.Label(addFrame,text="Event Handlers")
    title.grid(column=0,row=0,sticky="EW",padx=5,pady=5,columnspan=5)
    classHandlerLabel = tkinter.Label(addFrame,text="Class Handler")
    classHandlerLabel.grid(column=0,row=1,sticky="EW",padx=5,pady=5)
    nameLabel = tkinter.Label(addFrame,text="Name")
    nameLabel.grid(column=1,row=1,sticky="EW",padx=5,pady=5)
    serverHostname = tkinter.Label(addFrame,text="Server Hostname")
    serverHostname.grid(column=2,row=1,sticky="EW",padx=5,pady=5)
    serverIPLabel = tkinter.Label(addFrame,text="Server IP")
    serverIPLabel.grid(column=3,row=1,sticky="EW",padx=5,pady=5)
    serverPortLabel = tkinter.Label(addFrame,text="Server Port")
    serverPortLabel.grid(column=4,row=1,sticky="EW",padx=5,pady=5)
    
    classHandlerEntry = tkinter.Entry(addFrame)
    classHandlerEntry.grid(column=0,row=2,sticky="EW",padx=5,pady=5)
    nameEntry = tkinter.Entry(addFrame)
    nameEntry.grid(column=1,row=2,sticky="EW",padx=5,pady=5)
    serverHostnameEntry = tkinter.Entry(addFrame)
    serverHostnameEntry.grid(column=2,row=2,sticky="EW",padx=5,pady=5)
    serverIPEntry = tkinter.Entry(addFrame)
    serverIPEntry.grid(column=3,row=2,sticky="EW",padx=5,pady=5)
    serverPortEntry = tkinter.Entry(addFrame)
    serverPortEntry.grid(column=4,row=2,sticky="EW",padx=5,pady=5)
    addButton = tkinter.Button(addFrame,text="Add",command = lambda:eventHandlers.addEntry(classHandlerEntry.get(),nameEntry.get(),serverHostnameEntry.get(),serverIPEntry.get(),serverPortEntry.get(),entriesFrame))
    addButton.grid(column=0,row=3,columnspan=5)
    updateDisplayFrame(entriesFrame,eventHandlers.entries)
    
    #Adding to the Notebook
    note.add(networkTab,text="Network")
    note.add(hostsTab,text="Hosts")
    note.add(scenarioTab,text="Scenario")
    note.add(ipPoolsTab,text="IP Pools")
    note.add(eventHandlersTab,text="Event Handlers")
    note.add(teamsTab,text="Teams")
    
    note.grid()
    
    root.mainloop()
    exit()