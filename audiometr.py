#Główny plik skryptu audiometr
import odtwarzanie as play
import os #dla current directory

print("Audiometr")
sciezka = os.getcwd()
print(sciezka)
print(sciezka + "\\oktawy\\125.wav")#upewniam sie ze sciezka poprawna
play.odtwarzanie(sciezka + "\\oktawy\\125.wav")