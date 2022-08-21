from time import time
from pygame import mixer


print('This is a screen break Reminder:')
def music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while (True):
        _input_user = input()
        if _input_user== stopper:
            mixer.music.stop()
            break
        

def log_data(msg):
    with open('log_data.txt','a')as op:
        op.write(msg+'\n')

if __name__=='__main__':
    _init_time = time()
    maintime = 30*60
    
    while(1):
        if time()- _init_time>= maintime:
            print('plzz')
            
            
            music(open(r'C:\Users\hksai\OneDrive\Desktop\my codes\water.mp3'),'stop')
            msg= input('')
            log_data(msg)




    