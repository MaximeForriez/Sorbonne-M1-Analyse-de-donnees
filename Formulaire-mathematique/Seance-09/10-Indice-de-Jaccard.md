# Indice de Jaccard

L'indice[^1] de P. Jaccard[^2] compare la similarité entre des échantillons. Il s'agit du rapport entre le cardinal de l'intersection des ensembles considérés et le cardinal de l'union des ensembles[^3]. Soient $A$ et $B$, l'indice est :

$J \left( A, B \right) = \frac{\mathrm{card } \left( A \cap B \right)}{\mathrm{card } \left( A \cup B \right)}$

L'extension à $n$ ensembles est :

$J \left( S_1, S_2, \ldots{}, S_n \right) = \frac{\mathrm{card } \left( S_1 \cap S_2 \cap \ldots{} \cap S_n \right)}{\mathrm{card } \left( S_1 \cup S_2 \cup \ldots{} \cup S_n \right)}$

La **distance de Jaccard** mesure la dissimilarité entre les ensembles. Elle consiste à soustraire l'indice de Jaccard à 1.

$d = 1 - J \left( A, B \right) = 1 - \frac{\mathrm{card } \left( A \cap B \right)}{\mathrm{card } \left( A \cup B \right)} = \frac{\mathrm{card } \left( A \cup B \right) - \mathrm{card } \left( A \cap B \right)}{\mathrm{card } \left( A \cap B \right)}$

L'extension à $n$ ensembles est :

$d = 1 - J \left( S_1, S_2, \ldots{}, S_n \right) = \frac{\mathrm{card } \left( S_1 \cap S_2 \cap \ldots{} \cap S_n \right) - \mathrm{card } \left( S_1 \cup S_2 \cup \ldots{} \cup S_n \right)}{\mathrm{card } \left( S_1 \cup S_2 \cup \ldots{} \cup S_n \right)}$

## Liens

- [Topo en format P.D.F.](./PDF/10-Indice-de-Jaccard.pdf)

## Notes de bas de page

[^1]: ou le coefficient de Jaccard ou le coefficient de communauté

[^2]: Paul Jaccard (1868-1944)

[^3]: Jaccard, Paul, 1901, « Distribution de la flore alpine dans le bassin des Dranses et dans quelques régions voisines », *Bulletin de la société vaudoise des sciences naturelles*, n°37, p. 241-272
