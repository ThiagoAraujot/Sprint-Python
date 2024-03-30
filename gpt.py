consultas_marcadas = {}  # Dicionário para armazenar as consultas marcadas

def Menu():
    while True:
        print("Seja Bem-Vindo ao Sistema HC - Hospital das Clínicas!")
        name = input("Primeiramente, digite seu nome: ")
        while not valid_name(name):
            name = input("Digite seu nome novamente: ")
        age = input(f"Perfeito {name}, agora digite sua idade: ")
        while not valid_age(age):
            age = input("Idade Inválida, Digite sua idade novamente: ")
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
    return age.isnumeric()


def HC_options():
    options_dict = {
        1: "Marcar Consulta",
        2: "Ver Consultas Marcadas",
        3: "Cancelar Consulta",
        4: "Sair"
    }
    for key in options_dict:
        print(f"{key} - {options_dict[key]}")
    option = int(input("Escolha o número da opção desejada: "))
    
    if option == 1:
        marcar_consulta()
    elif option == 2:
        ver_consultas_marcadas()
    elif option == 3:
        cancelar_consulta()
    elif option == 4:
        print("Saindo do sistema. Até mais!")
        exit()
    else:
        print("Opção inválida.")


def marcar_consulta():
    paciente = input("Digite o nome do paciente: ")
    consulta = input("Digite o horário da consulta (hh:mm): ")
    consultas_marcadas[paciente] = consulta
    print("Consulta marcada com sucesso!")


def ver_consultas_marcadas():
    if consultas_marcadas:
        print("Consultas Marcadas:")
        for paciente, consulta in consultas_marcadas.items():
            print(f"Paciente: {paciente} - Horário da Consulta: {consulta}")
    else:
        print("Não há consultas marcadas no momento.")


def cancelar_consulta():
    paciente = input("Digite o nome do paciente para cancelar a consulta: ")
    if paciente in consultas_marcadas:
        del consultas_marcadas[paciente]
        print("Consulta cancelada com sucesso!")
    else:
        print("Paciente não tem consulta marcada.")


if __name__ == "__main__":
    Menu()
