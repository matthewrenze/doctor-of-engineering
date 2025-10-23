# Exercise 2C: Create a GAIA Agent Eval

An agent evaluation framework for the General AI Assistant (GAIA) benchmark.

## Notes:
Difficulty Levels:
- Level 1 - require 0 or 1 tool and no more than 5 steps
- Level 2 - require require multiple tools and 5-10 steps
- Level 3 - require many tools, many steps, near perfect assistant

## Error Analysis for react - gpt-4.1 - gaia-test-10
1 - Correct
2 - PDB file was too large and truncated, preventing access to ATOM coordinates.
3 - Required visiting ORCID webpages, which the agent cannot do.
4 - Required reading numbers from an image; agent described them but didn’t compute the result.
5 - Correct
6 - Spreadsheet relied on cell colors for interpretation, which the agent could not access or process.
7 - Required analyzing an XML file inside a ZIP, but the agent couldn’t extract or process ZIP contents properly.
8 - Required listening to an audio file, which the agent couldn’t process.
9 - Required analyzing qualifications in a spreadsheet and counting, but the agent stopped after listing qualifications and didn’t complete the count.
10 - File was too large and truncated, so the agent couldn't count the number of books

## Resources
- [Code](code/) - the source code for the agent
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals

## Sources
 - [GAIA: a Benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)

 
