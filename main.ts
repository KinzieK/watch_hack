input.onButtonPressed(Button.A, function () {
    if (hours < 23) {
        hours += 1
        basic.showString("" + hours)
        basic.pause(100)
        basic.clearScreen()
    } else {
        basic.showString("" + hours)
        hours = 0
        basic.pause(100)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    if (minutes < 59) {
        minutes += 1
        basic.showString("" + minutes)
    } else {
        minutes = 0
        basic.showString("" + minutes)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (minutes <= 9) {
        time = "" + hours + (":" + "0" + ("" + minutes))
        basic.showString(time)
    } else {
        time = "" + hours + ":" + ("" + minutes)
        basic.showString(time)
    }
})
let hours = 0
let minutes = 0
let time = ""
let adjust = 0
let ampm = false
time = ""
minutes = 0
hours = 0
basic.forever(function () {
    basic.pause(60000)
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
        hours += 1
    }
})
