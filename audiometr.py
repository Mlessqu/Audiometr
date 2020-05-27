#Główny plik skryptu audiometr
import odtwarzanie as play
import os #dla current directory
import time
import threading
import pyaudio
import wave
import stop
import keyboard
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)
def key_capture_thread():
    global keep_going
    while 1:
        a = keyboard.read_key()
        if a == "esc":
            keep_going = False
            time.sleep(0.1)
print("Audiometr")
lista_plikow = ["125.wav", "250.wav", "500.wav", "1k.wav", "2k.wav", "4k.wav", "8k.wav"]
sciezka = os.getcwd()
print(sciezka)
#muzyczka = threading.Thread(target=play.odtwarzanie, args=(sciezka + "\\oktawy\\125.wav", wf, p, stream), daemon=True)
#muzyczka.start()
czasy_slyszalnosci = []
button_capture = threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True)
button_capture.start()
for i in range (0, len(lista_plikow)):
    keep_going = True
    print("Odtwarzam:" + lista_plikow[i])
    p = pyaudio.PyAudio()
    wf = wave.open(sciezka + "\\oktawy\\" + lista_plikow[i], 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
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

for i in range(len(czasy_slyszalnosci)):
    print("Plik:" + lista_plikow[i])
    print("Usłyszano po:" + str(czasy_slyszalnosci[i]))
    dB = czasy_slyszalnosci[i] * 1/30 * 2 # 1/30 bo 30s trwa zmiana z 0 do 1 amplitudy(sciezka audio)
    # a jedna zmiana amplitudy się przekłada(chyba, badz w tym przypadku) na 2dB
    db = dB - 60 #maksymalna wartość to 0 więc odejmuję 60
    print("Decybele w tym momencei to:" + str(dB))