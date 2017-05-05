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
        Label(tab2, text='Host VM').grid(row=0, column=0, columnspan=13, pady=10)
        Label(tab2, text='Basevm').grid(row=1, column=0)
        self.bvm = Entry(tab2)
        self.bvm.grid(row=1, column=1)
        Label(tab2, text='Domain').grid(row=1, column=2)
        self.dom = Entry(tab2)
        self.dom.grid(row=1, column=3)
        Label(tab2, text='Hostname').grid(row=1, column=4)
        self.hon = Entry(tab2)
        self.hon.grid(row=1, column=5)
        Label(tab2, text='Label').grid(row=1, column=6)
        self.lab = Entry(tab2)
        self.lab.grid(row=1, column=7)
        Label(tab2, text='Phase').grid(row=1, column=8)
        self.pha = Entry(tab2)
        self.pha.grid(row=1, column=9)
        Label(tab2, text='RAM').grid(row=1, column=10)
        self.ram = Entry(tab2)
        self.ram.grid(row=1, column=11)
        host_add = Button(tab2, text="Add", command=self.add_host)
        host_add.grid(row=1, column=12)

        Label(tab2, text="Active").grid(row=2, column=0, pady=10)
        opts = ["none"]
        self.host_var = StringVar(tab2)
        self.host_var.set(opts[0])
        self.host_var.trace('w', self.update_packs)
        self.host_men = apply(OptionMenu, (tab2, self.host_var) + tuple(opts))
        self.host_men.grid(row=2, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_host).grid(row=2, column=12)

        Label(tab2, text='Interface').grid(row=3, column=0, columnspan=13, pady=10)
        Label(tab2, text='broadcast').grid(row=4, column=0)
        self.ibc = Entry(tab2)
        self.ibc.grid(row=4, column=1)
        Label(tab2, text='config').grid(row=4, column=2)
        self.cfg = Entry(tab2)
        self.cfg.grid(row=4, column=3)
        Label(tab2, text='gateway').grid(row=4, column=4)
        self.gtw = Entry(tab2)
        self.gtw.grid(row=4, column=5)
        Label(tab2, text='ipv4').grid(row=4, column=6)
        self.iip = Entry(tab2)
        self.iip.grid(row=4, column=7)
        Label(tab2, text='name').grid(row=4, column=8)
        self.ina = Entry(tab2)
        self.ina.grid(row=4, column=9)
        Label(tab2, text='network').grid(row=4, column=10)
        self.ine = Entry(tab2)
        self.ine.grid(row=4, column=11)
        Button(tab2, text="Set", command=self.set_interface).grid(row=4, column=12)

        Label(tab2, text="Content").grid(row=5, column=0, columnspan=13, pady=10)
        Label(tab2, text="Config").grid(row=6, column=0)
        self.pcon = Entry(tab2)
        self.pcon.grid(row=6, column=1)
        Label(tab2, text="Name").grid(row=6, column=2)
        self.pnam = Entry(tab2)
        self.pnam.grid(row=6, column=3)
        Button(tab2, text="Add", command=self.add_pack).grid(row=6, column=12)

        Label(tab2, text="Active Pack").grid(row=7, column=0, pady=10)
        opts2 = ["none"]
        self.pack_var = StringVar(tab2)
        self.pack_var.set(opts2[0])
        self.pack_var.trace('w', self.update_args)
        self.pack_men = apply(OptionMenu, (tab2, self.pack_var) + tuple(opts2))
        self.pack_men.grid(row=7, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_pack).grid(row=7, column=12)

        Label(tab2, text="Arguments").grid(row=8, column=0, columnspan=13, pady=10)
        Label(tab2, text="Argument").grid(row=9, column=0)
        self.arg = Entry(tab2)
        self.arg.grid(row=9, column=1)
        Label(tab2, text="Value").grid(row=9, column=2)
        self.val = Entry(tab2)
        self.val.grid(row=9, column=3)
        Button(tab2, text="Add", command=self.add_arg).grid(row=9, column=12)

        Label(tab2, text="Active Pack").grid(row=10, column=0, pady=10)
        opts3 = ["none"]
        self.arg_var = StringVar(tab2)
        self.arg_var.set(opts3[0])
        self.arg_men = apply(OptionMenu, (tab2, self.arg_var) + tuple(opts3))
        self.arg_men.grid(row=10, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_arg).grid(row=10, column=12)

    def update_display(self):
        text.delete(1.0, END)
        text.insert(INSERT, str(instance))
        
    def add_host(self):
        instance.add_host(self.bvm.get(), self.dom.get(), self.hon.get(), self.lab.get(), self.pha.get(), self.ram.get())
        self.update_host_men(instance.get_hosts())
        self.update_display()

    def remove_host(self):
        instance.remove_host(self.host_var.get())
        self.update_host_men(instance.get_hosts())
        self.update_display()

    def set_interface(self):
        instance.set_interface(self.host_var.get(), self.ibc.get(), self.cfg.get(), self.gtw.get(), self.iip.get(), self.ina.get(), self.ine.get())
        self.update_display()

    def add_pack(self):
        instance.add_pack(self.host_var.get(), self.pcon.get(), self.pnam.get())
        self.update_packs()
        self.update_display()

    def remove_pack(self):
        instance.remove_pack(self.host_var.get(), self.pack_var.get())
        self.update_packs()
        self.update_display()

    def add_arg(self):
        instance.add_arg(self.host_var.get(), self.pack_var.get(), self.arg.get(), self.val.get())
        self.update_display()
        self.update_args()

    def remove_arg(self):
        instance.remove_arg(self.host_var.get(), self.pack_var.get(), self.arg_var.get())
        self.update_display()

    def update_host_men(self, opts):
        menu = self.host_men["menu"]
        menu.delete(0, "end")
        for string in opts:
            menu.add_command(label=string, command=lambda value=string: self.host_var.set(value))
        self.update_packs()

    def update_packs(self, *args):
        packs = instance.get_packs(self.host_var.get())
        menu = self.pack_men['menu']
        menu.delete(0, 'end')
        for pack in packs:
            menu.add_command(label=pack, command=lambda p=pack: self.pack_var.set(p))
        self.update_args()

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






