Use MAX_STATIC_DATA of 500000.
When play begins, seed the random-number generator with 1234.

container is a kind of thing.
door is a kind of thing.
object-like is a kind of thing.
supporter is a kind of thing.
food is a kind of object-like.
key is a kind of object-like.
containers are openable, lockable and fixed in place. containers are usually closed.
door is openable and lockable.
object-like is portable.
supporters are fixed in place.
food is edible.
A room has a text called internal name.


The r_3 and the r_1 and the r_5 and the r_4 and the r_6 and the r_8 and the r_9 and the r_0 and the r_2 and the r_7 are rooms.

Understand "attic" as r_3.
The internal name of r_3 is "attic".
The printed name of r_3 is "-= Attic =-".
The attic part 0 is some text that varies. The attic part 0 is "Ah, the attic. This is some kind of attic, really great standard vibes in this place, a wonderful standard atmosphere. And now, well, you're in it.

 You can make out [if c_0 is locked]a locked[else if c_0 is open]an opened[otherwise]a closed[end if]".
The attic part 1 is some text that varies. The attic part 1 is " trunk in the corner.[if c_0 is open and there is something in the c_0] The trunk contains [a list of things in the c_0].[end if]".
The attic part 2 is some text that varies. The attic part 2 is "[if c_0 is open and the c_0 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The attic part 3 is some text that varies. The attic part 3 is " You can see a stand. Make a note of this, you might have to put stuff on or in it later on. [if there is something on the s_0]You see [a list of things on the s_0] on the stand.[end if]".
The attic part 4 is some text that varies. The attic part 4 is "[if there is nothing on the s_0]But oh no! there's nothing on this piece of garbage.[end if]".
The attic part 5 is some text that varies. The attic part 5 is " Hey, want to see a workbench? Look over there, a workbench. Why don't you take a picture of it, it'll last longer! [if there is something on the s_1]You see [a list of things on the s_1] on the workbench.[end if]".
The attic part 6 is some text that varies. The attic part 6 is "[if there is nothing on the s_1]However, the workbench, like an empty workbench, has nothing on it.[end if]".
The attic part 7 is some text that varies. The attic part 7 is "

 There is [if d_4 is open]an open[otherwise]a closed[end if]".
The attic part 8 is some text that varies. The attic part 8 is " portal leading north. There is [if d_0 is open]an open[otherwise]a closed[end if]".
The attic part 9 is some text that varies. The attic part 9 is " passageway leading west.".
The description of r_3 is "[attic part 0][attic part 1][attic part 2][attic part 3][attic part 4][attic part 5][attic part 6][attic part 7][attic part 8][attic part 9]".

west of r_3 and east of r_1 is a door called d_0.
north of r_3 and south of r_4 is a door called d_4.
Understand "parlor" as r_1.
The internal name of r_1 is "parlor".
The printed name of r_1 is "-= Parlor =-".
The parlor part 0 is some text that varies. The parlor part 0 is "You're now in a parlor.



 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The parlor part 1 is some text that varies. The parlor part 1 is " passageway leading east. There is an unblocked exit to the north. You don't like doors? Why not try going south, that entranceway is unblocked.".
The description of r_1 is "[parlor part 0][parlor part 1]".

The r_0 is mapped south of r_1.
The r_2 is mapped north of r_1.
east of r_1 and west of r_3 is a door called d_0.
Understand "office" as r_5.
The internal name of r_5 is "office".
The printed name of r_5 is "-= Office =-".
The office part 0 is some text that varies. The office part 0 is "You find yourself in an office. A typical kind of place.

 You make out a suitcase.[if c_1 is open and there is something in the c_1] The suitcase contains [a list of things in the c_1]. Hmmm... what else, what else?[end if]".
The office part 1 is some text that varies. The office part 1 is "[if c_1 is open and the c_1 contains nothing] The suitcase is empty! This is the worst thing that could possibly happen, ever![end if]".
The office part 2 is some text that varies. The office part 2 is " Were you looking for a chair? Because look over there, it's a chair. [if there is something on the s_2]You see [a list of things on the s_2] on the chair.[end if]".
The office part 3 is some text that varies. The office part 3 is "[if there is nothing on the s_2]However, the chair, like an empty chair, has nothing on it.[end if]".
The office part 4 is some text that varies. The office part 4 is " Hey, want to see a desk? Look over there, a desk. [if there is something on the s_3]You see [a list of things on the s_3] on the desk.[end if]".
The office part 5 is some text that varies. The office part 5 is "[if there is nothing on the s_3]But there isn't a thing on it.[end if]".
The office part 6 is some text that varies. The office part 6 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The office part 7 is some text that varies. The office part 7 is " gateway leading east. There is [if d_3 is open]an open[otherwise]a closed[end if]".
The office part 8 is some text that varies. The office part 8 is " hatch leading west.".
The description of r_5 is "[office part 0][office part 1][office part 2][office part 3][office part 4][office part 5][office part 6][office part 7][office part 8]".

west of r_5 and east of r_4 is a door called d_3.
east of r_5 and west of r_6 is a door called d_2.
Understand "workshop" as r_4.
The internal name of r_4 is "workshop".
The printed name of r_4 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "You've entered a workshop.



 There is [if d_3 is open]an open[otherwise]a closed[end if]".
The workshop part 1 is some text that varies. The workshop part 1 is " hatch leading east. There is [if d_4 is open]an open[otherwise]a closed[end if]".
The workshop part 2 is some text that varies. The workshop part 2 is " portal leading south.".
The description of r_4 is "[workshop part 0][workshop part 1][workshop part 2]".

south of r_4 and north of r_3 is a door called d_4.
east of r_4 and west of r_5 is a door called d_3.
Understand "shower" as r_6.
The internal name of r_6 is "shower".
The printed name of r_6 is "-= Shower =-".
The shower part 0 is some text that varies. The shower part 0 is "You've seen better showers, but at least this one seems pretty usual. You begin to take stock of what's here.



 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The shower part 1 is some text that varies. The shower part 1 is " gateway leading west. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The shower part 2 is some text that varies. The shower part 2 is " gate leading north. You don't like doors? Why not try going south, that entranceway is unguarded.".
The description of r_6 is "[shower part 0][shower part 1][shower part 2]".

west of r_6 and east of r_5 is a door called d_2.
The r_7 is mapped south of r_6.
north of r_6 and south of r_8 is a door called d_1.
Understand "sauna" as r_8.
The internal name of r_8 is "sauna".
The printed name of r_8 is "-= Sauna =-".
The sauna part 0 is some text that varies. The sauna part 0 is "You're now in a sauna.



 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The sauna part 1 is some text that varies. The sauna part 1 is " gate leading south. There is an unblocked exit to the west.".
The description of r_8 is "[sauna part 0][sauna part 1]".

The r_9 is mapped west of r_8.
south of r_8 and north of r_6 is a door called d_1.
Understand "kitchenette" as r_9.
The internal name of r_9 is "kitchenette".
The printed name of r_9 is "-= Kitchenette =-".
The kitchenette part 0 is some text that varies. The kitchenette part 0 is "Look at you, bigshot, walking into a kitchenette like it isn't some huge deal.

 You can see [if c_2 is locked]a locked[else if c_2 is open]an opened[otherwise]a closed[end if]".
The kitchenette part 1 is some text that varies. The kitchenette part 1 is " cabinet.[if c_2 is open and there is something in the c_2] The cabinet contains [a list of things in the c_2].[end if]".
The kitchenette part 2 is some text that varies. The kitchenette part 2 is "[if c_2 is open and the c_2 contains nothing] The cabinet is empty! This is the worst thing that could possibly happen, ever![end if]".
The kitchenette part 3 is some text that varies. The kitchenette part 3 is " You see a board. [if there is something on the s_4]On the board you make out [a list of things on the s_4].[end if]".
The kitchenette part 4 is some text that varies. The kitchenette part 4 is "[if there is nothing on the s_4]Looks like someone's already been here and taken everything off it, though.[end if]".
The kitchenette part 5 is some text that varies. The kitchenette part 5 is "

There is an exit to the east. Don't worry, it is unblocked.".
The description of r_9 is "[kitchenette part 0][kitchenette part 1][kitchenette part 2][kitchenette part 3][kitchenette part 4][kitchenette part 5]".

The r_8 is mapped east of r_9.
Understand "restroom" as r_0.
The internal name of r_0 is "restroom".
The printed name of r_0 is "-= Restroom =-".
The restroom part 0 is some text that varies. The restroom part 0 is "You are in a restroom. A standard kind of place.

 You can make out a shelf. The shelf is ordinary.[if there is something on the s_5] On the shelf you make out [a list of things on the s_5].[end if]".
The restroom part 1 is some text that varies. The restroom part 1 is "[if there is nothing on the s_5] Unfortunately, there isn't a thing on it.[end if]".
The restroom part 2 is some text that varies. The restroom part 2 is "

There is an exit to the north. Don't worry, it is unguarded.".
The description of r_0 is "[restroom part 0][restroom part 1][restroom part 2]".

The r_1 is mapped north of r_0.
Understand "playroom" as r_2.
The internal name of r_2 is "playroom".
The printed name of r_2 is "-= Playroom =-".
The playroom part 0 is some text that varies. The playroom part 0 is "You are in a playroom. You begin to take stock of what's in the room.

 You can make out a box. You shudder, but continue examining the room.[if c_3 is open and there is something in the c_3] The box contains [a list of things in the c_3].[end if]".
The playroom part 1 is some text that varies. The playroom part 1 is "[if c_3 is open and the c_3 contains nothing] The box is empty! This is the worst thing that could possibly happen, ever![end if]".
The playroom part 2 is some text that varies. The playroom part 2 is "

There is an exit to the south. Don't worry, it is unblocked.".
The description of r_2 is "[playroom part 0][playroom part 1][playroom part 2]".

The r_1 is mapped south of r_2.
Understand "chamber" as r_7.
The internal name of r_7 is "chamber".
The printed name of r_7 is "-= Chamber =-".
The chamber part 0 is some text that varies. The chamber part 0 is "You've moved into a standard room. Your mind races to think of what kind of room would be standard. And then it hits you. Of course. You're in the chamber. You decide to start listing off everything you see in the room, as if you were in a text adventure.



There is an exit to the north. Don't worry, it is unguarded.".
The description of r_7 is "[chamber part 0]".

The r_6 is mapped north of r_7.

The c_0 and the c_1 and the c_2 and the c_3 are containers.
The c_0 and the c_1 and the c_2 and the c_3 are privately-named.
The d_0 and the d_4 and the d_3 and the d_2 and the d_1 are doors.
The d_0 and the d_4 and the d_3 and the d_2 and the d_1 are privately-named.
The k_0 are keys.
The k_0 are privately-named.
The o_0 are object-likes.
The o_0 are privately-named.
The r_3 and the r_1 and the r_5 and the r_4 and the r_6 and the r_8 and the r_9 and the r_0 and the r_2 and the r_7 are rooms.
The r_3 and the r_1 and the r_5 and the r_4 and the r_6 and the r_8 and the r_9 and the r_0 and the r_2 and the r_7 are privately-named.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 are supporters.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 are privately-named.

The description of d_0 is "The passageway looks imposing. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_0 is "passageway".
Understand "passageway" as d_0.
The d_0 is open.
The description of d_4 is "it is what it is, a portal [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_4 is "portal".
Understand "portal" as d_4.
The d_4 is open.
The description of d_3 is "The hatch looks towering. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_3 is "hatch".
Understand "hatch" as d_3.
The d_3 is open.
The description of d_2 is "it is what it is, a gateway [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_2 is "gateway".
Understand "gateway" as d_2.
The d_2 is closed.
The description of d_1 is "The gate looks ominous. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_1 is "gate".
Understand "gate" as d_1.
The d_1 is open.
The description of c_0 is "The trunk looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_0 is "trunk".
Understand "trunk" as c_0.
The c_0 is in r_3.
The c_0 is closed.
The description of c_1 is "The suitcase looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_1 is "suitcase".
Understand "suitcase" as c_1.
The c_1 is in r_5.
The c_1 is closed.
The description of c_2 is "The cabinet looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_2 is "cabinet".
Understand "cabinet" as c_2.
The c_2 is in r_9.
The c_2 is open.
The description of c_3 is "The box looks strong, and impossible to destroy. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_3 is "box".
Understand "box" as c_3.
The c_3 is in r_2.
The c_3 is open.
The description of k_0 is "The passkey looks useful".
The printed name of k_0 is "passkey".
Understand "passkey" as k_0.
The k_0 is in r_0.
The description of o_0 is "The poem is unremarkable.".
The printed name of o_0 is "poem".
Understand "poem" as o_0.
The o_0 is in r_1.
The description of s_0 is "The stand is unstable.".
The printed name of s_0 is "stand".
Understand "stand" as s_0.
The s_0 is in r_3.
The description of s_1 is "The workbench is solidly built.".
The printed name of s_1 is "workbench".
Understand "workbench" as s_1.
The s_1 is in r_3.
The description of s_2 is "The chair is shaky.".
The printed name of s_2 is "chair".
Understand "chair" as s_2.
The s_2 is in r_5.
The description of s_3 is "The desk is an unstable piece of junk.".
The printed name of s_3 is "desk".
Understand "desk" as s_3.
The s_3 is in r_5.
The description of s_4 is "The board is durable.".
The printed name of s_4 is "board".
Understand "board" as s_4.
The s_4 is in r_9.
The description of s_5 is "The shelf is durable.".
The printed name of s_5 is "shelf".
Understand "shelf" as s_5.
The s_5 is in r_0.


The player is in r_8.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "go south / open gateway / go west / go west / go south / go west / take poem"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the k_0:
		end the story; [Lost]
	else if The player is in r_1 and The player carries the o_0:
		increase the score by 1; [Quest completed]
		if 1 is 1 [always true]:
			Now the quest0 completed is true;

Use scoring. The maximum score is 1.
This is the simpler notify score changes rule:
	If the score is not the last notified score:
		let V be the score - the last notified score;
		if V > 0:
			say "Your score has just gone up by [V in words] ";
		else:
			say "Your score changed by [V in words] ";
		if V >= -1 and V <= 1:
			say "point.";
		else:
			say "points.";
		Now the last notified score is the score;
	if quest0 completed is true:
		end the story finally; [Win]

The simpler notify score changes rule substitutes for the notify score changes rule.

Rule for listing nondescript items:
	stop.

Rule for printing the banner text:
	say "[fixed letter spacing]";
	say "                    ________  ________  __    __  ________        [line break]";
	say "                   |        \|        \|  \  |  \|        \       [line break]";
	say "                    \$$$$$$$$| $$$$$$$$| $$  | $$ \$$$$$$$$       [line break]";
	say "                      | $$   | $$__     \$$\/  $$   | $$          [line break]";
	say "                      | $$   | $$  \     >$$  $$    | $$          [line break]";
	say "                      | $$   | $$$$$    /  $$$$\    | $$          [line break]";
	say "                      | $$   | $$_____ |  $$ \$$\   | $$          [line break]";
	say "                      | $$   | $$     \| $$  | $$   | $$          [line break]";
	say "                       \$$    \$$$$$$$$ \$$   \$$    \$$          [line break]";
	say "              __       __   ______   _______   __        _______  [line break]";
	say "             |  \  _  |  \ /      \ |       \ |  \      |       \ [line break]";
	say "             | $$ / \ | $$|  $$$$$$\| $$$$$$$\| $$      | $$$$$$$\[line break]";
	say "             | $$/  $\| $$| $$  | $$| $$__| $$| $$      | $$  | $$[line break]";
	say "             | $$  $$$\ $$| $$  | $$| $$    $$| $$      | $$  | $$[line break]";
	say "             | $$ $$\$$\$$| $$  | $$| $$$$$$$\| $$      | $$  | $$[line break]";
	say "             | $$$$  \$$$$| $$__/ $$| $$  | $$| $$_____ | $$__/ $$[line break]";
	say "             | $$$    \$$$ \$$    $$| $$  | $$| $$     \| $$    $$[line break]";
	say "              \$$      \$$  \$$$$$$  \$$   \$$ \$$$$$$$$ \$$$$$$$ [line break]";
	say "[variable letter spacing][line break]";
	say "[objective][line break]".

Include Basic Screen Effects by Emily Short.

Rule for printing the player's obituary:
	if story has ended finally:
		center "*** The End ***";
	else:
		center "*** You lost! ***";
	say paragraph break;
	if maximum score is -32768:
		say "You scored a total of [score] point[s], in [turn count] turn[s].";
	else:
		say "You scored [score] out of a possible [maximum score], in [turn count] turn[s].";
	[wait for any key;
	stop game abruptly;]
	rule succeeds.

Carry out requesting the score:
	if maximum score is -32768:
		say "You have so far scored [score] point[s], in [turn count] turn[s].";
	else:
		say "You have so far scored [score] out of a possible [maximum score], in [turn count] turn[s].";
	rule succeeds.

Rule for implicitly taking something (called target):
	if target is fixed in place:
		say "The [target] is fixed in place.";
	otherwise:
		say "You need to take the [target] first.";
		set pronouns from target;
	stop.

Does the player mean doing something:
	if the noun is not nothing and the second noun is nothing and the player's command matches the text printed name of the noun:
		it is likely;
	if the noun is nothing and the second noun is not nothing and the player's command matches the text printed name of the second noun:
		it is likely;
	if the noun is not nothing and the second noun is not nothing and the player's command matches the text printed name of the noun and the player's command matches the text printed name of the second noun:
		it is very likely.  [Handle action with two arguments.]

Printing the content of the room is an activity.
Rule for printing the content of the room:
	let R be the location of the player;
	say "Room contents:[line break]";
	list the contents of R, with newlines, indented, including all contents, with extra indentation.

Printing the content of the world is an activity.
Rule for printing the content of the world:
	let L be the list of the rooms;
	say "World: [line break]";
	repeat with R running through L:
		say "  [the internal name of R][line break]";
	repeat with R running through L:
		say "[the internal name of R]:[line break]";
		if the list of things in R is empty:
			say "  nothing[line break]";
		otherwise:
			list the contents of R, with newlines, indented, including all contents, with extra indentation.

Printing the content of the inventory is an activity.
Rule for printing the content of the inventory:
	say "You are carrying: ";
	list the contents of the player, as a sentence, giving inventory information, including all contents;
	say ".".

The print standard inventory rule is not listed in any rulebook.
Carry out taking inventory (this is the new print inventory rule):
	say "You are carrying: ";
	list the contents of the player, as a sentence, giving inventory information, including all contents;
	say ".".

Printing the content of nowhere is an activity.
Rule for printing the content of nowhere:
	say "Nowhere:[line break]";
	let L be the list of the off-stage things;
	repeat with thing running through L:
		say "  [thing][line break]";

Printing the things on the floor is an activity.
Rule for printing the things on the floor:
	let R be the location of the player;
	let L be the list of things in R;
	remove yourself from L;
	remove the list of containers from L;
	remove the list of supporters from L;
	remove the list of doors from L;
	if the number of entries in L is greater than 0:
		say "There is [L with indefinite articles] on the floor.";

After printing the name of something (called target) while
printing the content of the room
or printing the content of the world
or printing the content of the inventory
or printing the content of nowhere:
	follow the property-aggregation rules for the target.

The property-aggregation rules are an object-based rulebook.
The property-aggregation rulebook has a list of text called the tagline.

[At the moment, we only support "open/unlocked", "closed/unlocked" and "closed/locked" for doors and containers.]
[A first property-aggregation rule for an openable open thing (this is the mention open openables rule):
	add "open" to the tagline.

A property-aggregation rule for an openable closed thing (this is the mention closed openables rule):
	add "closed" to the tagline.

A property-aggregation rule for an lockable unlocked thing (this is the mention unlocked lockable rule):
	add "unlocked" to the tagline.

A property-aggregation rule for an lockable locked thing (this is the mention locked lockable rule):
	add "locked" to the tagline.]

A first property-aggregation rule for an openable lockable open unlocked thing (this is the mention open openables rule):
	add "open" to the tagline.

A property-aggregation rule for an openable lockable closed unlocked thing (this is the mention closed openables rule):
	add "closed" to the tagline.

A property-aggregation rule for an openable lockable closed locked thing (this is the mention locked openables rule):
	add "locked" to the tagline.

A property-aggregation rule for a lockable thing (called the lockable thing) (this is the mention matching key of lockable rule):
	let X be the matching key of the lockable thing;
	if X is not nothing:
		add "match [X]" to the tagline.

A property-aggregation rule for an edible off-stage thing (this is the mention eaten edible rule):
	add "eaten" to the tagline.

The last property-aggregation rule (this is the print aggregated properties rule):
	if the number of entries in the tagline is greater than 0:
		say " ([tagline])";
		rule succeeds;
	rule fails;

The objective part 0 is some text that varies. The objective part 0 is "It's time to explore the amazing world of TextWorld! Here is how to play! First step, take a trip south. Okay, and then, ensure that the gateway inside the shower is open. After opening the gateway, g".
The objective part 1 is some text that varies. The objective part 1 is "o to the west. Then, go west. With that over with, try to go to the south. Following that, attempt to take a trip west. And then, lift the poem from the floor of the parlor. That's it!".

An objective is some text that varies. The objective is "[objective part 0][objective part 1]".
Printing the objective is an action applying to nothing.
Carry out printing the objective:
	say "[objective]".

Understand "goal" as printing the objective.

The taking action has an object called previous locale (matched as "from").

Setting action variables for taking:
	now previous locale is the holder of the noun.

Report taking something from the location:
	say "You pick up [the noun] from the ground." instead.

Report taking something:
	say "You take [the noun] from [the previous locale]." instead.

Report dropping something:
	say "You drop [the noun] on the ground." instead.

The print state option is a truth state that varies.
The print state option is usually false.

Turning on the print state option is an action applying to nothing.
Carry out turning on the print state option:
	Now the print state option is true.

Turning off the print state option is an action applying to nothing.
Carry out turning off the print state option:
	Now the print state option is false.

Printing the state is an activity.
Rule for printing the state:
	let R be the location of the player;
	say "Room: [line break] [the internal name of R][line break]";
	[say "[line break]";
	carry out the printing the content of the room activity;]
	say "[line break]";
	carry out the printing the content of the world activity;
	say "[line break]";
	carry out the printing the content of the inventory activity;
	say "[line break]";
	carry out the printing the content of nowhere activity;
	say "[line break]".

Printing the entire state is an action applying to nothing.
Carry out printing the entire state:
	say "-=STATE START=-[line break]";
	carry out the printing the state activity;
	say "[line break]Score:[line break] [score]/[maximum score][line break]";
	say "[line break]Objective:[line break] [objective][line break]";
	say "[line break]Inventory description:[line break]";
	say "  You are carrying: [a list of things carried by the player].[line break]";
	say "[line break]Room description:[line break]";
	try looking;
	say "[line break]-=STATE STOP=-";

Every turn:
	if extra description command option is true:
		say "<description>";
		try looking;
		say "</description>";
	if extra inventory command option is true:
		say "<inventory>";
		try taking inventory;
		say "</inventory>";
	if extra score command option is true:
		say "<score>[line break][score][line break]</score>";
	if extra score command option is true:
		say "<moves>[line break][turn count][line break]</moves>";
	if print state option is true:
		try printing the entire state;

When play ends:
	if print state option is true:
		try printing the entire state;

After looking:
	carry out the printing the things on the floor activity.

Understand "print_state" as printing the entire state.
Understand "enable print state option" as turning on the print state option.
Understand "disable print state option" as turning off the print state option.

Before going through a closed door (called the blocking door):
	say "You have to open the [blocking door] first.";
	stop.

Before opening a locked door (called the locked door):
	let X be the matching key of the locked door;
	if X is nothing:
		say "The [locked door] is welded shut.";
	otherwise:
		say "You have to unlock the [locked door] with the [X] first.";
	stop.

Before opening a locked container (called the locked container):
	let X be the matching key of the locked container;
	if X is nothing:
		say "The [locked container] is welded shut.";
	otherwise:
		say "You have to unlock the [locked container] with the [X] first.";
	stop.

Displaying help message is an action applying to nothing.
Carry out displaying help message:
	say "[fixed letter spacing]Available commands:[line break]";
	say "  look:                describe the current room[line break]";
	say "  goal:                print the goal of this game[line break]";
	say "  inventory:           print player's inventory[line break]";
	say "  go <dir>:            move the player north, east, south or west[line break]";
	say "  examine ...:         examine something more closely[line break]";
	say "  eat ...:             eat edible food[line break]";
	say "  open ...:            open a door or a container[line break]";
	say "  close ...:           close a door or a container[line break]";
	say "  drop ...:            drop an object on the floor[line break]";
	say "  take ...:            take an object that is on the floor[line break]";
	say "  put ... on ...:      place an object on a supporter[line break]";
	say "  take ... from ...:   take an object from a container or a supporter[line break]";
	say "  insert ... into ...: place an object into a container[line break]";
	say "  lock ... with ...:   lock a door or a container with a key[line break]";
	say "  unlock ... with ...: unlock a door or a container with a key[line break]";

Understand "help" as displaying help message.

Taking all is an action applying to nothing.
Check taking all:
	say "You have to be more specific!";
	rule fails.

Understand "take all" as taking all.
Understand "get all" as taking all.
Understand "pick up all" as taking all.

Understand "take each" as taking all.
Understand "get each" as taking all.
Understand "pick up each" as taking all.

Understand "take everything" as taking all.
Understand "get everything" as taking all.
Understand "pick up everything" as taking all.

The extra description command option is a truth state that varies.
The extra description command option is usually false.

Turning on the extra description command option is an action applying to nothing.
Carry out turning on the extra description command option:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	Now the extra description command option is true.

Understand "tw-extra-infos description" as turning on the extra description command option.

The extra inventory command option is a truth state that varies.
The extra inventory command option is usually false.

Turning on the extra inventory command option is an action applying to nothing.
Carry out turning on the extra inventory command option:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	Now the extra inventory command option is true.

Understand "tw-extra-infos inventory" as turning on the extra inventory command option.

The extra score command option is a truth state that varies.
The extra score command option is usually false.

Turning on the extra score command option is an action applying to nothing.
Carry out turning on the extra score command option:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	Now the extra score command option is true.

Understand "tw-extra-infos score" as turning on the extra score command option.

The extra moves command option is a truth state that varies.
The extra moves command option is usually false.

Turning on the extra moves command option is an action applying to nothing.
Carry out turning on the extra moves command option:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	Now the extra moves command option is true.

Understand "tw-extra-infos moves" as turning on the extra moves command option.

To trace the actions:
	(- trace_actions = 1; -).

Tracing the actions is an action applying to nothing.
Carry out tracing the actions:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	trace the actions;

Understand "tw-trace-actions" as tracing the actions.

The restrict commands option is a truth state that varies.
The restrict commands option is usually false.

Turning on the restrict commands option is an action applying to nothing.
Carry out turning on the restrict commands option:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	Now the restrict commands option is true.

Understand "restrict commands" as turning on the restrict commands option.

The taking allowed flag is a truth state that varies.
The taking allowed flag is usually false.

Before removing something from something:
	now the taking allowed flag is true.

After removing something from something:
	now the taking allowed flag is false.

Before taking a thing (called the object) when the object is on a supporter (called the supporter):
	if the restrict commands option is true and taking allowed flag is false:
		say "Can't see any [object] on the floor! Try taking the [object] from the [supporter] instead.";
		rule fails.

Before of taking a thing (called the object) when the object is in a container (called the container):
	if the restrict commands option is true and taking allowed flag is false:
		say "Can't see any [object] on the floor! Try taking the [object] from the [container] instead.";
		rule fails.

Understand "take [something]" as removing it from.

Rule for supplying a missing second noun while removing:
	if restrict commands option is false and noun is on a supporter (called the supporter):
		now the second noun is the supporter;
	else if restrict commands option is false and noun is in a container (called the container):
		now the second noun is the container;
	else:
		try taking the noun;
		say ""; [Needed to avoid printing a default message.]

The version number is always 1.

Reporting the version number is an action applying to nothing.
Carry out reporting the version number:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	say "[version number]".

Understand "tw-print version" as reporting the version number.

Reporting max score is an action applying to nothing.
Carry out reporting max score:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	if maximum score is -32768:
		say "infinity";
	else:
		say "[maximum score]".

Understand "tw-print max_score" as reporting max score.

To print id of (something - thing):
	(- print {something}, "^"; -).

Printing the id of player is an action applying to nothing.
Carry out printing the id of player:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	print id of player.

Printing the id of EndOfObject is an action applying to nothing.
Carry out printing the id of EndOfObject:
	Decrease turn count by 1;  [Internal framework commands shouldn't count as a turn.]
	print id of EndOfObject.

Understand "tw-print player id" as printing the id of player.
Understand "tw-print EndOfObject id" as printing the id of EndOfObject.

There is a EndOfObject.

