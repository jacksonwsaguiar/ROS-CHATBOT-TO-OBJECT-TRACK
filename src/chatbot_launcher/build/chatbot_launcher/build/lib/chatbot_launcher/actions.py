point_dict = {
        "biblioteca": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
        "almoxarifado": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
        "cozinha": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
        "lazer": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0),
        }

def go_to(point):
    if point in point_dict:
        print(f"Rota processada...\nIndo para '{point}': {point_dict[point]}")
    else:
        print("Não identifiquei o destino: {point}")