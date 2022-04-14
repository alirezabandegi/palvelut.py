import random

class Asiakas:
  
  """Luokka, joka ottaa kaikki tavikeet käytäjältä.
  :ivar __nimi: asikkaan nimi, arvotaan
  :type __nimi: str
  :ivar __ika: asikkaan ikä, arvotaan
  :type __ika: int

  Julkiset metodit:
    set_nimi()
    set_ika()
    set_numero()
      
  yksityiset metodit:
    __luo_nro()
    """
  
  def __init__(self, nimi, ika):
    """Konstruktori"""
    self.__nimi = nimi
    self.__asiakasnumero = self.__luo_nro
    self.__ika = ika
  
  def __luo_nro(self):
    """
    metodi joka, valita asiakkaan numerot
    :return: number
    :rtype: list(int)
    """

    number = []

    number.append(random.randint(0, 99))
    number.append(random.randint(0, 999))
    number.append(random.randint(0, 999))

    return number
  
  def set_nimi(self):
    """
    Palauttaa nimi.
    """
    try:
      return Asiakas.__nimi
    except ValueError:
      pass
  
  def set_ika(self):
    """
    palauttaa iän
    """
    try:
      return Asiakas.__ika
    except ValueError:
      pass

  def set_numero(self):
    """
    sijoittaa asikkaan numerot ja palauttaa niitä
    """
    return f'{Asiakas.__asiakasnumero[0]:02}-{Asiakas.__asiakasnumero[1]:03}-{Asiakas.__asiakasnumero[2]:03}'
