"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
  """
  Construya y retorne un dataframe de Pandas a partir del archivo
  'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

  - El dataframe tiene la misma estructura que el archivo original.
  - Los nombres de las columnas deben ser en minusculas, reemplazando los
    espacios por guiones bajos.
  - Las palabras clave deben estar separadas por coma y con un solo
    espacio entre palabra y palabra.


  """
  
  with open('files/input/clusters_report.txt', 'r') as file:
    data = file.read().split("\n")


  # for i in range(68):
  # if data[43]=="":
  #   print(True)
  # else:
  #   print(False)  
  df = pd.DataFrame(columns= ["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave","principales_palabras_clave"])
  inicia_fila = True
  i = 0
  texto = []
  for linea in data[4:-1]:
    fila = linea.split()
    if inicia_fila:
      inicia_fila = False
      df.loc[i] =[int(fila[0]),int(fila[1]),float(fila[2].replace(",",".")),""]
      texto+=fila[4:]
    else:
      texto+=linea.split()
    if fila ==[]:
      inicia_fila = True
      texto = " ".join(texto)
      texto = texto.replace(".","")
      df.loc[i,"principales_palabras_clave"] = texto
      texto = []
      i+=1
  # df.to_csv("files/salida.csv", sep="\t", index=False)
  return df
# pregunta_01()
