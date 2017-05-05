from Tkinter import *
from ttk import *
from ScenarioGenerator import *

instance = Instance_Builder()

root = Tk()
note = Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)

class Host_Tab:
    def __init__(self, tab2):
        self.pack_var = StringVar(tab2)
        self.arg_var = StringVar(tab2)
        self.pack_men = OptionMenu(tab2, StringVar(tab2))
        self.arg_men = OptionMenu(tab2, StringVar(tab2))
        
        tab2.pack(side=TOP)
        Label(tab2, text='Scenario').grid(row=0, column=0, columnspan=13, pady=10)
        Label(tab2, text='Description').grid(row=1, column=0)
        self.sdes = Entry(tab2)
        self.sdes.grid(row=1, column=1)
        Label(tab2, text='game-id').grid(row=1, column=2)
        self.sgid = Entry(tab2)
        self.sgid.grid(row=1, column=3)
        Label(tab2, text='name').grid(row=1, column=4)
        self.snam = Entry(tab2)
        self.snam.grid(row=1, column=5)
        Label(tab2, text='type').grid(row=1, column=6)
        self.styp = Entry(tab2)
        self.styp.grid(row=1, column=7)
        Button(tab2, text="Set").grid(row=1, column=12)
        
        Label(tab2, text='Length').grid(row=2, column=0, columnspan=13, pady=10)
        Label(tab2, text='format').grid(row=3, column=0)
        self.slen = Entry(tab2)
        self.slen.grid(row=3, column=1)
        Label(tab2, text='time').grid(row=3, column=2)
        self.stim = Entry(tab2)
        self.stim.grid(row=3, column=3)
        Button(tab2, text='Set').grid(row=3, column = 12)

        Label(tab2, text='Users').grid(row=4, column=0, columnspan=13, pady=10)
        Label(tab2, text='user-name').grid(row=5, column=0)
        self.unam = Entry(tab2)
        self.unam.grid(row=5, column=1)
        Label(tab2, text='password').grid(row=5, column=2)
        self.upas = Entry(tab2)
        self.upas.grid(row=5, column=3)
        Button(tab2, text = "Add").grid(row=5, column=12)

        Label(tab2, text="Active User").grid(row=6, column=0, pady=10)
        opts2 = ["none"]
        self.usr_var = StringVar(tab2)
        self.usr_var.set(opts2[0])
        self.usr_men = apply(OptionMenu, (tab2, self.usr_var) + tuple(opts2))
        self.usr_men.grid(row=6, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_pack).grid(row=6, column=12)

        Label(tab2, text='User-Interface').grid(row=7, column=0, columnspan=13, pady=10)
        Label(tab2, text='name').grid(row=8, column=0)
        self.uinam = Entry(tab2)
        self.uinam.grid(row=8, column=1)
        Label(tab2, text='show-other-controls').grid(row=8, column=2)
        self.soc = Entry(tab2)
        self.soc.grid(row=8, column=3)
        Label(tab2, text='show-scoreboard').grid(row=8, column=4)
        self.uinam = Entry(tab2)
        self.uinam.grid(row=8, column=5)
        Label(tab2, text='show-teams-all').grid(row=8, column=6)
        self.uinam = Entry(tab2)
        self.uinam.grid(row=8, column=7)
        Button(tab2, text = "Add").grid(row=8, column=12)

        Label(tab2, text="Active UI").grid(row=9, column=0, pady=10)
        opts2 = ["none"]
        self.ui_var = StringVar(tab2)
        self.ui_var.set(opts2[0])
        #self.ui_var.trace('w', self.update_ui_men)
        self.ui_men = apply(OptionMenu, (tab2, self.ui_var) + tuple(opts2))
        self.ui_men.grid(row=9, column=1, columnspan=11)
        Button(tab2, text="Remove").grid(row=9, column=12)

        Label(tab2, text="scoreboard").grid(row=10, column=0)
        self.ui_sb = Entry(tab2)
        self.ui_sb.grid(row=10, column=1)
        Button(tab2, text="Set")

    def update_display(self):
        text.delete(1.0, END)
        text.insert(INSERT, str(instance))
        
    def add_host(self):
        instance.add_host(self.bvm.get(), self.dom.get(), self.hon.get(), self.lab.get(), self.pha.get(), self.ram.get())
        self.update_host_men(instance.get_hosts())
        self.update_display()

    def remove_host(self):
        print "meep"
        self.update_host_men(instance.get_hosts())
        self.update_display()

    def set_interface(self):
        instance.set_interface(self.host_var.get(), self.ibc.get(), self.cfg.get(), self.gtw.get(), self.iip.get(), self.ina.get(), self.ine.get())
        self.update_display()

    def update_args(self, *args):
        args = instance.get_args(self.host_var.get(), self.pack_var.get())
        menu = self.arg_men['menu']
        menu.delete(0, 'end')
        for arg in args:
            menu.add_command(label=arg, command=lambda a=arg: self.arg_var.set(a))




textPad=Frame(root)
text=Text(textPad,height=10,width=90)	
# add a vertical scroll bar to the text area
scroll=Scrollbar(textPad)
text.configure(yscrollcommand=scroll.set)
#pack everything
text.insert(INSERT, str(instance))
text.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)
textPad.pack(side=BOTTOM)

merp = Host_Tab(tab2)

note.add(tab1, text = "Network", compound=TOP)
note.add(tab2, text = "Hosts")
note.add(tab3, text = "Tab Three")
note.pack()




root.mainloop()






