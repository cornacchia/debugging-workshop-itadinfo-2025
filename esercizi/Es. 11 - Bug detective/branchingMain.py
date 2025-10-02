# Versione 1 - sappiamo cosa aspettarci nei diversi punti
from branching1 import controlla_se_piove, controlla_se_sole, controlla_temperatura_sotto_zero, controlla_tanto_vento
# Versione 2 - dati i controlli, manipolare i dati per catturare il bug
#from branching2 import controlla_se_piove, controlla_se_sole, controlla_temperatura_sotto_zero, controlla_tanto_vento

"""
Esercizio 1 - Importare le funzioni da branching1.py e implementare dei controlli delle assunzioni sullo stato del
programma nei diversi punti dove compare l'etichetta "Controllo". Usare questi controlli per catturare il bug contenuto
in una delle funzioni importate da branching1.

Esercizio 2 - Mantenendo i controlli implementati per l'esercizio 1, manipolare lo stato cambiando i valori delle variabili
pioggia, sole, vento, temperatura per individuare qualche funzione importata da branching2 contiene un bug.
"""

stato = {
  "pioggia": False,
  "sole": False,
  "vento": 0,
  "temperatura": 0
}

if controlla_se_piove(stato):
  # Controllo
  if controlla_temperatura_sotto_zero(stato):
    # Controllo
    print("Prendi tuta da neve")
  else:
    if controlla_tanto_vento(stato):
      # Controllo
      print("Non uscire")
    else:
      # Controllo
      print("Prendi ombrello")
else:
  if controlla_se_sole(stato):
    # Controllo
    print("Prendi occhiali da sole")
  else:
    # Controllo
    print("Prendi felpa")