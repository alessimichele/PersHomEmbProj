# PersHomEmbProj
Persistent Homology invariance under embedding and projection

I try to ask the following.
Given a dataset $M$, it is well known that it is possible to associate its persistent homology diagrams, say for $H_0$, $H_1$ and $H_2$.

Suppose we want to embed our dataset in a higher dimensional space. A trivial way to do it to simply add $0$ coordinates to each points of $M$; another option is to randomly choose number within, for example, minimum and maximum values in $M$.

Once we have this embedding, we also have a new dataset, say $M'$. The question is: if we 'come back' to the initial dimension (kernelPCA), can we retrieve the persistent diagrams we had for $M$?

Formally:
let $M \subset \mathbb{R}^{N \times d}$,  $M' \subset \mathbb{R}^{N \times D}$,  $M'' \subset \mathbb{R}^{N \times d}$ wehere $N=$ number of points, $d=$ original dimension of the dataset, $D=$ dimension of the embedding space.

After the following maps

$$ M \xrightarrow{\text{embedding}} M' \xrightarrow{\text{kernelPCA}} M'' $$

is it tru that PersistenDiagrams($M$) ~ PersistenDiagrams($M''$)?

**Why do we care about this?**

Note, if the above mentioned is true, this means that persistent diagrams are insensible to higher dimenisonal embedding. In particular,suppose we have a high dimensional dataset: using its intrinsic dimension, we obtain somehow a new dataset with same "geometrical properties" of the initial one, meaning that the other dimensions where "noise".

Now, we can perform kernelPCA on the initial dataset, projecting onto "principal components"="intrinsic dimension", and study the persistent diagrams of this new "smaller" space.

Scheme:

![](schema.jpeg)
