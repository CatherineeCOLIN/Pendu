import random
import tkinter as tk

# Liste de mots pour le jeu, à modifier pour plus d ediversité, voir s'il y a pas un dictionnaire 
liste_mots = ["pomme", "banane", "orange", "kiwi", "citron"]

# Fonction pour choisir un mot aléatoire de la liste
def choisir_mot(liste):
    mot = random.choice(liste)
    return (mot)
# Fonction pour initialiser la chaîne de caractères de la réponse
def initialiser_reponse(mot):
  reponse = "_" * len(mot)
  return (reponse)

# Fonction pour vérifier si la lettre est dans le mot
def verifier_lettre(lettre, mot, reponse):
    nouvelle_reponse = ""
    for i in range(len(mot)):
        if mot[i] == lettre:
            nouvelle_reponse += lettre
        else:
            nouvelle_reponse += reponse[i]
    return (nouvelle_reponse)

# Fonction principale du jeu
def jouer():
    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Jeu du pendu")

    # Choix d'un mot aléatoire dans la liste
    mot = choisir_mot(liste_mots)
    reponse = initialiser_reponse(mot)
    vies = 6
    lettres_utilisees = []

    # Fonction pour mettre à jour le dessin du pendu
def dessiner_pendu():
  pendu_items = [tete, bras_gauche, bras_droit, corps, jambe_gauche, jambe_droite]
  vies = 6
  for i in range(0, 6):
    if i < vies:
      pendu_items[i].config(state=tk.NORMAL)
    else:
      pendu_items[i].config(state=tk.DISABLED)

  # Fonction appelée lorsqu'une lettre est entrée
def entrer_lettre():
  vies, lettres_utilisees, reponse
  lettre = lettre_entree.get().lower()
  lettre_entree.delete(0, tk.END)  # Effacer l'entrée après avoir appuyé sur le bouton
  if lettre in lettres_utilisees:
    lettre_deja_utilisee_label.config(text="Vous avez déjà entré cette lettre!")
  elif lettre in mot:
    reponse = verifier_lettre(lettre, mot, reponse), mot_label.config(text="Mot: " + reponse)
  else:
    vies -= 1
    vies_restantes_label.config(text="Vies restantes: " + str(vies))
    lettre_deja_utilisee_label.config(text="La lettre " + lettre + " n'est pas dans le mot."), dessiner_pendu(), lettres_utilisees.append(lettre)
    if "_" not in reponse:
      gagne_label = tk.Label(fenetre, text="Vous avez gagné! Le mot était " + mot + ".")
      gagne_label.pack()
      jouer_bouton.config(state=tk.DISABLED)  
      # Désactiver le bouton Jouer si la partie est terminée
    elif  vies == 0:
      perdu_label = tk.Label(fenetre, text="Vous avez perdu! Le mot était " + mot + ".")
      perdu_label.pack()
      jouer_bouton.config(state=tk.DISABLED)  
      # Désactiver le bouton Jouer

  # Création des éléments de la fenêtre
mot_label = tk.Label(fenetre, text="Mot: " + reponse)
mot_label.pack()
vies_restantes_label = tk.Label(fenetre, text="Vies restantes: " + str(vies))
vies_restantes

print(dessiner_pendu, mot_label)
