from database import get

def newFigher():
    battler = get("format")

    battler = battler.replace("#adjective#", get("adjective"))
    battler = battler.replace("#character#", get("character"))
    battler = battler.replace("#occupation#", get("occupation"))
    battler = battler.replace("#power#", get("power"))
    battler = battler.replace("#weapon#", get("weapon"))

    return battler