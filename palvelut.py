import random
from typing import List


class Asiakas:
    __nimi: str
    __asiakasnro: List[int]
    __ika: int

    """Luokka, joka ottaa kaikki tavikeet käytäjältä.

    :ivar __nimi: asikkaan nimi, arvotaan
    :type __nimi: str
    :ivar __ika: asikkaan ikä, arvotaan
    :type __ika: int

    Julkiset metodit:
        nimi()
        ika()
        asiakasnro()

    suojatut metodit:
        _randfixed_digit(int)

    yksityiset metodit:
        __luo_nro(int)
    """    

    def __init__(self, nimi, ika) -> None:
        """Konstruktori"""

        self.__nimi = nimi
        self.__ika = ika
        self.__luo_nro()

    @property
    def nimi(self):
        """Palauttaa nimi.

        :return: nimi
        :rtype: str
        """
        return self.__nimi

    @nimi.setter
    def nimi(self, nimi: str):
        """Palauttaa nimi.

        :param nimi: nimi
        :type nimi: str
        :return: nimi
        :rtype: str
        """
        if(nimi):
            self.__nimi = nimi
        else:
            raise Exception("Oho, tuli jotain vihe!\nAntaa uuden nimen.")

    @property
    def ika(self):
        """Palauttaa ikä.

        :param ika: ikä
        :type ika: int
        :return: ikä
        :rtype: int
        """
        return self.__ika

    @ika.setter
    def ika(self, ika: int):
        """Palauttaa ikä.

        :param ika: ikä
        :type ika: int
        :return: ikä
        :rtype: int
        """
        if(ika):
            self.__ika = ika
        else:
            raise Exception("Oho, tuli jotain vihe!\nAntaa uuden iän.")

    @property
    def asiakasnro(self):
        """Palauttaa asikasnumero.

        :return: asikasnumero
        :rtype: str
        """
        return f"{str(self.__asiakasnro[0:2])}-{self.__asiakasnro[2:5]}-{self.__asiakasnro[5:9]}"

    @asiakasnro.setter
    def asiakasnro(self, asiaksnro: list[int]):
        self.__asiakasnro = asiaksnro

    def _randfixed_digit(self, digits):
        """Palauttaa satunnaisen asikasnumero.

        :param digits: digits näyttää, kuninka monta kertaa pitää toistaa
        :type digits: int
        :return: asikasnumero
        :rtype: str
        """
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, digits)])

    def __luo_nro(self):
        """sijoittaa kaikki numerot oikeaan paikkaan.

        :return: asikasnumero
        :rtype: str
        """
        self.__asiakasnro = [self._randfixed_digit(
            2), self._randfixed_digit(3), self._randfixed_digit(3)]


class Palvelu():
    tuotenimi: str
    __asiakkaat: List[Asiakas]

    """Luokka, joka tulostaa asikkaan tiedot.

    :ivar tuotenimi: tuotenimi, arvotaan
    :type tuotenimi: str
    :ivar __asiakkaat: asiakkaiden nimet, ottaa kaikki asiakkaiden nimet.
    :type __asiakkaat: str

    Julkiset metodit:
        lisaa_asiakas()
        poista_asiakas()
        tulosta_asiakkaat()

    suojatut metodit:
        _luo_asiakarivi(str)
    """    

    def __init__(self, tuotenimi: str):
        """Konstruktori"""
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakarivi(self, asiakas: Asiakas) -> str:
        """rakentaa asikas tiedot 

        :return: asikas tiedot
        :rtype: str
        """
        return f"{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika}-vuotias."

    def lisaa_asiakas(self, asiakas: Asiakas):
        """lisää asikas __asikkaat listaan

        :return: asikas class:in asikaat nimet
        :rtype: str
        """
        if(asiakas):
            self.__asiakkaat.append(asiakas)

        else:
            raise Exception("Oho, tuli jotain vihe!\nAntaa Asiakas.")

    def poista_asiakas(self, asiakas: Asiakas):
        """poitaa asikas __asikkaat listasta

        :return: poistaa asikas
        :rtype: str
        """
        try:
            self.__asiakkaat.remove(asiakas)
        except:
            print("Ei valittetavasi lyötynyt.")
            pass

    def tulosta_asiakkaat(self):
        """tulostaa asikas tiedot.

        :return: asikaat tiedot
        :rtype: str
        """
        print(f"Tuotteen {self.__asiakkaat[-1]} asiakkaat ovat:")
        print(self._luo_asiakarivi)
        



class ParempiPalvelu(Palvelu):
    __edut: List[str]

    """Luokka, joka toteuttaa edut.

    :ivar tuotenimi: tuotenimi, arvotaan
    :type tuotenimi: str
    :ivar __edut: asikkaan edu
    :type __edut: str

    Julkiset metodit:
        lisaa_etu(str)
        poista_etu(str)
        tulosta_edut()
    """ 

    def __init__(self, tuotenimi):
        """Konstruktori"""
        super(ParempiPalvelu, self).__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, b: str):
        """lisää edut __edut listaan

        :return: asikas Edut
        :rtype: str
        """
        if(b):
            self.__edut.append(b)
        else:
            raise Exception("Oho, tuli jotain vihe!\nAntaa edu.")

    def poista_etu(self, b: str):
        """poistaa edut __edut listaan

        :return: asikas Edut
        :rtype: str
        """
        try:
            self.__edut.remove(b)
        except:
            print("Ei valittetavasi lyötynyt.")
            pass

    def tulosta_edut(self):
        """tulostaa asiakkaan ostokset tiedot.

        :return: asikaat tiedot
        :rtype: str
        """

        print(f"Tuotteen {self.__asiakkaat} edut ovat:")
        print(f"Jauhaa {self.__edut}.")
