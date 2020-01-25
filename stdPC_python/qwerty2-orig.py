from adafruit_hid.keycode import Keycode

MOUSE_INCR = 5
MOUSE_NW=-1
MOUSE_N=-2
MOUSE_NE=-3
MOUSE_W=-4
MOUSE_CLICK=-5
MOUSE_E=-6
MOUSE_SW=-7
MOUSE_S=-8
MOUSE_SE=-9
MOUSE_DBL_CLICK=-10
MOUSE_RIGHT_CLICK=-11
MOUSE_DRAG=-12

qwerty = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.WINDOWS,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))

overlay2 = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.WINDOWS,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))
overlay3 = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.WINDOWS,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))
overlay4 = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.WINDOWS,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))
overlay5 = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.WINDOWS,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))
overlay6 = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.WINDOWS,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))