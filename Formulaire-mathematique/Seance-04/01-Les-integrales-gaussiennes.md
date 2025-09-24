# Les intégrales gaussiennes

## Formule n°1

Soit une variable centrée réduite $Z = \frac{X - \mu}{\sigma}$ avec $\mu$ la moyenne et $\sigma$ l'écart type.

$\int_{+\infty}^{-\infty} e^{-Z^2} \mathrm{d} Z = \sqrt{\pi}$

d'où

$\int_{+\infty}^{-\infty} e^{- \frac{1}{2} Z^2} \mathrm{d} Z = \sqrt{2 \pi}$

###### Démonstration

Soit $I = \int_{-\infty}^{+\infty} e^{-x^2} \mathrm{d} x = 2 \int_{-\infty}^{+\infty} e^{-x^2} \mathrm{d} x$ puisque $e^{-x^2}$ est une fonction paire.

On écrit le carr'{e} de cette intégrale :

$I^2 = 4 \lim_{\gamma \rightarrow +\infty} \left[ \left( \int_{0}^{R} e^{-x^2} \mathrm{d} x \right) \left( \int_{0}^{R} e^{-y^2} \mathrm{d} y \right) \right] = 4 \lim_{\gamma \rightarrow +\infty} \left[ \int_{0}^{R} \int_{0}^{R} e^{- \left( x^2 + y^2 \right)} \mathrm{d} x \mathrm{d} y \right]$

On procède à un changement de variable en passant en coordonnées polaires. Dès lors, on écrira le Jacobien également dans ces mêmes coordonnées :

$\begin{array}{l} I^2 = 4 \lim_{\gamma \rightarrow +\infty} \left[ \int_{0}^{\frac{\pi}{2}} \int_{0}^{R} e^{-{\gamma}^2} r \mathrm{d} r \mathrm{d} \phi \right] \\ I^2 = 4 \frac{\pi}{2} \lim_{\gamma \rightarrow +\infty} \left[ \int_{0}^{R} e^{-{\gamma}^2} r \mathrm{d} r \mathrm{d} \phi \right] \\ I^2 = 2\pi \lim_{\gamma \rightarrow +\infty} \left[ - \frac{1}{2} e^{-{\gamma}^2} \right]_0^{+\infty} \\ I^2 = 2\pi \lim_{\gamma \rightarrow +\infty} \left( 1 - \frac{1}{2} \right) = \pi \end{array}$

donc :

$I = \sqrt{\pi}$

Par extension pour $e^{-\frac{1}{2} x^2}$, on a $I = \sqrt{2\pi}$.

## Formule n°2

Soit un polynôme $Q \left( x \right) = A x^2 + B x + C$ avec $A, B, C \in \mathbb{C}$. Pour assurer une convergence, il faut nécessaire que $\Re (A) > 0$.

$\int_{+\infty}^{-\infty} e^{- Q \left( x \right)} \mathrm{d} x = \sqrt{\frac{\pi}{A}} e^{- C + \frac{B^2}{4 A}}$

> [!WARNING]
> Si $A, B, C \in \mathbb{R}$, alors on obtient la formule de R. Gibrat[^1].

Cette formule polynomiale se généralise de la manière suivante :

$\int_{+\infty}^{-\infty} X^n e^{- Z^2} \mathrm{d} Z = \int_{+\infty}^{-\infty} \left( \sum_{k = 0}^{n}  \frac{n!}{k! \left( n - k \right)!} {\sigma}^n \left( \frac{\mu}{\sigma} \right)^k Z^{n - k} \right) e^{- Z^2} \mathrm{d} Z$

avec $Z$, une variable centrée réduite, $\mu$ la moyenne et $\sigma$ l'écart type.

## Liens

- [Topo en format P.D.F.](./PDF/01-Les-integrales-gaussiennes.pdf)

## Notes de bas de page

[^1]: Robert Gibrat (1904-1980)