def Menu():
    print("Seja Bem-Vindo ao Sistema HC - Hospital das Clínicas!")
    name = valid_name("Primeiramente, digite seu nome: ")
    age = valid_age(f"Perfeito {name}! Agora digite sua idade: ")
    HC_options()


def valid_name(msg):
    name = input(msg)
    while name.isalpha() == False or len(name) < 3:
        name = input("Nome inválido! Digite seu nome novamente: ")
    return name
    

def valid_age(msg):
    age = input(msg)
    while age.isnumeric() == False:
        age = input("Idade inválida! Digite sua idade novamente: ")
    if int(age) < 18:
        print("É necessário ser maior de idade para utilizar o sistema.")
        exit()
    return age


def HC_options():
    while True:
        options_dict = {1: "Marcar Consulta",
                        2: "Ver Consultas Marcadas",
                        3: "Cancelar Consulta",
                        4: "Sair"
                        }
        for key in options_dict:
            print(f"{key} - {options_dict[key]}")
        option = input("Escolha o número da opção desejada: ")
        match option:
            case "1":
                marcar_consulta()
            case "2":
                ver_consultas_marcadas()
            case "3":
                cancelar_consulta()
            case "4":
                print("Saindo do sistema. Até mais!")
                exit()
            case _:
                print("Opção inválida.")

dic_consulta = {
        'Exame': [],
        'Convênio': [],
        'Dia': [],
        'Mês': [],
        'Horário': []
    }
exames_validos = {
        1: "Exame de Sangue",
        2: "Exame de Urina",
        3: "Exame de Fezes",
        4: "Exame de Imagem",
        5: "Exame de Cardiologia",
        6: "Exame de Neurologia",
        7: "Exame de Endocrinologia",
        8: "Exame de Gastroenterologia",
        9: "Exame de Pediatria",
        10: "Exame de Ortopedia",
        11: "Exame de Oftalmologia",
        12: "Exame de Otorrinolaringologia",
        13: "Exame de Dermatologia",
        14: "Exame de Urologia",
        15: "Exame de Ginecologia",
        16: "Exame de Obstetrícia",
    }
convenios_validos = {
        1: "Unimed",
        2: "SulAmérica",
        3: "Bradesco",
        4: "Amil",
        5: "Golden Cross",
        6: "Particular"
    }

def marcar_consulta():
    print("---Marcar Consulta---")

    for key in exames_validos.keys():
        print(f"{key} - {exames_validos[key]}")
    option = int(input("Escolha o número do exame desejado: "))
    dic_consulta['Exame'].append(exames_validos[int(option)])

    print("Convênios Válidos:")
    for key in convenios_validos.keys():
        print(f"{key} - {convenios_validos[key]}")
    option = int(input("Escolha o número do convênio desejado: "))
    dic_consulta['Convênio'].append(convenios_validos[int(option)])

    dia = valida_dia("Digite o dia da consulta: ")
    dic_consulta['Dia'].append(dia)

    mes = valida_mes("Digite o mês da consulta: ")
    dic_consulta['Mês'].append(mes)

    horario = valida_mes("Digite o horário da consulta: ")
    dic_consulta['Horário'].append(horario)

    print("--Sua consulta foi solicitada, aguarde nossa confirmação por e-mail--")
    return


def ver_consultas_marcadas():
    print("---Consultas Marcadas---")
    if len(dic_consulta['Exame']) < 1:
            print("Não há consultas marcadas no momento.")
            return
    else:
        for exame in dic_consulta['Exame']:
            print(f"Consulta: {exame}")
    option = input("Digite o Nome do exame que deseja ver:")
    for i in range(len(dic_consulta['Exame'])):
        if dic_consulta['Exame'][i] == option:
            index = i
            for key in dic_consulta:
                print(f"{key}: {dic_consulta[key][index]}")
    return

def cancelar_consulta():
    print("---Cancelar Consulta---")
    for exame in dic_consulta['Exame']:
        if not exame:
            print("Não há consultas marcadas no momento.")
            return
        else:
            print(f"Consulta: {exame}")
    option = input("Digite o Nome do exame que deseja cancelar: ")
    for i in range(len(dic_consulta['Exame'])):
        if dic_consulta['Exame'][i] == option:
            index = i
            for key in dic_consulta:
                dic_consulta[key].pop(index)
            print("Consulta cancelada com sucesso!")
    return


def valida_dia(msg):
    dia = input(msg)
    while dia.isnumeric() == False or int(dia) < 1 or int(dia) > 31:
        dia = input("Dia inválido, digite novamente: ")
    return dia

def valida_mes(msg):
    mes = input(msg)
    while mes.isnumeric() == False or int(mes) < 1 or int(mes) > 12:
        mes = input("Mês inválido, digite novamente: ")
    return mes

def valida_horario(msg):
    horario = input(msg)
    while horario.isnumeric() == False or int(horario) < 8 or int(horario) > 17:
        horario = input("Horário inválido, digite novamente: ")
    return horario


if __name__ == "__main__":
    Menu()