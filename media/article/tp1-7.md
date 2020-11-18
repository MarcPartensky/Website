# ARM TP1

## Préparation

### 1. Coder les chiffres suivants de décimal vers hexadécimal:
* 100 => 0x64
* 10000 => 0x2710

### 2. Coder les chiffres suivants de hexadécimal vers décimal
* 0x1234 => 4660
* 0x12345678 => 305419896

### 3. Expliquer le fonctionnement du programme suivant

```asm
        B       main
main    NOP
        B main
```

L'instruction B est une instruction de CPU ARM qui permet de sauter d'une section de code à une autre.
En l'occurence ce programme saute à la section main qui n'exécute rien pour l'instant. Puis il recommence en boucle.

## A) Manipulation partie 1

### 4. Expliquer et corriger l'erreur

Une addition ne peut prendre que 2 opérandes et 3 lui sont fournis.
```asm
ldr     r0,=100
ldr     r1,=10000
Add     r2,r1,r0
```

### 5. Comment les instructions suivantes ont-elles été tranformées?

```asm
ldr     r0,=100
=>
mov     r0,#0x64
```

```asm
ldr     r1,=10000
=>
ldr r1, [PC, #+4]
```

### 6. Rappeler dans quelles conditions on peut utiliser l’instruction MOV pour affecter une valeur à un registre.


MOV permet contrairement à LDR de charger des valeurs à l'étape de compilation.
La valeur d'origine peut:
* provenir d'un autre registe
* d'un registre décalé
* être une constante


### 7. Expliquer le codage du chiffre 0x2774 en mémoire 0x9000

Le programme a additionné les valeurs 0x64 et 0x2710 des registres r0 et r1, il a ensuite stocké le résultat dans le registre r2, enfin il a allouée la case 0x9000 pour y placer la valeur du registre r2 qui vaut alors 0x2774 (=10000+100=10100)


### 8. Proposer 2 valeurs à placer dans r0 et r1 pour que l'addition lève le drapeau Z

```asm
NB1     equ     0x00000000
NB2     equ     0x00000000
```

### 9. Proposer 2 valeurs permettant de lever V.

```asm
NB1     equ     0x0fffffff
NB2     equ     0x0fffffff
```

### 10. Proposer 2 valeurs permettant de lever N.

```asm
NB1     equ     0xf0000000
NB2     equ     0xf0000000
```

# ARM TP2

## A) Manipulation - partie 1 - environnement et représentation

### 1. Quelle est l'adresse de début de votre programme? Combien d'instructions au total comporte ce programe?

L'adresse de deebut de programme est 0x0. Il y'a 7 instructions écrites et 52 exécutions d'instruction étant donné que 5 instructions sont dans une boucle exécutée 10 fois.

### 2. Quelle est le code de l’instruction : MOV R10,0x24

```asm
ldr     r10,=table
```

### 3. Quelle est l'adresse de l'instruction: MOV R2,#0xA

Il s'agit de l'adresse 0x4.

### 4. Combien faut-il d’octets pour coder l’instruction MOV R2,#0A

Il faut 4 octets pour code l'instruction MOV R2,#0A car la valeur de l'adresse 0x4 est E3A0200A hexadécimal ce qui fait 8 chiffres donc 4 chiffres en octal.

### 5. Quel est le registre qui compte (ou décompte) le nombre de boucles exécutées ?

Le registre qui décompte le nombre de boucles exécutées est le registre R2, lorsqu'il atteint la valeur 0, la boucle est terminée.

### 6. Quelle est la signification et le rôle de l’instruction BNE ?

L'instruction BNE signifie Branch if Not Equal. Elle sert de boucle conditionnelle, si le drapeau Z est nulle, la boucle continue sinon on en sort.

### 7. Quelle est la ligne qui spécifie le nombre de boucles ?

Il s'agit de la ligne:
```asm
NB      equ     10
```
Celle-ci place la valeur 10 dans NB qui sera utilisée plus tard pour charger le registre R2.

### 8. A partir de quelle adresse repérés par l’étiquette table les valeurs 0x30,0x31,0x32, etc; sont-elles stockées ?

L'adresse à partir de laquelle sont stockées les valeurs de la table est 0x24.

### 9. Que contient le registre R0 puis R1 lors de chaque boucle et pourquoi ?

* Le registre R0 contient toutes les valeurs de la table successivement lors de l'exécution de la boucle. 

* Le registre R1 contient le double de R0 car on utilise R0 pour calculer R1 en appliquant l'instruction lsl qui décale les chiffres d'un pas vers la gauche ce qui a pour effet de multiplier par 2 en binaire.


### 10. Que contient le registre R10 ?

Le registre R10 contient successivement toutes les valeurs de la table. Il est incrémenté de 1 à chaque tour de boucle.

### 11. A quel endroit doit-on placer cette instruction STRB et quelle est sa syntaxe ? Ecrire et placer l’instruction STRB avec les opérandes adéquats.

On doit placer l'instruction STRB avant d'incrémenter R10 car sa valeur n'est plus nécessaire à cet étape du programme.

```asm
...
ADD     r10, R10, #1
STRB    R1, [R10]
...
```

### 12. Quels registres sont utilisés pour les variables : i, a, b ?

* i est chargé dans le registre R0
* a est chargé dans le registre R1
* puis b est aussi chargé dans le R1 à son tour

### 13. Combien d’instructions en C sont exécutées pour une itération de la bouche for ?

Pour une itération de la boucle for il faut 3 instructions en C.

### 14. Combien d’instructions assembleur après compilation du programme C sont exécutées pour une itération de la bouche for

Après compilation du programme C ce sont 6 instructions qui sont exécutées pour une itération de la boucle for.

### 15. Quel est le nombre total d’instructions assembleur après compilation ? (Etiquette \_main et étiquette \_exit). Quel est le rapport entre ce nombre d’instructions et celui trouvé à la question 1 ? (Nombre d’instructions d’un programme écrit directement en assembleur)

Le nombre total d'instruction exécutée en C correspond à la différence entre \_main et \_exit soit 90.
Il y'a donc 38 instructions exécutées de plus en C qu'en assembleur.
