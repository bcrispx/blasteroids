import pygame
import time

class BackgroundSound:
    def __init__(self):
        self.current_tempo = 1.0  # Base tempo multiplier
        self.base_interval = 1.0  # Base interval between beats in seconds
        self.last_beat_time = 0
        self.beat_count = 0
        self.is_playing = False
        
        # Create two different pitched beats
        self.low_beat = self._create_beat(220.0)  # A3 note
        self.high_beat = self._create_beat(440.0)  # A4 note
        
    def _create_beat(self, frequency):
        """Create a sine wave beat sound"""
        sample_rate = 44100
        duration = 0.1  # 100ms
        num_samples = int(sample_rate * duration)
        
        # Generate sine wave
        buf = pygame.mixer.Sound.get_length(pygame.mixer.Sound(buffer=bytes(num_samples)))
        pygame.sndarray.make_sound(buf)
        return pygame.mixer.Sound(buffer=buf)
        
    def update(self, level):
        """Update the tempo based on the current level"""
        self.current_tempo = 1.0 + (level - 1) * 0.2  # Increase tempo by 20% per level
        current_time = time.time()
        
        if current_time - self.last_beat_time >= self.base_interval / self.current_tempo:
            self._play_beat()
            self.last_beat_time = current_time
            
    def _play_beat(self):
        """Play alternating high and low beats"""
        if self.beat_count % 2 == 0:
            self.low_beat.play()
        else:
            self.high_beat.play()
        self.beat_count += 1
        
    def start(self):
        """Start playing the background sound"""
        self.is_playing = True
        self.last_beat_time = time.time()
        
    def stop(self):
        """Stop playing the background sound"""
        self.is_playing = False
