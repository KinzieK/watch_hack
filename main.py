def on_button_pressed_a():
    global hours
    if hours < 23:
        hours += 1
        basic.show_string("" + str((hours)))
    else:
        hours = 0
        basic.show_string("" + str((hours)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global time
    if minutes <= 9:
        time = "" + str(hours) + (":" + "0" + str(minutes))
        basic.clear_screen()
        basic.show_string(time)
    else:
        time = "" + str(hours) + ":" + str(minutes)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

hours = 0
minutes = 0
time = ""
basic.show_leds("""
    . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
""")
basic.pause(10)
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.show_icon(IconNames.CHESSBOARD)
basic.clear_screen()
time = ""
adjust = 0
minutes = 0
hours = 0
ampm = False

def on_forever():
    pass
basic.forever(on_forever)
