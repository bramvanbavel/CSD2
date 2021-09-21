
import winsound
from playsound import playsound

val = int(input("enter the number (1,2,3, etc) of times you want to play the sample:"))


for i in range(val):
    playsound("samples\\KickBeelow.wav",winsound.SND_ASYNC)
  