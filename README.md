# Electronic Text Corpus of Syntactically Annotated Neo-Sumerian (ETCSANS)

Sumerian is a language of utmost importance to the cultural heritage of all humankind. As the very first written language, it has a vast literature spanning thousands of years (4th to 1st millenium BC) and ranges from genres as diverse as poems and songs over mythological and historical treatises, laws and letters to contracts and administrative records.
At the same time, however, much of this data remained underexplored and only accessible to experts, so far. Although portals such as the Cuneiform Digital Library Initiative (CDLI) and the Open Richly Annotated Cuneiform corpus (ORACC) provided much of the textual data in digital form, very little of it had been translated and/or annotated, and if so, only at the level of morphological glosses (Cunningham et al., 2006; Zólyomi et al., 2008). In order to improve access to these texts for both a larger audience and machines, we developed an innovative annotation workflow (Chiarcos et al. 2018) and now provide the first syntactically annotated corpus of Sumerian, ETCSANS: The Electronic Text Corpus of Syntactically Annotated Neo-Sumerian. Our talk describes its creation, access strategies and usage scenario.

The ETCSANS corpus is the result of the trilateral project Machine Translation and Automated Annotation of Cuneiform Languages (MTAAC, 2017-2020) conducted in the context of CDLI and in collaboration between the University of Toronto, Goethe University Frankfurt and University of California, Los Angeles, and the annotations it aims to provide are primarily meant as a tool for the study of economy and society of the Neo-Sumerian period (2100-2000 BCE). ETCSANS complements two other corpus projects for Sumerian, the Electronic Text Corpus of Sumerian Literature (ETCSL, primarily focusing on the post-Sumerian period),  and the Electronic Text Corpus of Sumerian Royal Inscriptions (ETCSRI, covering all periods, for a limited domain). However, they provide parts-of-speech (ETCSL) and morphological (ETCSRI) annotations only, whereas no resources have been published so far that also provide syntactic or semantic analyses. ETCSANS fills this gap, and in order to facilitate the usability of syntactic structures for concrete research questions as well as their interpretability for colleagues from areas beyond Assyriology, we followed the model of the Universal Dependencies (UD), which provide cross-linguistically applicable dependency labels and adopt a semantics-oriented approach to dependency syntax.

With a total of 24,460 syntactically annotated texts, the ETCSANS core corpus currently covers about 22% of the overall Neo-Sumerian textual data. The core corpus consists of three subcorpora whose characteristics allowed us to bootstrap syntax annotations in a semi-automated fashion, based on the domain (transaction subcorpus: 22,276 texts, 1,742,634 tokens), the possibility of annotation projection (parallel subcorpus: 1,572 texts, 46,321 tokens) or the existence of specialized morphological annotations (royal subcorpus: 612 texts, 9,133 tokens). Given the complexities of Sumerian writing and the specific nature of the Sumerian language, manual annotation had largely to focus on morphology, whereas manual syntax annotation is limited to a small evaluation corpus (11,220 tokens). The extended ETCSANS corpus contains another 47,476 texts (1,775,582 tokens), for which we provide automated annotations for morphology and named entities and a generic, rule-based annotator that exploits the explicit morphological marking of phrase structure boundaries in Sumerian morphology.

Overall, ETCSANS syntax annotation is largely derived from manual annotation or translations rather than manually created. Given the amount of data and the high degree of specialization required in doing the annotation, this is unavoidable, but from a methodological view, it presents a challenge. We plan for a moderated crowdsourcing process to improve and verify annotations via CDLI (which provides such a workflow since more than 10 years for transcriptions). The necessary tools are linked in the [`tools/`](tools) folder.

## Known issues

- `v.0.1/extended`: change from morphology format to syntax format, run annotator
- `v.0.1/core`: transaction provide partial annotations, only, to be complemented with morphology-based pre-annotation
- The royal subcorpus incorporates morphological annotations from the ETCSRI corpus. Note that ETCSRI data is different in transliteration and tokenization, and sometimes, in readings, and that annotations projected from ETCSRI to CDLI/ETCSANS data may be partially incorrect.

## History

- 2021-12-08 v.0.1a: initial conversion of transaction subcorpus
- 2021-12-04 v.0.1: consolidated corpus repository, see linked submodules under [`dev/`](dev/) for their respective histories.

## Acknowledgements

funding by MTAAC
student support within GSoC
partially supported by LiODi
