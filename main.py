consultas_marcadas = {
    'Nome': [],
    'Dia': [],
    'Mês': [],
    'Horário': []
}

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
    consulta = {}
    for key in consultas_marcadas:
        consulta[key] = input(f"Digite o {key} da consulta: ")
    consultas_marcadas['Nome'].append(consulta['Nome'])
    consultas_marcadas['Dia'].append(consulta['Dia'])
    consultas_marcadas['Mês'].append(consulta['Mês'])
    consultas_marcadas['Horário'].append(consulta['Horário'])
    print("Consulta marcada com sucesso!")


def ver_consultas_marcadas():
    if consultas_marcadas['Nome']:
        print("Consultas Marcadas:")
        for i in range(len(consultas_marcadas['Nome'])):
            consulta = {}
            for key in consultas_marcadas:
                consulta[key] = consultas_marcadas[key][i]
            print(f"Paciente: {consulta['Nome']} - Data da Consulta: {consulta['Dia']}/{consulta['Mês']} - Horário da Consulta: {consulta['Horário']}")
    else:
        print("Não há consultas marcadas no momento.")


def cancelar_consulta():
    nome = input("Digite o nome do paciente para cancelar a consulta: ")
    if nome in consultas_marcadas['Nome']:
        index = consultas_marcadas['Nome'].index(nome)
        for key in consultas_marcadas:
            consultas_marcadas[key].pop(index)
        print("Consulta cancelada com sucesso!")
    else:
        print("Paciente não tem consulta marcada.")


if __name__ == "__main__":
    Menu()
    Menu()
valid_name()
valid_age()
HC_options()
marcar_consulta()
ver_consultas_marcadas()
cancelar_consulta()