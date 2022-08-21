
# 9am-5pm
# Water - water.mp3 (3.5) litres - Drank -log
# Eyes - eyes.mp3 -every 30 min - EyDone - log
# Physical activity - physical.mp3 every -45 min - ExDone - log

# Rules 
# Pygame module to play audio 
from pygame import mixer
from datetime import datetime
from time import time

def musicofloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        _input = input()
        if _input == stopper:
            mixer.music.stop()
            break
            

def log_now(msg):
    with open('mylog.txt','a') as op:
        op.write(f'{msg} {datetime.now()}\n')

if __name__ == '__main__':
    _initwater=time()
    _initexr= time()
    _initphy =time()
    watersecs = 4
    exsecs =30
    physecs =45
    while True:
        if time() - _initwater > watersecs:
            print("Water Drinking time Enter 'drank' to stop the alarm")
            musicofloop(r'C:\Users\hksai\OneDrive\Desktop\my codes\water.mp3','drank')
            _initwater=time()
            log_now("Drank Water at ")
        
        if time() - _initexr > exsecs:
            print("Eye Exercise time Enter 'eydone' to stop the alarm")
            musicofloop(r'C:\Users\hksai\OneDrive\Desktop\my codes\eyes.mp3','eydone')
            _initexr = time()
            log_now("Eyes relaxed at ")
        if time() - _initphy > physecs:
            print("Physical Activity time Enter 'exdone' to stop the alarm")
            musicofloop(r'C:\Users\hksai\OneDrive\Desktop\my codes\physical.mp3','exdone')
            _initphy = time()
            log_now("Physical Exercise at ")
