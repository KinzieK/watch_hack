def on_button_pressed_a():
    global hours
    if hours < 23:
        hours += 1
        basic.show_string("" + str((hours)))
        basic.pause(100)
        basic.clear_screen()
    else:
        basic.show_string("" + str((hours)))
        hours = 0
        basic.pause(100)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global time
    if minutes <= 9:
        time = "" + str(hours) + (":" + "0" + ("" + str(minutes)))
        basic.show_string(time)
    else:
        time = "" + str(hours) + ":" + ("" + str(minutes))
        basic.show_string(time)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        minutes += 1
        basic.show_string("" + str(minutes))
    else:
        minutes = 0
        basic.show_string("" + str(minutes))
input.on_button_pressed(Button.B, on_button_pressed_b)

hours = 0
minutes = 0
time = ""
ampm = False
adjust = 0
time = ""
minutes = 0
hours = 0

def on_forever():
    global minutes, hours
    basic.pause(60000)
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
        hours += 1
basic.forever(on_forever)
