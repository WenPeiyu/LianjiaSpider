
from socket import *
from MK500.autocmd import *


def send_cmd_2_mk500(cmd):
    print(cmd)
    addr = (dstIP, dstPort)
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(str(cmd), addr)
    s.close()


if __name__ == '__main__':    
    while True:
        step = input()

        if step == 'a':
            send_cmd_2_mk500(Attach)
        if step == 'd':
            send_cmd_2_mk500(Detach)
        if step == 'p':
            send_cmd_2_mk500(UpPing)
        if step == 'c':
            send_cmd_2_mk500(ClearAttach)
            send_cmd_2_mk500(ClearPing)
            send_cmd_2_mk500(ClearAttachDelay)
            send_cmd_2_mk500(ClearUeState)
            send_cmd_2_mk500(ClearSignal)
        if step == 's':
            send_cmd_2_mk500(SaveAttach)
            send_cmd_2_mk500(SavePing)
            send_cmd_2_mk500(SaveAttachDelay)
            send_cmd_2_mk500(SaveUeState)
            send_cmd_2_mk500(SaveMeasure)
        if step == 'ul':
            send_cmd_2_mk500(UPackage)
        if step == 'dl':
            send_cmd_2_mk500(DPackage)
        if step == 'stop':
            send_cmd_2_mk500(CloseService)
        if step == 'b':
            send_cmd_2_mk500(ShuiBiao)
        if step == 'q':
            break
            

