#install an external module and use it perform an operation of your interest

import pyttsx3 # type: ignore
engine=pyttsx3.init()
engine.say("Hey Rahul How are You")
engine.runAndWait()
