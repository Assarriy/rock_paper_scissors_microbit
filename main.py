def on_gesture_shake():
    global Tangan
    Tangan = randint(1, 3)
    if Tangan == 1:
        basic.show_icon(IconNames.SCISSORS)
    elif Tangan == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.SQUARE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Tangan = 0
basic.show_icon(IconNames.YES)

def on_forever():
    pass
basic.forever(on_forever)
