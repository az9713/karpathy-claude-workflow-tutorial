# Build another Andrej Karpathy using Claude

A step-by-step tutorial on Nate Herk's workflow for turning Andrej Karpathy's public writing, lectures, and repositories into a Claude Code teaching agent.

**[Read the live tutorial on GitHub Pages](https://az9713.github.io/karpathy-claude-workflow-tutorial/)**

[![Preview of the live step-by-step tutorial](assets/tutorial-preview.jpg)](https://az9713.github.io/karpathy-claude-workflow-tutorial/)

The tutorial brings the video's explanation, seven teaching rules, reusable prompts, and timestamp references into one self-contained web page.

## Inspiration

This project is inspired by Nate Herk's video, **[I Built Another Andrej Karpathy Using Claude](https://www.youtube.com/watch?v=bvGptCLDhyo)**. The workflow and demonstrated prompts come from his video. This project organizes them into a written tutorial with explanations and source limitations.

“Build another Andrej Karpathy” is the video's framing for an agent guided by methods distilled from public sources. The workflow builds a source-backed wiki and teaching instructions; it does not describe training new model weights or transferring a person's mind.

## Follow the workflow

Open the [live tutorial](https://az9713.github.io/karpathy-claude-workflow-tutorial/) and work through the prompts in order:

1. **Gather the evidence.** Collect public blogs, repositories, lecture captions, and posts into an unchanged raw-source folder. Record files, word counts, and retrieval failures. [Video: 02:48](https://www.youtube.com/watch?v=bvGptCLDhyo&t=168s)
2. **Compile a wiki.** Create source pages, principles, methods, an index, a log, and a compact hot page. Link claims to their supporting sources. [Video: 03:56](https://www.youtube.com/watch?v=bvGptCLDhyo&t=236s)
3. **Derive the teaching rules.** Keep recurring rules supported in at least two places, with quotations and source references. [Video: 05:37](https://www.youtube.com/watch?v=bvGptCLDhyo&t=337s)
4. **Create the agent and skill.** Package the rules into a `karpathy` subagent and a `karpathy-teach` skill. Bound the reading context and require an account of what ran, what came out, and what changed. [Video: 06:43](https://www.youtube.com/watch?v=bvGptCLDhyo&t=403s)
5. **Add the run gate.** Ask for a Stop hook that prevents the relevant agent from finishing after code changes without running code afterward. [Video: 07:26](https://www.youtube.com/watch?v=bvGptCLDhyo&t=446s)
6. **Test the teaching loop.** Build a tiny byte-pair tokenizer: define success, predict the output, run it, compare results, show a failure, and repair it. [Video: 08:08](https://www.youtube.com/watch?v=bvGptCLDhyo&t=488s)

Then apply the method to [code review](https://az9713.github.io/karpathy-claude-workflow-tutorial/#review) and [new-source ingestion](https://az9713.github.io/karpathy-claude-workflow-tutorial/#ingest).

## The seven teaching rules

The video synthesizes the following rules from Karpathy's public work:

1. Build it or you don't understand it.
2. First-order term first.
3. Predict, then run, then compare.
4. Show the wrong version first.
5. Prove it, don't claim it.
6. Say what you assumed.
7. Simpler wins.

The tutorial explains how each rule shapes the demonstrated workflow. Execution evidence supports a claim under particular inputs and environments; merely running something does not prove general correctness.

## Using the tutorial

Read it in your browser, copy the prompts into your Claude Code project, and replace demonstration paths with your own. Reading the page requires no API key or installation. Carrying out the workflow requires a Claude Code environment that can read files and run code; its X-source collection prompt also assumes a configured TwitterAPI.io key.

The page includes 12 readable user prompts or command templates and one delegated review instruction block. It provides copy buttons, dark/light themes, mobile-friendly prose, and print/PDF styling. You can also download `index.html` and open it locally; only reference links need an internet connection.

## Coverage and reproduction limits

- This repository contains the tutorial, rather than a finished Karpathy agent or the underlying source corpus.
- The opening montage's sixth numbered prompt card is blurred. The tutorial uses the readable tokenizer test command demonstrated later and marks that distinction.
- The video demonstrates `karpathy-ingest` without showing a readable prompt that creates that skill. Reproducing ingestion requires an additional implementation.
- The delegated review block replaces the creator's machine-specific repository name and path with portable placeholders.
- Reported corpus size, retrieval duration/cost, and example results remain attributed to Nate's demonstration. They are not independently reproduced benchmarks or current pricing estimates.

## Repository contents

- [`index.html`](index.html): the complete standalone tutorial, served by GitHub Pages.
- [`README.md`](README.md): project overview, inspiration, and live-page links.
- [`assets/tutorial-preview.jpg`](assets/tutorial-preview.jpg): a clickable preview of the live page in this README.

GitHub's README links open the rendered tutorial on GitHub Pages. The HTML source itself is available above for download or inspection.
