from database import get

def newFighter() -> str:
    battler = get("format")

    battler = battler.replace("#adjective#", get("adjective"))
    battler = battler.replace("#character#", get("character"))
    battler = battler.replace("#sidekick#", get("character"))
    battler = battler.replace("#power#", get("power"))
    battler = battler.replace("#weapon#", get("weapon"))

    return battler