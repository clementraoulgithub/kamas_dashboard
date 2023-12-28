"""All enums used in the project are defined here"""

from enum import Enum, unique


@unique
class ServerRetro(Enum):
    """Enum of the differents RETRO servers"""

    BOUNE = "boune"
    CRAIL = "crail"
    ERATZ = "eratz"
    GALGARION = "galgarion"
    HENUAL = "henual"


@unique
class ServerClassic(Enum):
    """Enum of the differents CLASSIC servers"""

    DRACONIROS = "draconiros"
    HELLMINA = "hellmina"
    IMAGIRO = "imagiro"
    OMBRE = "ombre"
    ORUKAM = "orukam"
    TALKASHA = "talkasha"
    TYLEZIA = "tylezia"


@unique
class ServerTouch(Enum):
    """Enum of the differents TOUCH servers"""

    BRUTAS = "brutas"
    DODGE = "dodge"
    GRANDAPAN = "grandapan"
    HERDEGRIZE = "herdegrize"
    OSHIMO = "oshimo"
    TERRA_COGITA = "terra-cogita"


@unique
class LineGraphScope(Enum):
    """Enum of the differents line graph scope"""

    YEAR = 0
    SIX_MONTHS = 1
    THREE_MONTHS = 2
    MONTH = 3
    WEEK = 4
    DAY = 5


@unique
class Website(Enum):
    """
    Enum of the differents websites to scrap

    Args:
        Enum (Enum): the enum class
    """

    D2GATE = ("D2gate", "https://fr.d2gate.net")
    KAMAS_FACILE = ("Kamas facile", "https://www.kamasfacile.com")
    FUN_SHOP = ("Fun shop", "https://www.funshopes.com")
    MODE_MARCHAND = ("Mode marchand", "https://www.mode-marchand.net")
    TRY_AND_JUDGE = ("Try and judge", "https://www.tryandjudge.com")
    IG_PLAYS = ("Ig plays", "https://www.igplays.com")
    LE_KAMAS = ("Le kamas", "https://www.lekamas.fr")
    I_GAME_GOLD = ("I game gold", "https://www.igamegold.com")
