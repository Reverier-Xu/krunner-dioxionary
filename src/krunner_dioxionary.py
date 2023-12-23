from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import dbus.service
import os

DBusGMainLoop(set_as_default=True)

objpath = "/dioxionary"
iface = "org.kde.krunner1"


class Alias:
    def __init__(self, name, command):
        self.name = name
        self.command = command


class Runner(dbus.service.Object):
    def __init__(self):
        dbus.service.Object.__init__(
            self, dbus.service.BusName("org.kde.dioxionary", dbus.SessionBus()), objpath
        )

    @dbus.service.method(iface, in_signature="s", out_signature="a(sssida{sv})")
    def Match(self, originalQuery: str):
        prefix = originalQuery.split(":", 1)[0]
        if prefix != 'dx':
            return []
        query = originalQuery[len(prefix) + 1:].strip()
        if not query:
            return []
        os.system(f"fish -c 'dx {query} > /tmp/dioxionary'")
        lines = []
        with open("/tmp/dioxionary") as f:
            lines = f.readlines()
        return [('dict', ''.join(lines).replace('\n', ' ').replace(query, ''), "Terminal", 100, 100, {}), ]


    @dbus.service.method(iface, in_signature="ss")
    def Run(self, data: str, action_id: str):
        os.system(data)


runner = Runner()
loop = GLib.MainLoop()
loop.run()
