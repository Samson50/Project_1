import xml.etree.ElementTree as ET

class Pack:
    def __init__(self, config, name):
        self.config = config
        self.name = name
        self.args = {}

    def __repr__(self):
        ret = '<pack config="%s" name="%s">' % (self.config, self.name)
        for arg in args:
            ret += "<"+arg+">"+args(arg)+"</"+arg+">"
        ret += "</pack>"

    def add_arg(self, arg, val):
        self.args(arg) = val

class Content:
    def __init__(self):
        self.packs = []

    def __repr__(self):
        ret = '<content>'
        for pack in packs:
            ret += pack
        ret += '</content>'
        
    def add_pack(self, config, name):
        self.packs += Pack(config, name)

class Interface:
    def __init__(self, broadcast, config, gateway, ipv4, name, network):
        self.broadcast = broadcast
        self.config = config
        self.gateway = gateway
        self.ipv4 = ipv4
        self.name = name
        self.network = network

    def __repr__(self):
        ret = '<interface broadcast="%s" config="%s" gateway="%s" ipv4="%s" name="%s" network="%s"/>' % (self.broadcast, self.config, self.gateway, self.ipv4, self.name, self.network)
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

    def __repr__(self):
        ret = '<host basevm="%s" domain="%s" hostname="%s" label="%s" phase="%s" ram="%s">' % (self.basevm, self.domain, self.hostname, self.label, self.phase, self.ram)
        ret += self.content
        for interface in self.interfaces:
            ret += interface
        ret += "</host>"
        return ret
    
    def add_interface(self, broadcast, config, gateway, ipv4, name, network):
        self.interfaces += Interface(broadcast, config, gateway, ipv4, name, network)

class User_Interface:
    def __init__(self, name, soc, showboard, sta):
        self.name = name
        self.soc = soc
        self.showboard = showboard
        self.sta = sta

class Scoreboard:
    def __init__(self, name, update_rate):
        self.name = name
        self.update_rate = update_rate
        self.score_name = []

    def __repr__(self)
        ret = '<scoreboard name="%s" update-rate="%s">' % (self.name, self.update_rate)
        ret += self.score_name
        ret += '</scoreboard>'

    def set_name(self, name):
        self.score_name += '<score-name name="%s"/>' % (name)]

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

    def __repr__(self):
        ret = '<scenario description="%s" gameid="%s" name="%s" type="%s">' % (self.description, self.gameid, self.name, self.tipe)
        ret += self.length
        ret += self.networkid
        ret += '<users>'
        for user in self.users:
            ret += user
        ret += '</users>'
        ret += '<user-interfaces>'
        for ui in self.user_interfaces:
            ret += ui
        ret += '</user-interfaces>'
        ret += '<score-labels>'
        for label in self.score_labels:
            ret += label
        ret += '</score-labels>'
        ret += '<score-names>'
        for nam in self.score_names:
            ret += nam
        ret += '</score-names>'
        ret += '<scoreboards>'
        for scoreboard in self.scoreboards:
            ret += scoreboard
        ret += '</scoreboards>'
        ret += '</scenario>'

    def set_length(self, format, time):
        self.length = '<length format="%s" time="%s"/>' % (format, time)

    def set_networkid(self, number):
        self.networkid = '<networkid number="%s"/>' % (number)

    def add_user(self, name, passwd):
        self.users += ['<user name="%s" pass="%s"/>' % (name, passwd)]

    def add_interface(self, name, soc, showboard, sta):
        self.user_interfaces += User_Interface(name, soc, showboard, sta)

    def add_score_label(self, name, sql):
        self.score_labels += ['<score-label name="%s" sql="%s"/>' % (name, sql)]

    def add_score_name(self, descr, formula, name):
        self.score_names += ['<score-name descr="%s" formula="%s" name="%s"/>' % (descr, formula, name)]

    def add_scoreboard(self, name, update_rate):
        self.scoreboards += Scoreboard(name, update_rate)
        

class ScenarioGen():
    def __init__(self):
        self.tree = ET.Element("root")

    def add_user(self, element, usr, passwd):
        users = element.find("users")
        if not users:
            users = ET.SubElement(element, "users")
        ET.SubElement(users, "user", {"name":usr, "pass":passwd})

    def add_interface(self, host, name, config=False, ipv4=False, auto=False, broadcast=False, gateway=False, network=False):
        tags = {"name" : name}
        if config != False:     tag["config"] = config
        if ipv4 != False:       tag["ipv4"] = ipv4
        if auto != False:       tag["auto"] = auto
        if broadcast != False:  tag["broadcast"] = broadcast
        if gateway != False:    tag["gateway"] = gateway
        if network != False:    tag["network"] = network
        ET.SubElement(host, "interface", tags)

    def add_content(self, host, pack, args={}):
        content = host.find("content")
        if not content:
            content = ET.SubElement(host, "content")
        con_pack = ET.SubElement(content, "pack", {"name":pack})
        for tag in args:
            arg = ET.SubElement(con_pack, tag)
            arg.text = args[tag]

    def add_team(self, name):
        team = ET.SubElement(self.tree, "team", {"name":name})
        evnt_list = ET.SubElement(team, "team-event-list")

    def add_team_event(self, team_name, name, handler, ipaddress, starttime, endtime, frequency, drift):
        teams = self.tree.findall("team")
        for team in teams:
            if team.get("name") == team_name:
                return ET.SubElement(team, "team-event", {"name":name, "handler":handler, "ipaddress":ipaddress, "starttime":starttime, "endtime":endtime, "frequency":frequency, "drift":drift})

    def add_event_params(self, event, params):
        for param in params:
            event.set(param, params[param])
            
        
        
        
def demo():
    t = ScenarioGen()
    t.add_team("blue team")
    t.add_team("red team")
    t.add_team_event("red team", "malign", "ExecHandler", "10.2.10.1", "0", "999999", "124", "09132")
    evnt = t.add_team_event("blue team", "ping", "ExecHandler", "10.2.10.41", "0", "9999", "0", "0")
    t.add_event_params(evnt, {"command":"ping 8.8.8.8"})
    ET.dump(t.tree)
