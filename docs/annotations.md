## Annotation guidelines
This page includes the major cases that annotators discussed while building the KLM corpus, with the purpose of consistent annotations and better evaluation of morpheme tokenizers/taggers of interest.


### Causative and passive markers

Voice markers such as *-i/hi/li/ki/wu/kwu/chwu-* (morphological causative) and *-i/hi/li/ki-* (suffixal passive) indicate causative and passive voices. They attach to a root to form causative or passive verbs, altering the number of arguments a predicate controls in a clausal construction. We parsed these morphemes and assigned a XSV tag.

- Example: `mek+ta "to eat" (VV+ EF); mek+hi+ta "to be eaten" (VV+XSV+EF)`

### Auxiliary verbs

Verbs like *iss-* "to be/exist/have", *ha-* "to do", and *toy-* "to become" can act as both main and auxiliary verbs. As main verbs, they represent concepts of existence, activity, or possession. In these cases, we assigned a VV tag.

- Example: `ku+nun cha+ka iss+ta (VV+EF) "He has a car"`

As auxiliary verbs, they work with a main verb to convey grammatical meanings, such as continuous or progressive actions. In these instances, we assigned a VX tag.

- Example: `ku+nye+nun chayk+ul ilk+ko iss+ta (VX+EF) "She is reading a book"`

### Copula (Positive)

The copula (*-i*) links the subject of a sentence with a predicate, often conveying a positive meaning (VCP). Parsing complexities arise when the copula combines with the ending *-lanun*. This combination links the subject of a sentence to a noun or descriptive phrase, adding a specification, identification, or definition nuance.

- Example: `swukcey+lanun "(the thing) called homework" → swukcey+i+lanun (NNG+VCP+ETM).`

### `advmod` vs. `obl`

- noun+보조사(`advmod`): -까지, -뿐만, -도, -만
- noun+격조사(`obl`): -에, -에게, -보다, -한테, -처럼, -(으)로, -와/과, -에서, -보고

### Spelling errors

Instead of subjectively interpreting misspelled words, we assigned three tags from the Sejong tag set: NA (Undefined), NF (Undefined, but considered a noun), and NV (Undefined, but considered a verb).

##### * We will update more detailed guidelines/examples for other morpheme categories shortly!
