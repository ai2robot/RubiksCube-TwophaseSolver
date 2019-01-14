# coding=utf-8
import serial
import time

solveList = ['U1', 'U2', 'U3', 'D1', 'D2', 'D3', 'L1', 'L2', 'L3',
             'R1', 'R2', 'R3', 'F1', 'F2', 'F3', 'B1', 'B2', 'B3']
stepList = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def send_arduino(com, txt):
    """Send command to arduino"""
    try:
        x = serial.Serial(com, 9600)
        #x.open()
        if x.isOpen() > 0:
            print("open com")
            time.sleep(2)
            #x.write('0'.encode())
            #print("send to com")
            #data = x.read()
            index = 0
            while 1:
                if txt[index*3] == '(':
                   break
                solve_step = txt[index*3:index*3+2]
                step_index = solveList.index(solve_step)
                step_data = stepList[step_index]
                x.write(step_data.encode())
                data = x.read()
                index = index + 1
                #time.sleep(2)
            x.close()
    except:
        print('Cannot open com.')


