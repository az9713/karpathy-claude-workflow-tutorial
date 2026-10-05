# Evidence ledger

Audit date: 2026-10-05. Target: Richard P. Feynman's documented exposition of the classical harmonic oscillator. Route: primary edited lecture text plus direct teaching self-report; narrow reconstruction, with fidelity unmeasured.

## Local audit and access

The requested `./sources` directory did not exist when audited. Existing repository files concerned Nate Herk's Karpathy workflow and were not used as evidence of Feynman's methods. No local Feynman corpus was available; nothing was silently substituted for it. No interviews, contact, purchases, or publication occurred.

Public pages were read through web retrieval. Access states describe inspected text, not entire books. Figures were not visually inspected; their captions and associated explanation were available. Audio was not played. No source downloads, full-text extracts, figures, or transcripts are included in this bundle. Extraction consists of the short labeled paraphrases below, kept separately from the public originals.

All lecture entries: *The Feynman Lectures on Physics*, Vol. I, original publication 1963; current Caltech New Millennium online edition inspected on the audit date. Exact lecture dates and current site revision identifiers were not verified. The book is credited to Richard P. Feynman, Robert B. Leighton, and Matthew Sands. These chapters are edited presentations of Feynman's lectures; the exact authorship of individual sentences cannot be established here. Mirrors and later editions count as the same origin, not new corroboration.

| ID | Title / origin | Type, attribution, exact inspected coverage | Access / limits |
| --- | --- | --- | --- |
| S09 | [Newton's Laws of Dynamics](https://www.feynmanlectures.caltech.edu/I_09.html) | Edited lecture; sections 9-4 through 9-6, Eqs. 9.11-9.16, Table 9-1, Fig. 9-4 caption | Partial chapter; relevant text inspected; no figure/audio review |
| S21 | [The Harmonic Oscillator](https://www.feynmanlectures.caltech.edu/I_21.html) | Edited lecture; all text, sections 21-1 through 21-5, Eqs. 21.1-21.12 | Complete chapter text; figures not inspected; page says lecture recording is missing |
| S23 | [Resonance](https://www.feynmanlectures.caltech.edu/I_23.html) | Edited lecture; sections 23-1 through 23-3; section 23-4 atmospheric-tide example through independent period check; Eqs. 23.1-23.20, Table 23-1 | Partial chapter; later examples in 23-4 not used for method extraction; page says recording is missing |
| S24 | [Transients](https://www.feynmanlectures.caltech.edu/I_24.html) | Edited lecture; sections 24-1 through 24-3 through Eq. 24.21 and following sentence | Partial chapter; final passage not fully inspected; page says recording is missing |
| SP | [Feynman's Preface](https://www.feynmanlectures.caltech.edu/I_91.html) | Direct named self-report; paragraphs on editing, deductions/new ideas, core/extensions, missing feedback, examination performance | Complete preface text inspected; no learning-outcome replication |
| SE | [Preface to the New Millennium Edition](https://www.feynmanlectures.caltech.edu/I_90.html) | Kip Thorne, not Feynman; "Memories of Feynman's Lectures" and "A History of Errata" through discussion of errata types | Partial; editorial provenance and proxy reception evidence only |
| SR | [Copyright notice](https://www.feynmanlectures.caltech.edu/I_copyright.html) | Publisher notice; entire notice; publication/edition dates and use restrictions | Complete; establishes restrictions, not a teaching method |
| C22 | [Algebra](https://www.feynmanlectures.caltech.edu/I_22.html) | Candidate chapter; title/metadata retrieved only | Metadata-only in this audit; no method support taken from it |

An initial guessed copyright URL under `/info/copyright.html` failed. SR was then obtained from the actual chapter footer link; the failed URL supplies no evidence.

## Permissions and provenance

These public pages were accessible without bypassing controls. The user authorized reading and synthesis through this assistant; source-owner permission for uploading/storing a complete corpus in a hosted model was not established. The publisher retains copyright and restricts unauthorized scanning, uploading, and distribution [SR]. There is no identified open redistribution license.

| Action | Status in this task |
| --- | --- |
| Read | Public pages accessed normally; no restricted local material |
| Model processing | User-authorized limited public-page analysis; no independent grant for full-corpus ingestion |
| Quote | No source quotations in the bundle; use limited attributed quotation only when appropriate and permitted |
| Store | Original synthesis, bibliographic links and authored fixtures stored; no raw corpus archived |
| Share | Initially local; the user subsequently authorized publishing the derived skill and tutorials. No raw lecture corpus is included. Source rights still apply; links are not a license |

SE reports expansion/editing from recordings and blackboard photographs by the coauthors. SP independently states the lectures were edited. Therefore "direct" below means an explicitly stated preference in SP, or documented behavior in the edited exposition; it does not mean verbatim original delivery.

## Method support

Each row separates observation from the builder's procedural inference. No minimal quotes were needed. No method is expert-reviewed or behaviorally validated; numerical checks are described separately in evaluations.md.

| Method | Trigger / scope | Observable support and locator | Inference, checks, rejected alternative, stopping condition |
| --- | --- | --- | --- |
| M1 | Learner needs the meaning of a dynamical equation, or a numerical construction | S09 sections 9-5/9-6, Eq. 9.16: state evolution, refinement, staggered updates | Inferred from a worked case. Recompute at a smaller step; stop only at stated accuracy. Reject treating a coarse first update as exact. Single chapter context |
| M2 | Free linear spring motion | S21 sections 21-2/21-4: unsuccessful amplitude rescaling, time rescaling, initial-data solution, energy check; section 21-3: projection | Inferred from exposition. Substitute and compare initial data and conservation; reject altered amplitude as a frequency fix. Stop if the force is nonlinear. Related normalization also appears in S09, but within the same course |
| M3 | Linear sinusoidal forcing or a circuit transfer | S23 sections 23-1/23-3: complex representation, linearity restriction, damping, circuit correspondence; Table 23-1 | Inferred. Match terms and return to real observables; reject nonlinear phasor substitution or analogy by appearance. Stop at unsupported constitutive physics. S21 introduces driving; same course, not independent evidence |
| M4 | Damping or quadratic observables | S24 section 24-1: real-before-square warning; 24-2/24-3: approximate decay, exact roots, nonoscillatory response | Inferred. Compare approximation to roots and damping regime; reject universal damped cosines. Stop using weak-loss approximations outside their regime. Related damping model in S23 |
| M5 | A fit is offered as confirmation | S23 section 23-4: tide-response fit contrasted with an independently observed period | Inferred verification habit in one narrow example. Seek an additional observable; stop claiming confirmation without it. Single-source; not a universal personal rule |
| M6 | An explanation mixes a core and advanced extensions | SP, paragraphs beginning "For this reason" and "At the same time" | Direct stated preference; builder adapts it to a layered lesson. Check what is deduced versus assumed. Stop expanding when the core outcome is met. Self-report, not demonstrated teaching efficacy |

## Contradictions, exceptions, and corrections

- S21 section 21-5 says a homogeneous contribution usually dies away while discussing an undamped equation. In that equation it persists. Positive damping in S23 supplies the missing condition. Preserve the difference rather than repeat the statement unqualified.
- The divergent nonresonant forced formula at exact resonance is not a finite-time infinite displacement. The builder derives a secular solution in the evaluation checks. This correction is mathematical reasoning, not a newly documented Feynman method.
- S24's weak-loss energy-envelope discussion is approximate; exact instantaneous mechanical energy need not be a pure exponential. Distinguish the exact displacement envelope from averaged energy.
- SP describes lack of feedback and dissatisfaction with examination performance. SE reports mixed retrospective student reception. They concern different evidence and times; neither supports guaranteed learner improvement.

## Coverage gaps

1. No local sources, original audio review, blackboard review, lesson timing, or live learner interaction. Edited text cannot recover delivery or internal decisions.
2. All physics cases come from one course/book lineage. Recurrence across chapters is limited within-series support, not independent documentation of a lifelong method.
3. No expert reference answers for fresh tasks, independent physics reviewer, learner outcome study, or same-model baseline comparison. Fidelity and added value are unmeasured.
4. No evidence for a universal four-step "Feynman technique," obligatory child-level language, invented humor/persona, or an invariant number of teaching rules. These are excluded from operating rules.
5. Quantum oscillator, nonlinear pendulum, stochastic motion, normal-mode reduction, and cross-domain biological claims have not been source-audited for this skill. Generic physics extensions must retain their own attribution.
6. Exact lecture dates, sentence authorship, changing online revisions, and broader republication permissions remain unknown.

Most valuable next case: have a consenting learner solve an unfamiliar oscillator problem after the explanation, then compare the same model/tools with and without the skill. Most valuable next source: accessible authorized worked problem-solving material by Feynman with observable corrections; verify access and rights first, without arranging contact or interviews.
