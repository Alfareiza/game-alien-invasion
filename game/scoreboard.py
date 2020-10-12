import pygame.font


class Scoreboard():
    """Uma classe para mostrar informações da pontuação"""

    def __init__(self, ai_settings, screen, stats):
        """Inicializa os atributos da puntuação"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (255, 237, 0)
        self.font = pygame.font.SysFont(None, 48)

        # prepares the image of the initial score
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)

    def prep_high_score(self):
        pass
