import pygame

class AudioManager:
    def __init__(self):

        pygame.mixer.init()

        self.bgm_channel = pygame.mixer.Channel(0)
        self.effect_channel = pygame.mixer.Channel(1)

    def play_bgm(self, file_path):

        sound = pygame.mixer.Sound(file_path)
        self.bgm_channel.play(sound, loops=-1, fade_ms=1000)

    def click_effect(self):

        sound_effect = pygame.mixer.Sound("sources/audio/click.wav")
        self.effect_channel.play(sound_effect)
