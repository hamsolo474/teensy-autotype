import time
import serial
import serial.tools.list_ports
from tkinter import Tk

message = ''
with open('pasteme.txt') as f:
    message = f.read()

#message = Tk().clipboard_get()
#message = 'abcdefghijklmnopqrstuvwxyz'
delay = 10 # seconds delay before pasting
ports = {}

def get_ports():
    portlist = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(portlist):
        hw       = hwid.split(' ')
        contype  = hw[0]
        pid      = hw[1][8:]
        ser      = hw[2][4:]
        location = hw[3][9:]
        ports[port] = {'port': port,
                       'desc': desc,
                       'type': contype,
                       'pid': pid,
                       'ser': ser,
                       'location': location,
                       'hwid':hwid}
    print(ports)
    # {'COM3': {'port': 'COM3', 'desc': 'USB Serial Device (COM3)', 'hwid': 'USB VID:PID=16C0:0487 SER=12345 LOCATION=1-3:x.0', 'type': 'USB', 'pid': '16C0:0487', 'ser': '12345', 'location': '1-3:x.0'}}
    # {'COM3': {'port': 'COM3', 'desc': 'USB Serial Device (COM3)', 'hwid': 'USB VID:PID=16C0:0487 SER=12345 LOCATION=1-4.4:x.0', 'type': 'USB', 'pid': '16C0:0487', 'ser': '12345', 'location': '1-4.4:x.0'}}



def find_teensy():
    criteria = {'pid': '16C0:0487','ser': '12345'}
    found = None
    for pk, pv in ports.items():
        breakOuter = False
        for ck, cv in criteria.items():
            try:
                if cv == pv[ck]:
                    found = pk
                    breakOuter = True
                    break
            except KeyError:
                breakOuter = True
                break
    return found


get_ports()
find_teensy()
print(f'Message loaded: {len(message)} chars')

# type
with serial.Serial(find_teensy(), 9600) as con:
    time.sleep(delay)
    for i in message.split('\n'):
        time.sleep(0.5)
        con.write(f'PRINT {i}\n'.encode())
        print(i)
