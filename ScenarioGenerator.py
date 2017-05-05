import xml.etree.ElementTree as ET

class Pack:
    def __init__(self, config, name):
        self.config = config
        self.name = name
        self.args = {}

    def __str__(self):
        ret = '\t\t\t<pack config="%s" name="%s">\n' % (self.config, self.name)
        for arg in self.args:
            ret += "\t\t\t\t<"+arg+">"+self.args[arg]+"</"+arg+">\n"
        ret += "\t\t\t</pack>\n"
        return ret
		
    def sharg(self, arg):
        return "<"+arg+">"+self.args[arg]+"</"+arg+">"
		
    def show(self):
        return '<pack config="%s" name="%s">' % (self.config, self.name)

    def add_arg(self, arg, val):
        self.args[arg] = val

class Content:
    def __init__(self):
        self.packs = []

    def __str__(self):
        ret = '\t\t<content>\n'
        for pack in self.packs:
            ret += str(pack)
        ret += '\t\t</content>\n'
        return ret
        
    def add_pack(self, config, name):
        self.packs += [Pack(config, name)]

class Interface:
    def __init__(self, broadcast, config, gateway, ipv4, name, network):
        self.broadcast = broadcast
        self.config = config
        self.gateway = gateway
        self.ipv4 = ipv4
        self.name = name
        self.network = network

    def __str__(self):
        ret = '\t\t<interface broadcast="%s" config="%s" gateway="%s" ipv4="%s" name="%s" network="%s"/>\n' % (self.broadcast, self.config, self.gateway, self.ipv4, self.name, self.network)
        return ret
    
class Host:
    def __init__(self, basevm, domain, hostname, label, phase, ram):
        self.basevm = basevm
        self.domain = domain
        self.hostname = hostname
        self.label = label
        self.phase = phase
        self.ram = ram
        self.content = Content()
        self.interfaces = []

    def __str__(self):
        ret = '\t<host basevm="%s" domain="%s" hostname="%s" label="%s" phase="%s" ram="%s">\n' % (self.basevm, self.domain, self.hostname, self.label, self.phase, self.ram)
        ret += str(self.content)
        for interface in self.interfaces:
            ret += str(interface)
        ret += "\t</host>\n"
        return ret
		
    def show(self):
        return '<host basevm="%s" domain="%s" hostname="%s" label="%s" phase="%s" ram="%s">' % (self.basevm, self.domain, self.hostname, self.label, self.phase, self.ram)
    
    def add_interface(self, broadcast, config, gateway, ipv4, name, network):
        self.interfaces += [Interface(broadcast, config, gateway, ipv4, name, network)]

class User_Interface:
    def __init__(self, name, soc, showboard, sta):
        self.name = name
        self.soc = soc
        self.showboard = showboard
        self.sta = sta
        self.board = ""
        self.permitted_users = []

    def __str__(self):
        ret = '\t\t\t<user-interface name="%s" show-other-controls="%s" show-scoreboard="%s" show-teams-all="%s">\n' % (self.name, self.soc, self.showboard, self.sta)
        if self.board != "":
            ret += '\t\t\t\t<scoreboard name="%s"/>\n' % (self.board)
        ret += '\t\t\t\t<permitted-users>\n'
        for usr in self.permitted_users:
            ret += '\t\t\t\t\t<user name="%s"/>\n' % (usr)
        ret += '\t\t\t\t</permitted-users>\n'
        ret += '\t\t\t</user-interface>\n'

    def add_user(self, name):
        self.permitted_users += [name]

    def remove_user(self, name):
        try:
            self.permitted_users.remove(name)
        except:
            print "No such user: "+name

    def set_scoreboard(self, name):
        self.board = name

class Scoreboard:
    def __init__(self, name, update_rate):
        self.name = name
        self.update_rate = update_rate
        self.score_name = []

    def __str__(self):
        ret = '\t\t\t<scoreboard name="%s" update-rate="%s">\n' % (self.name, self.update_rate)
        ret += self.score_name
        ret += '\t\t\t</scoreboard>\n'

    def set_name(self, name):
        self.score_name += ['\t\t\t\t<score-name name="%s"/>\n' % (name)]

class Scenario:
    def __init__(self, description, gameid, name, tipe):
        self.description = description
        self.gameid = gameid
        self.name = name
        self.tipe = tipe
        self.length = ""
        self.networkid = ""
        self.users = []
        self.user_interfaces = []
        self.score_labels = []
        self.score_names = []
        self.scoreboards = []

    def __str__(self):
        ret = '\t<scenario description="%s" gameid="%s" name="%s" type="%s">\n' % (self.description, self.gameid, self.name, self.tipe)
        ret += self.length
        ret += self.networkid
        ret += '\t\t<users>\n'
        for user in self.users:
            ret += user
        ret += '\t\t</users>\n'
        ret += '\t\t<user-interfaces>\n'
        for ui in self.user_interfaces:
            ret += ui
        ret += '\t\t</user-interfaces>\n'
        ret += '\t\t<score-labels>\n'
        for label in self.score_labels:
            ret += label
        ret += '\t\t</score-labels>\n'
        ret += '\t\t<score-names>\n'
        for nam in self.score_names:
            ret += nam
        ret += '\t\t</score-names>\n'
        ret += '\t\t<scoreboards>\n'
        for scoreboard in self.scoreboards:
            ret += scoreboard
        ret += '\t\t</scoreboards>\n'
        ret += '\t</scenario>\n'
        return ret

    def set_length(self, format, time):
        self.length = '\t\t<length format="%s" time="%s"/>\n' % (format, time)

    def set_networkid(self, number):
        self.networkid = '\t\t<networkid number="%s"/>\n' % (number)

    def add_user(self, name, passwd):
        self.users += ['\t\t\t<user name="%s" pass="%s"/>\n' % (name, passwd)]

    def add_interface(self, name, soc, showboard, sta):
        self.user_interfaces += User_Interface(name, soc, showboard, sta)

    def add_score_label(self, name, sql):
        self.score_labels += ['\t\t\t<score-label name="%s" sql="%s"/>\n' % (name, sql)]

    def add_score_name(self, descr, formula, name):
        self.score_names += ['\t\t\t<score-name descr="%s" formula="%s" name="%s"/>\n' % (descr, formula, name)]

    def add_scoreboard(self, name, update_rate):
        self.scoreboards += Scoreboard(name, update_rate)

class Address:
    def __init__(self, addr, count, select, tipe):
        self.addr = addr
        self.count = count
        self.select = select
        self.tipe = tipe

    def __str__(self):
        return '\t\t\t<address addr="%s" count="%s" select="%s" type="%s"/>\n' % (self.addr, self.count, self.select, self.tipe)

class IP_Pool:
    def __init__(self, cidr, name, network):
        self.cidr = cidr
        self.name = name
        self.network = network
        self.addresses = []

    def __str__(self):
        ret = '\t\t<pool cidr="%s" name="%s" network="%s">\n' % (self.cidr, self.name, self.network)
        for addr in self.addresses:
            ret += addr
        ret += '\t\t</pool>\n'
        return ret

    def add_address(self, addr, count, select, tipe):
        self.address += Address(addr, count, select, tipe)

class IP_Pools:
    def __init__(self):
        self.pools = []

    def __str__(self):
        ret = '\t<ip-pools>\n'
        for pool in self.pools:
            ret += pool
        ret += '\t</ip-pools>\n'
        return ret

class Handler:
    def __init__(self, ch, name, sh, si, sp):
        self.ch = ch
        self.name = name
        self.sh = sh
        self.si = si
        self.sp = sp

    def __str__(self):
        return '\t\t<handler class-handler="%s" name="%s" server-hostname="%s" server-ip="%s" server-port="%s"/>\n' % (self.ch, self.name, self.sh, self.si, self.sp)

class Event_Handlers:
    def __init__(self):
        self.handlers = []

    def __str__(self):
        ret = '\t<event-handlers>\n'
        for han in self.handlers:
            ret += han
        ret += '\t</event-handlers>\n'
        return ret

    def add_handler(self, class_handler, name, server_hostname, server_ip, server_port):
        self.handlers += Handler(class_handler, name, server_hostname, server_ip, server_port)

class Team_Event:
    def __init__(self, command, drift, endtime, freq, guid, handler, id, ipaddr, name, st):
        self.command = command
        self.drift = drift
        self.endtime = endtime
        self.freq = freq
        self.guid = guid
        self.handler = handler
        self.id = id
        self.ipaddr = ipaddr
        self.name = name
        self.st = st
        self.factors = []

    def __str__(self):
        ret = '\t\t\t<team-event command="%s" drift="%s" endtime="%s" frequency="%s" guid="%s" handler="%s" id="%s" ipaddress="%s" name="%s" start-time="%s">\n' % (self.command, self.drift, self.endtime, self.freq, self.guid, self.handler, self.id, self.ipaddr, self.name, self.st)
        for fact in self.factors:
            ret += fact
        ret += '\t\t\t</team-event>\n'
        return ret
        
    def add_score_factor(self, points, score_group, when):
        self.factors += ['\t\t\t\t<score-atomic points="%s" score-group="%s" when="%s"/>\n' % (points, score_group, when)]

    def remove_factor(self, index):
        self.factors.drop(index)

class Team:
    def __init__(self, name,host,speed):
        self.name = name
        self.host = host
        self.speed = speed
        self.events = []

    def __str__(self):
        ret = '\t<team name="%s">\n' % self.name
        ret += '\t\t<team-host hostname="%s"/>\n' % self.host
        ret += '\t\t<speed factor="%s"/>\n' % self.speed
        ret += '\t\t<team-event-list>\n'
        for event in self.events:
            ret += '\t\t\t'+str(event)
        ret += '\t\t</team-event-list>\n'
        ret += '\t</team>\n'
        return ret

    def set_host(self, host):
        self.host = host
        
    def set_speed(self, speed):
        self.speed = str(speed)
        
    def add_event(self, command, drift, endtime, frequency, guid, handler, id, ipaddress, name, start_time):
        self.events.append(Team_Event(command, drift, endtime, frequency, guid, handler, id, ipaddress, name, start_time))

class Instance_Builder:
    def __init__(self):
        self.dns = []
        self.networks = []
        self.hosts = []
        self.ip_pools = IP_Pools()
        self.event_handlers = Event_Handlers()
        self.teams = []

    def __str__(self):
        ret = '<occpchallenge>\n'
        ret += '\t<rootdns>\n'
        for d in self.dns:
            ret += d
        ret += '\t</rootdns>\n'
        for net in self.networks:
            ret += net
        for host in self.hosts:
            ret += str(host)
        ret += str(self.ip_pools)
        ret += str(self.event_handlers)
        for team in self.teams:
            ret += str(team)
        ret += '</occpchallenge>'
        return ret

    def add_dns_entry(self, name, rrtype, value):
        self.dns += ['\t\t<entry name="%s" rrtype="%s" value="%s"/>\n' % (name, rrtype, value)]

    def add_network(self, label):
        self.networks += ['\t<network label="%s"/>\n' % label]

    def remove_net(self, net):
        for work in self.networks:
            if work.strip() == net:
                self.networks.remove(work)

    def remove_dns(self, dnss):
        for dns in self.dns:
            if dns.strip() == dnss:
                self.dns.remove(dns)

    def add_host(self, basevm, domain, hostname, label, phase, ram):
        self.hosts += [Host(basevm, domain, hostname, label, phase, ram)]

    def add_team(self, name,host,speed):
        self.teams.append(Team(name,host,speed))

    def start_scenario(self, description, gameid, name, tipe):
        self.scenario = Scenario(description, gameid, name, tipe)
		
    def get_hosts(self):
        ret = []
        for host in self.hosts:
            ret += [host.show()]
        return ret
		
    def remove_host(self, hostt):
        for host in self.hosts:
            if host.show() == hostt:
                self.hosts.remove(host)
				
    def get_packs(self, hostt):
        ret = []
        for host in self.hosts:
            if host.show() == hostt:
                for pack in host.content.packs:
                    ret += [pack.show()]
        return ret

    def get_args(self, hostt, packk):
        ret = []
        for host in self.hosts:
            if host.show() == hostt:
                for pack in host.content.packs:
                    if pack.show() == packk:
                        for arg in pack.args:
                            ret += [pack.sharg(arg)]
        return ret
		
    def set_interface(self, hostt, broadcast, config, gateway, ipv4, name, network):
        for host in self.hosts:
            if host.show() == hostt:
                host.add_interface(broadcast, config, gateway, ipv4, name, network)			

    def add_pack(self, hostt, config, name):
        for host in self.hosts:
            if host.show() == hostt:
                host.content.add_pack(config, name)	

    def remove_pack(self, hostt, pakk):
        for host in self.hosts:
            if host.show() == hostt:
                for pack in host.content.packs:
                    if pack.show() == pakk: host.content.packs.remove(pack)				

    def add_arg(self, hostt, pakk, arg, val):
        for host in self.hosts:
            if host.show() == hostt:
                for pack in host.content.packs:					
                    if pack.show() == pakk: pack.add_arg(arg, val)
					
    def remove_arg(self, hostt, pakk, argg):
        for host in self.hosts:
            if host.show() == hostt:
                for pack in host.content.packs:					
                    if pack.show() == pakk: 
                        for arg in pack.args:
                            if argg == pack.sharg(arg):
                                pack.args.remove(arg)							

    def add_event(self,team, command, drift, endtime, frequency, guid, handler, id, ipaddress, name, start_time):
        team.add_event(command,drift,endtime,frequency,guid,handler,id,ipaddress,name,start_time)
    
def demo():
    print "working"
    inst = Instance_Builder()
    print inst
