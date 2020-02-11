# Trinket IO demo
# Welcome to CircuitPython 3.1.1 :)

import board
import adafruit_dotstar as dotstar
import time
import busio
import struct
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from qwertyMAC import *

overlay = webaccess

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.7)

uart = busio.UART(board.TX, board.RX, baudrate=115200)

#while True:
#    for led in range(0,9):
#        onMsg = struct.pack('bbb',2,led,3)
#        uart.write(onMsg)
#        time.sleep(.3)
#        offMsg = struct.pack('bbb',2,led,0)
#        uart.write(offMsg)
#        time.sleep(.2)

kbd = Keyboard()
mouse = Mouse()
lastKey = 0


######################### MAIN LOOP ##############################

CLIENT = True

dot[0] = (0,0,60)
if CLIENT:
    dot[0] = (255,0,255)

WRITE_DELAY=.005

POLL = struct.pack('b',1)

cellData = bytearray(2)

i = 0

shiftState= False
altState = False
ctrlState = False
commandState = False
dragState = False

#def updateToggles(key, pressed):
#    print(("TOGGLE:",key, pressed))
#    if (key == Keycode.LEFT_SHIFT):
#        shiftState = pressed
#        if (pressed):
#            msg = struct.pack('bbb',1,1)
#            uart.write(msg)
#        else:
#            msg = struct.pack('bbb',1,0)
#            uart.write(msg)

def pressKey(newKey):
    global kbd,shiftState,ctrlState,altState,commandState,uart
    if (newKey == Keycode.LEFT_SHIFT):
        shiftState = not shiftState
        val = 0
        if (shiftState):
            val = 1
        msg = struct.pack('bbb',2,1,val)
        uart.write(msg)
        kbd.press(newKey)
        return
    if (newKey == Keycode.CONTROL):
        ctrlState= not ctrlState
        val = 0
        if (ctrlState):
            val = 1
        msg = struct.pack('bbb',2,5,val)
        uart.write(msg)
        kbd.press(newKey)
        return
    if (newKey == Keycode.LEFT_ALT):
        altState = not altState
        val = 0
        if (altState):
            val = 1
        msg = struct.pack('bbb',2,2,val)
        uart.write(msg)
        kbd.press(newKey)
        return
    if (newKey == Keycode.COMMAND):
        commandState = not commandState
        val = 0
        if (commandState):
            val = 1
        msg = struct.pack('bbb',2,6,val)
        uart.write(msg)
        kbd.press(newKey)
        return

    keys = [newKey]
    if (shiftState):
        print("Adding Shift")
        keys.append(Keycode.LEFT_SHIFT)
        shiftState = False
        msg = struct.pack('bbb',2,1,0)
        uart.write(msg)
    if (altState):
        print("Adding ALT")
        keys.append(Keycode.LEFT_ALT)
        altState = False
        msg = struct.pack('bbb',2,2,0)
        uart.write(msg)
    if (ctrlState):
        print("Adding CONTROl")
        keys.append(Keycode.CONTROL)
        ctrlState= False
        msg = struct.pack('bbb',2,1,0)
        uart.write(msg)
    if (commandState):
        print("Adding COMMAND")
        keys.append(Keycode.COMMAND)
        commandState= False
        msg = struct.pack('bbb',2,6,0)
        uart.write(msg)
    kbd.press(*keys)

overlayId = 0
while True:
    time.sleep(0.025) # make bigger to slow down
    uart.reset_input_buffer()
#        print("SENDING POLL")
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
    if (newOverlay != overlayId):
        print(("New Overlay: ", newOverlay))
        overlayId = newOverlay
        if (overlayId == 0):
            overlay = webaccess
        elif(overlayId == 5):
            overlay = qwerty

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
        action = overlay[row//3][col//2]
#            print((row//3, col//2, action),end=',')
        newKey = overlay[row//3][col//2]
        if (action > 0):
            if (lastKey != 0):
                if (lastKey != newKey):
                    kbd.release(lastKey)
                    pressKey(newKey)
            else:
                pressKey(newKey)
                lastKey = newKey
        else:
            if (action < -99):
                #These are shortcuts
                index = (-1 * action) - 100
                sc = shortcuts[index]
                #Reset the lights & states for a shortcut
                shiftState = False
                msg = struct.pack('bbb',2,1,0)
                uart.write(msg)
                altState = False
                msg = struct.pack('bbb',2,2,0)
                uart.write(msg)
                ctrlState = False
                msg = struct.pack('bbb',2,5,0)
                uart.write(msg)
                commandState = False
                msg = struct.pack('bbb',2,6,0)
                uart.write(msg)
                #if this is a list, we send each item
                if (type(sc) is list):
                    print(sc)
                    for codes in sc:
                        if (type(codes) is tuple):
                            kbd.press(*codes)
                            kbd.release_all()
                        else:
                            kbd.press(codes)
                            kbd.release(codes)
                        time.sleep(.1)
                else:
                    kbd.press(*sc)
                    kbd.release_all
            elif (action == MOUSE_NW):
                mouse.move(-MOUSE_INCR,-MOUSE_INCR)
            elif (action == MOUSE_N):
                mouse.move(0,-MOUSE_INCR)
            elif (action == MOUSE_NE):
                mouse.move(MOUSE_INCR,-MOUSE_INCR)
            elif (action == MOUSE_W):
                mouse.move(-MOUSE_INCR,0)
            elif (action == MOUSE_E):
                mouse.move(MOUSE_INCR,0)
            elif (action == MOUSE_SW):
                mouse.move(-MOUSE_INCR,MOUSE_INCR)
            elif (action == MOUSE_S):
                mouse.move(0,MOUSE_INCR)
            elif (action == MOUSE_SE):
                mouse.move(MOUSE_INCR,MOUSE_INCR)
            elif (action == MOUSE_CLICK):
                mouse.click(Mouse.LEFT_BUTTON)
                time.sleep(.3)
            elif (action == MOUSE_RIGHT_CLICK):
                mouse.click(Mouse.RIGHT_BUTTON)
                time.sleep(.3)
            elif (action == MOUSE_DBL_CLICK):
                mouse.click(Mouse.LEFT_BUTTON)
                mouse.click(Mouse.LEFT_BUTTON)
                time.sleep(.3)
            elif (action == MOUSE_DRAG):
                print(("Mouse drag: ",dragState))
                if lastKey != MOUSE_DRAG:
                    dragState = True
                    lastKey = MOUSE_DRAG
                    mouse.press(Mouse.LEFT_BUTTON)
                else:
                    dragState = False
                    mouse.release(Mouse.LEFT_BUTTON)
                time.sleep(.3)
            lastKey = newKey

        cellCount = cellCount + 1
    if (cellCount == 0):
        if (lastKey != 0):
            lastKey = 0
            kbd.release_all()