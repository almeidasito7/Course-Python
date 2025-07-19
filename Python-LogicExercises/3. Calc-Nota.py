#solicitando os dados dos alunos
print("")
print("--------------------------")
print("DIGITE OS DADOS DOS ALUNOS")
print("--------------------------")
print("")
email_aluno = input("Informe o e-mail do aluno: ")
nota_semestral = input("Informe a nota semestral do aluno: ")
print("")
#convertendo a nota para float
nota_semestral = float(nota_semestral)
#realizando o teste lógico
if nota_semestral > 8.5:
    print("ENVIANDO CONVITE PARA O E-MAIL: {}".format(email_aluno))
    print("")
else:
    print("Infelizmente sua nota não atingiu a média necessária para o programa, agradecemos sua participação.")
    print("")