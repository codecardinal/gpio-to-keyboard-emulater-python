import wiringpi as w
import uinput

w.wiringPiSetup() # Initialize pins

# Pin mapping
PIN_A = 0
PIN_B = 2

PIN_UP = 22
PIN_LEFT = 23
PIN_DOWN = 24
PIN_RIGHT = 25

PIN_SELECT = 3
PIN_START = 21

# State mapping
STATE_A = False
STATE_B = False

STATE_UP = False
STATE_LEFT = False
STATE_DOWN = False
STATE_RIGHT = False

STATE_SELECT = False
STATE_START = False

# Set pinmodes
w.pinMode(PIN_A, w.GPIO.INPUT)
w.pinMode(PIN_B, w.GPIO.INPUT)

w.pinMode(PIN_UP, w.GPIO.INPUT)
w.pinMode(PIN_LEFT, w.GPIO.INPUT)
w.pinMode(PIN_DOWN, w.GPIO.INPUT)
w.pinMode(PIN_RIGHT, w.GPIO.INPUT)

w.pinMode(PIN_SELECT, w.GPIO.INPUT)
w.pinMode(PIN_START, w.GPIO.INPUT)

# Set internal pull up 
w.pullUpDnControl(PIN_A, w.GPIO.PUD_UP)
w.pullUpDnControl(PIN_B, w.GPIO.PUD_UP)

w.pullUpDnControl(PIN_UP, w.GPIO.PUD_UP)
w.pullUpDnControl(PIN_LEFT, w.GPIO.PUD_UP)
w.pullUpDnControl(PIN_DOWN, w.GPIO.PUD_UP)
w.pullUpDnControl(PIN_RIGHT, w.GPIO.PUD_UP)

w.pullUpDnControl(PIN_SELECT, w.GPIO.PUD_UP)
w.pullUpDnControl(PIN_START, w.GPIO.PUD_UP)

# Initialize uinput
events = (uinput.KEY_UP, uinput.KEY_DOWN, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_Q, uinput.KEY_B, uinput.KEY_S, uinput.KEY_SEMICOLON)
device = uinput.Device(events)

# Loop through shit
while True:
  OUTPUT_A = not w.digitalRead(PIN_A)
  OUTPUT_B = not w.digitalRead(PIN_B)
  
  OUTPUT_UP = not w.digitalRead(PIN_UP)
  OUTPUT_LEFT = not w.digitalRead(PIN_LEFT)
  OUTPUT_DOWN = not w.digitalRead(PIN_DOWN)
  OUTPUT_RIGHT = not w.digitalRead(PIN_RIGHT)

  OUTPUT_SELECT = not w.digitalRead(PIN_SELECT)
  OUTPUT_START = not w.digitalRead(PIN_START)

  if(OUTPUT_A and (not STATE_A)):
    print 'Press A, state was false\n'
    device.emit(uinput.KEY_Q, 1)
    STATE_A = True
  elif((not OUTPUT_A) and STATE_A):
    print 'Release A, state was true\n'
    device.emit(uinput.KEY_Q, 0)
    STATE_A = False

  if(OUTPUT_B and (not STATE_B)):
    print 'Press B, state was false\n'
    device.emit(uinput.KEY_B, 1)
    STATE_B = True
  elif((not OUTPUT_B) and STATE_B):
    print 'Release B, state was true\n'
    device.emit(uinput.KEY_B, 0)
    STATE_B = False

  if(OUTPUT_UP and (not STATE_UP)):
    print 'Press UP, state was false\n'
    device.emit(uinput.KEY_UP, 1)
    STATE_UP = True
  elif((not OUTPUT_UP) and STATE_UP):
    print 'Release UP, state was true\n'
    device.emit(uinput.KEY_UP, 0)
    STATE_UP = False

  if(OUTPUT_LEFT and (not STATE_LEFT)):
    print 'Press LEFT, state was false\n'
    device.emit(uinput.KEY_LEFT, 1)
    STATE_LEFT = True
  elif((not OUTPUT_LEFT) and STATE_LEFT):
    print 'Release LEFT, state was true\n'
    device.emit(uinput.KEY_LEFT, 0)
    STATE_LEFT = False

  if(OUTPUT_DOWN and (not STATE_DOWN)):
    print 'Press DOWN, state was false\n'
    device.emit(uinput.KEY_DOWN, 1)
    STATE_DOWN = True
  elif((not OUTPUT_DOWN) and STATE_DOWN):
    print 'Release DOWN, state was true\n'
    device.emit(uinput.KEY_DOWN, 0)
    STATE_DOWN = False

  if(OUTPUT_RIGHT and (not STATE_RIGHT)):
    print 'Press RIGHT, state was false\n'
    device.emit(uinput.KEY_RIGHT, 1)
    STATE_RIGHT = True
  elif((not OUTPUT_RIGHT) and STATE_RIGHT):
    print 'Release RIGHT, state was true\n'
    device.emit(uinput.KEY_RIGHT, 0)
    STATE_RIGHT = False

  if(OUTPUT_SELECT and (not STATE_SELECT)):
    print 'Press SELECT, state was false\n'
    device.emit(uinput.KEY_S, 1)
    STATE_SELECT = True
  elif((not OUTPUT_SELECT) and STATE_SELECT):
    print 'Release SELECT, state was true\n'
    device.emit(uinput.KEY_S, 0)
    STATE_SELECT = False

  if(OUTPUT_START and (not STATE_START)):
    print 'Press START, state was false\n'
    device.emit(uinput.KEY_SEMICOLON, 1)
    STATE_START = True
  elif((not OUTPUT_START) and STATE_START):
    print 'Release START, state was true\n'
    device.emit(uinput.KEY_SEMICOLON, 0)
    STATE_START = False

  w.delay(100)

