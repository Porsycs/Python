print("Qual seu nome?")
nome = input()

print("Meu nome é %s"%nome.title())

print("Qual sua idade?")
idade = input()

print("Nome: " + nome.title() + " Idade: " + idade)

print("Nome: %s Idade: %s" %(nome.title(),idade))

print(f"Nome: {nome.title()} Idade: {idade}")

print(f"{nome.title()} nasceu em: {2020 - int(idade)}")