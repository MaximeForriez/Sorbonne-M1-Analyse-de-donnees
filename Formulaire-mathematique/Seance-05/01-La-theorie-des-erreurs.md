# La théorie des erreurs

## L'erreur absolue et l'erreur relative

### L'erreur absolue

**Définition.** L'**erreur absolue** commise sur le nombre $x$ lorsqu'on lui substitue une valeur approchée $\bar{x}$ est la différence $\Delta x$ :

$\Delta x = x - \bar{x}$

ou

$\bar{x} = x - \Delta x$

Dans la pratique, on connaît la valeur approchée $\bar{x}$, et non pas l'erreur, mais seulement un majorant $\varepsilon$ de cette erreur. Dit autrement, on est en mesure d'affirmer que $x$ satisfasse à la double inégalité :

$\bar{x} - \varepsilon < x < \bar{x} + \varepsilon$

ce qui se lit : « $\bar{x}$ est une valeur approchée de $x$ avec une erreur inférieure à $\varepsilon$, ou avec une incertitude égale à $\varepsilon$ ».

Dire que $\bar{x}$  est une **valeur approchée par défaut** de $x$, l'erreur étant inférieure à $\varepsilon$, c'est dire que $x$ satisfasse la double inégalité :

$\bar{x} < x < \bar{x} + \varepsilon$

Dire que $\bar{x}$ est une **valeur approchée par excès** de $x$, l'erreur étant inférieure à $\varepsilon$, c'est dire que $x$ satisfasse la double inégalité :

$\bar{x} - \varepsilon < x < \bar{x}$

### L'erreur relative

**Définition.** L'**erreur relative** commise sur le nombre $x$ lorsqu'on lui substitue une valeur approchée $\bar{x}$ est le quotient :

$\frac{\Delta x}{x} = \frac{x - \bar{x}}{x} = 1 - \frac{\bar{x}}{x}$

de l'erreur absolue $\Delta x$ par la valeur exacte $x$.

De l’encadrement

$0 < \left| \bar{x} \right| - \varepsilon < \left| x \right| < \left| \bar{x} \right| + \varepsilon$

on en déduit $\frac{\left| \Delta x \right|}{x} < \frac{\varepsilon}{\left| \bar{x} \right| - \varepsilon}$ ; il en résulte que $\frac{\varepsilon}{\left| \bar{x} \right| - \varepsilon}$ est un majorant de l'erreur relative.

## Premier problème de la théorie des erreurs

### Erreur systématique et erreur due au calcul

$f$ étant une fonction donnée, par exemple de trois variables, et $\bar{x}$, $\bar{y}$ et $\bar{z}$ des valeurs approchées des nombres $x$, $y$ et $z$, lorsqu'on prend $\bar{\omega} = f \left( \bar{x}, \bar{y}, \bar{z} \right)$ pour valeur approchée du nombre $\omega = f \left( x, y, z \right)$, on commet une erreur dit **erreur systématique**, $e_1 = \omega - \bar{\omega}$.

Pour diverses raisons, il arrive souvent que l'on ne sache pas calculer exactement $\bar{\omega}$ et que l'on doive se contenter d'une valeur approchée ${\omega}^{*}$ de ce nombre. La différence $e_2 = \bar{\omega} - {\omega}^{*}$ est dite **erreur due au calcul**.

L'**erreur totale** commise s'écrit :

$\begin{array}{c} e = \left( \omega - \bar{\omega} \right) + \left( \bar{\omega} - {\omega}^{*} \right) = e_1 + e_2 \\ e = \omega - {\omega}^{*} \end{array}$

On en déduit :

$\left| e \right| \leq \left| e_1 \right| + \left| e_2 \right|$

Si on sait calculer un majorant ${\alpha}_1$ de $\left| e_ 1 \right|$ et un majorant ${\alpha}_2$ de $\left| e_ 2 \right|$, on peut affirmer que ${\alpha}_1 + {\alpha}_2$ est un majorant de $\left| e \right|$.

> [!WARNING]
> Il n'existe pas de méthode générale pour majorer l'erreur due au calcul.

> [!NOTE]
> La formule des accroissements finis permet de majorer l'erreur systématique.

### Erreur systématique sur le calcul du nombre $\omega = f \left( x \right)$

1. La formule des accroissements finis, appliquée à la fonction $f$ sur $\left[ x, \bar{x} \right]$, donne

$f \left( x \right) - f \left( \bar{x} \right) = \left( x - \bar{x} \right) f' \left( \xi \right) \textrm{ avec } \xi \in \left] x, \bar{x} \right[$

et

$\left| \omega - \bar{\omega} \right| = \left| x - \bar{x} \right| \left| f' \left( \xi \right) \right|$

On obtient ainsi un majorant ${\varepsilon}_{\omega}$ de $\omega - \bar{\omega}$ en multipliant un majorant ${\varepsilon}_{\alpha}$ de $x - \bar{x}$ par un majorant de $\left| f' \left( \xi \right) \right|$ ; d'où la formule

${\varepsilon}_{\omega} = A {\varepsilon}_{\alpha}$

dans laquelle $A$ désigne un majorant de $\left| f' \left( x \right) \right|$ sur un champ qui contient $\left] x, \bar{x} \right[$.

2. Plus généralement, la formule de Taylor montre que, si l'on prend pour valeur approchée du nombre $f \left( x \right) = f \left( \bar{x} + \Delta x \right)$ la somme suivante :

$\bar{f \left( x \right)} = f \left( \bar{x} \right) + \frac{\Delta x}{1!} f' \left( \bar{x} \right) + \ldots{} + \frac{\Delta x}{n!} f^{\left( n \right)} \left( \bar{x} \right)$

on commet une erreur qui a pour expression

$\frac{\Delta x^{n + 1}}{\left( n + 1 \right)!} f^{\left( n + 1 \right)} \left( \xi \right) \textrm{ avec } \xi \in \left] x, \bar{x} \right[$

Si l'on connaît un majorant $A$ de $\left| f^{\left( n + 1 \right)} \left( \xi \right) \right|$ sur un champ qui contient $\left] x, \bar{x} \right[$, on peut affirmer que la valeur absolue de l'erreur est inférieure à :

$A \frac{\left| \Delta x \right|^{n + 1}}{\left( n + 1 \right)!}$

### Erreur systématique sur le calcul du nombre $\omega = f \left( x, y, z \right)$

La formule des accroissements finis s'écrit, en désignant par $M$ et $\bar{M}$ les points $\left( x, y, z \right)$ et $\left( \bar{x}, \bar{y}, \bar{z} \right)$

$f \left( M \right) - f \left( \bar{M} \right) = \left( x - \bar{x} \right) f'_{x} \left( P \right) + \left( y - \bar{y} \right) f'_{y} \left( P \right) + \left( z - \bar{z} \right) f'_{z} \left( P \right)$

$P$ désignant le segment de droite $M\bar{M}$.

On en déduit que

$\left| \omega - \bar{\omega} \right| = \left| x - \bar{x} \right| \left| f'_x \left( P \right) \right| + \left| y - \bar{y} \right| \left| f'_y \left( P \right) \right| + \left| z - \bar{z} \right| \left| f'_z \left( P \right) \right|$

ce qui montre que si ${\varepsilon}_x, {\varepsilon}_y, {\varepsilon}_z$  désignent respectivement des majorants de $\left| x - \bar{x} \right|$, $\left| y - \bar{y} \right|$, $\left| z - \bar{z} \right|$ un majorant ${\varepsilon}_{\omega}$ de $\left| \omega - \bar{\omega} \right|$ est fourni par la formule :

${\varepsilon}_{\omega} = A {\varepsilon}_x + B {\varepsilon}_y + C {\varepsilon}_z$

dans laquelle $A$, $B$, $C$ désignent respectivement des majorants de $\left| f'_{x} \left( x, y, z \right) \right|$, $\left| f'_{y} \left( x, y, z \right) \right|$, $\left| f'_{z} \left( x, y, z \right) \right|$ sur un champ qui contient le segment de droite défini par les points $M \left( x, y, z \right)$ et $\bar{M} \left( x, y, z \right)$.

> [!WARNING]
> Cette formule fournit une majoration de l’erreur commise sur $\omega = f \left( x, y, z \right)$ aussi bien sur $x, y, z$ sont des variable indépendantes qui si ce sont des fonctions d'une même variable $t$. Dit autrement, $\omega = f \left( x \left( t \right), y \left( t \right), z \left( t \right) \right) = g \left( t \right)$.

### Formulaire des erreurs

À partir des fonctions $f \left( x, y, z \right)$ convenablement choisies, la formule ${\varepsilon}_{\omega} = A {\varepsilon}_x + B {\varepsilon}_y + C {\varepsilon}_z$ va permettre de majorer les erreurs systématiques commises dans les opérations les plus souvent utilisées.

#### La somme

$\begin{array}{l} \omega = x + y \\ \Rightarrow A = B = 1 \\ \Rightarrow {\varepsilon}_{\omega} = {\varepsilon}_x + {\varepsilon}_y \end{array}$

Cette relation est valable quelle que soit la somme.

#### La différence

$\begin{array}{l} \omega = x - y \\ \Rightarrow A = B = 1 \\ \Rightarrow {\varepsilon}_{\omega} = {\varepsilon}_x - {\varepsilon}_y \end{array}$

Cette relation est valable quelle que soit la différence.

#### Règle

**On obtient un majorant de l'erreur absolue commise sur une somme ou sur une différence en additionnant des majorants des erreurs absolues commises sur les termes**.

#### Produit

$\begin{array}{l} \omega = xy \\ \Rightarrow \left\lbrace  \begin{array}{c} A = \sup \left| y \right| \\ B = \sup \left| x \right| \end{array} \right. \\ \Rightarrow {\varepsilon}_{\omega} = \sup \left| y \right| {\varepsilon}_x + \sup \left| x \right| {\varepsilon}_y \end{array}$

Comme $\sup \left| y \right| \leq y + {\varepsilon}_y$ et $\sup \left| x \right| \leq x + {\varepsilon}_x$, on commet une erreur au plus égale à $2 {\varepsilon}_x {\varepsilon}_y$, donc négligeable dans la pratique, en écrivant

${\varepsilon}_{\omega} = \left| y \right| {\varepsilon}_x + \left| x \right| {\varepsilon}_y$

On en déduit, en divisant les deux membres par $\left| \omega \right| = \left| x \right| \left| y \right|$, la formule pratique :

$\frac{{\varepsilon}_{\omega}}{\left| \omega \right|} = \frac{{\varepsilon}_{x}}{\left| x \right|} + \frac{{\varepsilon}_{y}}{\left| y \right|}$

relation qui s'étend de proche en proche au cas du produit d'un nombre quelconque de facteurs.

#### Quotient

$\begin{array}{l} \omega = \frac{x}{y} \\ \Rightarrow \left\lbrace  \begin{array}{c} A = \sup \left| \frac{1}{y} \right| = \frac{1}{\inf \left| y \right|} \\ B = \sup \left| \frac{x}{y^2} \right| = \frac{\sup \left| x \right|}{\inf y^2} \end{array} \right. \\ \Rightarrow {\varepsilon}_{\omega} = \frac{1}{\inf \left| y \right|} {\varepsilon}_x + \frac{\sup \left| x \right|}{\inf y^2} {\varepsilon}_y \end{array}$ 

Dans la pratique, on commet une erreur négligeable en écrivant

${\varepsilon}_{\omega} = \frac{1}{\left| y \right|} {\varepsilon}_x + \frac{\left| x \right|}{y^2} {\varepsilon}_y$

On en déduit, en divisant les deux membres par $\left| \omega \right| = \frac{\left| x \right|}{\left| y \right|}$, la formule pratique

$\frac{{\varepsilon}_{\omega}}{\left| \omega \right|} = \frac{{\varepsilon}_{x}}{\left| x \right|} + \frac{{\varepsilon}_{\omega}}{\left| y \right|}$

#### Règle

**Dans la pratique, on obtient un majorant de l'erreur relative commise sur un produit ou un quotient en additionnant des majorants des erreurs relatives commises sur les termes**.

#### Logarithme

$\Omega = \ln X \Rightarrow \left\lbrace  \begin{array}{l} A = \frac{1}{\inf \left| X \right|} \\ {\varepsilon}_{\Omega} = \frac{1}{\inf \left| X \right|} {\varepsilon}_X \end{array} \right.$

Dans la pratique, on écrit

${\varepsilon}_{\Omega} = \frac{{\varepsilon}_X}{\left| X \right|}$

Soit une expression de la forme $\omega = x^{\alpha} y^{\beta} z^{\gamma}$ dans laquelle $\alpha, \beta, \gamma \in \mathbb{R}$. On obtient alors :

$\ln \omega = \alpha \ln x + \beta \ln y + \gamma \ln z$

d'où

${\varepsilon}_{\omega} = \left| \alpha \right| \frac{{\varepsilon}_x}{\left| x \right|} + \left| \beta \right| \frac{{\varepsilon}_y}{\left| y \right|} + \left| \gamma \right| \frac{{\varepsilon}_z}{\left| z \right|}$

## Deuxième problème de la théorie des erreurs

**Avec quelle approximation suffit-il de connaître les données d'un calcul pour en déduire le résultat de ce calcul avec une erreur inférieure à un nombre donné $\alpha$ ?**

On cherche des majorants ${\varepsilon}_x$, ${\varepsilon}_y$, ${\varepsilon}_z$ de $\left| x - \bar{x} \right|$, $\left| y - \bar{y} \right|$, $\left| z - \bar{z} \right|$ tels que, en calculant une valeur approchée ${\omega}^{*}$ de $\bar{'\omega} = f \left( \bar{x}, \bar{y}, \bar{z} \right)$, on obtient une valeur approchée de $\omega = f \left( x, y, z \right)$ avec une erreur inférieure à $\alpha$.

1. De l'erreur tolérée $\alpha$, on fait deux parts :

    - ${\alpha}_2$ est consacrée à l'erreur due au calcul $\left| \bar{\omega} - {\omega}^{*} \right|$ ;

    - ${\alpha}_1$ est consacrée à l'erreur systématique $\left| \omega - \bar{\omega} \right|$ qui vérifie $\left| \omega - \bar{\omega} \right| \leq A {\varepsilon}_x + B {\varepsilon}_y + C{\varepsilon}_z$.

2. On calcule un majorant $A$ de $\left| f'_x \left( x, y, z \right) \right|$ assez largement pour qu'il convienne sur le segment de droite défini par les deux points $\left( x, y, z \right)$ et $\left( \bar{x}, \bar{y}, \bar{z} \right)$, bien que ce segment ne soit connu que d'une manière approximative. On calcule de même le majorant $B$ et $C$ de $\left| f'_y \left( x, y, z \right) \right|$ et $\left| f'_z \left( x, y, z \right) \right|$.

3. $A$, $B$, $C$ et ${\alpha}_1$ étant connus, il reste à choisir trois nombres positifs ${\varepsilon}_x$, ${\varepsilon}_y$,${\varepsilon}_z$ vérifiant la condition $A {\varepsilon}_x + B {\varepsilon}_y + C {\varepsilon}_z \leq {\alpha}_1$.

> [!WARNING]
> Il n'est pas nécessaire que ${\alpha}_1 = {\alpha}_2$.

**Exemple.** On pose $x = \sqrt{2}$, $y = \sqrt{3}$ et $z = \pi$. Quelle approximation est suffisante pour calculer le nombre $\omega = \frac{\sqrt{3} - \sqrt{2}}{\pi}$ avec une erreur inférieure à $10^{-4}$ ?

$\omega = f \left( x, y, z \right) = \frac{x - y}{z} \Rightarrow \left\lbrace \begin{array}{l} f'_x = \frac{1}{z} = A \\ f'_y = \frac{1}{-z} = B \\ f'_x = -\frac{x - y}{-z^2} = C \end{array} \right.$

${\varepsilon}_{\omega} = A {\varepsilon}_x + B {\varepsilon}_y + C {\varepsilon}_z$

$\begin{array}{l}  A = B = \frac{1}{\inf \left| z \right|} \\ C = \frac{\sup \left| x - y \right|}{\inf z^2} \end{array}$

or $\pi > 3$ c'est-à-dire $z \Rightarrow A = B = \frac{1}{3}$.  De plus, $\sqrt{3} - \sqrt{2} < 0,4$ (avec $\sqrt{3} < 1,8$ et $\sqrt{2} > 1,4$).

$\Rightarrow C = \frac{0,4}{3^2} = \frac{0,4}{9}$

L'erreur systématique est inférieure à $\frac{1}{3} {\varepsilon}_x + \frac{1}{3} {\varepsilon}_y + \frac{0,4}{9} {\varepsilon}_z$, donc *a fortiori* de $0,4 {\varepsilon}_x + 0,4 {\varepsilon}_y + 0,05 {\varepsilon}_z < \frac{4}{3} \omega$.

L'erreur tolérée $\alpha$ est $10^{-4}$. On fait deux parts égales. Dit autrement, on choisit ${\varepsilon}_x$, ${\varepsilon}_y$, ${\varepsilon}_z$ telles que :

$0,4 \left( {\varepsilon}_x + {\varepsilon}_y \right) + 0,05 {\varepsilon}_z < 5 \times 10^{-5}$

et on fera la division avec une erreur inférieure à $5 \times 10^{-5}$.

${\varepsilon}_x = {\varepsilon}_y = {\varepsilon}_z = 5 \times 10^{-5}$ conviennent visiblement. On peut ainsi utiliser les valeurs approchées $\bar{x}, \bar{y}, \bar{z}$ de $\sqrt{3}, \sqrt{2}, \pi$ données par une table à quatre décimales.

$\left.  \begin{array}{l} \bar{x} = 1,7321 \\ \bar{y} = 1,4142 \\ \bar{z} = 3,1416 \end{array} \right\rbrace \Rightarrow \frac{\bar{x} - \bar{y}}{\bar{z}} = \frac{0,3179}{3,1416} \approx 0,10119\ldots{}$

En conclusion, le nombre ${\omega}^{*} = 0,1012$ est une valeur approchée du nombre $\frac{\sqrt{3} - \sqrt{2}}{\pi}$ avec une erreur systématique à $10^{-4}$.

## Les erreurs statistiques

L'**erreur** est la différence entre la valeur mesurée et la valeur exacte, mais, en statistique, on ignore la valeur exacte. On a deux types d'incertitudes possibles : \begin{inparaenum} \item les erreurs systématiques \item les erreurs \end{inparaenum}.

### Incertitudes absolues et relatives

L'incertitude absolue (due aux appareils de mesure) permet de connaître l'approximation du dernier chiffre significatif de celle-ci :

$\begin{array}{c} x - \Delta x \leq x \leq x + \Delta x \\ \Rightarrow x = x \pm \Delta x \end{array}$

L'incertitude relative vaut alors :

$\frac{\Delta x}{x}$

### Erreurs statistiques

Dans la plupart des mesures, on peut estimer l'erreur due à des phénomènes aléatoires par une série de $n$ mesures $x_1, x_2, \ldots{}, x_i, \ldots{}, x_n$.

La valeur de la moyenne arithmétique sera alors :

$\mu = \frac{1}{n} \sum_{i = 1}^{n} x_i$

et l'écart type (qui est un estimateur biaisé) vaut :

${\sigma}^2 = \bar{\Delta x} = \frac{1}{n} \sum_{i = 1}^{n} \left( x_i - \mu \right)^2$

et l'écart type (estimateur sans biais) vaut :

${{\sigma}^{*}}^2 = \frac{1}{n - 1} \sum_{i = 1}^{n} \left( x_i - \mu \right)^2$

et de l'écart quadratique moyen c'est-à-dire l'écart type de la moyenne, vaut :

$\mathrm{SE} = \frac{\sigma}{\sqrt{n}} = \frac{1}{\sqrt{n}} \sqrt{\frac{1}{n - 1} \sum_{i = 1}^{n} \left( x_i - \mu \right)^2}$

Après un grand nombre de mesures indépendantes, la distribution des erreurs sur une mesure suit une loi normale telle que l'on puisse écrire :

\begin{enumerate}
	\item $\hat{x_i} - \sigma < x_i < \hat{x_i} + \sigma$ (68 % des valeurs) ;
	\item $\hat{x_i} - 2\sigma < x_i < \hat{x_i} + 2\sigma$ (95 % des valeurs) ; 
	\item $\hat{x_i} - 3\sigma < x_i < \hat{x_i} + 3\sigma$  (99 % des valeurs).
\end{enumerate}

### Propagation des erreurs statistiques

Soit une mesure $x \pm \Delta x$ et $y = f \left( x \right)$ une fonction de $x$. Quelle est l'incertitude sur $y$ ?

Lorsque $\Delta x$ est petit, $f \left( x \right)$ est remplacé au voisinage de $x$ par sa tangente :

$\Delta y = \left| \frac{\mathrm{d} f}{\mathrm{d} x} \right| \Delta x$

mais si $y$ dépend de plusieurs grandeurs $x$, $z$, $t$ mesurées avec les incertitudes $\Delta x$, $\Delta z$, $\Delta t$ :

$y = f \left( x, z, t \right)$

alors l'erreur minimale possible est alors la différentielle totale exacte :

$\Delta y = \left| \frac{\partial f}{\partial x} \right| \Delta x + \left| \frac{\partial f}{\partial z} \right| \Delta z + \left| \frac{\partial f}{\partial t} \right| \Delta t$

ce qui conduit à :

$\left.  \begin{array}{c} y = x + z \\ y = x - z \end{array} \right\rbrace \Rightarrow \Delta y = \Delta x + \Delta z$

$\left.  \begin{array}{c} y = xz \Rightarrow \Delta y = z \Delta x + x \Delta z \\ y = \frac{x}{z} \Rightarrow \Delta y = \frac{z \Delta x - x \Delta z}{z^2} \end{array} \right\rbrace \Rightarrow \frac{\Delta y}{y} = \frac{\Delta x}{x} + \frac{\Delta z}{z}$

## Liens

- [Topo en format P.D.F.](./PDF/01-La-theorie-des-erreurs.pdf)
