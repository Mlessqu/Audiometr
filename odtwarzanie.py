import pyaudio
import wave
import time
def odtwarzanie(filename,wf,p,stream):
    chunk = 1024
    data = wf.readframes(chunk)
    stream.start_stream()
    #stream.stop_stream()
    #stream.close()
    #wf.close()
    #p.terminate()