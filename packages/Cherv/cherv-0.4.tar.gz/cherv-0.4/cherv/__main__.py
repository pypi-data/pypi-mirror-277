import sys
from cherv.cherv import cherv_say
import json

settings = json.load(open("cherv/settings.json", 'r'))
SKIN = settings["skin"]
skins = {0: "Белый", 1: "Чёрный"}
def main():
    global SKIN
    if (len(sys.argv) >= 2):
        if (sys.argv[1] == "--help"):
            print(
                """Использование: python -m cherv [сообщение]
                Список доступных команд:
                --help    Справка по использованию
                --skin    Выбрать облик червя
                """)
            return
        if (sys.argv[1] == "--skin"):
            print("Введите номер облика, чтобы использовать его.")
            print("Доступные облики червя:\n")
            for k, v in skins.items():
                print(f"{k} - {v}")
            num = int(input("-> "))
            if num not in skins.keys():
                print("Неверное значение.\n")
                return
            SKIN = num
            settings["skin"] = num
            cherv_say("Облик изменён!", skin=SKIN)
            return         
        cherv_say(" ".join(sys.argv[1:]), skin=SKIN)

    if len(sys.argv) < 2:
        cherv_say(skin=SKIN)

if __name__ == "__main__":
    main()
    json.dump(obj=settings, fp=open("cherv/settings.json", 'w'))