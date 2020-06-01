#Główny plik skryptu audiometr
import odtwarzanie as play
import os #dla current directory
import time
import threading
import pyaudio
import wave
import stop

class odtwarzanie():
    def __init__(self, filename):
        #self.lista_plikow = ["125.wav", "250.wav", "500.wav", "1k.wav", "2k.wav", "4k.wav", "8k.wav"]
        self.nazwa_pliku
        self.sciezka = os.getcwd()
        self.p = pyaudio.PyAudio()
        self.czasy_slyszalnosci = []
        self.wf = wave.open(self.sciezka + "\\oktawy\\" + self.filename, 'rb')
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True,
                        stream_callback=self.callback)
    def callback(self,in_data, frame_count, time_info, status): #funkcja callbacku do odtwarzania w tle niezaleznie wzieta z dokumentacji PyAudio
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
    def odtwarzanie(self):
        chunk = 1024
        print("Odtwarzam:" + filename)
        data = self.wf.readframes(chunk)
        self.stream.start_stream()
        # stream.stop_stream()
        # stream.close()
        # wf.close()
        # p.terminate()


    # muzyczka = threading.Thread(target=play.odtwarzanie, args=(sciezka + "\\oktawy\\125.wav", wf, p, stream), daemon=True)
    # muzyczka.start()

    for i in range(0, len(lista_plikow)):



        play.odtwarzanie(sciezka + "\\oktawy\\" + lista_plikow[i], wf, p, stream)
        start = time.time()
        # muzyczka = threading.Thread(target=play.odtwarzanie(sciezka+ "\\oktawy\\"+lista_plikow[i],wf, p, stream))
        # muzyczka.start()
        while keep_going:
            pass
        koniec = time.time()
        stop.stop(p, stream)
        koniec = time.time()
        stream.stop_stream()
        stream.close()
        wf.close()
        czas = koniec - start
        print(czas)
        czasy_slyszalnosci.append(czas)
        p.terminate()
