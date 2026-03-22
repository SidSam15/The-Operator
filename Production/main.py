import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, TextEntry
keyboard = KMKKeyboard()
keyboard.keymap = [
    [
        KC.LCTRL(KC.LALT(KC.F)),  #Fusion
        KC.LCTRL(KC.LALT(KC.B)),  #Bambu Lab
        KC.LCTRL(KC.LALT(KC.V)),  #VS Code
        KC.LCTRL(KC.LALT(KC.G)),  #Google Chrome
    ],
]
keyboard.col_pins = (
    board.GP10,
    board.GP9,
    board.GP8,
    board.GP7,
)
keyboard.row_pins = ()
keyboard.diode_orientation = None
keyboard.internal_pullup = True
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = (
    (board.GP0, board.GP1, board.GP2),
)
led_on = True
def toggle_leds(key, keyboard, *args):
    global led_on
    if led_on:
        rgb.disable()
    else:
        rgb.enable()
    led_on = not led_on
    update_oled_status()
encoder_handler.map = [
    (
        (KC.VOLU, KC.VOLD), 
        toggle_leds    
    ),
]
rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=16,
)
rgb.brightness = 0.2
keyboard.extensions.append(rgb)
ssd1306_display = SSD1306(i2c=board.I2C())
key_text = TextEntry(text='Last key: None', x=0, y=0)
rgb_text = TextEntry(text='RGB: ON', x=0, y=10)
oled = Display(
    display=ssd1306_display,
    width=128,
    height=64,
    entries=[key_text, rgb_text],
)
keyboard.extensions.append(oled)
last_key = "None"
def update_oled_status(key=None):
    key_text.text = f"Last key: {last_key}"
    rgb_text.text = f"RGB: {'ON' if led_on else 'OFF'}"
    oled.text(f"Last key: {last_key}", 0, 0)
    oled.text(f"RGB: {'ON' if led_on else 'OFF'}", 0, 10)
    oled.show()
def on_key_press(key, keyboard, *args):
    update_oled_status(key)

keyboard.on_press.append(on_key_press)
if __name__ == "__main__":
    keyboard.go()