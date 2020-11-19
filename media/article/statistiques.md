#!/usr/local/marc/markdown.py

# Chapitre 1: La statistique descriptive


## Caractérisation des séries statistiques
Médiane: valeur qui partage en 2 effectifs égaux les individus rangés par ordre croissant des valeurs prises par la variable statistique
* autant au dessus qu'au dessous
* Fx(xm)


## Mode


## La Moyenne
La différence des différence à la moyenne est nulle.

## Étendu
Différence valeur max et valeur min.

## Caractéristiques de dispersion
Référence à la médiane
* Ecart probable: médiane de la série des écarts à la médiane |xi-xm|
* Écart moyen à la médiane: moyenne de la série des écarts à la médiane

> $$ e(\bar{x})

$$ \sigma^2 = \frac{1}{n}\sum_{j=1}^N(x_j-\bar{x})^2 $$

### Quantiles:
Quantile d'ordre alpha la valeur xa telle que:
$$ F(x_\alpha) = \alpha \space  pour 0 \leq \alpha \leq 1 $$

### Quartile


### Coefficient de Pearson


### Coefficient de Fisher
distribution symétrique:
$$ \gamma_1 = 0 $$

### Coefficient de forme
Coefficient d'aplatissemeent

## En R
La fonction skewness permet de calculer le coefficient d'asymétrie
La fonction kurtosis() per met de calculer 
