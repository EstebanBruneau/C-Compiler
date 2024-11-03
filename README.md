Making a compiler for a part of the C language. Handling most of the language to be able to compile c programs.

# Prerequisites

- Operating System: Windows/Linux/MacOS
- Python environment with the following modules:
    - sys (built-in)
    - os (built-in)
    - glob (built-in)
    - colorama (external)

# USAGE

**fr:**

- Ajouter les fichiers C dans le dossier ``./Code``
- Lancer le compliateur.py
- Les fichiers de code machine sont créés dans le dossier ``./Output``

**eng:**
- Put your C source files in the ``./Code`` directory
- Run the Python compiler script
- The compiled assembly files will be generated in the ``./Output`` directory

# Specifications

## Opérateurs unaires

|  | |
| --- | --- |
| + | Fonctionne |
| - | Fonctionne |
| ! | Fonctionne |

## Opérateurs binaires

|  | |
| --- | --- |
| * | Fonctionne |
| / | Fonctionne |
| + | Fonctionne |
| - | Fonctionne |
| == | Fonctionne |
| = | Fonctionne |
| > | Fonctionne |
| < | Fonctionne |
| ! = | Fonctionne |
| && | Fonctionne |
| || | Fonctionne |

## Reste des expressions

|  | |
| --- | --- |
| parenthèses | Fonctionne |
| constantes | Fonctionne |

## Conditionnelles

|  | ||
| --- | --- | --- |
| if | Fonctionne |  |
| else | Fonctionne |  |

## Boucles

|  | |||
| --- | --- | --- | --- |
| for | Fonctionne |  |  |
| while | Fonctionne |  |  |
| do while | Fonctionne pas | Pas implémenté | On a préféré ne pas l’implémenter parce qu’on avait déjà for et while, qui sont les plus importantes et on a préféré se concentrer sur d’autres parties du compilateur |

## Variables

|  | ||
| --- | --- | --- |
| définition | Fonctionne |  |
| scopes | Fonctionne pas | Nous n’avons pas réussi à trouver la raison du bug : les scopes ne sont pas créés aux bons endroits. En tentant d’ajouter les scopes lors de la création d’un bloc, cela empêche l’accessibilité des variables des scopes précédents (plus larges). En revanche, pour les fonctions les scopes sont gérés correctement  |
| affectation | Fonctionne |  |

## Reste des instructions

|  | | ||
| --- | --- | --- | --- |
| break  | Fonctionne pas | Pas implémenté | |
| continue | Fonctionne pas | Pas implémenté |  |
|  |  |  |  |

## Fonctions

|  | |
| --- | --- |
| Définition, appel | Fonctionne |
| Avec arguments | Fonctionne |

## Pointeurs

||||
| --- | --- | --- |
| * | Fonctionne |  |
| & | Fonctionne |  |


## Bibliothèque

|  | ||
| --- | --- | --- |
| malloc | Fonctionne |  |
| free | Fonctionne pas | Pas implémenté |
| read | Fonctionne pas | Pas implémenté |
| print | Fonctionne pas | Pas implémenté |

## Bonus

||||
| --- | --- | --- |
| commentaires | Fonctionne | Possibilité d'écrire des commentaire commençant par // |


## Personal thoughts

I genuinely loved working on this project. Understanding the process of translating a code into tokens, then making an AST. I have learned a lot throughout this project. It's a shame I could not finish everything in time, but I am still happy to have a working compiler. I might come back to update it in the future.