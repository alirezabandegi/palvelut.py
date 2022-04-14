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
  
class Palvelu(Asiakas):
   
  def __init__(self, tuotenimi):
    """Konstruktori"""
    self.tuotenimi = tuotenimi
    self.__asiakkaat = []

  def _luo_asiakasrivi(self, Asiakas):
    return f"{self.set_nimi} ({self.set_numero}) on {self.set_ika}-vuotias."
 
  def lisaa_asiakas(self, Asiakas):
    try:
      self.__asiakkaat.append(Asiakas)
    except ValueError:
      pass
  
  def poista_asiakas(self, Asiakas):
    try:
      self.__asiakkaat.pop(Asiakas)
    except ValueError:
        pass

  def tulosta_asiakkaat(self):
    print(f" tuotteen " + self.tuotenimi + " asiakkaat ovat: ")
    for Asiakas in self.__asiakkaat:
      print(self._luo_asiakasrivi(Asiakas))
  
