import os
import pygame
import numpy as np

class SoundManager:
    def __init__(self):
        self.sounds = {}
        pygame.mixer.init(44100, -16, 2, 2048)
        pygame.mixer.set_num_channels(8)
        self._load_sounds()
        self._create_background_beats()
        self.last_beat_time = 0
        self.beat_interval = 1.0  # Start with 1 second between beats
        self.beat_toggle = False
        
    def _create_background_beats(self):
        """Create the classic arcade-style background beats"""
        sample_rate = 44100
        duration = 0.1  # 100ms
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        
        # Create low beat (110 Hz)
        low_beat = np.sin(2 * np.pi * 110 * t) * 0.3
        self.sounds['low_beat'] = pygame.mixer.Sound(low_beat.astype(np.float32))
        self.sounds['low_beat'].set_volume(0.2)
        
        # Create high beat (146.8 Hz, D3 note)
        high_beat = np.sin(2 * np.pi * 146.8 * t) * 0.3
        self.sounds['high_beat'] = pygame.mixer.Sound(high_beat.astype(np.float32))
        self.sounds['high_beat'].set_volume(0.2)
        
    def _load_sounds(self):
        """Load all sound effects"""
        sound_dir = os.path.join(os.path.dirname(__file__), 'sounds')
        
        # Define sound files and their volumes
        sound_files = {
            'shoot': ('shoot.wav', 0.3),
            'explosion_large': ('explosion_large.wav', 0.4),
            'explosion_small': ('explosion_small.wav', 0.3),
            'thrust': ('thrust.wav', 0.2),
            'game_over': ('game_over.wav', 0.5),
            'level_up': ('level_up.wav', 0.4)
        }
        
        # Load each sound file
        for name, (filename, volume) in sound_files.items():
            try:
                full_path = os.path.join(sound_dir, filename)
                if os.path.exists(full_path):
                    sound = pygame.mixer.Sound(full_path)
                    sound.set_volume(volume)
                    self.sounds[name] = sound
            except pygame.error:
                pass
    
    def update_background(self, level, current_time):
        """Update background beat based on level"""
        # Adjust beat interval based on level (faster at higher levels)
        target_interval = max(0.3, 1.0 - (level - 1) * 0.1)  # Don't go faster than 0.3s
        self.beat_interval = target_interval
        
        # Check if it's time for next beat
        if current_time - self.last_beat_time >= self.beat_interval:
            self.beat_toggle = not self.beat_toggle
            if self.beat_toggle:
                self.sounds['low_beat'].play()
            else:
                self.sounds['high_beat'].play()
            self.last_beat_time = current_time
    
    def play(self, sound_name):
        """Play a sound by name"""
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except pygame.error:
                pass
    
    def play_thrust(self):
        """Special handling for thrust sound to avoid overlapping"""
        if 'thrust' in self.sounds:
            # Only play if it's not already playing
            if not pygame.mixer.get_busy():
                try:
                    self.sounds['thrust'].play()
                except pygame.error:
                    pass
    
    def stop_thrust(self):
        """Stop the thrust sound"""
        if 'thrust' in self.sounds:
            try:
                self.sounds['thrust'].stop()
            except pygame.error:
                pass
