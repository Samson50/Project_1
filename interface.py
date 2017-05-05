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

class Host:
    def __init__(self):
        pass

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
        else: 
            label = tkinter.Label(frame,text=entry)
            label.grid(column=0,row=row,sticky="EW",padx=5,pady=5)
        row += 1

if __name__ == "__main__":
    root = tkinter.Tk()
    note = tkinter.ttk.Notebook(root)
    
    root.title("OCCP Scenario Builder")
    
    networkTab = tkinter.Frame(note)
    hostsTab = tkinter.Frame(note)
    
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
    
    note.add(networkTab,text="Network")
    note.add(hostsTab,text="Hosts")
    
    note.grid()
    
    root.mainloop()
    exit()