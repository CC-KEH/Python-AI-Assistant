import speech_recognition as sr
import os
import webbrowser
from assistant import assistant
from organise import organiser
from ai import Ai
if __name__ =="__main__":
    assistant = assistant()
    organizer = organiser()
    ai = Ai()
    sites = [['youtube','https://youtube.com'],['google','https://google.com'],['twitch','https://twitch.tv'],['wikipedia','https://wikipedia.com']]
    while True:
        print('Listening...')
        query = assistant.take_command()
        for site in sites:
            if(f"Open {site[0]}".lower() in query.lower()):
                assistant.say(f"opening {site[0]}")
                webbrowser.open(f'{site[1]}')
        
        if('open' in query):
            command = query.lower().replace('open ', '')
            assistant.open_program(command)
                         
        if('organise' in query):
            # documents in programs in c drive
            # documents \\ programs \\ c drive
            # cdrive \\ programs \\ documents
            query = query.title().replace('In','\\')
            path = list(query.split(' \\ '))
            path.append('C:\\Users')
            path.pop(0)
            path.reverse()
            print(path)
            
            # cdrive\\programs\\documents by converting to string
            
            final_path = organiser.makePath(path)
            organiser.organise(final_path)
            print(final_path)
        if('what' or 'which' or 'who' or 'when' or 'how' in query):
             assistant.say(ai.bard(question=query))