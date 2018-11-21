import glob
# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
from pathlib import Path
# The final path component, without its suffix
 
 
mon_chemin = input('Quel est le chemin relatif du répertoire contenant les fichiers csv ?\n')
#"./MIB_Files/"
 
mon_alias = input('Alias du fichier py créé (sera ./MaBase_alias.py) ?\n')
 
mon_fic = "MaBase_%s.py" % mon_alias
 
mes_csv_file = {Path(f).stem:open(f,"r") for f in glob.glob(mon_chemin + "*.csv")}
 
mes_csv = {Path(f).stem:open(f,"r").readlines() for f in glob.glob(mon_chemin + "*.csv")}
 
mon_py = open(mon_fic,"w+")
 
 
def creer_classes():
    for b in mes_csv:
        mon_py.write("class " + b[4:-1] + ":\n\tdef __init__(self")
        lignes = mes_csv[b]
        attributs = lignes[0].split()[0].split(',')
        for a in attributs:
            mon_py.write(", " + a)
        mon_py.write("):\n\t\t")
        for a in attributs:
            mon_py.write("self.%s = %s\n\t\t" % (a,a))
        mon_py.write("\n\n")
        
            
def creer_bases():
    for b in mes_csv:
        nom = b[4:-1]
        mon_py.write(b + " = { ")
        lignes = mes_csv[b]
        for index,ligne in enumerate(lignes[1:]):
            ligne = ligne.split()[0].split(',')
            debut = '' if index == 0 else ', '
            mon_py.write(debut + nom + "(")
            for att in ligne[:-1]:
                mon_py.write("'" + att + "', ")
            mon_py.write("'" + ligne[-1] +"')")
        mon_py.write(" }\n\n")
        
 
def ferme():
    for b in mes_csv_file:
        mes_csv_file[b].close()
    mon_py.close()
 
 
creer_classes()
creer_bases()
ferme()class Responsable:
        def __init__(self, NoAllee, Nom):
                self.NoAllee = NoAllee
                self.Nom = Nom
                
 
class Miam:
        def __init__(self, NomAlien, Aliment):
                self.NomAlien = NomAlien
                self.Aliment = Aliment
                
 
class Agent:
        def __init__(self, Nom, Ville):
                self.Nom = Nom
                self.Ville = Ville
                
 
class Gardien:
        def __init__(self, Nom, NoCabine):
                self.Nom = Nom
                self.NoCabine = NoCabine
                
 
class Alien:
        def __init__(self, Nom, Sexe, Planete, NoCabine):
                self.Nom = Nom
                self.Sexe = Sexe
                self.Planete = Planete
                self.NoCabine = NoCabine
                
 
class Cabine:
        def __init__(self, NoCabine, NoAllee):
                self.NoCabine = NoCabine
                self.NoAllee = NoAllee
                
 
BaseResponsables = { Responsable('1', 'Seldon'), Responsable('2', 'Pelorat') }
 
BaseMiams = { Miam('Zorglub', 'Bortsch'), Miam('Blorx', 'Bortsch'), Miam('Urxiz', 'Zoumise'), Miam('Zbleurdite', 'Bortsch'), Miam('Darneurane', 'Schwanstucke'), Miam('Mulzo', 'Kashpir'), Miam('Zzzzzz', 'Kashpir'), Miam('Arghh', 'Zoumise'), Miam('Joranum', 'Bortsch') }
 
BaseAgents = { Agent('Branno', 'Terminus'), Agent('Darell', 'Terminus'), Agent('Demerzel', 'Uco'), Agent('Seldon', 'Terminus'), Agent('Dornick', 'Kalgan'), Agent('Hardin', 'Terminus'), Agent('Trevize', 'Hesperos'), Agent('Pelorat', 'Kalgan'), Agent('Riose', 'Terminus') }
 
BaseGardiens = { Gardien('Branno', '1'), Gardien('Darell', '2'), Gardien('Demerzel', '3'), Gardien('Seldon', '4'), Gardien('Dornick', '5'), Gardien('Hardin', '6'), Gardien('Trevize', '7'), Gardien('Pelorat', '8'), Gardien('Riose', '9') }
 
BaseAliens = { Alien('Zorglub', 'M', 'Trantor', '1'), Alien('Blorx', 'M', 'Euterpe', '2'), Alien('Urxiz', 'M', 'Aurora', '3'), Alien('Zbleurdite', 'F', 'Trantor', '4'), Alien('Darneurane', 'M', 'Trantor', '4'), Alien('Mulzo', 'M', 'Helicon', '6'), Alien('Zzzzzz', 'F', 'Aurora', '7'), Alien('Arghh', 'M', 'Nexon', '8'), Alien('Joranum', 'F', 'Euterpe', '9') }
 
BaseCabines = { Cabine('1', '1'), Cabine('2', '1'), Cabine('3', '1'), Cabine('4', '1'), Cabine('5', '1'), Cabine('6', '2'), Cabine('7', '2'), Cabine('8', '2'), Cabine('9', '2') }
