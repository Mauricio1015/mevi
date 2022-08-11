import speech_recognition as sr
import subprocess as sub
import pyttsx3, wikipedia, pywhatkit, datetime, keyboard, cam 
from pygame import mixer

name = "mevi"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites={
                'instagram':'https://www.instagram.com/mauriciocorrea1015/',
                'google':'google.com',
                'youtube':'https://www.youtube.com/channel/UCipRzgHhzcGykywQ_NrVrpg',
                'facebook':'https://www.facebook.com/profile.php?id=100011671425992',
                'whatsapp':'web.whatsapp.com',
                'github':'https://github.com/mauricio1111111'
            }

files = {
    'carta':'Carta Pasantia - mauricio_correa.pdf',
    'cedula':'Cedula y papeleta - mauricio_correa.docx',
    'foto':'Foto mauricio_correa.jpg'
}

commands = {
    'play':'spotify play',
    'pausa':'spotify pause'
}

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Te escucho...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
            return rec
    except:
        talk("No te entiendo")
        return "No te entiendo"

def run_mevi():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce','')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)

        elif 'busca'in rec:
                search = rec.replace('buscar','')
                wikipedia.set_lang("es") 
                wiki = wikipedia.summary(search, 1)
                print(search +": " + wiki)
                talk(wiki)       
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip() 
            talk("Alarma activada a las " + num + " horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("DESPIERTA!!!")
                    mixer.init()
                    mixer.music.load("alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'colores' in rec:
            talk("Enseguida")
            cam.capture()
        elif 'abre' in rec:            
            for site in sites:
                if site in rec:
                    sub.call(f'start brave.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abriendo {file}')   
        elif 'chao' in rec:
            talk('Adios!')
            break

def buscar_youtube(search):
    pywhatkit.playonyt(search)                     
            
        

if __name__ == '__main__':
    run_mevi()
