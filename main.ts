input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    if (hours < 23) {
        basic.clearScreen()
        hours += 1
        basic.showString("" + hours)
    } else {
        basic.clearScreen()
        hours = 0
        basic.showString("" + hours)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (minutes <= 9) {
        time = "" + hours + (":" + "0" + ("" + minutes))
        basic.clearScreen()
        basic.showString(time)
    } else {
        time = "" + hours + ":" + ("" + minutes)
        basic.clearScreen()
        basic.showString(time)
    }
})
input.onButtonPressed(Button.B, function () {
    if (minutes < 59) {
        basic.clearScreen()
        minutes += 1
        basic.showString("" + minutes)
    } else {
        basic.clearScreen()
        minutes = 0
        basic.showString("" + minutes)
    }
})
let hours = 0
let minutes = 0
let time = ""
let adjust = 0
let ampm = false
let ampm2 = false
let time2 = ""
let adjust2 = 0
let hours2 = 0
let minutes2 = 0
time = ""
minutes = 0
hours = 0
basic.pause(10)
basic.showLeds(`
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    `)
basic.showIcon(IconNames.Chessboard)
basic.clearScreen()
basic.forever(function () {
    basic.pause(60000)
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
    }
})
