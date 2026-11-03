def on_button_pressed_a():
    OLED.clear()
    OLED.draw_filled_circle(Támadóx - 20, Támadóy, 10)
    OLED.draw_filled_circle(Ellensegx, Ellensegy, 10)
    OLED.draw_filled_circle(Ellensegx + 20, Ellensegy, 10)
    OLED.draw_filled_circle(Ellensegx + 40, Ellensegy, 10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Pontszám
    for index in range(5):
        OLED.draw_circle(Támadóx, Fegyver, 10)
    if Támadóx == 40 or Fegyver == 10:
        Pontszám += 1
        OLED.write_num_new_line(Pontszám)
    if Támadóx == 60 or Fegyver == 10:
        Pontszám += 1
        OLED.write_num_new_line(Pontszám)
    if Támadóx == 80 or Fegyver == 10:
        Pontszám += 1
        OLED.write_num_new_line(Pontszám)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    OLED.clear()
    OLED.draw_filled_circle(Támadóx + 20, Támadóy, 10)
    OLED.draw_filled_circle(Ellensegx, Ellensegy, 10)
    OLED.draw_filled_circle(Ellensegx + 20, Ellensegy, 10)
    OLED.draw_filled_circle(Ellensegx + 40, Ellensegy, 10)
input.on_button_pressed(Button.B, on_button_pressed_b)

Fegyver = 0
Támadóy = 0
Támadóx = 0
Ellensegy = 0
Ellensegx = 0
Pontszám = 0
OLED.clear()
Pontszám = 0
Ellensegx = 40
Ellensegy = 10
Támadóx = 40
Támadóy = 50
Fegyver = 50
OLED.init(128, 64)
OLED.draw_filled_circle(Támadóx, Támadóy, 10)
OLED.draw_filled_circle(Ellensegx, Ellensegy, 10)
OLED.draw_filled_circle(Ellensegx + 20, Ellensegy, 10)
OLED.draw_filled_circle(Ellensegx + 40, Ellensegy, 10)

def on_forever():
    pass
basic.forever(on_forever)
