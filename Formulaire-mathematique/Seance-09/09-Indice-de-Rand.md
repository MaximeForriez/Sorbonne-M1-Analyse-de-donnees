# Indice de Rand

L'indice de Rand est une **mesure de similarité** entre deux partitions d'un ensemble[^1]. Son principe est de mesurer la consistance entre deux partitions.

Soit $\pi = {\left\lbrace u_i \right\rbrace}_I$ une partition de l'ensemble $E$, deux éléments $e_1$ et $e_2$ de $E$ sont dits « groupés » dans $\pi$ s'ils appartiennent à un même sous-ensemble de $\pi$, c'est-à-dire $\exists i \in I \ \left( e_1, e_2 \right) \in U_i \times U_i$. On dit que deux éléments $e_1$ et $E_2$ sont séparés dans $\pi$ s'ils appartiennent à deux sous-ensembles distincts de $\pi$.

Soient deux partitions ${\pi}_1$ et ${\pi}_2$ de $E$ et soient les comptages :

- $a$ le nombre de paires éléments de $E$ groupés dans ${\pi}_1$ et dans ${\pi}_2$ ;

- $b$ le nombre de paires éléments de $E$ groupés dans ${\pi}_1$, mais séparés dans ${\pi}_2$ ;

- $c$ le nombre de paires éléments de $E$ groupés dans ${\pi}_2$, mais séparés dans ${\pi}_1$ ;

- $a$ le nombre de paires éléments de $E$ séparés dans ${\pi}_1$ et dans ${\pi}_2$.

La somme $a + d$ représente la **consistance** entre deux partitions.

La somme $b + c$ représente l'**inconsistance** entre deux partitions.

L'indice de Rand vaut :

$RI \left( {\pi}_1, {\pi}_2 \right) = \frac{a + d}{a + b + c + d}$

c'est-à-dire la proportion des paires d'éléments qui sont conjointement groupées ou conjointement séparées.

La distance de Rand vaut :

$d = 1 - RI \left( {\pi}_1, {\pi}_2 \right)$

## Liens

- [Topo en format P.D.F.](./PDF/09-Indice-de-Rand.pdf)

## Notes de bas de page

[^1]: Rand, William M., 1971, "Objective Criteria for the Evaluation of Clustering Methods", *Journal of the American Statistical Association*, vol. 66, n°336, p. 846-850
