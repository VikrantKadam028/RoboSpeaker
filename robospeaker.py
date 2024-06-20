# import os
import win32com.client as wc

#For MAC OS
# if __name__=='__main__':
#     print("Welcome to RoboSpeaker 2.0 | Created by Vikrant")
#     while True:
#         x = input("Enter what to pronounce? (q for Quit):")
#         if x .upper()=="q":
#             break
#         else:
#             command = f"say{x}"
#             os.system(command)


#For Windows
def text_to_speech(text):
    speaker = wc.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

if __name__=="__main__":
    print("Welcome to RoboSpeaker 2.0 | Created by Vikrant")
    while True:
        text = input("What to Pronounce? (q for Quit) :")
        if text.lower() == "q":
            text_to_speech("Bye,Have a nice day!")
            break
        else:
            text_to_speech(text)
