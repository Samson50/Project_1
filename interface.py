from tkinter import *
from ttk import *
from ScenarioGenerator import *

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

class Net_Tab:
    def __init__(self, tab2):
        tab2.pack(side=TOP)
        Label(tab2, text='DNS Entries').grid(row=0, column=0, columnspan=13, pady=10)
        Label(tab2, text='name').grid(row=1, column=0)
        self.dnam = Entry(tab2)
        self.dnam.grid(row=1, column=1)
        Label(tab2, text='rrtype').grid(row=1, column=2)
        self.rrt = Entry(tab2)
        self.rrt.grid(row=1, column=3)
        Label(tab2, text='value').grid(row=1, column=4)
        self.val = Entry(tab2)
        self.val.grid(row=1, column=5)
        Button(tab2, text="Add", command=self.add_dns).grid(row=1, column = 12)

        Label(tab2, text="Active").grid(row=2, column=0, pady=10)
        opts = ["none"]
        self.dns_var = StringVar(tab2)
        self.dns_var.set(opts[0])
        self.dns_men = apply(OptionMenu, (tab2, self.dns_var) + tuple(opts))
        self.dns_men.grid(row=2, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_dns).grid(row=2, column=12)

        Label(tab2, text='Network').grid(row=3, column=0, columnspan=13, pady=10)
        Label(tab2, text='label').grid(row=4, column=0)
        self.nam = Entry(tab2)
        self.nam.grid(row=4, column=1)
        Button(tab2, text="Add", command=self.add_net).grid(row=4, column = 12)

        Label(tab2, text="Active").grid(row=5, column=0, pady=10)
        opts = ["none"]
        self.net_var = StringVar(tab2)
        self.net_var.set(opts[0])
        self.net_men = apply(OptionMenu, (tab2, self.net_var) + tuple(opts))
        self.net_men.grid(row=6, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_net).grid(row=6, column=12)

    def add_net(self):
        instance.add_network(self.nam.get())
        self.update_display()
        self.update_net()
                                                            
    def remove_net(self):
        instance.remove_net(self.net_var.get())
        self.update_display()
        self.update_net()

    def update_net(self):
        menu = self.net_men["menu"]
        menu.delete(0, "end")
        for string in instance.networks:
            string = string.strip()
            menu.add_command(label=string, command=lambda value=string: self.net_var.set(value))

    def add_dns(self):
        instance.add_dns_entry(self.dnam.get(), self.rrt.get(), self.val.get())
        self.update_display()
        self.update_dns()

    def remove_dns(self):
        instance.remove_dns(self.dns_var.get())
        self.update_display()
        self.update_dns()

    def update_dns(self):
        menu = self.dns_men["menu"]
        menu.delete(0, "end")
        for string in instance.dns:
            string = string.strip()
            menu.add_command(label=string, command=lambda value=string: self.dns_var.set(value))

    def update_display(self):
        text.delete(1.0, END)
        text.insert(INSERT, str(instance))

class Event_Tab:
    def __init__(self, tab2):
        tab2.pack(side=TOP)
        Label(tab2, text='Handlers').grid(row=0, column=0, columnspan=13, pady=10)
        Label(tab2, text='class-handler').grid(row=1, column=0)
        self.chan = Entry(tab2)
        self.chan.grid(row=1, column=1)
        Label(tab2, text='name').grid(row=1, column=2)
        self.nam = Entry(tab2)
        self.nam.grid(row=1, column=3)
        Label(tab2, text='server-hostname').grid(row=1, column=4)
        self.shn = Entry(tab2)
        self.shn.grid(row=1, column=5)
        Label(tab2, text='server-ip').grid(row=1, column=6)
        self.sip = Entry(tab2)
        self.sip.grid(row=1, column=7)
        Label(tab2, text='server-port').grid(row=1, column=8)
        self.sport = Entry(tab2)
        self.sport.grid(row=1, column=9)
        Button(tab2, text="Add", command=self.add_event).grid(row=1, column=12)

        Label(tab2, text="Active").grid(row=2, column=0, pady=10)
        opts = ["none"]
        self.event_var = StringVar(tab2)
        self.event_var.set(opts[0])
        self.event_men = apply(OptionMenu, (tab2, self.event_var) + tuple(opts))
        self.event_men.grid(row=2, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_event).grid(row=2, column=12)

    def add_event(self):
        instance.event_handlers.add_handler(self.chan.get(), self.nam.get(), self.shn.get(), self.sip.get(), self.sport.get())
        self.update_display()
        self.update_event()

    def remove_event(self):
        instance.event_handlers.remove_handler(self.event_var.get())
        self.update_display()
        self.update_event()

    def update_event(self):
        menu = self.event_men["menu"]
        menu.delete(0, "end")
        for string in instance.event_handlers.handlers:
            string = string.strip()
            menu.add_command(label=string, command=lambda value=string: self.event_var.set(value))

    def update_display(self):
        text.delete(1.0, END)
        text.insert(INSERT, str(instance))

class Pools_Tab:
    def __init__(self, tab2):
        tab2.pack(side=TOP)
        Label(tab2, text='IP-Pool').grid(row=0, column=0, columnspan=13, pady=10)
        Label(tab2, text='cidr').grid(row=1, column=0)
        self.cidr = Entry(tab2)
        self.cidr.grid(row=1, column=1)
        Label(tab2, text='name').grid(row=1, column=2)
        self.nam = Entry(tab2)
        self.nam.grid(row=1, column=3)
        Label(tab2, text='network').grid(row=1, column=4)
        self.net = Entry(tab2)
        self.net.grid(row=1, column=5)
        Button(tab2, text="Add", command=self.add_pool).grid(row=1, column=12)

        Label(tab2, text="Active").grid(row=2, column=0, pady=10)
        opts = ["none"]
        self.pool_var = StringVar(tab2)
        self.pool_var.set(opts[0])
        self.pool_men = apply(OptionMenu, (tab2, self.pool_var) + tuple(opts))
        self.pool_men.grid(row=2, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_pool).grid(row=2, column=12)

        Label(tab2, text="Address").grid(row=3, column=0, columnspan=13, pady=10)
        Label(tab2, text="addr").grid(row=4, column=0)
        self.addr = Entry(tab2)
        self.addr.grid(row=4, column=1)
        Label(tab2, text="count").grid(row=4, column=2)
        self.cnt = Entry(tab2)
        self.cnt.grid(row=4, column=3)
        Label(tab2, text="select").grid(row=4, column=4)
        self.sel = Entry(tab2)
        self.sel.grid(row=4, column=5)
        Label(tab2, text="type").grid(row=4, column=6)
        self.typ = Entry(tab2)
        self.typ.grid(row=4, column=7)
        Button(tab2, text="Add", command=self.add_addr).grid(row=4, column=12)

        Label(tab2, text="Active").grid(row=5, column=0, pady=10)
        opts = ["none"]
        self.addr_var = StringVar(tab2)
        self.addr_var.set(opts[0])
        self.addr_men = apply(OptionMenu, (tab2, self.addr_var) + tuple(opts))
        self.addr_men.grid(row=5, column=1, columnspan=11)
        Button(tab2, text="Remove", command=self.remove_addr).grid(row=5, column=12)

    def add_addr(self):
        instance.add_address(self.pool_var.get(), self.addr.get(), self.cnt.get(), self.sel.get(), self.typ.get())
        self.update_display()
        self.update_addr()

    def remove_addr(self):
        print "asdf"

    def update_addr(self):
        print "asdf"

    def add_pool(self):
        instance.ip_pools.add_pool(self.cidr.get(), self.nam.get(), self.net.get())
        self.update_display()
        self.update_pool()

    def remove_pool(self):
        instance.ip_pools.remove_pool(self.pool_var.get())
        self.update_display()
        self.update_pool()

    def update_pool(self):
        menu = self.pool_men["menu"]
        menu.delete(0, "end")
        for string in instance.ip_pools.pools:
            string = string.show()
            menu.add_command(label=string, command=lambda value=string: self.pool_var.set(value))

    def update_display(self):
        text.delete(1.0, END)
        text.insert(INSERT, str(instance))

if __name__ == "__main__":

    instance = Instance_Builder()
    root = Tk()
    note = Notebook(root)
    
    root.title("OCCP Scenario Builder")
    
    # Tabs
    networkTab = Frame(note)
    hostsTab = Frame(note)
    scenarioTab = Frame(note)
    ipPoolsTab = Frame(note)
    eventHandlersTab = Frame(note)
    teamsTab = Frame(note)
    
    # NETWORK TAB
    herp = Net_Tab(networkTab)
    
    #EVENT HANDLERS TAB

    flrp = Pools_Tab(ipPoolsTab)
    
    derp = Event_Tab(eventHandlersTab)

    merp = Host_Tab(hostsTab)
    
    #Adding to the Notebook
    note.add(networkTab,text="Network")
    note.add(hostsTab,text="Hosts")
    note.add(scenarioTab,text="Scenario")
    note.add(ipPoolsTab,text="IP Pools")
    note.add(eventHandlersTab,text="Event Handlers")
    note.add(teamsTab,text="Teams")
    
    note.pack()

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
    
    root.mainloop()
    exit()
