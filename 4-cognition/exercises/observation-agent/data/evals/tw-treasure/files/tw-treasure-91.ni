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


The r_1 and the r_0 and the r_10 and the r_11 and the r_12 and the r_13 and the r_14 and the r_15 and the r_17 and the r_3 and the r_2 and the r_4 and the r_6 and the r_5 and the r_7 and the r_8 and the r_9 and the r_16 and the r_18 and the r_19 are rooms.

Understand "workshop" as r_1.
The internal name of r_1 is "workshop".
The printed name of r_1 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "You've just walked into a workshop. I guess you better just go and list everything you see here.

 Oh wow! Is that what I think it is? It is! It's an armchair. [if there is something on the s_0]You see [a list of things on the s_0] on the armchair. You can't wait to tell the folks at home about this![end if]".
The workshop part 1 is some text that varies. The workshop part 1 is "[if there is nothing on the s_0]Looks like someone's already been here and taken everything off it, though.[end if]".
The workshop part 2 is some text that varies. The workshop part 2 is "

 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The workshop part 3 is some text that varies. The workshop part 3 is " portal leading north. There is an exit to the east. Don't worry, it is unguarded. You don't like doors? Why not try going south, that entranceway is unguarded. You need an unblocked exit? You should try going west.".
The description of r_1 is "[workshop part 0][workshop part 1][workshop part 2][workshop part 3]".

The r_0 is mapped west of r_1.
The r_2 is mapped south of r_1.
north of r_1 and south of r_5 is a door called d_0.
The r_4 is mapped east of r_1.
Understand "cookery" as r_0.
The internal name of r_0 is "cookery".
The printed name of r_0 is "-= Cookery =-".
The cookery part 0 is some text that varies. The cookery part 0 is "You're now in a cookery. You begin looking for stuff.



There is an unblocked exit to the east.".
The description of r_0 is "[cookery part 0]".

The r_1 is mapped east of r_0.
Understand "chamber" as r_10.
The internal name of r_10 is "chamber".
The printed name of r_10 is "-= Chamber =-".
The chamber part 0 is some text that varies. The chamber part 0 is "You're now in a chamber.

 You make out a dresser.[if c_0 is open and there is something in the c_0] The dresser contains [a list of things in the c_0].[end if]".
The chamber part 1 is some text that varies. The chamber part 1 is "[if c_0 is open and the c_0 contains nothing] The dresser is empty! This is the worst thing that could possibly happen, ever![end if]".
The chamber part 2 is some text that varies. The chamber part 2 is " You can make out [if c_1 is locked]a locked[else if c_1 is open]an opened[otherwise]a closed[end if]".
The chamber part 3 is some text that varies. The chamber part 3 is " box.[if c_1 is open and there is something in the c_1] The box contains [a list of things in the c_1].[end if]".
The chamber part 4 is some text that varies. The chamber part 4 is "[if c_1 is open and the c_1 contains nothing] The box is empty, what a horrible day![end if]".
The chamber part 5 is some text that varies. The chamber part 5 is " You make out a desk. The desk is typical.[if there is something on the s_1] On the desk you make out [a list of things on the s_1]. Wow! Just like in the movies![end if]".
The chamber part 6 is some text that varies. The chamber part 6 is "[if there is nothing on the s_1] The desk appears to be empty.[end if]".
The chamber part 7 is some text that varies. The chamber part 7 is " You see a bench. You shudder, but continue examining the bench. The bench is standard.[if there is something on the s_2] On the bench you make out [a list of things on the s_2]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The chamber part 8 is some text that varies. The chamber part 8 is "[if there is nothing on the s_2] But the thing is empty, unfortunately.[end if]".
The chamber part 9 is some text that varies. The chamber part 9 is "

There is an exit to the east. Don't worry, it is unblocked. There is an exit to the south. Don't worry, it is unblocked. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_10 is "[chamber part 0][chamber part 1][chamber part 2][chamber part 3][chamber part 4][chamber part 5][chamber part 6][chamber part 7][chamber part 8][chamber part 9]".

The r_11 is mapped west of r_10.
The r_12 is mapped south of r_10.
The r_9 is mapped east of r_10.
Understand "cellar" as r_11.
The internal name of r_11 is "cellar".
The printed name of r_11 is "-= Cellar =-".
The cellar part 0 is some text that varies. The cellar part 0 is "You are in a cellar. A standard kind of place. The room seems oddly familiar, as though it were only superficially different from the other rooms in the building.



You don't like doors? Why not try going east, that entranceway is unguarded. There is an exit to the south. Don't worry, it is unguarded.".
The description of r_11 is "[cellar part 0]".

The r_13 is mapped south of r_11.
The r_10 is mapped east of r_11.
Understand "steam room" as r_12.
The internal name of r_12 is "steam room".
The printed name of r_12 is "-= Steam Room =-".
The steam room part 0 is some text that varies. The steam room part 0 is "You've entered a steam room. You can barely contain your excitement.

 You make out a case. I mean, just wow! Isn't TextWorld just the best?[if c_2 is open and there is something in the c_2] The case contains [a list of things in the c_2].[end if]".
The steam room part 1 is some text that varies. The steam room part 1 is "[if c_2 is open and the c_2 contains nothing] The case is empty, what a horrible day![end if]".
The steam room part 2 is some text that varies. The steam room part 2 is " You see a counter. [if there is something on the s_3]You see [a list of things on the s_3] on the counter.[end if]".
The steam room part 3 is some text that varies. The steam room part 3 is "[if there is nothing on the s_3]The counter appears to be empty.[end if]".
The steam room part 4 is some text that varies. The steam room part 4 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The steam room part 5 is some text that varies. The steam room part 5 is " gate leading south. You don't like doors? Why not try going east, that entranceway is unblocked. There is an exit to the north. Don't worry, it is unguarded. You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_12 is "[steam room part 0][steam room part 1][steam room part 2][steam room part 3][steam room part 4][steam room part 5]".

The r_13 is mapped west of r_12.
south of r_12 and north of r_15 is a door called d_2.
The r_10 is mapped north of r_12.
The r_14 is mapped east of r_12.
Understand "cubicle" as r_13.
The internal name of r_13 is "cubicle".
The printed name of r_13 is "-= Cubicle =-".
The cubicle part 0 is some text that varies. The cubicle part 0 is "You are in a cubicle. A normal kind of place. Okay, just remember what you're here to do, and everything will go great.

 You can make out [if c_3 is locked]a locked[else if c_3 is open]an opened[otherwise]a closed[end if]".
The cubicle part 1 is some text that varies. The cubicle part 1 is " standard looking toolbox right there by you.[if c_3 is open and there is something in the c_3] The toolbox contains [a list of things in the c_3]. You shudder, but continue examining the room.[end if]".
The cubicle part 2 is some text that varies. The cubicle part 2 is "[if c_3 is open and the c_3 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The cubicle part 3 is some text that varies. The cubicle part 3 is " You can make out a display. Now why would someone leave that there?[if c_4 is open and there is something in the c_4] The display contains [a list of things in the c_4].[end if]".
The cubicle part 4 is some text that varies. The cubicle part 4 is "[if c_4 is open and the c_4 contains nothing] The display is empty, what a horrible day![end if]".
The cubicle part 5 is some text that varies. The cubicle part 5 is "

There is an unguarded exit to the east. You need an unblocked exit? You should try going north.".
The description of r_13 is "[cubicle part 0][cubicle part 1][cubicle part 2][cubicle part 3][cubicle part 4][cubicle part 5]".

The r_11 is mapped north of r_13.
The r_12 is mapped east of r_13.
Understand "kitchenette" as r_14.
The internal name of r_14 is "kitchenette".
The printed name of r_14 is "-= Kitchenette =-".
The kitchenette part 0 is some text that varies. The kitchenette part 0 is "You are in a kitchenette. A standard kind of place.



You need an unblocked exit? You should try going north. There is an exit to the west. Don't worry, it is unblocked.".
The description of r_14 is "[kitchenette part 0]".

The r_12 is mapped west of r_14.
The r_9 is mapped north of r_14.
Understand "bathroom" as r_15.
The internal name of r_15 is "bathroom".
The printed name of r_15 is "-= Bathroom =-".
The bathroom part 0 is some text that varies. The bathroom part 0 is "You've entered a bathroom.



 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The bathroom part 1 is some text that varies. The bathroom part 1 is " gate leading north. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The bathroom part 2 is some text that varies. The bathroom part 2 is " hatch leading west. There is an exit to the south. Don't worry, it is unblocked.".
The description of r_15 is "[bathroom part 0][bathroom part 1][bathroom part 2]".

west of r_15 and east of r_17 is a door called d_1.
The r_16 is mapped south of r_15.
north of r_15 and south of r_12 is a door called d_2.
Understand "closet" as r_17.
The internal name of r_17 is "closet".
The printed name of r_17 is "-= Closet =-".
The closet part 0 is some text that varies. The closet part 0 is "Well, here we are in a closet. Let's see what's in here.

 You can make out a chest.[if c_5 is open and there is something in the c_5] The chest contains [a list of things in the c_5].[end if]".
The closet part 1 is some text that varies. The closet part 1 is "[if c_5 is open and the c_5 contains nothing] The chest is empty, what a horrible day![end if]".
The closet part 2 is some text that varies. The closet part 2 is " You can make out [if c_6 is locked]a locked[else if c_6 is open]an opened[otherwise]a closed[end if]".
The closet part 3 is some text that varies. The closet part 3 is " safe.[if c_6 is open and there is something in the c_6] The safe contains [a list of things in the c_6].[end if]".
The closet part 4 is some text that varies. The closet part 4 is "[if c_6 is open and the c_6 contains nothing] The safe is empty! This is the worst thing that could possibly happen, ever![end if]".
The closet part 5 is some text that varies. The closet part 5 is "

 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The closet part 6 is some text that varies. The closet part 6 is " hatch leading east. There is [if d_3 is open]an open[otherwise]a closed[end if]".
The closet part 7 is some text that varies. The closet part 7 is " door leading south.".
The description of r_17 is "[closet part 0][closet part 1][closet part 2][closet part 3][closet part 4][closet part 5][closet part 6][closet part 7]".

south of r_17 and north of r_18 is a door called d_3.
east of r_17 and west of r_15 is a door called d_1.
Understand "dish-pit" as r_3.
The internal name of r_3 is "dish-pit".
The printed name of r_3 is "-= Dish-Pit =-".
The dish-pit part 0 is some text that varies. The dish-pit part 0 is "You're now in a dish-pit.

 You see a platter. [if there is something on the s_4]You see [a list of things on the s_4] on the platter. Hmmm... what else, what else?[end if]".
The dish-pit part 1 is some text that varies. The dish-pit part 1 is "[if there is nothing on the s_4]But there isn't a thing on it.[end if]".
The dish-pit part 2 is some text that varies. The dish-pit part 2 is "

There is an unguarded exit to the north. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_3 is "[dish-pit part 0][dish-pit part 1][dish-pit part 2]".

The r_2 is mapped west of r_3.
The r_4 is mapped north of r_3.
Understand "vault" as r_2.
The internal name of r_2 is "vault".
The printed name of r_2 is "-= Vault =-".
The vault part 0 is some text that varies. The vault part 0 is "You are in a vault. A typical kind of place.



There is an exit to the east. Don't worry, it is unguarded. You need an unblocked exit? You should try going north.".
The description of r_2 is "[vault part 0]".

The r_1 is mapped north of r_2.
The r_3 is mapped east of r_2.
Understand "basement" as r_4.
The internal name of r_4 is "basement".
The printed name of r_4 is "-= Basement =-".
The basement part 0 is some text that varies. The basement part 0 is "You arrive in a normal kind of place. That is to say, you're in a basement.



You need an unguarded exit? You should try going south. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_4 is "[basement part 0]".

The r_1 is mapped west of r_4.
The r_3 is mapped south of r_4.
Understand "restroom" as r_6.
The internal name of r_6 is "restroom".
The printed name of r_6 is "-= Restroom =-".
The restroom part 0 is some text that varies. The restroom part 0 is "You are in a restroom. A normal one. Let's see what's in here.

 You see a drawer.[if c_7 is open and there is something in the c_7] The drawer contains [a list of things in the c_7].[end if]".
The restroom part 1 is some text that varies. The restroom part 1 is "[if c_7 is open and the c_7 contains nothing] The drawer is empty, what a horrible day![end if]".
The restroom part 2 is some text that varies. The restroom part 2 is " You make out [if c_8 is locked]a locked[else if c_8 is open]an opened[otherwise]a closed[end if]".
The restroom part 3 is some text that varies. The restroom part 3 is " basket.[if c_8 is open and there is something in the c_8] The basket contains [a list of things in the c_8].[end if]".
The restroom part 4 is some text that varies. The restroom part 4 is "[if c_8 is open and the c_8 contains nothing] The basket is empty! What a waste of a day![end if]".
The restroom part 5 is some text that varies. The restroom part 5 is "

 There is [if d_6 is open]an open[otherwise]a closed[end if]".
The restroom part 6 is some text that varies. The restroom part 6 is " gateway leading north. There is [if d_7 is open]an open[otherwise]a closed[end if]".
The restroom part 7 is some text that varies. The restroom part 7 is " passageway leading west.".
The description of r_6 is "[restroom part 0][restroom part 1][restroom part 2][restroom part 3][restroom part 4][restroom part 5][restroom part 6][restroom part 7]".

west of r_6 and east of r_5 is a door called d_7.
north of r_6 and south of r_7 is a door called d_6.
Understand "office" as r_5.
The internal name of r_5 is "office".
The printed name of r_5 is "-= Office =-".
The office part 0 is some text that varies. The office part 0 is "You have entered an office. Not the office you'd expect. No, this is an office. Let's see what's in here.



 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The office part 1 is some text that varies. The office part 1 is " portal leading south. There is [if d_7 is open]an open[otherwise]a closed[end if]".
The office part 2 is some text that varies. The office part 2 is " passageway leading east.".
The description of r_5 is "[office part 0][office part 1][office part 2]".

south of r_5 and north of r_1 is a door called d_0.
east of r_5 and west of r_6 is a door called d_7.
Understand "study" as r_7.
The internal name of r_7 is "study".
The printed name of r_7 is "-= Study =-".
The study part 0 is some text that varies. The study part 0 is "You're now in the study. You start to take note of what's in the room.

 You make out [if c_10 is locked]a locked[else if c_10 is open]an opened[otherwise]a closed[end if]".
The study part 1 is some text that varies. The study part 1 is " portmanteau.[if c_10 is open and there is something in the c_10] The portmanteau contains [a list of things in the c_10].[end if]".
The study part 2 is some text that varies. The study part 2 is "[if c_10 is open and the c_10 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The study part 3 is some text that varies. The study part 3 is " As if things weren't amazing enough already, you can even see a suitcase. Classic TextWorld.[if c_9 is open and there is something in the c_9] The suitcase contains [a list of things in the c_9].[end if]".
The study part 4 is some text that varies. The study part 4 is "[if c_9 is open and the c_9 contains nothing] The suitcase is empty! What a waste of a day![end if]".
The study part 5 is some text that varies. The study part 5 is "

 There is [if d_6 is open]an open[otherwise]a closed[end if]".
The study part 6 is some text that varies. The study part 6 is " gateway leading south. There is [if d_5 is open]an open[otherwise]a closed[end if]".
The study part 7 is some text that varies. The study part 7 is " stone portal leading west.".
The description of r_7 is "[study part 0][study part 1][study part 2][study part 3][study part 4][study part 5][study part 6][study part 7]".

west of r_7 and east of r_8 is a door called d_5.
south of r_7 and north of r_6 is a door called d_6.
Understand "attic" as r_8.
The internal name of r_8 is "attic".
The printed name of r_8 is "-= Attic =-".
The attic part 0 is some text that varies. The attic part 0 is "You've just shown up in an attic.

 You rest your hand against a wall, but you miss the wall and fall onto a shelf. [if there is something on the s_5]You see [a list of things on the s_5] on the shelf. Now that's what I call TextWorld![end if]".
The attic part 1 is some text that varies. The attic part 1 is "[if there is nothing on the s_5]But there isn't a thing on it.[end if]".
The attic part 2 is some text that varies. The attic part 2 is "

 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The attic part 3 is some text that varies. The attic part 3 is " stone portal leading east. There is [if d_4 is open]an open[otherwise]a closed[end if]".
The attic part 4 is some text that varies. The attic part 4 is " stone passageway leading west.".
The description of r_8 is "[attic part 0][attic part 1][attic part 2][attic part 3][attic part 4]".

west of r_8 and east of r_9 is a door called d_4.
east of r_8 and west of r_7 is a door called d_5.
Understand "kitchen" as r_9.
The internal name of r_9 is "kitchen".
The printed name of r_9 is "-= Kitchen =-".
The kitchen part 0 is some text that varies. The kitchen part 0 is "You're now in the kitchen. The room is well lit.

 You hear a noise behind you and spin around, but you can't see anything other than a cabinet.[if c_11 is open and there is something in the c_11] The cabinet contains [a list of things in the c_11].[end if]".
The kitchen part 1 is some text that varies. The kitchen part 1 is "[if c_11 is open and the c_11 contains nothing] The cabinet is empty! This is the worst thing that could possibly happen, ever![end if]".
The kitchen part 2 is some text that varies. The kitchen part 2 is " You rest your hand against a wall, but you miss the wall and fall onto a freezer.[if c_12 is open and there is something in the c_12] The freezer contains [a list of things in the c_12]. I mean, just wow! Isn't TextWorld just the best?[end if]".
The kitchen part 3 is some text that varies. The kitchen part 3 is "[if c_12 is open and the c_12 contains nothing] The freezer is empty! What a waste of a day![end if]".
The kitchen part 4 is some text that varies. The kitchen part 4 is " You see a pan. The pan is typical.[if there is something on the s_6] On the pan you see [a list of things on the s_6].[end if]".
The kitchen part 5 is some text that varies. The kitchen part 5 is "[if there is nothing on the s_6] But the thing is empty.[end if]".
The kitchen part 6 is some text that varies. The kitchen part 6 is "

 There is [if d_4 is open]an open[otherwise]a closed[end if]".
The kitchen part 7 is some text that varies. The kitchen part 7 is " stone passageway leading east. You don't like doors? Why not try going south, that entranceway is unblocked. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_9 is "[kitchen part 0][kitchen part 1][kitchen part 2][kitchen part 3][kitchen part 4][kitchen part 5][kitchen part 6][kitchen part 7]".

The r_10 is mapped west of r_9.
The r_14 is mapped south of r_9.
east of r_9 and west of r_8 is a door called d_4.
Understand "studio" as r_16.
The internal name of r_16 is "studio".
The printed name of r_16 is "-= Studio =-".
The studio part 0 is some text that varies. The studio part 0 is "You've just walked into a studio.



There is an exit to the north. Don't worry, it is unguarded.".
The description of r_16 is "[studio part 0]".

The r_15 is mapped north of r_16.
Understand "austere study" as r_18.
The internal name of r_18 is "austere study".
The printed name of r_18 is "-= Austere Study =-".
The austere study part 0 is some text that varies. The austere study part 0 is "You have moved into the most austere of all possible studys. You decide to just list off a complete list of everything you see in the room, because hey, why not?



 There is [if d_3 is open]an open[otherwise]a closed[end if]".
The austere study part 1 is some text that varies. The austere study part 1 is " door leading north. You need an unblocked exit? You should try going south.".
The description of r_18 is "[austere study part 0][austere study part 1]".

The r_19 is mapped south of r_18.
north of r_18 and south of r_17 is a door called d_3.
Understand "austere office" as r_19.
The internal name of r_19 is "austere office".
The printed name of r_19 is "-= Austere Office =-".
The austere office part 0 is some text that varies. The austere office part 0 is "You've just sauntered into an austere office.



You don't like doors? Why not try going north, that entranceway is unblocked.".
The description of r_19 is "[austere office part 0]".

The r_18 is mapped north of r_19.

The c_0 and the c_1 and the c_10 and the c_11 and the c_12 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are containers.
The c_0 and the c_1 and the c_10 and the c_11 and the c_12 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are privately-named.
The d_0 and the d_2 and the d_1 and the d_3 and the d_7 and the d_6 and the d_5 and the d_4 are doors.
The d_0 and the d_2 and the d_1 and the d_3 and the d_7 and the d_6 and the d_5 and the d_4 are privately-named.
The f_0 and the f_1 are foods.
The f_0 and the f_1 are privately-named.
The r_1 and the r_0 and the r_10 and the r_11 and the r_12 and the r_13 and the r_14 and the r_15 and the r_17 and the r_3 and the r_2 and the r_4 and the r_6 and the r_5 and the r_7 and the r_8 and the r_9 and the r_16 and the r_18 and the r_19 are rooms.
The r_1 and the r_0 and the r_10 and the r_11 and the r_12 and the r_13 and the r_14 and the r_15 and the r_17 and the r_3 and the r_2 and the r_4 and the r_6 and the r_5 and the r_7 and the r_8 and the r_9 and the r_16 and the r_18 and the r_19 are privately-named.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 are supporters.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 are privately-named.

The description of d_0 is "it is what it is, a portal [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_0 is "portal".
Understand "portal" as d_0.
The d_0 is closed.
The description of d_2 is "it is what it is, a gate [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_2 is "gate".
Understand "gate" as d_2.
The d_2 is open.
The description of d_1 is "The hatch looks solid. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_1 is "hatch".
Understand "hatch" as d_1.
The d_1 is open.
The description of d_3 is "The door looks grand. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_3 is "door".
Understand "door" as d_3.
The d_3 is open.
The description of d_7 is "The passageway looks grand. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_7 is "passageway".
Understand "passageway" as d_7.
The d_7 is open.
The description of d_6 is "it is what it is, a gateway [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_6 is "gateway".
Understand "gateway" as d_6.
The d_6 is open.
The description of d_5 is "it is what it is, a stone portal [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_5 is "stone portal".
Understand "stone portal" as d_5.
Understand "stone" as d_5.
Understand "portal" as d_5.
The d_5 is open.
The description of d_4 is "it's a rugged passageway [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_4 is "stone passageway".
Understand "stone passageway" as d_4.
Understand "stone" as d_4.
Understand "passageway" as d_4.
The d_4 is open.
The description of c_0 is "The dresser looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_0 is "dresser".
Understand "dresser" as c_0.
The c_0 is in r_10.
The c_0 is open.
The description of c_1 is "The box looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_1 is "box".
Understand "box" as c_1.
The c_1 is in r_10.
The c_1 is closed.
The description of c_10 is "The portmanteau looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_10 is "portmanteau".
Understand "portmanteau" as c_10.
The c_10 is in r_7.
The c_10 is locked.
The description of c_11 is "The cabinet looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_11 is "cabinet".
Understand "cabinet" as c_11.
The c_11 is in r_9.
The c_11 is open.
The description of c_12 is "The freezer looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_12 is "freezer".
Understand "freezer" as c_12.
The c_12 is in r_9.
The c_12 is locked.
The description of c_2 is "The case looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_2 is "case".
Understand "case" as c_2.
The c_2 is in r_12.
The c_2 is open.
The description of c_3 is "The toolbox looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_3 is "toolbox".
Understand "toolbox" as c_3.
The c_3 is in r_13.
The c_3 is locked.
The description of c_4 is "The display looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_4 is "display".
Understand "display" as c_4.
The c_4 is in r_13.
The c_4 is closed.
The description of c_5 is "The chest looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_5 is "chest".
Understand "chest" as c_5.
The c_5 is in r_17.
The c_5 is open.
The description of c_6 is "The safe looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_6 is "safe".
Understand "safe" as c_6.
The c_6 is in r_17.
The c_6 is closed.
The description of c_7 is "The drawer looks strong, and impossible to destroy. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_7 is "drawer".
Understand "drawer" as c_7.
The c_7 is in r_6.
The c_7 is closed.
The description of c_8 is "The basket looks strong, and impossible to destroy. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_8 is "basket".
Understand "basket" as c_8.
The c_8 is in r_6.
The c_8 is locked.
The description of c_9 is "The suitcase looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_9 is "suitcase".
Understand "suitcase" as c_9.
The c_9 is in r_7.
The c_9 is locked.
The description of f_0 is "that's an ordinary broccoli!".
The printed name of f_0 is "broccoli".
Understand "broccoli" as f_0.
The f_0 is in r_3.
The description of f_1 is "that's an ordinary candy bar!".
The printed name of f_1 is "candy bar".
Understand "candy bar" as f_1.
Understand "candy" as f_1.
Understand "bar" as f_1.
The f_1 is in r_8.
The description of s_0 is "The armchair is undependable.".
The printed name of s_0 is "armchair".
Understand "armchair" as s_0.
The s_0 is in r_1.
The description of s_1 is "The desk is durable.".
The printed name of s_1 is "desk".
Understand "desk" as s_1.
The s_1 is in r_10.
The description of s_2 is "The bench is durable.".
The printed name of s_2 is "bench".
Understand "bench" as s_2.
The s_2 is in r_10.
The description of s_3 is "The counter is undependable.".
The printed name of s_3 is "counter".
Understand "counter" as s_3.
The s_3 is in r_12.
The description of s_4 is "The platter is balanced.".
The printed name of s_4 is "platter".
Understand "platter" as s_4.
The s_4 is in r_3.
The description of s_5 is "The shelf is reliable.".
The printed name of s_5 is "shelf".
Understand "shelf" as s_5.
The s_5 is in r_8.
The description of s_6 is "The pan is reliable.".
The printed name of s_6 is "pan".
Understand "pan" as s_6.
The s_6 is in r_9.


The player is in r_5.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "open portal / go south / go east / go south / take broccoli"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the f_1:
		end the story; [Lost]
	else if The player is in r_3 and The player carries the f_0:
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

The objective part 0 is some text that varies. The objective part 0 is "Who's got a virtual machine and is about to play through an exciting round of TextWorld? You do! Here is how to play! First of all, you could, like, ensure that the portal in the office is open. Then,".
The objective part 1 is some text that varies. The objective part 1 is " make an attempt to take a trip south. And then, attempt to take a trip east. And then, attempt to take a trip south. Then, retrieve the broccoli from the floor of the dish-pit. Once that's all handle".
The objective part 2 is some text that varies. The objective part 2 is "d, you can stop!".

An objective is some text that varies. The objective is "[objective part 0][objective part 1][objective part 2]".
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

