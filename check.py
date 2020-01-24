from gi.repository import Gtk as gtk
import os
import sys
import gi
from xml.sax.saxutils import escape

gi.require_version('Gtk', '3.0')

print('check')

formats = [
    ".AVI", ".MP4", ".MKV", ".WEBM", ".WMV", ".3GP", ".AMV", ".3GPP", ".MOV", ".MPG", ".OGG"
]
convt = []
displayList = []


def tab(num):
    i = num
    tbs = ''
    while(i > 0):
        tbs = tbs + "\t"
        i = i - 1
    return tbs


lst = [
    '<?xml version="1.0" encoding="UTF-8"?> \n',
    '<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\n',
    tab(1)+'<title>Playlist</title>\n',
    tab(2)+'<trackList>\n'
]


def track(loctn, id):
    # print(locn)
    locn = escape(loctn)
    trck = tab(3)+'<track>\n'+tab(4)+'<location>file://'+locn+'</location>\n'+tab(4)+'<duration> 0 </duration>\n'+tab(4)+'<extension application="http://www.videolan.org/vlc/playlist/0">\n'+tab(5)+'<vlc:id>' + \
        str(id) + '</vlc:id>\n'+tab(4)+'</extension>\n'+tab(3)+'</track>\n'
    return trck


def rez(video, music):
    vid = []
    muz = []
    # vid_conv = []
    # for fold in os.listdir(folder):
    x = 0
    locatn = ""

    # find videos
    for filename in os.listdir(video):
        locatn = video + filename
        name, file_extension = os.path.splitext(filename)

        if file_extension.upper() in formats:
            # print('vid', name)
            vid.append(name + ':' + file_extension)
            # vid_conv.append(name + file_extension)

    # find music
    for filename in os.listdir(music):
        locatn = music + filename
        name, file_extension = os.path.splitext(filename)

        if file_extension.upper() == '.MP3':
            # print('muz', name)
            muz.append(name)

    # compare both folders and list out unconverted vidoes
    for vd in vid:
        # print(vd)
        # vd = vd['name']
        z = vd.split(':')
        # print(z[0])
        if z[0] not in muz:
            nm = video + '/' + z[0] + z[1]
            print(z[0])
            convt.append(nm)
            displayList.append('' + z[0] + z[1])

    # print('m', muz)  # len(muz))
    # print('v', len(vid))

    # create vlc plalist
    with open('list.xspf', 'w') as file:
        file.writelines(lst)
        i = 0
        for vd in convt:
            file.write(track(vd, i))
            i = i+1
        file.write(tab(2)+'</trackList>\n')
        file.write(
            tab(2)+'<extension application = "http://www.videolan.org/vlc/playlist/0">\n')
        y = 0
        for vd in convt:
            file.write(tab(3)+'<vlc:item tid="'+str(y)+'"/>\n')
            y = y+1
        file.write(tab(2)+'</extension>\n')
        file.write('</playlist>')
        print('Success!!!!!!!!!!!!!!!!')
        return displayList


def trim(folder):
    n = 0
    for filename in os.listdir(folder):
        print(filename)
        if len(filename) > 19:
            print(len(filename))
            os.remove(folder+'/'+filename)


# rez("/home/rico/Vid/Anime/Music/New folder")
# rez("/home/rico/Vid/Anime/Music")
# rez(sys.argv[1])

if __name__ == "__main__":
    while 1:
        vid = input("Enter your video folder path or type exit to close: ")
        muz = input("Enter your music folder path or type exit to close: ")

        if vid == 'exit' or muz == 'exit':
            break
        else:
            try:
                rez(vid, muz)
            except Exception as e:
                print('Error')
                raise


#gtk = gi.repository.Gtk


# class Main:
#     def __init__(self):
#         # print('go')
#         gladeFile = "main.glade"
#         self.builder = gtk.Builder()
#         self.builder.add_from_file(gladeFile)
#         self.builder.connect_signals(self)

#         # button = self.builder.get_object("button")
#         # button.connect("clicked",self.prnt)

#         window = self.builder.get_object("Main")
#         window.connect("delete-event",gtk.main_quit)
#         window.show()

#     def prnt(self, widget):
#         print("Yooo!!!!")


# if __name__ == '__main__':
#     main = Main()
#     gtk.main()
