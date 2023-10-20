import pyfirmata
import time

board = pyfirmata.Arduino('COM7')
print("Communication Successfully started")

while True:
    board.digital[9].write(1)
    time.sleep(1)
    board.digital[9].write(0)
    time.sleep(1)
    board.digital[10].write(1)
    time.sleep(1)
    board.digital[10].write(0)
    time.sleep(1)
    board.digital[11].write(1)
    time.sleep(1)
    board.digital[11].write(0)
    time.sleep(1)
    board.digital[12].write(1)
    time.sleep(1)
    board.digital[12].write(0)
    time.sleep(1)
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
