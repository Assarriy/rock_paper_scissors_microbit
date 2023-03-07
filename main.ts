input.onGesture(Gesture.Shake, function () {
    Hand = randint(1, 3)
    if (Hand == 1) {
        basic.showIcon(IconNames.Scissors)
    } else if (Hand == 2) {
        basic.showIcon(IconNames.SmallSquare)
    } else {
        basic.showIcon(IconNames.Square)
    }
})
let Hand = 0
basic.showIcon(IconNames.Happy)
basic.forever(function () {
	
})
