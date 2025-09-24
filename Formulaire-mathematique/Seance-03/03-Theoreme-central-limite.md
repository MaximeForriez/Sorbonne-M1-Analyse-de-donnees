# Théorème central limite

Le théorème central limite (ou théorème de la limite centrale) établit la convergence en loi de la somme de variables aléatoires indépendantes vers la loi normale sous des hypothèses faibles.

## Théorème central limite (première forme)

Soit $\left( X_n \right)$ une suite de variables aléatoires, indépendantes, de même loi, d'espérance mathématique $\mu$ et d'écart type $\sigma$.

Lorsque $n$ tend vers l'infini, la loi de la variable aléatoire :

$\frac{1}{\sqrt{n}} \frac{\left( x_1 + \ldots{} + X_n \right) - n\mu}{\sigma} = \sum_{i = 1}^{n} \frac{X_i - \mu}{\sigma \sqrt{n}} = \frac{\bar{X} - \mu}{\sigma \sqrt{n}}$

tend vers la loi normale, centrée, réduite $N \left( 0, 1 \right)$.

## Théorème central limite ou théorème de J. W. Lindeberg[^1] (forme générale)

$\left( X_i \right)$ est une suite de variables aléatoires indépendantes, non nécessairement de même loi, d'espérance mathématique ${\mu}_i$ et d'écart type ${\sigma}_i$. Soit $F_i \left( x \right)$ la fonction de répartition de $X_i - {}\mu_i$.

On pose :

${S_n}^2 = \sum_{i = 1}^{n} {{\sigma}_i}^n$

Si la limite de $\frac{1}{S_n} \sum_{i = 1}^{n} \int_{\left| x \right| > S_n} x^2 \mathrm{d} F_i \left( n \right)$ est égale à zéro, lorsque $n$ tend vers l'infini, alors la variable aléatoireé: $\frac{1}{S_n} \sum_{i = 1}^{n} \left( X_i - {\mu}_i \right)$ converge en loi vers une variable aléatoire $U$ suivant la loi normale $N \left( 0, 1 \right)$. Les variables aléatoires qui figurent dans la somme sont uniformément petites.

Le théorème central limite possède de nombreuses applications en théorie de l'estimation.

## Liens

- [Topo en format P.D.F.](./PDF/03-Theoreme-central-limite.pdf)

## Note de bas de page

[^1]: Jarl Waldemar Lindeberg (1876-1932)
