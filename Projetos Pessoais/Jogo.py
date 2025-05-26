import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Plataforma 2D")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Clock para controlar o FPS
clock = pygame.time.Clock()
FPS = 60


# Classe do Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (100, ALTURA - 100)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.pulando = False
        self.vidas = 3
        self.pontuacao = 0

    def update(self):
        # Aplica gravidade
        self.velocidade_y += 0.8
        if self.velocidade_y > 10:
            self.velocidade_y = 10

        # Atualiza posição
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Limita movimento nas bordas
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
            self.pulando = False
            self.velocidade_y = 0

    def pular(self):
        if not self.pulando:
            self.velocidade_y = -15
            self.pulando = True

    def mover_esquerda(self):
        self.velocidade_x = -5

    def mover_direita(self):
        self.velocidade_x = 5

    def parar(self):
        self.velocidade_x = 0


# Classe da Plataforma
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Classe do Inimigo
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = 1
        self.velocidade = 2
        self.contador_movimento = 0

    def update(self):
        self.rect.x += self.direcao * self.velocidade
        self.contador_movimento += 1

        # Inverte direção após certo tempo ou se colidir com algo
        if self.contador_movimento > 100:
            self.direcao *= -1
            self.contador_movimento = 0


# Classe da Moeda (para coletar)
class Moeda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# Função para criar o nível
def criar_nivel():
    plataformas = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()
    moedas = pygame.sprite.Group()

    # Plataforma principal
    plataformas.add(Plataforma(0, ALTURA - 40, LARGURA, 40))

    # Outras plataformas
    plataformas.add(Plataforma(100, ALTURA - 150, 200, 20))
    plataformas.add(Plataforma(400, ALTURA - 250, 200, 20))
    plataformas.add(Plataforma(200, ALTURA - 350, 200, 20))
    plataformas.add(Plataforma(500, ALTURA - 450, 200, 20))

    # Inimigos
    inimigos.add(Inimigo(300, ALTURA - 170))
    inimigos.add(Inimigo(500, ALTURA - 270))

    # Moedas
    for i in range(10):
        x = random.randint(50, LARGURA - 50)
        y = random.randint(50, ALTURA - 100)
        moedas.add(Moeda(x, y))

    return plataformas, inimigos, moedas


# Função principal do jogo
def main():
    jogador = Jogador()
    todas_sprites = pygame.sprite.Group()
    todas_sprites.add(jogador)

    plataformas, inimigos, moedas = criar_nivel()
    todas_sprites.add(plataformas)
    todas_sprites.add(inimigos)
    todas_sprites.add(moedas)

    # Fonte para texto
    fonte = pygame.font.SysFont('Arial', 24)

    # Loop principal do jogo
    executando = True
    while executando:
        # Processa eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            # Controles do jogador
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogador.mover_esquerda()
                if evento.key == pygame.K_RIGHT:
                    jogador.mover_direita()
                if evento.key == pygame.K_SPACE:
                    jogador.pular()
                if evento.key == pygame.K_ESCAPE:
                    executando = False

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jogador.velocidade_x < 0:
                    jogador.parar()
                if evento.key == pygame.K_RIGHT and jogador.velocidade_x > 0:
                    jogador.parar()

        # Atualiza sprites
        todas_sprites.update()
        inimigos.update()

        # Verifica colisão com plataformas
        if jogador.velocidade_y > 0:  # Se estiver caindo
            colisoes_plataforma = pygame.sprite.spritecollide(jogador, plataformas, False)
            if colisoes_plataforma:
                for plataforma in colisoes_plataforma:
                    if jogador.rect.bottom < plataforma.rect.centery:
                        jogador.rect.bottom = plataforma.rect.top
                        jogador.velocidade_y = 0
                        jogador.pulando = False

        # Verifica colisão com inimigos
        colisoes_inimigos = pygame.sprite.spritecollide(jogador, inimigos, False)
        if colisoes_inimigos:
            # Verifica se está pulando em cima do inimigo
            for inimigo in colisoes_inimigos:
                if jogador.velocidade_y > 0 and jogador.rect.bottom < inimigo.rect.centery:
                    inimigo.kill()
                    jogador.velocidade_y = -10  # Salto ao matar inimigo
                    jogador.pontuacao += 100
                else:
                    jogador.vidas -= 1
                    jogador.rect.x = 100  # Respawn
                    jogador.rect.y = ALTURA - 100
                    if jogador.vidas <= 0:
                        executando = False

        # Verifica colisão com moedas
        colisoes_moedas = pygame.sprite.spritecollide(jogador, moedas, True)
        for moeda in colisoes_moedas:
            jogador.pontuacao += 10
            # Adiciona nova moeda
            x = random.randint(50, LARGURA - 50)
            y = random.randint(50, ALTURA - 100)
            nova_moeda = Moeda(x, y)
            moedas.add(nova_moeda)
            todas_sprites.add(nova_moeda)

        # Renderização
        tela.fill(PRETO)
        todas_sprites.draw(tela)

        # Mostra vidas e pontuação
        texto_vidas = fonte.render(f'Vidas: {jogador.vidas}', True, BRANCO)
        texto_pontuacao = fonte.render(f'Pontuação: {jogador.pontuacao}', True, BRANCO)
        tela.blit(texto_vidas, (10, 10))
        tela.blit(texto_pontuacao, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()