class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GRAY = (50, 50, 50)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 105, 180)
    BROWN = (139, 69, 19)

    INDEX = {
        'BLACK': 0,
        'RED': 1,
        'GREEN': 2,
        'BLUE': 3,
        'YELLOW': 4,
        'CYAN': 5,
        'MAGENTA': 6,
        'ORANGE': 7,
        'PURPLE': 8,
        'PINK': 9,
        'BROWN': 10,
        'GRAY': 11,
        'LIGHT_GRAY': 12,
        'DARK_GRAY': 13,

    }

    COLOR = {v: k for k, v in INDEX.items()}

    @classmethod
    def get_index(cls, color_name: str) -> int:
        return cls.INDEX.get(color_name.upper(), -1)

    @classmethod
    def get_color(cls, color_index: int):
        color_name = cls.COLOR.get(color_index, 'BLACK')
        return getattr(cls, color_name)

    @classmethod
    def get_name(cls, rgb: tuple) -> str:
        for attr, value in cls.__dict__.items():
            if value == rgb:
                return attr
        return 'BLACK'


class StateMent:
    ORIGINAL = 100
    PENCIL = 200
    BUCKET = 300


class Settings:
    def __init__(self):
        self.METHOD: int = StateMent.PENCIL
        self.selected_color: int = Colors.get_index('RED')
        self.want_to_change = None

