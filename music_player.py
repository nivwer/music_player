import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.init()
        pygame.mixer.init()
        self.volume = 0.5
        pygame.mixer.music.set_volume(self.volume)
        self.music_folder = music_folder
        
    def help(self):
        print("\n Commands:\n   play.song/p.song\n   stop/s\n   pause\n   new.song/n.song\n   queue.song/q.song\n   volume.num/v.num\n   exit\n   help\n   ")

    def verify(self, song_name):
        song_name = song_name.lower()
        for file in os.listdir(self.music_folder):
            if file.lower() == f"{song_name}.mp3":
                song_path = os.path.join(self.music_folder, file)
                file = file.split(".")
                return [song_path, file]
        return False
        
    def play_song(self, song_name):
        file = self.verify(song_name)
        if file == False:
            return print("song not found")
        pygame.mixer.music.load(file[0]) 
        pygame.mixer.music.play()
        print(f" + {file[1][0]}")
            
    def stop_song(self):
        pygame.mixer.music.stop()
        print(" - Stopped")

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            if pygame.mixer.music.get_pos() > 0:
                if not pygame.mixer.music.get_paused():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    def play_new_song(self, song_name):
        self.stop_song()
        self.play_song(song_name)

    def queue_song(self, song_name):
        file = self.verify(song_name)
        if file == False:
            return print("song not found")
        pygame.mixer.music.queue(file[0])
        print(f" + {file[1][0]}")

    def set_volume(self, volume):
        self.volume = float(volume) / 100.0
        pygame.mixer.music.set_volume(self.volume)
        
    def exit(self):
        exit()
        
    

