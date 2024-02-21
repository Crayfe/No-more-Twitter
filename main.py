
import time, gi, re
gi.require_version('Wnck', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Wnck

import sys, os
import tkinter as tk
from pygame import mixer
import tkinter.messagebox
from gtts import gTTS

if __name__ == '__main__':
  screen = Wnck.Screen.get_default()
  screen.force_update()
  running = True
  while running:
      while Gtk.events_pending():
        Gtk.main_iteration()
      time.sleep(3)
      focus = screen.get_active_window().get_name()
      program = re.split(' — | - ',focus)[-1]
      
      if program == 'Google Chrome':
        chrome = re.split(' - Google Chrome',focus)[-2]
        page = re.split(' - | / | • ',chrome)[-1]
        
        if page == 'YouTube':
          video = re.split(' - YouTube',focus)[0]
          print(program+" -> "+page+" -> "+video)
      
        elif page == 'X':
          print(program+" -> "+page)
          root = tk.Tk()
          root.withdraw()
          texto = "Te comento esto por si no lo sabías: cada vez que abres twitter muere un gatito en el mundo ¿No te dan pena los gatitos?"

          if not os.path.exists('aviso.mp3'):
            audio = gTTS(text = "Nuevo aviso del sistema", lang= 'es')
            audio.save('aviso.mp3')
    
          audio = gTTS(text = texto, lang= 'es')
          audio.save('audio.mp3')
          mixer.init()
          mixer.music.set_volume(1.0)
          mixer.music.load("aviso.mp3")

          mixer.music.queue("audio.mp3")
          mixer.music.play()
          tk.messagebox.showinfo("Tienes un aviso", texto) # título, mensaje
          os.remove('audio.mp3')
        else:
          print(program+" -> "+page)
      else:
        print(program)
