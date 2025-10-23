# Exercise 2B: Create a TextWorld Agent Eval

An agent evaluation framework for the textworld environment.

## Run in Console
ubuntu.exe
source /home/matthew/.virtualenvs/pycharm_test/bin/activate
cd /mnt/c/Users/Matthew/Dropbox/School/JHU/DEng/Repository/2-evaluations/exercises/textworld-agent/code/
python 2_run_eval.py

## Simple game
- Objective: find the specified food item and cook it
- Difficulty levels: only one
- Map always stays the same
- Objects change based on random seed
- Contains test and training modes (objects change)
- Rewards can be sparse, balanced, or dense
- Goal can be detailed, brief, or none

## Coin game
- Objective: collect coins in a sequential (chain) maze
- Difficulty levels: 1-300
- Difficulty modes:
  - Easy (1-100) - 1-100 rooms, no distractor rooms,
  - Medium (101-200) - 1-100 rooms, with orthogonal distractor rooms
  - Hard (201-300) - 1-100 rooms, with random distractor rooms
- Randomly generated: map, distractors (hard mode)
- Static: player starts at beginning of maze and coin is at the end

## Treasure Game
- Objective: find specified object in a maze
- Difficulty levels: 1-30
- Difficulty modes:
  - Easy (1-10) - no distractors and all doors open
    - Quest length ranges from 1 to 5
  - Medium (11-20) - 10 distractors, closed doors, and closed containers
     - Quest length ranges from 2 to 10
  - Hard (21-30) - 20 distractors, locked doors, and locked containers (with keys in inventory)
     - Quest length ranges from 3 to 20
- Randomly generated: map, start location, treasure, distractors

## Cooking Game
- Objective: cook a specified dish
- Difficulty level: specified by parameters below
  - Recipe: number of ingredients [1-5]
  - Take: number of ingredients (not already in inventory) [1-5]
  - Go: number of rooms [1, 6, 9, 12]
  - Open: whether containers need to be opened [T/F]
  - Cook: whether cooking is required [T/F]
  - Cut: whether cutting is required [T/F]
  - Drop: whether dropping is required (limited inventory capacity) [T/F]
Note: Actions (drop, open, cut, cook) can be sequenced:
 - 0=none, 1=take, 2=open, 3=cut, 4=cook, 5=drop

## Resources
- [Code](code/) - the source code for the agent
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals

## Sources
 - [TextWorld](https://arxiv.org/abs/1806.11532)

 
