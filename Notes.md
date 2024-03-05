Methode hyper sensible aux choix des options (nb population, taille population, taux de migration, taille des tournois...).

Sur une issue github, on peut trouver des valeurs par défaut meilleures que celle par défaut installées.

La facon d'échantilloner les données est primordial. Il faut s'assurer d'avoir des points dans les bords de la distribution. Il faut surreprésenter les points extrêmes pour uniformiser les données (applatir la distribution des points pris).

Option de faire du batchking : on envoie tout le data set par petit lot, il faut jouer sur la taille du batch.

imblearn est une librairie pour prendre plus d'outlier dans le set (imbalanced learn).

On peut donner des contraintes dans PySR : ça va déterminer la liste d'opérateurs (ajouter puissance et tanh car tanh et puissance sont dans shue 98) et la complexité de ce qu'on peut trouver à l'intérieur d'un opérateur (par exemple pas plus de 10 de complexité dans la tanh). 

Attention, doc de PySR (cf GitHub) est pas mise à jour par rapport à la libraire.

Nested constraint : contraintes imbriqués : il faut mettre une valeur assez simple, car sinon on va se retrouver avec des sin(cos(sin(...))) ce qui arrive peu dans les équations de la physique. Lui indiquer que l'on ne peut pas faire tan(arctan()) par exemple, tout en laissant les possibilités de tan(log(...))

Il faut qu'on commence petit avec uniquement les opérateurs que l'on connait déjà dans l'équation, puis ajouter des opérateurs en les contraignant rigoureusement.

C'est un algo assez lent, et le temps de calcul est aléatoire.

Peut etre voir pour améliorer la probabilité d'optimiser les constantes à chaque itérations, ce qui n'est pas recommandé dans la doc mais qui peut etre pas mal chez nous car on a beacoup de constantes.

On peut récupérer le .pkl en direct (il est modifié pendant le run du programme) et observer depuis un autre note book ce qu'il se passe.

Peut etre regarder pour essayer de fixer une max de chiffres significatifs, car ici on a des constantes avec 15 chiffres après la virgule.

On peut aussi essayer de contraindre nos constantes en 10^-1 et 10^02.

Sur un terminal (hors notebook), faire q puis entrée permet de terminer la run.

"warmup_maxsize_by" permet de forcer le modèle à se "remettre en question" et ne pas rester bloquer sur une expression complexe qui est en réalité un minimum local.

-----------------------------------------------------------------------------------------------------
Questions pour séance du 05/03 à venir :

- Il faut absolument mettre un poids pour pénaliser (ou plutôt récompenser) les valeurs "extrème" de vents solaires car sinon l'algo va préférer bien prédire 4900 points qui sont proches de la normale (et donc l'algo va ressortir par exemple une réponse constante) et en louper 100 qui sont les plus interessant que de pédire 4000 bons et 1000 loupés mais avec 100% de bonnes prédictions pour les valeurs de vent solaire.
MAIS, comment faire un bon poids ? Somme quadratique des distances à la moyenne de chaque variable ? (peut être normaliser aussi)
idée : poids inversement proportionnels à r0, mais on peut aussi essayer de faire ça et ajouter du poids aux points qui sont dans une zone moins dense, et avec scikitlearn on peut essayer de trouver des estimateurs de densité et utiliser l'inverse de cette valeur pour faire le poids.

- Comment afficher en temps réel le fichier .pkl pour le lire avec un second terminal ?

- Peut être définir la frontière entre point "normal" et point de "tempête solaire". Est-ce une valeur seuil de Bz (surement), de Pd, une combinaison des deux ? ou plutôt un certaine date (exemple octobre/novembre 2003) ?
Tirage qui sur-représente les valeurs faible de r0 (et non réfléchir sur pd et bz).

Param names dans fit : permets de renommer x0 et x1 ou donner un tableau pandas plutôt qu'un array numpy.

Prochaine séance : 11/03 de 16h à 17h.
