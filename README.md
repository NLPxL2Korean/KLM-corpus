# Korean (L2) Learner Morpheme (KLM) corpus 


## Basic information

This repository is for the KLM corpus, a manually annotated dataset consisting of 129,784 morphemes from second language (L2) learners of Korean. This dataset features morpheme tokenization and part-of-speech (POS) tagging, with morpheme tags are based on the Sejong tag set.

- The data includes information on classroom proficiency levels (ranging from 1 to 6 as a proxy for learner proficiency), nationality, gender, and writing topics.

- The dataset was constructed by randomly extracting 600 texts from the original corpus (Park & Lee, 2016). Each proficiency level is represented by 100 texts.

- The corpus was manually annotated by three native Korean speakers, providing detailed descriptions during the annotation process and their subsequent evaluations.

## CoNNL-U Format

The data is organized in the universally accepted [CoNLL-U](https://universaldependencies.org/format.html) format, following the Universal Dependencies (UD) formalism (Nivre et al., 2020). Sentences consist of one or more word lines, and each word line contains the following fields:

1. ID: Word index
2. FORM: *Eojeol* (sequences of Korean characters separated by white-spaces) form or punctuation symbol 
3. LEMMA: Morphemes connected by '+' within an eojeol-unit (**manually annotated**)
4. UPOS: [Universal part-of-speech-tag](https://universaldependencies.org/u/pos/index.html) (automatically annotated by Stanza)
5. XPOS: [Sejong tag set](https://nlpxl2korean.github.io/KLM-corpus/sejong) (language-specific part-of-speech tag) (**manually annotated**)
6. FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available (currently empty)
7. HEAD: Head of the current word, which is either a value of ID or zero (0) (currently empty)
8. DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one (currently empty)
9. DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs (currently empty)
10. MISC: Any other annotation


## Annotation guidelines

Detailed morpheme annotation guidelines for building the KLM corpus are available [here](https://nlpxl2korean.github.io/KLM-corpus/annotations).


## Citation

If you use the KLM corpus in your research, please cite the following:

Sung, H., & Shin, G-H. (2023). Towards L2-friendly pipelines for learner corpora: A case of written production by L2-Korean learners, In *Proceedings the 18th Workshop on Innovative Use of NLP for Building Educational Applications*, Association for Computational Linguistics.

## On-going/Future works

- We are currently re-evaluating the Korean language proficiency of individual learners through a holistic evaluation of their essays by trained human raters.

- Our aim is to extend the scope of our research to include dependency parsing.


## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

