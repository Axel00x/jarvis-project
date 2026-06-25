import asyncio
import edge_tts
import pygame
import os

async def tts(text):
    await edge_tts.Communicate(text, "it-IT-DiegoNeural").save("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
    
    # close voice file after playback
    pygame.mixer.quit()
    os.remove("voice.mp3")