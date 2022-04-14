import random

class Asiakas:
  
  def __init__(self, nimi, ika):
    """Konstruktori"""
    self.__nimi = nimi
    self.__asiakasnumero = self.__luo_nro
    self.__ika = ika
  
  def __luo_nro(self):
    number = []

    number.append(random.randint(0, 99))
    number.append(random.randint(0, 999))
    number.append(random.randint(0, 999))

    return number
  
  def set_nimi(self):
    try:
      return Asiakas.__nimi
    except ValueError:
      pass
  
  def set_ika(self):
    try:
      return Asiakas.__ika
    except ValueError:
      pass

  def set_numero(self):
    return f'{Asiakas.__asiakasnumero[0]:02}-{Asiakas.__asiakasnumero[1]:03}-{Asiakas.__asiakasnumero[2]:03}'
