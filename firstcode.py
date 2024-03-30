def Menu():
    while True:
        print("Seja Bem-Vindo ao Sistema HC - Hospital das Clínicas!")
        name = input("Primeiramente, digite seu nome: ")
        while valid_name(name) == False:
            name = input("Digite seu nome novamente: ")
        age = input(f"Perfeito {name}, agora digite sua idade: ")
        valid_age(age)
        if int(age) < 18:
            print("É necessário ser maior de idade para utilizar o sistema.")
            break
        HC_options()


def valid_name(name):
    if name.isalpha() and len(name) > 3:
        return True
    else:
        print(f"\'{name}\' não é um nome válido, tente novamente!")
        return False


def valid_age(age):
    while age.isnumeric() == False:
        age = input("Idade Inválida, Digite sua idade novamente: ")
    return True


def HC_options():
    options_dict = {1: "Marcar Consulta",
                    2: "Ver Consultas Marcadas",
                    3: "Cancelar Consulta",
                    4: "Sair"
                    }
    for key in options_dict:
        print(f"{key} - {options_dict[key]}")
    option = input("Escolha o número da opção desejada: ")


if __name__ == "__main__":
    Menu()
valid_name()
valid_age()
HC_options()