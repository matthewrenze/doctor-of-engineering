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


The r_0 and the r_1 and the r_3 and the r_10 and the r_9 and the r_11 and the r_13 and the r_12 and the r_14 and the r_16 and the r_4 and the r_19 and the r_18 and the r_2 and the r_15 and the r_5 and the r_6 and the r_7 and the r_8 and the r_17 are rooms.

Understand "basement" as r_0.
The internal name of r_0 is "basement".
The printed name of r_0 is "-= Basement =-".
The basement part 0 is some text that varies. The basement part 0 is "You find yourself in a basement. An usual kind of place.

 You can see [if c_0 is locked]a locked[else if c_0 is open]an opened[otherwise]a closed[end if]".
The basement part 1 is some text that varies. The basement part 1 is " locker.[if c_0 is open and there is something in the c_0] The locker contains [a list of things in the c_0].[end if]".
The basement part 2 is some text that varies. The basement part 2 is "[if c_0 is open and the c_0 contains nothing] The locker is empty, what a horrible day![end if]".
The basement part 3 is some text that varies. The basement part 3 is " Look out! It's a- oh, never mind, it's just a suitcase.[if c_1 is open and there is something in the c_1] The suitcase contains [a list of things in the c_1].[end if]".
The basement part 4 is some text that varies. The basement part 4 is "[if c_1 is open and the c_1 contains nothing] The suitcase is empty! This is the worst thing that could possibly happen, ever![end if]".
The basement part 5 is some text that varies. The basement part 5 is " Oh wow! Is that what I think it is? It is! It's a rack. [if there is something on the s_0]On the rack you can see [a list of things on the s_0]. Now that's what I call TextWorld![end if]".
The basement part 6 is some text that varies. The basement part 6 is "[if there is nothing on the s_0]However, the rack, like an empty rack, has nothing on it.[end if]".
The basement part 7 is some text that varies. The basement part 7 is "

You need an unguarded exit? You should try going north. There is an unguarded exit to the south. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_0 is "[basement part 0][basement part 1][basement part 2][basement part 3][basement part 4][basement part 5][basement part 6][basement part 7]".

The r_1 is mapped west of r_0.
The r_4 is mapped south of r_0.
The r_11 is mapped north of r_0.
Understand "workshop" as r_1.
The internal name of r_1 is "workshop".
The printed name of r_1 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "You find yourself in a workshop. A typical kind of place. You decide to just list off a complete list of everything you see in the room, because hey, why not?



You don't like doors? Why not try going east, that entranceway is unblocked. You need an unblocked exit? You should try going south. You need an unblocked exit? You should try going west.".
The description of r_1 is "[workshop part 0]".

The r_3 is mapped west of r_1.
The r_2 is mapped south of r_1.
The r_0 is mapped east of r_1.
Understand "canteen" as r_3.
The internal name of r_3 is "canteen".
The printed name of r_3 is "-= Canteen =-".
The canteen part 0 is some text that varies. The canteen part 0 is "Ah, the canteen. This is some kind of canteen, really great usual vibes in this place, a wonderful usual atmosphere.

 You can see [if c_2 is locked]a locked[else if c_2 is open]an opened[otherwise]a closed[end if]".
The canteen part 1 is some text that varies. The canteen part 1 is " refrigerator.[if c_2 is open and there is something in the c_2] The refrigerator contains [a list of things in the c_2]. There's something strange about this being here, but you can't put your finger on it.[end if]".
The canteen part 2 is some text that varies. The canteen part 2 is "[if c_2 is open and the c_2 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The canteen part 3 is some text that varies. The canteen part 3 is " You smell a pungent smell, and follow it to a counter. The counter is usual.[if there is something on the s_1] On the counter you make out [a list of things on the s_1]. Huh, weird.[end if]".
The canteen part 4 is some text that varies. The canteen part 4 is "[if there is nothing on the s_1] Looks like someone's already been here and taken everything off it, though.[end if]".
The canteen part 5 is some text that varies. The canteen part 5 is "

You need an unguarded exit? You should try going east. There is an unblocked exit to the north.".
The description of r_3 is "[canteen part 0][canteen part 1][canteen part 2][canteen part 3][canteen part 4][canteen part 5]".

The r_14 is mapped north of r_3.
The r_1 is mapped east of r_3.
Understand "cookhouse" as r_10.
The internal name of r_10 is "cookhouse".
The printed name of r_10 is "-= Cookhouse =-".
The cookhouse part 0 is some text that varies. The cookhouse part 0 is "Well, here we are in a cookhouse.



There is an exit to the west. Don't worry, it is unguarded.".
The description of r_10 is "[cookhouse part 0]".

The r_9 is mapped west of r_10.
Understand "salon" as r_9.
The internal name of r_9 is "salon".
The printed name of r_9 is "-= Salon =-".
The salon part 0 is some text that varies. The salon part 0 is "You arrive in a salon. An usual kind of place.



You need an unblocked exit? You should try going east. There is an unblocked exit to the north. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_9 is "[salon part 0]".

The r_8 is mapped west of r_9.
The r_6 is mapped north of r_9.
The r_10 is mapped east of r_9.
Understand "office" as r_11.
The internal name of r_11 is "office".
The printed name of r_11 is "-= Office =-".
The office part 0 is some text that varies. The office part 0 is "You've just sauntered into an office. You start to take note of what's in the room.

 You can make out [if c_3 is locked]a locked[else if c_3 is open]an opened[otherwise]a closed[end if]".
The office part 1 is some text that varies. The office part 1 is " box in the corner.[if c_3 is open and there is something in the c_3] The box contains [a list of things in the c_3].[end if]".
The office part 2 is some text that varies. The office part 2 is "[if c_3 is open and the c_3 contains nothing] The box is empty! This is the worst thing that could possibly happen, ever![end if]".
The office part 3 is some text that varies. The office part 3 is "

There is an exit to the east. Don't worry, it is unblocked. You don't like doors? Why not try going south, that entranceway is unguarded. There is an unguarded exit to the west.".
The description of r_11 is "[office part 0][office part 1][office part 2][office part 3]".

The r_13 is mapped west of r_11.
The r_0 is mapped south of r_11.
The r_12 is mapped east of r_11.
Understand "shower" as r_13.
The internal name of r_13 is "shower".
The printed name of r_13 is "-= Shower =-".
The shower part 0 is some text that varies. The shower part 0 is "You arrive in a shower. An ordinary kind of place.

 You can make out a shelf. The shelf is usual.[if there is something on the s_2] On the shelf you make out [a list of things on the s_2]. Something scurries by right in the corner of your eye. Probably nothing.[end if]".
The shower part 1 is some text that varies. The shower part 1 is "[if there is nothing on the s_2] But the thing hasn't got anything on it.[end if]".
The shower part 2 is some text that varies. The shower part 2 is "

There is an exit to the east. Don't worry, it is unguarded. There is an exit to the west. Don't worry, it is unblocked.".
The description of r_13 is "[shower part 0][shower part 1][shower part 2]".

The r_14 is mapped west of r_13.
The r_11 is mapped east of r_13.
Understand "closet" as r_12.
The internal name of r_12 is "closet".
The printed name of r_12 is "-= Closet =-".
The closet part 0 is some text that varies. The closet part 0 is "You've just shown up in a closet.



You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_12 is "[closet part 0]".

The r_11 is mapped west of r_12.
Understand "recreation zone" as r_14.
The internal name of r_14 is "recreation zone".
The printed name of r_14 is "-= Recreation Zone =-".
The recreation zone part 0 is some text that varies. The recreation zone part 0 is "You've just walked into a recreation zone.

 You can see a safe.[if c_4 is open and there is something in the c_4] The safe contains [a list of things in the c_4].[end if]".
The recreation zone part 1 is some text that varies. The recreation zone part 1 is "[if c_4 is open and the c_4 contains nothing] The safe is empty, what a horrible day![end if]".
The recreation zone part 2 is some text that varies. The recreation zone part 2 is " What's that over there? It looks like it's a basket. Hmm. You always thought you'd be more excited to see a basket in a room.[if c_5 is open and there is something in the c_5] The basket contains [a list of things in the c_5], so there's that.[end if]".
The recreation zone part 3 is some text that varies. The recreation zone part 3 is "[if c_5 is open and the c_5 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The recreation zone part 4 is some text that varies. The recreation zone part 4 is " You can make out a mantle. The mantle is typical.[if there is something on the s_3] On the mantle you can make out [a list of things on the s_3].[end if]".
The recreation zone part 5 is some text that varies. The recreation zone part 5 is "[if there is nothing on the s_3] Unfortunately, there isn't a thing on it. You make a mental note to not get your hopes up the next time you see a mantle in a room.[end if]".
The recreation zone part 6 is some text that varies. The recreation zone part 6 is "

There is an exit to the east. Don't worry, it is unguarded. You need an unblocked exit? You should try going south.".
The description of r_14 is "[recreation zone part 0][recreation zone part 1][recreation zone part 2][recreation zone part 3][recreation zone part 4][recreation zone part 5][recreation zone part 6]".

The r_3 is mapped south of r_14.
The r_13 is mapped east of r_14.
Understand "kitchen" as r_16.
The internal name of r_16 is "kitchen".
The printed name of r_16 is "-= Kitchen =-".
The kitchen part 0 is some text that varies. The kitchen part 0 is "You arrive in a kitchen. A standard kind of place. You decide to start listing off everything you see in the room, as if you were in a text adventure.

 You can make out a freezer.[if c_6 is open and there is something in the c_6] The freezer contains [a list of things in the c_6].[end if]".
The kitchen part 1 is some text that varies. The kitchen part 1 is "[if c_6 is open and the c_6 contains nothing] What a letdown! The freezer is empty![end if]".
The kitchen part 2 is some text that varies. The kitchen part 2 is " You make out [if c_7 is locked]a locked[else if c_7 is open]an opened[otherwise]a closed[end if]".
The kitchen part 3 is some text that varies. The kitchen part 3 is " case nearby.[if c_7 is open and there is something in the c_7] The case contains [a list of things in the c_7]. You check the price tag that hangs off the case. 70 bucks? What a deal! You'll have to ask where they got this![end if]".
The kitchen part 4 is some text that varies. The kitchen part 4 is "[if c_7 is open and the c_7 contains nothing] What a letdown! The case is empty![end if]".
The kitchen part 5 is some text that varies. The kitchen part 5 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The kitchen part 6 is some text that varies. The kitchen part 6 is " hatch leading west. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The kitchen part 7 is some text that varies. The kitchen part 7 is " passageway leading south.".
The description of r_16 is "[kitchen part 0][kitchen part 1][kitchen part 2][kitchen part 3][kitchen part 4][kitchen part 5][kitchen part 6][kitchen part 7]".

west of r_16 and east of r_4 is a door called d_2.
south of r_16 and north of r_17 is a door called d_1.
Understand "cookery" as r_4.
The internal name of r_4 is "cookery".
The printed name of r_4 is "-= Cookery =-".
The cookery part 0 is some text that varies. The cookery part 0 is "You're now in a cookery.

 Were you looking for a chest? Because look over there, it's a chest.[if c_8 is open and there is something in the c_8] The chest contains [a list of things in the c_8].[end if]".
The cookery part 1 is some text that varies. The cookery part 1 is "[if c_8 is open and the c_8 contains nothing] What a letdown! The chest is empty![end if]".
The cookery part 2 is some text that varies. The cookery part 2 is " You can see [if c_9 is locked]a locked[else if c_9 is open]an opened[otherwise]a closed[end if]".
The cookery part 3 is some text that varies. The cookery part 3 is " fancy looking freezer in the corner.[if c_9 is open and there is something in the c_9] The fancy freezer contains [a list of things in the c_9].[end if]".
The cookery part 4 is some text that varies. The cookery part 4 is "[if c_9 is open and the c_9 contains nothing] The freezer is empty! What a waste of a day![end if]".
The cookery part 5 is some text that varies. The cookery part 5 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The cookery part 6 is some text that varies. The cookery part 6 is " hatch leading east. You don't like doors? Why not try going north, that entranceway is unguarded. There is an exit to the south. Don't worry, it is unblocked. You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_4 is "[cookery part 0][cookery part 1][cookery part 2][cookery part 3][cookery part 4][cookery part 5][cookery part 6]".

The r_2 is mapped west of r_4.
The r_5 is mapped south of r_4.
The r_0 is mapped north of r_4.
east of r_4 and west of r_16 is a door called d_2.
Understand "bathroom" as r_19.
The internal name of r_19 is "bathroom".
The printed name of r_19 is "-= Bathroom =-".
The bathroom part 0 is some text that varies. The bathroom part 0 is "You've just shown up in a bathroom.

 You see a trunk.[if c_10 is open and there is something in the c_10] The trunk contains [a list of things in the c_10].[end if]".
The bathroom part 1 is some text that varies. The bathroom part 1 is "[if c_10 is open and the c_10 contains nothing] The trunk is empty! This is the worst thing that could possibly happen, ever![end if]".
The bathroom part 2 is some text that varies. The bathroom part 2 is "

You need an unguarded exit? You should try going west.".
The description of r_19 is "[bathroom part 0][bathroom part 1][bathroom part 2]".

The r_18 is mapped west of r_19.
Understand "spare room" as r_18.
The internal name of r_18 is "spare room".
The printed name of r_18 is "-= Spare Room =-".
The spare room part 0 is some text that varies. The spare room part 0 is "You are in a spare room. A normal one.



 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The spare room part 1 is some text that varies. The spare room part 1 is " door leading north. You need an unguarded exit? You should try going east.".
The description of r_18 is "[spare room part 0][spare room part 1]".

north of r_18 and south of r_17 is a door called d_0.
The r_19 is mapped east of r_18.
Understand "cubicle" as r_2.
The internal name of r_2 is "cubicle".
The printed name of r_2 is "-= Cubicle =-".
The cubicle part 0 is some text that varies. The cubicle part 0 is "You've just shown up in a cubicle. You start to take note of what's in the room.



There is an exit to the east. Don't worry, it is unguarded. There is an exit to the north. Don't worry, it is unblocked. There is an exit to the south. Don't worry, it is unblocked. You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_2 is "[cubicle part 0]".

The r_15 is mapped west of r_2.
The r_6 is mapped south of r_2.
The r_1 is mapped north of r_2.
The r_4 is mapped east of r_2.
Understand "studio" as r_15.
The internal name of r_15 is "studio".
The printed name of r_15 is "-= Studio =-".
The studio part 0 is some text that varies. The studio part 0 is "Guess what, you are in a place we're calling a studio. I guess you better just go and list everything you see here.

 As if things weren't amazing enough already, you can even see a cabinet.[if c_11 is open and there is something in the c_11] The cabinet contains [a list of things in the c_11].[end if]".
The studio part 1 is some text that varies. The studio part 1 is "[if c_11 is open and the c_11 contains nothing] The cabinet is empty! What a waste of a day![end if]".
The studio part 2 is some text that varies. The studio part 2 is "

You don't like doors? Why not try going east, that entranceway is unguarded. There is an exit to the south. Don't worry, it is unguarded.".
The description of r_15 is "[studio part 0][studio part 1][studio part 2]".

The r_7 is mapped south of r_15.
The r_2 is mapped east of r_15.
Understand "pantry" as r_5.
The internal name of r_5 is "pantry".
The printed name of r_5 is "-= Pantry =-".
The pantry part 0 is some text that varies. The pantry part 0 is "You've just sauntered into a pantry.

 You can make out [if c_12 is locked]a locked[else if c_12 is open]an opened[otherwise]a closed[end if]".
The pantry part 1 is some text that varies. The pantry part 1 is " display.[if c_12 is open and there is something in the c_12] The display contains [a list of things in the c_12].[end if]".
The pantry part 2 is some text that varies. The pantry part 2 is "[if c_12 is open and the c_12 contains nothing] What a letdown! The display is empty![end if]".
The pantry part 3 is some text that varies. The pantry part 3 is "

You don't like doors? Why not try going north, that entranceway is unguarded. There is an exit to the west. Don't worry, it is unblocked.".
The description of r_5 is "[pantry part 0][pantry part 1][pantry part 2][pantry part 3]".

The r_6 is mapped west of r_5.
The r_4 is mapped north of r_5.
Understand "study" as r_6.
The internal name of r_6 is "study".
The printed name of r_6 is "-= Study =-".
The study part 0 is some text that varies. The study part 0 is "I am sorry to announce that you are now in the study. You begin to take stock of what's here.

 You can see a mantelpiece. The mantelpiece is ordinary.[if there is something on the s_4] On the mantelpiece you see [a list of things on the s_4]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The study part 1 is some text that varies. The study part 1 is "[if there is nothing on the s_4] The mantelpiece appears to be empty.[end if]".
The study part 2 is some text that varies. The study part 2 is "

You need an unguarded exit? You should try going east. You don't like doors? Why not try going north, that entranceway is unblocked. You don't like doors? Why not try going south, that entranceway is unguarded. There is an exit to the west. Don't worry, it is unblocked.".
The description of r_6 is "[study part 0][study part 1][study part 2]".

The r_7 is mapped west of r_6.
The r_9 is mapped south of r_6.
The r_2 is mapped north of r_6.
The r_5 is mapped east of r_6.
Understand "scullery" as r_7.
The internal name of r_7 is "scullery".
The printed name of r_7 is "-= Scullery =-".
The scullery part 0 is some text that varies. The scullery part 0 is "I am required to announce that you are now in the scullery.

 You can make out [if c_13 is locked]a locked[else if c_13 is open]an opened[otherwise]a closed[end if]".
The scullery part 1 is some text that varies. The scullery part 1 is " fridge, which looks normal, right there by you.[if c_13 is open and there is something in the c_13] The fridge contains [a list of things in the c_13].[end if]".
The scullery part 2 is some text that varies. The scullery part 2 is "[if c_13 is open and the c_13 contains nothing] The fridge is empty, what a horrible day![end if]".
The scullery part 3 is some text that varies. The scullery part 3 is "

There is an unblocked exit to the east. There is an exit to the north. Don't worry, it is unblocked. There is an exit to the south. Don't worry, it is unblocked.".
The description of r_7 is "[scullery part 0][scullery part 1][scullery part 2][scullery part 3]".

The r_8 is mapped south of r_7.
The r_15 is mapped north of r_7.
The r_6 is mapped east of r_7.
Understand "launderette" as r_8.
The internal name of r_8 is "launderette".
The printed name of r_8 is "-= Launderette =-".
The launderette part 0 is some text that varies. The launderette part 0 is "You have fallen into a launderette. Not the launderette you'd expect. No, this is a launderette.

 [if c_14 is locked]A locked[else if c_14 is open]An open[otherwise]A closed[end if]".
The launderette part 1 is some text that varies. The launderette part 1 is " drawer is in the room.[if c_14 is open and there is something in the c_14] The drawer contains [a list of things in the c_14]. There's something strange about this being here, but you can't put your finger on it.[end if]".
The launderette part 2 is some text that varies. The launderette part 2 is "[if c_14 is open and the c_14 contains nothing] What a letdown! The drawer is empty![end if]".
The launderette part 3 is some text that varies. The launderette part 3 is "

There is an unblocked exit to the east. There is an unblocked exit to the north.".
The description of r_8 is "[launderette part 0][launderette part 1][launderette part 2][launderette part 3]".

The r_7 is mapped north of r_8.
The r_9 is mapped east of r_8.
Understand "serious office" as r_17.
The internal name of r_17 is "serious office".
The printed name of r_17 is "-= Serious Office =-".
The serious office part 0 is some text that varies. The serious office part 0 is "Well, here we are in the serious office.



 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The serious office part 1 is some text that varies. The serious office part 1 is " passageway leading north. There is [if d_0 is open]an open[otherwise]a closed[end if]".
The serious office part 2 is some text that varies. The serious office part 2 is " door leading south.".
The description of r_17 is "[serious office part 0][serious office part 1][serious office part 2]".

south of r_17 and north of r_18 is a door called d_0.
north of r_17 and south of r_16 is a door called d_1.

The c_0 and the c_1 and the c_10 and the c_11 and the c_12 and the c_13 and the c_14 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are containers.
The c_0 and the c_1 and the c_10 and the c_11 and the c_12 and the c_13 and the c_14 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are privately-named.
The d_1 and the d_2 and the d_0 are doors.
The d_1 and the d_2 and the d_0 are privately-named.
The f_0 are foods.
The f_0 are privately-named.
The k_0 and the k_1 are keys.
The k_0 and the k_1 are privately-named.
The r_0 and the r_1 and the r_3 and the r_10 and the r_9 and the r_11 and the r_13 and the r_12 and the r_14 and the r_16 and the r_4 and the r_19 and the r_18 and the r_2 and the r_15 and the r_5 and the r_6 and the r_7 and the r_8 and the r_17 are rooms.
The r_0 and the r_1 and the r_3 and the r_10 and the r_9 and the r_11 and the r_13 and the r_12 and the r_14 and the r_16 and the r_4 and the r_19 and the r_18 and the r_2 and the r_15 and the r_5 and the r_6 and the r_7 and the r_8 and the r_17 are privately-named.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 are supporters.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 are privately-named.

The description of d_1 is "it's a noble passageway [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_1 is "passageway".
Understand "passageway" as d_1.
The d_1 is open.
The description of d_2 is "it's a stuffy hatch [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_2 is "hatch".
Understand "hatch" as d_2.
The d_2 is locked.
The description of d_0 is "it is what it is, a door [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_0 is "door".
Understand "door" as d_0.
The d_0 is open.
The description of c_0 is "The locker looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_0 is "locker".
Understand "locker" as c_0.
The c_0 is in r_0.
The c_0 is open.
The description of c_1 is "The suitcase looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_1 is "suitcase".
Understand "suitcase" as c_1.
The c_1 is in r_0.
The c_1 is locked.
The description of c_10 is "The trunk looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_10 is "trunk".
Understand "trunk" as c_10.
The c_10 is in r_19.
The c_10 is closed.
The description of c_11 is "The cabinet looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_11 is "cabinet".
Understand "cabinet" as c_11.
The c_11 is in r_15.
The c_11 is open.
The description of c_12 is "The display looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_12 is "display".
Understand "display" as c_12.
The c_12 is in r_5.
The c_12 is open.
The description of c_13 is "The fridge looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_13 is "fridge".
Understand "fridge" as c_13.
The c_13 is in r_7.
The c_13 is closed.
The description of c_14 is "The drawer looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_14 is "drawer".
Understand "drawer" as c_14.
The c_14 is in r_8.
The c_14 is open.
The description of c_2 is "The refrigerator looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_2 is "refrigerator".
Understand "refrigerator" as c_2.
The c_2 is in r_3.
The c_2 is open.
The description of c_3 is "The box looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_3 is "box".
Understand "box" as c_3.
The c_3 is in r_11.
The c_3 is locked.
The description of c_4 is "The safe looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_4 is "safe".
Understand "safe" as c_4.
The c_4 is in r_14.
The c_4 is locked.
The description of c_5 is "The basket looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_5 is "basket".
Understand "basket" as c_5.
The c_5 is in r_14.
The c_5 is closed.
The description of c_6 is "The freezer looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_6 is "freezer".
Understand "freezer" as c_6.
The c_6 is in r_16.
The c_6 is open.
The description of c_7 is "The case looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_7 is "case".
Understand "case" as c_7.
The c_7 is in r_16.
The c_7 is locked.
The description of c_8 is "The chest looks strong, and impossible to destroy. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_8 is "chest".
Understand "chest" as c_8.
The c_8 is in r_4.
The c_8 is open.
The description of c_9 is "The fancy freezer looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_9 is "fancy freezer".
Understand "fancy freezer" as c_9.
Understand "fancy" as c_9.
Understand "freezer" as c_9.
The c_9 is in r_4.
The c_9 is closed.
The description of k_0 is "The metal of the latchkey is satin.".
The printed name of k_0 is "latchkey".
Understand "latchkey" as k_0.
The k_0 is in r_19.
The description of k_1 is "The keycard is cold to the touch".
The printed name of k_1 is "keycard".
Understand "keycard" as k_1.
The k_1 is in r_4.
The matching key of the d_2 is the k_1.
The description of s_0 is "The rack is an unstable piece of junk.".
The printed name of s_0 is "rack".
Understand "rack" as s_0.
The s_0 is in r_0.
The description of s_1 is "The counter is balanced.".
The printed name of s_1 is "counter".
Understand "counter" as s_1.
The s_1 is in r_3.
The description of s_2 is "The shelf is wobbly.".
The printed name of s_2 is "shelf".
Understand "shelf" as s_2.
The s_2 is in r_13.
The description of s_3 is "The mantle is wobbly.".
The printed name of s_3 is "mantle".
Understand "mantle" as s_3.
The s_3 is in r_14.
The description of s_4 is "The mantelpiece is wobbly.".
The printed name of s_4 is "mantelpiece".
Understand "mantelpiece" as s_4.
The s_4 is in r_6.
The description of f_0 is "The fondue looks delicious.".
The printed name of f_0 is "fondue".
Understand "fondue" as f_0.
The f_0 is in the c_0.


The player is in r_14.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "go east / go east / go south / go west / go south / go west / go south / go east / go east / go north / take keycard / unlock hatch with keycard / open hatch / go east / go south / go south / go east / take latchkey"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the f_0:
		end the story; [Lost]
	else if The player is in r_19 and The player carries the k_0:
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

The objective part 0 is some text that varies. The objective part 0 is "It's time to explore the amazing world of TextWorld! First off, if it's not too much trouble, I need you to move east. That done, try to go east. Once you get around to doing that, attempt to take a t".
The objective part 1 is some text that varies. The objective part 1 is "rip south. Once you succeed at that, make an effort to move west. Once you do that, attempt to go south. Once you manage that, move west. Following that, try to go south. After that, travel east. If y".
The objective part 2 is some text that varies. The objective part 2 is "ou can get around to doing that, make an effort to go east. Then, venture north. And then, pick up the keycard from the floor of the cookery. After taking the keycard, unlock the hatch with the keycar".
The objective part 3 is some text that varies. The objective part 3 is "d. After that, open the hatch inside the cookery. Then, try to take a trip east. And then, attempt to take a trip south. And then, venture south. And then, attempt to go to the east. With that over wi".
The objective part 4 is some text that varies. The objective part 4 is "th, recover the latchkey from the floor of the bathroom. Once that's all handled, you can stop!".

An objective is some text that varies. The objective is "[objective part 0][objective part 1][objective part 2][objective part 3][objective part 4]".
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

