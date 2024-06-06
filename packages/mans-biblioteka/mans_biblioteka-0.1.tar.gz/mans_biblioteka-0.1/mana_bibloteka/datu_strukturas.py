class Persona:
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards

    def pilns_vards(self):
        return self.vards + " " + self.uzvards
