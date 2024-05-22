# outside imports
import speech_recognition as sr
import time
import playsound as ps
import os
import sys
import pygetwindow as getwindow
import tkinter as Tk
import random
from googletrans import Translator

# keyboard imports
import pynput
from pynput.keyboard import Key, Controller
import pyautogui as pg

# my project imports
import create_audio_file as createAudio
import main as mn
import main_background as main_background
#from main import stop

keyboard = Controller()

def command(question):
    print("question: "+question)
    #double check
    # !!! all definitions of words should be in lower case !!!
    if(question=="0" or question=="jan" or question=="jam"):
        ps.playsound("sound/"+"slucham.mp3",True)
        return 1
    
    elif("zdjęcie" in question or "zdjęć" in question or "fokus" in question or "focus" in question):
        conf=1
        conf_step=0.1
        debug = 1
        found = 0
        while found == 0:
            if("zdjęcie" in question or "zdjęć" in question):
                red_location = pg.locateCenterOnScreen('find_zdjecie.png',confidence=conf)
            else:
                red_location = pg.locateCenterOnScreen('find_focus.png',confidence=conf)
            if(red_location != None):
                if debug==1:
                    print('found')
                    pg.moveTo(red_location)
                else:
                    pg.click(red_location)
                found = 1
                print("found")
            else:
                conf = conf-conf_step
        return 1

    elif("otwórz" in question):
        focusing = question.split("otwórz",1)[1]
        print("focusing: "+focusing)
        if(len(focusing) >=1):
            try:
                firefoxWindow= getwindow.getWindowsWithTitle(focusing)[0]
                firefoxWindow.activate()
            except:
                print("nie udało się znaleźć: "+focusing)
                ps.playsound("sound/"+"nieznalazlem.mp3")
                print("może uruchom?")
        return 1
    # keyboard simple functionality

    elif("pisz" in question or "napisz" in question):
        writing = question.split("pisz",1)[1]
        writing = writing.split("enter",1)[0]
        print("pisanie: "+writing)
        if(len(writing) >=1):
            pg.typewrite(writing,0.1)
            if("enter" in question):
                pg.press('enter')
        return 1

    elif("naciśnij" in question or "kliknij" in question):
        pressing = question.split("nij",1)[1]
        if(len(pressing) >=1):
            if("control" in pressing): pressing = "ctrl"
            pressing = pressing.replace(" ","")
            print("klikanie: -"+pressing+"-")
            pg.press(pressing)
        return 1

    elif("skrót" in question):
        print("tworzenie")
        first_half = question.split("skrót",1)[1]
        first_half = first_half.split("plus",1)[0]
        second_half = question.split("plus",1)[1]
        
        if(len(first_half) >= 1 and len(second_half) >= 1):
            if("control" in first_half): first_half = "ctrl"
            first_half = first_half.replace(" ","")
            second_half = second_half.replace(" ","")
            print("klikanie: -"+first_half+"- i -"+ second_half+"-")
            pg.hotkey(first_half,second_half)
        return 1

    elif("enter" in question):
        pg.press('enter')
        return 1

    elif("nic" in question or "dzięki" in question):
        ps.playsound("sound/"+"okej.mp3")
        return 0

    elif("funkcje" in question):
        nazwa = "funkcje"
        if("aktualizuj" in question):
            if(os.path.exists(nazwa+".mp3")):
                os.remove("sound/"+nazwa+".mp3")
            with open(nazwa+'.txt', mode='r' ,encoding="utf-8") as file:
                allFunctions = file.read()
            print(allFunctions)
            createAudio.create_audio_file(nazwa,allFunctions) 
        else:
            ps.playsound("sound/"+nazwa+".mp3")
        return 1

    #media control
    elif("uruchom muzykę" in question  or "zatrzymaj muzykę" in question or "włącz muzykę" in question or "wyłącz muzykę" in question or "puść muzykę" in question):
        keyboard.press(Key.media_play_pause)
        return 1
    elif("następna" in question or "kolejna" in question or "następny" in question or "kolejny" in question):
        keyboard.press(Key.media_next)
        return 1
    elif("poprzednia" in question or "wcześniejsza" in question or "poprzedni" in question or "wcześniejszy" in question):
        keyboard.press(Key.media_previous)
        return 1
    #down
    elif("ścisz" in question or "ciszej" in question):        
        if(" o" in question):
            if("zero" in question): 
                number = question.split("o",2)[2]
            else: 
                number = question.split("o",1)[1]
            print(number)
            for i in range(int(number)):
                print("int i to: "+str(i))
                keyboard.press(Key.media_volume_down)
        else:
            keyboard.press(Key.media_volume_down)
        return 1
    # up
    elif("głośniej" in question):
        if(" o" in question):
            if("zero" in question): 
                number = question.split("o",3)[3]
            else: 
                number = question.split("o",2)[2]
            print(number)
            for i in range(int(number)):
                print("int i to: "+str(i))
                keyboard.press(Key.media_volume_up)
        else:
            keyboard.press(Key.media_volume_up)
        return 1   
    elif("podgłośnij" in question):
        if(" o" in question):
            if("zero" in question): 
                number = question.split("o",4)[4]
            else: 
                number = question.split("o",3)[3]
            print(number)
            for i in range(int(number)):
                print("int i to: "+str(i))
                keyboard.press(Key.media_volume_up)
        else:
            keyboard.press(Key.media_volume_up)
        return 1
    #mute
    elif("wycisz" in question or "wyciszenie" in question):
        keyboard.press(Key.media_volume_mute)
        return 1

    elif("używaj głośniku" in question or "używaj głośników" in question or "na głośniki" in question):
        os.system("D:\\GAMES_SHORTS\\PYTHON\\NirCmd_forAudio\\nircmd.exe setdefaultsounddevice \"2269WM\" ")
        ps.playsound("sound/naglosniki.mp3")
        return 1
    elif("używaj słuchawek" in question or "na słuchawki" in question):
        os.system("D:\\GAMES_SHORTS\\PYTHON\\NirCmd_forAudio\\nircmd.exe setdefaultsounddevice \"22EA53\" ")
        ps.playsound("sound/nasluchawki.mp3")
        return 1

    elif("uruchom" in question):
        run = question.split("uruchom",1)[1]
        #run="123"
        print("uruchamianie: "+run)
        ps.playsound("sound/uruchamiam.mp3")
        if(len(run) >=1):
            pg.press('winleft')
            pg.typewrite(run,0.1)
            pg.press('enter')
        return 1

    elif("wyszukaj" in question):
        searching = question.split("wyszukaj",1)[1]
        #run="123"
        print("szukanie: "+searching)
        
        if(len(searching) >=1):
            firefoxWindow= getwindow.getWindowsWithTitle("Firefox")[0]
            firefoxWindow.activate()
            pg.hotkey("ctrl","t")
            pg.hotkey("ctrl","e")
            pg.press('backspace')
            pg.press('backspace')
            searching = searching.replace(" ","")
            pg.typewrite(searching,0.1)
            pg.press('enter')
        return 1

    elif("szukaj" in question or "znajdź" in question):
        searching = question.split("szukaj",1)[1]
        if(len(searching) <1):
            searching = question.split("znajdź",1)[1]
        if(len(searching) >=1):
            pg.hotkey("ctrl","f")
            pg.typewrite(searching,0.1)
            pg.press('enter')

    elif("śpij" in question or "śpi" in question or "sleep" in question or "idź spać" in question):
        ps.playsound("sound/spij.mp3")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return 1

    elif("wyłącz komputer" in question):
        print("PC: wyłączanie")
        os.system("shutdown -s")
        return 1

    elif("zresetuj komputer" in question or "zrestartuj komputer" in question):
        print("PC: reset")
        os.system("shutdown -r")
        return 1

    elif("stwórz audio" in question):
        print("tworzenie")
        tresc = question.split("o treści",1)[1]
        tresc = tresc.split("o tytule",1)[0]
        tytul = question.split("o tytule",1)[1]
        print("tytul: "+tytul)
        print("tresc: "+tresc)
        if(len(tytul) >= 1 and len(tresc) >= 1):
            createAudio.create_audio_file(tytul,tresc) 
            ps.playsound("sound/stworzono.mp3")
            print("stworzono")
        else:
            ps.playsound("sound/nie udalo.mp3")
            print("nie udało się stworzyć pliku")
        return 1

    elif("przeczytaj" in question or "tłumacz" in question or "przetłumacz" in question):
        
        print("czytanie zaznaczonego")
        pg.hotkey("ctrl","c")
        form = Tk.Tk()
        dataToRead = str(form.clipboard_get())
        print(dataToRead)
        if("tłumacz" in question or "przetłumacz" in question):
            translator = Translator()
            dt = translator.detect(dataToRead)
            translated = translator.translate(dataToRead,src=dt.lang,dest='pl')
            dataToRead = translated.text

        seed = 123
        #print("data to read: "+dataToRead+" seed: "+str(seed))
        if(len(dataToRead) >= 1):
            print("tworzenie i odtwarzanie")
            createAudio.create_audio_file(str(seed),dataToRead) 
            os.remove("sound/"+str(seed)+".mp3")
            print("usunięto")
        else:
            ps.playsound("sound/nie udalo.mp3")
            print("nie udało się stworzyć pliku")
        return 1

    #elif("Zrestartuj się"):
    #    print("restarting")
    #    pg.hotkey("ctrl","c")
    #    return 1

    elif("czym jesteś" in question):
        print("jestem interfejsem głosowym")
        ps.playsound("sound/interface.mp3")
        return 1

    elif("dzień dobry" in question or "dobry" in question):
        ps.playsound("sound/dziendobry.mp3")
        return 1

    elif("przywitaj się" in question or "witaj się" in question):
        ps.playsound("sound/dziendobry.mp3")
        return 1
        
    elif("przedstaw się" in question):
        ps.playsound("sound/jestem.mp3")
        return 1

    elif("stop" in question or "wyłącz się" in question):
        if("na" in question):
            na_czas = question.split("na",1)[1]
            if(len(na_czas) >=1):
                print("sleeping: "+na_czas)
                time.sleep(int(na_czas))
        else:
            print("stopping")
            ps.playsound("sound/dowidzenia.mp3")
            #global stop
            mn.stopProgram()
        return 1
    else:
        ps.playsound("sound/jeszczeraz.mp3")
        return 1
    return 0

def main():
    # we start here and we declare mn as main() from main
    #mn.main()
    main_background.main_background()

if __name__ == "__main__":
    main()