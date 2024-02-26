import pygame
import os
import random
arr=[i for i in range(1,9)]

# music_file = "C:/Users/Rayat/Downloads/pepperfry/vijay_proj/a.mp3"
def play_music(music):
    pygame.init()
    pygame.mixer.music.load(f"C:/Users/Rayat/Downloads/pepperfry/vijay_proj/{music}.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    
            query=input("pause/play/change: ")
            match query:
                
                case "pause":
                        pygame.mixer.music.pause()
                            
                case "change":
                        pygame.mixer.music.pause()
                        rand2=None
                        
                        rand2=random.choice(arr)
                        play_music(rand2)
                       

                case _:
                        print("nothing")


def main():
    rand=random.choice(arr)

    play_music(rand)

    pygame.quit()
    
main()
