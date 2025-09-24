# Le rapport de corrélation ${\eta}^2$

On partage les variables qualitatives en $p$ groupes d'effectif $n_i$. Chaque groupe dispose également d'une moyenne ${\bar{x}}_i$ et d'une variance ${{\sigma}_i}^2$.

La rapport de corrélation nécessite de calculer la variance inter-groupe et la variance totale.

La moyenne générale des groupes vaut :

$\bar{x} = \frac{n_1 {\bar{x}}_1 + n_2 {\bar{x}}_2 + \ldots{} + n_p {\bar{x}}_p}{n}$

La variance intra-groupe vaut :

$\mathbb{V}_{\textrm{intra}} = \frac{n_1 {{\sigma}_1}^2 + n_1 {{\sigma}_1}^2 + \ldots{} + n_p {{\sigma}_p}^2}{n}$

La variance inter-groupe vaut :

$\mathbb{V}_{\textrm{inter}} = \frac{n_1 {{\bar{x}}_1}^2 + n_1 {{\bar{x}}_1}^2 + \ldots{} + n_p {{\bar{x}}_p}^2}{n} - {\bar{x}}^2$

La variance totale vaut :

$\mathbb{V}_{\textrm{totale}} = \mathbb{V}_{\textrm{intra}} + \mathbb{V}_{\textrm{inter}}$

Le rapport de corrélation ${\eta}^2$ vaut :

${\eta}^2 = \frac{\mathbb{V}_{\textrm{inter}}}{\mathbb{V}_{\textrm{totale}}}$

**Exercice pour comprendre (Nathalie Vialaneix).** Comparer les bières françaises et les bières belges. Sur un total de 529 bières, on note les bières sur une échelle allant de 0 à 5. On souhaite étudier le rapport entre la note attribuée et le pays d'origine de la bière.

On constitue deux groupes : celui des bières françaises (groupe 1) et celui des bières belges (groupe 2). Le score obtenue par les 231 bières françaises est 490, tandis que les 298 bières belges ont atteint 846,5. La variance observée pour les bières françaises est 1257,5 et pour les bières belges 2689,75.

1. On calcule les moyennes conditionnelles de chaque groupe.

$x_1 = \frac{490}{231} \approx 2,121$

et

$x_2 = \frac{846,5}{231} \approx 2,841$

2. On peut calculer les variances conditionnelles de chaque groupe avec la formule de König-Huygens.

${{\omega}_1}^2 = \frac{1257,5}{231} - 2,121^2 \approx 0,945$

et

${{\omega}_2}^2 = \frac{2689,75}{298} - 2,841^2 \approx 0,955$

3. On peut calculer la moyenne générale sur le goût.

$\bar{x} = \frac{231 \times 2,121 + 298 \times 2,841}{529} \approx 2,527$

4. On peut calculer la variance inter-groupe.

$\mathbb{V}_{\textrm{inter}} = \frac{231 \times 2,121^2 + 298 \times 2,841^2}{529} - 2,527^2 \approx 0,125$

5. On peut calculer la variance intra-groupe.

$\mathbb{V}_{\textrm{intra}} = \frac{231 \times 0,945 + 298 \times 0,955}{529} \approx 0,951$

6. On peut calculer la variance totale.

$\mathbb{V}_{\textrm{totale}} = \mathbb{V}_{\textrm{intra}} + \mathbb{V}_{\textrm{inter}} \approx 0,951 + 0,125 \approx 1,076$

7. Le rapport de corrélation vaut :

${\eta}^2 = {\mathbb{V}_{\textrm{inter}}}{\mathbb{V}_{\textrm{totale}}} \approx \frac{0,125}{1,076} \approx 0,116$

$\eta \approx \sqrt{0,116} \approx 0,341$

## Liens

- [Topo en format P.D.F.](./PDF/02-Le-rapport-de-correlation-eta-2.pdf)
