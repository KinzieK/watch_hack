def on_button_pressed_a():
    global hours
    basic.clear_screen()
    if hours < 23:
        basic.clear_screen()
        hours += 1
        basic.show_string("" + str(hours))
    else:
        basic.clear_screen()
        hours = 0
        basic.show_string("" + str(hours))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global time
    if minutes <= 9:
        time = "" + str(hours) + (":" + "0" + ("" + str(minutes)))
        basic.clear_screen()
        basic.show_string(time)
    else:
        time = "" + str(hours) + ":" + ("" + str(minutes))
        basic.clear_screen()
        basic.show_string(time)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        basic.clear_screen()
        minutes += 1
        basic.show_string("" + str(minutes))
    else:
        basic.clear_screen()
        minutes = 0
        basic.show_string("" + str(minutes))
input.on_button_pressed(Button.B, on_button_pressed_b)

hours = 0
minutes = 0
time = ""
adjust = 0
ampm = False
ampm2 = False
time2 = ""
adjust2 = 0
hours2 = 0
minutes2 = 0
time = ""
minutes = 0
hours = 0
basic.pause(10)
basic.show_leds("""
    # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
""")
basic.show_icon(IconNames.CHESSBOARD)
basic.clear_screen()

def on_forever():
    
    def on_gesture_shake():
        global adjust2, time2
        adjust2 = hours2
        if ampm2:
            if hours2 > 12:
                adjust2 = hours2 - 12
            elif hours2 == 0:
                adjust2 = 12
        time2 = "" + ("" + str(adjust2))
        time2 = time2 + ":"
        if minutes2 < 10:
            time2 = time2 + "0"
        time2 = time2 + ("" + str(minutes2))
        if ampm2:
            if hours2 > 11:
                time2 = time2 + "PM"
            else:
                time2 = time2 + "AM"
        basic.show_string(time2)
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
    
basic.forever(on_forever)
