class Treino:
    def __init__(self, nome_treino, carga, tempo_de_descanso, series, repeticoes):
        self.nome_treino = nome_treino
        self.carga = carga
        self.tempo_de_descanso = tempo_de_descanso
        self.series = series
        self.repeticoes = repeticoes


    def exibir_info_treino(self):
        print(f'Treino: {self.nome_treino}')
        print(f'Carga: {self.carga} kg')
        print(f'Tempo de Descanso: {self.tempo_de_descanso} seg')
        print(f'Séries: {self.series}')
        print(f'Repeticoes: {self.repeticoes}')

class SessaoTreino:
    def __init__(self):
        self.treinos = []

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

    def exibir_info_sessao(self):
        print(f"Sessão de Treino: {nome_sessao}")
        print(" ")
        for treino in self.treinos:
            print(f"Treino: {treino.nome_treino}")
            print(f"Carga: {treino.carga} kg")
            print(f"Tempo de Descanso: {treino.tempo_de_descanso} segundos")
            print(f"Séries: {treino.series} séries")
            print(f"Repeticoes: {treino.repeticoes}")
            print('----------'*3)

# ...

class Aluno:
    def __init__(self, nome_aluno, idade, peso, altura):
        self.nome_aluno = nome_aluno
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.treinos = []  # Alteração aqui

    def criar_sessao_treino(self):
        nova_sessao = SessaoTreino()
        self.treinos.append(nova_sessao)  # Alteração aqui
        return nova_sessao
    
    def exibir_info_aluno(self):
        print(' ')
        print(f"Nome: {self.nome_aluno}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")

    def imc(self):
        imc = self.peso/(self.altura *self.altura)
        if imc < 18.5:
            result_imc =('ABAIXO DO PESO')
        elif imc<25.1:
            result_imc =("PESO IDEAL")
        elif imc<30.1:
            result_imc =("SOBREPESO")
        elif imc<40.1:
            result_imc =("OBESIDADE")
        else:
            result_imc=("OBESIDADE MÓRBIDA")
        print(f"Seu imc é de {imc:.2f}, logo encontra-se na faixa de: {result_imc}")
        # return(imc, result_imc)

        

    def exibir_treinos(self):
        if self.treinos:
            print(F"\nEXERCÍCIOS DO ALUNO: {self.nome_aluno}")
            print(" ")
            for treino in self.treinos:
                treino.exibir_info_sessao()  # Alteração aqui
                print('=' * 30)
        else:
            print(self.nome_aluno, "ainda não possui treinos!")

# ...

# Exemplo de uso:
aluno1 = Aluno("Rafael Guimarães", 42, 96.6, 1.72)

# Criar treinos
nome_sessao = ("Peito")
exerc1 = Treino("Supino Inclinado com Halteres", 20, 60, 4, 'Máximo 11')
exerc2 = Treino("Supino Reto com Halteres", 20, 65, 4, 'Máximo 10')
exerc3 = Treino("Voador na Máquina", 50, 60, 4, 'Máximo 9')
exerc4 = Treino("Flexões", '--' , 60, 4, 'Máximo')
exerc5 = Treino("Triceps na Polia", 40 , 60, 4, 'Máximo 10')

# Criar sessão de treino para o aluno

sessao_peito = aluno1.criar_sessao_treino()
sessao_peito.adicionar_treino(exerc1)
sessao_peito.adicionar_treino(exerc2)
sessao_peito.adicionar_treino(exerc3)
sessao_peito.adicionar_treino(exerc4)
sessao_peito.adicionar_treino(exerc5)

# sessao_do_dia = aluno1.criar_sessao_treino()
# sessao_do_dia.adicionar_treino(exerc1)
# sessao_do_dia.adicionar_treino(exerc2)
# sessao_do_dia.adicionar_treino(exerc3)
# sessao_do_dia.adicionar_treino(exerc4)
# sessao_do_dia.adicionar_treino(exerc5)

# Exibir informações do aluno e da sessão de treino
aluno1.exibir_info_aluno()
aluno1.imc()
aluno1.exibir_treinos()

