# Trinket IO demo
# Welcome to CircuitPython 3.1.1 :)

import board
import adafruit_dotstar as dotstar
import time
import busio
import struct

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.7)

uart = busio.UART(board.TX, board.RX, baudrate=115200)

lastKey = 0

######################### MAIN LOOP ##############################

dot[0] = (80,255,80)

WRITE_DELAY=.005

POLL = struct.pack('b',1)

cellData = bytearray(2)

i = 0

shiftState = False
altState = False
ctrlState = False
overlayId = 0

def range_map(value, in_min, in_max, out_min, out_max):
    return int(max(out_min,min(out_max,(value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min)))

def pressButton(butNum, newShiftState):
    print("Send Button ", butNum, newShiftState)

def moveJoystick(row, col, centerRow, centerCol, newShiftState):
    maxMap = 255
    minMap = 0
    midMap = 127
    deadRows = 2
    deadCols = 1

    #print(("moveJoystick()", row, col, centerRow, centerCol, newShiftState))
    rowDiff = (centerRow - row)
    colDiff = (centerCol - col) * -1
#    print((rowDiff, colDiff))
    if abs(rowDiff) < deadRows:
        rowMapped = midMap
    else:
        rowMapped = range_map(rowDiff, -6.5,6.5,minMap,maxMap)
    if abs(colDiff) < deadCols:
        colMapped = midMap
    else:
        colMapped = range_map(colDiff, -4,4,minMap,maxMap)
    print((rowMapped, colMapped))

while True:
    time.sleep(0.10) # make bigger to slow down
    uart.reset_input_buffer()
#    print("SENDING POLL")
    uart.write(POLL)
    uart.write(struct.pack('BBB',1 if shiftState else 0,
                                 1 if altState else 0,
                                 1 if ctrlState else 0))
    time.sleep(WRITE_DELAY)
    response = uart.read(1)
    if response is None:
        print("No response")
        continue
    newOverlay=response[0]

    time.sleep(WRITE_DELAY)
    response = uart.read(1)
    if response is None:
        continue
    numCells = response[0]
#        print("Got Count: ", numCells)
    cellCount = 0
    while (cellCount < numCells):
        uart.readinto(cellData)
#            print("Got Data: ", cellData)
        (idx,) = struct.unpack('<H', cellData)
        col = idx//24
        row = idx % 24
        #Ok, we need to find the button/joystick
        #Three stripes
        if row < 4:
            #Top Buttons
            if col > 1 and col < 6:
                pressButton(5, False) #A = 5, Shift =False
            elif col > 6 and col < 11:
                pressButton(6, False) #B = 6, Shift =False
            elif col > 11 and col < 16:
                pressButton(5, True) #X = 5, Shift =True
            elif col > 16 and col < 21:
                pressButton(6, True) #Y = 6, Shift =True
        elif row > 19:
            #Bottom Buttons
            if col > 1 and col < 6:
                pressButton(3, False) #LB = 7, Shift =False
            elif col > 6 and col < 11:
                pressButton(4, False) #XB = 2, Shift =False
            elif col > 11 and col < 16:
                pressButton(3, True) #MENU = 7, Shift =True
            elif col > 16 and col < 21:
                pressButton(4, True) #RB = 2, Shift =True
        elif row > 4 and row < 19:
            if col > 1 and col < 11:
                #First Joystick
                moveJoystick(row, col, 11.5,6,False)
            elif col > 11 and col < 21:
                #First Joystick
                moveJoystick(row, col, 11.5,17,True)
        cellCount = cellCount + 1