#Główny plik skryptu audiometr
import odtwarzanie as play
import os #dla current directory
import time
import threading
import pyaudio
import wave
import stop

class odtwarzanie():
    def __init__(self):
        #self.lista_plikow = ["125.wav", "250.wav", "500.wav", "1k.wav", "2k.wav", "4k.wav", "8k.wav"]
        self.sciezka = os.getcwd()
        self.p = pyaudio.PyAudio()

    def callback(self,in_data, frame_count, time_info, status): #funkcja callbacku do odtwarzania w tle niezaleznie wzieta z dokumentacji PyAudio
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def stop(self):
        print("Stopuję:" + self.filename)
        self.stream.close()

    def odtwarzanie(self,filename):
        chunk = 1024
        self.filename = filename
        print("Odtwarzam:" + filename)
        self.wf = wave.open(self.sciezka + "\\" + filename, 'rb')
        data = self.wf.readframes(chunk)
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                  channels=self.wf.getnchannels(),
                                  rate=self.wf.getframerate(),
                                  output=True,
                                  stream_callback=self.callback)

        self.stream.start_stream()
        # stream.stop_stream()
        # stream.close()
        # wf.close()
        # p.terminate()


    # muzyczka = threading.Thread(target=play.odtwarzanie, args=(sciezka + "\\oktawy\\125.wav", wf, p, stream), daemon=True)
    # muzyczka.start()

