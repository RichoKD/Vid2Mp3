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

# Add tabs to string


def tab(num):
    i = num
    tbs = ''
    while(i > 0):
        tbs = tbs + "\t"
        i = i - 1
    return tbs


# Add track to plalist


def track(loctn, id):
    # print(locn)
    locn = escape(loctn)  # escape XML invalid characters
    trck = tab(3)+'<track>\n'+tab(4)+'<location>file://'+locn+'</location>\n'+tab(4)+'<duration> 0 </duration>\n'+tab(4)+'<extension application="http://www.videolan.org/vlc/playlist/0">\n'+tab(5)+'<vlc:id>' + \
        str(id) + '</vlc:id>\n'+tab(4)+'</extension>\n'+tab(3)+'</track>\n'
    return trck


# compare files in video and music folder create playlist and run in VLC


def rez(video, music):
    vid = []  # Video list
    muz = []  # Music list
    locatn = ""

    # find videos
    for filename in os.listdir(video):
        locatn = video + filename
        name, file_extension = os.path.splitext(filename)

        if file_extension.upper() in formats:
            vid.append(name + ':' + file_extension)

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
        z = vd.split(':')
        # print(z[0])
        if z[0] not in muz:
            nm = video + '/' + z[0] + z[1]
            # print(z[0])
            convt.append(nm)
            displayList.append('' + z[0] + z[1])

    # create vlc plalist
    with open('list.xspf', 'w') as file:
        lst = [
            '<?xml version="1.0" encoding="UTF-8"?> \n',
            '<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\n',
            tab(1)+'<title>Playlist</title>\n',
            tab(2)+'<trackList>\n'
        ]

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
