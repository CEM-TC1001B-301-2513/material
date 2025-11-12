variable = 150
match variable:
    case 50:
        print("Vale 50")
    case 100:
        print("Vale 100")
    case "hola":
        print("Hola")
    case _:
        print("Caso por default")