import xml.etree.ElementTree as ET

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
