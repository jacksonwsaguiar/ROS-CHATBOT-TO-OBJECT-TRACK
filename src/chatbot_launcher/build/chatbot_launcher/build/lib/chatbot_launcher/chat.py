import re
from . import actions

intent_dict = {
        r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)": actions.go_to,
        r"\b[Mm][e](?:\sleve)?\s?[at][ée]?\s(.+)": actions.go_to,
        r"\b[Cc][hegue](?:\sno)?\s?[ponto]?\s(.+)": actions.go_to,
        }

def main():
    command = input("Digite o seu comando: ")
    for key, function in intent_dict.items():
        pattern = re.compile(key)
        point = pattern.findall(command)
        if point:
            print("Encontrei uma intenção! Computando...")
            function(point[0])
            break

if __name__ == "__main__":
    main()