input.onButtonPressed(Button.A, function () {
    OLED.clear()
    OLED.drawFilledCircle(Támadóx - 20, Támadóy, 10)
    OLED.drawFilledCircle(Ellensegx, Ellensegy, 10)
    OLED.drawFilledCircle(Ellensegx + 20, Ellensegy, 10)
    OLED.drawFilledCircle(Ellensegx + 40, Ellensegy, 10)
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index <= 4; index++) {
        OLED.drawCircle(Támadóx, Fegyver, 10)
    }
    if (Támadóx == 40 || Fegyver == 10) {
        Pontszám += 1
        OLED.writeNumNewLine(Pontszám)
    }
    if (Támadóx == 60 || Fegyver == 10) {
        Pontszám += 1
        OLED.writeNumNewLine(Pontszám)
    }
    if (Támadóx == 80 || Fegyver == 10) {
        Pontszám += 1
        OLED.writeNumNewLine(Pontszám)
    }
})
input.onButtonPressed(Button.B, function () {
    OLED.clear()
    OLED.drawFilledCircle(Támadóx + 20, Támadóy, 10)
    OLED.drawFilledCircle(Ellensegx, Ellensegy, 10)
    OLED.drawFilledCircle(Ellensegx + 20, Ellensegy, 10)
    OLED.drawFilledCircle(Ellensegx + 40, Ellensegy, 10)
})
let Fegyver = 0
let Támadóy = 0
let Támadóx = 0
let Ellensegy = 0
let Ellensegx = 0
let Pontszám = 0
Pontszám = 0
Ellensegx = 40
Ellensegy = 10
Támadóx = 40
Támadóy = 50
Fegyver = 50
OLED.init(128, 64)
OLED.drawFilledCircle(Támadóx, Támadóy, 10)
OLED.drawFilledCircle(Ellensegx, Ellensegy, 10)
OLED.drawFilledCircle(Ellensegx + 20, Ellensegy, 10)
OLED.drawFilledCircle(Ellensegx + 40, Ellensegy, 10)
basic.forever(function () {
	
})
