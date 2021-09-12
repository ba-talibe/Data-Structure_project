import sys

class Noeud:
    def __init__(self, parent, nom):
        self.parent = parent
        self.nom = nom
        self.fils = list()

    def __call__(self):
        print(self.nom)

    def listdir(self):
        for i in self.fils:
            print(i.nom)
        print()

    def ajoutFils(self, nom):
        trouve = False
        for i in self.fils:
            if i.nom == nom:
                trouve = True
        if not trouve:
            self.fils.append(Noeud(self, nom))
        else:
            print(nom, "existe deja")

    def supprimeFils(self, nom):
        trouve = False
        for i in self.fils:
            if i.nom == nom:
                self.fils.remove(i)
                trouve = True

        if not trouve:
            print("impossible de trouver le repeertoire", nom)

    def getcwd(self): #repertoire de travail actuel
        noeud = self
        cwd = [self.nom]
        while  noeud.parent != None:
            noeud = noeud.parent
            cwd.append(noeud.nom)
        cwd.reverse()
        cwd = "/".join(cwd)
        return cwd





root = Noeud(None, "root")
currentN = root

def usage():
    print("Usage : ")
    print("\t cd      : pour changer de repertoire")
    print("\t mkdir   : pour creer un repertoire")
    print("\t ls      : pour lister les elements du repertoire courant")
    print("\t pwd     : pour connaitre le chemin du repertoire courant")
    print("\t tree    : pour afficher l'arborescence des repertoires")
    print("\t rm      : pour supprimer un repertoire")
    print("\n")


def affiche(noeud, n):
    print("\t"*(n-1) + "|" + "-------" + noeud.nom)
    for i in noeud.fils:
        affiche(i, n+1)

def tree(root):
    niveau = 1
    affiche(root, niveau)


def main():
    usage()
    root = Noeud(None, "root")
    currentN = root

    cmd = ""
    while cmd != "exit":
        try:
            print()
            prompt = currentN.getcwd() + "~$ "
            cmd = input(prompt)
            if cmd == "ls":
                currentN.listdir()
            elif cmd[:2] == "cd":
                cmd = cmd.split(" ")
                if len(cmd) == 1:
                    currentN = root
                    continue
                rep = cmd[1]
                found = False
                if rep == "..":
                    if currentN.parent == None:
                        print("Vous etes a la racine")
                    else:
                        currentN = currentN.parent
                    continue

                for reps in currentN.fils:
                    if rep == reps.nom:
                        currentN = reps
                        found = True
                if not found:
                    print("impossible de trouver le repeertoire", rep)

            elif cmd[:5] == "mkdir":
                cmd = cmd[5:].split()
                for rep in cmd:
                    currentN.ajoutFils(rep)

            elif cmd[:2] == "rm":
                cmd = cmd[2:].split()
                for rep in cmd:
                    currentN.supprimeFils(rep)

            elif cmd == "ls":
                currentN.listdir()

            elif cmd == "pwd":
                print(currentN.getcwd())

            elif cmd == "tree":
                print("======== arborescence =======")
                tree(root)
            elif cmd == "exit":
                sys.exit(0)
            else:
                usage()
        except KeyboardInterrupt:
            print("\nArret ...")
            sys.exit(0)

if __name__ == "__main__":
    main()
