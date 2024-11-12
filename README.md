# L2 Korean Learner Morpheme (KLM) corpus 
- Please see the most updated version of the corpus [here](https://github.com/UniversalDependencies/UD_Korean-KSL/tree/dev)!
  
## CoNLL-U Format
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
This corpus was built from the following project: 
- Sung, H., & Shin, G-H. (2023). Towards L2-friendly pipelines for learner corpora: A case of written production by L2-Korean learners, In *Proceedings the 18th Workshop on Innovative Use of NLP for Building Educational Applications*, 72-82, Association for Computational Linguistics.

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

