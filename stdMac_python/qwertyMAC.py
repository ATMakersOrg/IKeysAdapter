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

SHORTCUT_TILDE=-100
SHORTCUT_BACK=-101
SHORTCUT_FWD=-102
SHORTCUT_REFRESH=-103
SHORTCUT_HOME=-104
SHORTCUT_SEARCH=-105
SHORTCUT_BOOKMARKS=-106
SHORTCUT_HISTORY=-107
SHORTCUT_PRINT=-108
SHORTCUT_COPY=-109
SHORTCUT_SYSBROWSER=-110
SHORTCUT_CHROME=-111
SHORTCUT_ADDRBAR=-112
SHORTCUT_WWW=-113
SHORTCUT_COM=-114
SHORTCUT_NET=-115
SHORTCUT_GOV=-116
SHORTCUT_EDU=-117
SHORTCUT_ORG=-118
SHORTCUT_IKEYS=-119

shortcuts=((Keycode.LEFT_SHIFT,Keycode.GRAVE_ACCENT),(Keycode.COMMAND,Keycode.LEFT_ARROW),
            (Keycode.COMMAND,Keycode.RIGHT_ARROW),
            (Keycode.COMMAND,Keycode.R),
            (Keycode.COMMAND,Keycode.LEFT_SHIFT,Keycode.H),
            (Keycode.COMMAND,Keycode.F),
            (Keycode.COMMAND,Keycode.LEFT_SHIFT,Keycode.B),
            (Keycode.COMMAND,Keycode.Y),
            (Keycode.COMMAND,Keycode.P),
            (Keycode.COMMAND,Keycode.C),
            [(Keycode.COMMAND,Keycode.SPACE),Keycode.S,Keycode.A,Keycode.F,Keycode.A,Keycode.R,Keycode.I,Keycode.ENTER],
            [(Keycode.COMMAND,Keycode.SPACE),Keycode.C,Keycode.H,Keycode.R,Keycode.O,Keycode.M,Keycode.E,Keycode.ENTER],
            (Keycode.COMMAND,Keycode.L),
            [Keycode.W,Keycode.W,Keycode.W,Keycode.PERIOD],
            [Keycode.PERIOD,Keycode.C,Keycode.O,Keycode.M],
            [Keycode.PERIOD,Keycode.N,Keycode.E,Keycode.T],
            [Keycode.PERIOD,Keycode.G,Keycode.O,Keycode.V],
            [Keycode.PERIOD,Keycode.E,Keycode.D,Keycode.U],
            [Keycode.PERIOD,Keycode.O,Keycode.R,Keycode.G],
            (Keycode.COMMAND,Keycode.LEFT_SHIFT,Keycode.H))

qwerty = ((Keycode.ESCAPE,Keycode.TAB,Keycode.GRAVE_ACCENT,Keycode.KEYPAD_NUMLOCK,Keycode.KEYPAD_NUMLOCK,Keycode.INSERT,Keycode.HOME,Keycode.END,Keycode.END,Keycode.PAGE_UP,Keycode.PAGE_DOWN,Keycode.DELETE),
	  (Keycode.F1,Keycode.F2,Keycode.F3,Keycode.F4,Keycode.F5,Keycode.F6,Keycode.F7,Keycode.F8,Keycode.F9,Keycode.F10,Keycode.F11,Keycode.F12),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.COMMA,Keycode.PERIOD,Keycode.FORWARD_SLASH,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.COMMAND,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))

webaccess = ((SHORTCUT_BACK,SHORTCUT_FWD,Keycode.ESCAPE,SHORTCUT_REFRESH,SHORTCUT_HOME,SHORTCUT_SEARCH,SHORTCUT_BOOKMARKS,SHORTCUT_HISTORY,SHORTCUT_PRINT,SHORTCUT_COPY,SHORTCUT_SYSBROWSER,SHORTCUT_CHROME),
	  (Keycode.TAB,Keycode.FORWARD_SLASH,SHORTCUT_TILDE,Keycode.KEYPAD_NUMLOCK,SHORTCUT_ADDRBAR,SHORTCUT_WWW,SHORTCUT_COM,SHORTCUT_NET,SHORTCUT_GOV,SHORTCUT_EDU,SHORTCUT_ORG,SHORTCUT_IKEYS),
	  (Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO,Keycode.MINUS,Keycode.EQUALS),
	  (Keycode.Q,Keycode.W,Keycode.E,Keycode.R,Keycode.T,Keycode.Y,Keycode.U,Keycode.I,Keycode.O,Keycode.P,Keycode.BACKSPACE,Keycode.BACKSPACE),
	  (Keycode.A,Keycode.S,Keycode.D,Keycode.F,Keycode.G,Keycode.H,Keycode.J,Keycode.K,Keycode.L,MOUSE_NW,MOUSE_N,MOUSE_NE),
	  (Keycode.Z,Keycode.X,Keycode.C,Keycode.V,Keycode.B,Keycode.N,Keycode.M,Keycode.SEMICOLON,Keycode.QUOTE,MOUSE_W,MOUSE_CLICK,MOUSE_E),
	  (Keycode.CAPS_LOCK,Keycode.LEFT_SHIFT,Keycode.LEFT_SHIFT,Keycode.PAGE_UP,Keycode.SPACEBAR,Keycode.SPACEBAR,Keycode.PAGE_DOWN,Keycode.COMMA,Keycode.PERIOD,MOUSE_SW,MOUSE_S,MOUSE_SE),
	  (Keycode.LEFT_CONTROL,Keycode.LEFT_ALT,Keycode.COMMAND,Keycode.LEFT_ARROW,Keycode.RIGHT_ARROW,Keycode.UP_ARROW,Keycode.DOWN_ARROW,Keycode.ENTER,Keycode.ENTER,MOUSE_DBL_CLICK,MOUSE_RIGHT_CLICK,MOUSE_DRAG))
