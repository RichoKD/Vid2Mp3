from gi.repository import Gio, GObject
from gi.repository import Gtk as gtk
import check as ck
import gi
import subprocess

gi.require_version('Gtk', '3.0')


class Item(GObject.GObject):

    text = GObject.property(type=str)

    def __init__(self):
        GObject.GObject.__init__(self)


class Main:

    def __init__(self):

        gladeFile = "main2.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        window = self.builder.get_object("Main")
        window.connect("delete-event", gtk.main_quit)
        window.show()

    def create_widget_func(self, item):
        label = gtk.Label(item.text)
        return label

    def createPlaylist(self, widget):

        inputV = self.builder.get_object("inputV")  # filepicker for Videos
        inputM = self.builder.get_object("inputM")  # filepicker for music
        listbox = self.builder.get_object("lstbox")

        liststore = Gio.ListStore()

        inpv = inputV.get_filename()
        inpm = inputM.get_filename()

        print("V ", inpv)
        print("M ", inpm)

        names = ck.rez(inpv, inpm)
        # liststore.empty()
        for name in names:
            print(name)
            itemz = Item()
            itemz.text = name
            liststore.append(itemz)
        listbox.bind_model(liststore, self.create_widget_func)

        try:
            subprocess.Popen(["vlc", "list.xspf"])
        except Exception as e:
            print('Error')
            raise


if __name__ == '__main__':
    main = Main()
    gtk.main()
