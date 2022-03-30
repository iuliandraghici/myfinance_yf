from automobil import Automobil


class Achizitie:
    def __init__(self, masina1: Automobil, masina2: Automobil, masina3: Automobil,
                 masina4: Automobil, masina5: Automobil, masina6: Automobil, masina7: Automobil):
        self.masini = [masina1, masina2, masina3, masina4, masina5, masina6, masina7]

    def return_proposed_vehicles(self) -> list[Automobil]:
        nr_cilindri = int(input("Nr cilindri?"))
        nr_roti = int(input("Nr roti?"))
        culoare = input("Culoare?")
        vopsea_metalizata = bool(input("Vopsea metalizata?"))
        return [
            m for m in self.masini
            if nr_cilindri == m.get_motor().get_nr_cilindiri() and
               nr_roti == m.get_nr_roti() and
               culoare == m.get_culoare() and
               vopsea_metalizata == m.get_vopsea_metalizata()
        ]
