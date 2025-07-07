import pyttsx3
import pyjokes
engine = pyttsx3.init()
# engine.say('''I will speak this text :
#       hello Harsh ! 
#        How are you....
#       what are you doing now 
#       hello''')

jokes = pyjokes.get_joke()
engine.say("jokes :",jokes)
print("Joke: ", jokes)
engine.runAndWait()
# engine.runAndWait() is used to process the voice commands
