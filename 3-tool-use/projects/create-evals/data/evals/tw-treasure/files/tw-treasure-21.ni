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


The r_0 and the r_1 and the r_11 and the r_13 and the r_18 and the r_14 and the r_17 and the r_15 and the r_16 and the r_19 and the r_2 and the r_3 and the r_6 and the r_7 and the r_8 and the r_9 and the r_10 and the r_12 and the r_4 and the r_5 are rooms.

Understand "kitchen" as r_0.
The internal name of r_0 is "kitchen".
The printed name of r_0 is "-= Kitchen =-".
The kitchen part 0 is some text that varies. The kitchen part 0 is "You have fallen into a kitchen. Not the kitchen you'd expect. No, this is a kitchen. You begin to take stock of what's in the room.



There is an unblocked exit to the east. You need an unguarded exit? You should try going north. You need an unguarded exit? You should try going west.".
The description of r_0 is "[kitchen part 0]".

The r_1 is mapped west of r_0.
The r_6 is mapped north of r_0.
The r_11 is mapped east of r_0.
Understand "canteen" as r_1.
The internal name of r_1 is "canteen".
The printed name of r_1 is "-= Canteen =-".
The canteen part 0 is some text that varies. The canteen part 0 is "Well I'll be, you are in a place we're calling a canteen.

 You see [if c_0 is locked]a locked[else if c_0 is open]an opened[otherwise]a closed[end if]".
The canteen part 1 is some text that varies. The canteen part 1 is " freezer.[if c_0 is open and there is something in the c_0] The freezer contains [a list of things in the c_0].[end if]".
The canteen part 2 is some text that varies. The canteen part 2 is "[if c_0 is open and the c_0 contains nothing] The freezer is empty! This is the worst thing that could possibly happen, ever![end if]".
The canteen part 3 is some text that varies. The canteen part 3 is " [if c_1 is locked]A locked[else if c_1 is open]An open[otherwise]A closed[end if]".
The canteen part 4 is some text that varies. The canteen part 4 is " ordinary looking refrigerator is close by.[if c_1 is open and there is something in the c_1] The refrigerator contains [a list of things in the c_1]. Classic TextWorld.[end if]".
The canteen part 5 is some text that varies. The canteen part 5 is "[if c_1 is open and the c_1 contains nothing] What a letdown! The refrigerator is empty![end if]".
The canteen part 6 is some text that varies. The canteen part 6 is "

There is an unguarded exit to the east. There is an unguarded exit to the north.".
The description of r_1 is "[canteen part 0][canteen part 1][canteen part 2][canteen part 3][canteen part 4][canteen part 5][canteen part 6]".

The r_2 is mapped north of r_1.
The r_0 is mapped east of r_1.
Understand "closet" as r_11.
The internal name of r_11 is "closet".
The printed name of r_11 is "-= Closet =-".
The closet part 0 is some text that varies. The closet part 0 is "Look around you. Take it all in. It's not every day someone gets to be in a closet. You start to take note of what's in the room.

 You lean against the wall, inadvertently pressing a secret button. The wall opens up to reveal a crate. Something scurries by right in the corner of your eye. Probably nothing.[if c_2 is open and there is something in the c_2] The crate contains [a list of things in the c_2].[end if]".
The closet part 1 is some text that varies. The closet part 1 is "[if c_2 is open and the c_2 contains nothing] What a letdown! The crate is empty![end if]".
The closet part 2 is some text that varies. The closet part 2 is " You can make out a workbench. The workbench is typical.[if there is something on the s_0] On the workbench you can make out [a list of things on the s_0]. Now that's what I call TextWorld![end if]".
The closet part 3 is some text that varies. The closet part 3 is "[if there is nothing on the s_0] But the thing is empty, unfortunately. Aw, here you were, all excited for there to be things on it![end if]".
The closet part 4 is some text that varies. The closet part 4 is "

You need an unblocked exit? You should try going east. You need an unguarded exit? You should try going west.".
The description of r_11 is "[closet part 0][closet part 1][closet part 2][closet part 3][closet part 4]".

The r_0 is mapped west of r_11.
The r_9 is mapped east of r_11.
Understand "sauna" as r_13.
The internal name of r_13 is "sauna".
The printed name of r_13 is "-= Sauna =-".
The sauna part 0 is some text that varies. The sauna part 0 is "Well, here we are in a sauna. You decide to start listing off everything you see in the room, as if you were in a text adventure.

 You make out a basket.[if c_3 is open and there is something in the c_3] The basket contains [a list of things in the c_3]. I mean, just wow! Isn't TextWorld just the best?[end if]".
The sauna part 1 is some text that varies. The sauna part 1 is "[if c_3 is open and the c_3 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The sauna part 2 is some text that varies. The sauna part 2 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The sauna part 3 is some text that varies. The sauna part 3 is " gate leading south. You don't like doors? Why not try going east, that entranceway is unblocked. There is an exit to the north. Don't worry, it is unguarded. There is an unguarded exit to the west.".
The description of r_13 is "[sauna part 0][sauna part 1][sauna part 2][sauna part 3]".

The r_18 is mapped west of r_13.
south of r_13 and north of r_12 is a door called d_2.
The r_14 is mapped north of r_13.
The r_16 is mapped east of r_13.
Understand "shower" as r_18.
The internal name of r_18 is "shower".
The printed name of r_18 is "-= Shower =-".
The shower part 0 is some text that varies. The shower part 0 is "You've entered a shower.

 You lean against the wall, inadvertently pressing a secret button. The wall opens up to reveal a safe.[if c_4 is open and there is something in the c_4] The safe contains [a list of things in the c_4].[end if]".
The shower part 1 is some text that varies. The shower part 1 is "[if c_4 is open and the c_4 contains nothing] The safe is empty! This is the worst thing that could possibly happen, ever![end if]".
The shower part 2 is some text that varies. The shower part 2 is " You hear a noise behind you and spin around, but you can't see anything other than a shelf. The shelf is normal.[if there is something on the s_1] On the shelf you see [a list of things on the s_1].[end if]".
The shower part 3 is some text that varies. The shower part 3 is "[if there is nothing on the s_1] But there isn't a thing on it.[end if]".
The shower part 4 is some text that varies. The shower part 4 is "

There is an exit to the east. Don't worry, it is unguarded. There is an unguarded exit to the north.".
The description of r_18 is "[shower part 0][shower part 1][shower part 2][shower part 3][shower part 4]".

The r_17 is mapped north of r_18.
The r_13 is mapped east of r_18.
Understand "workshop" as r_14.
The internal name of r_14 is "workshop".
The printed name of r_14 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "Well, here we are in the workshop. Okay, just remember what you're here to do, and everything will go great.



You don't like doors? Why not try going east, that entranceway is unguarded. There is an unblocked exit to the south. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_14 is "[workshop part 0]".

The r_17 is mapped west of r_14.
The r_13 is mapped south of r_14.
The r_15 is mapped east of r_14.
Understand "study" as r_17.
The internal name of r_17 is "study".
The printed name of r_17 is "-= Study =-".
The study part 0 is some text that varies. The study part 0 is "Okay, so you're in a study, cool, but is it ordinary? You better believe it is.

 Look out! It's a- oh, never mind, it's just a desk. The desk is standard.[if there is something on the s_2] On the desk you can make out [a list of things on the s_2].[end if]".
The study part 1 is some text that varies. The study part 1 is "[if there is nothing on the s_2] But there isn't a thing on it.[end if]".
The study part 2 is some text that varies. The study part 2 is "

There is an unblocked exit to the east. There is an unguarded exit to the south.".
The description of r_17 is "[study part 0][study part 1][study part 2]".

The r_18 is mapped south of r_17.
The r_14 is mapped east of r_17.
Understand "salon" as r_15.
The internal name of r_15 is "salon".
The printed name of r_15 is "-= Salon =-".
The salon part 0 is some text that varies. The salon part 0 is "You find yourself in a salon. An ordinary one.

 [if c_5 is locked]A locked[else if c_5 is open]An open[otherwise]A closed[end if]".
The salon part 1 is some text that varies. The salon part 1 is " dresser is here.[if c_5 is open and there is something in the c_5] The dresser contains [a list of things in the c_5]. There's something strange about this being here, but you can't put your finger on it.[end if]".
The salon part 2 is some text that varies. The salon part 2 is "[if c_5 is open and the c_5 contains nothing] What a letdown! The dresser is empty![end if]".
The salon part 3 is some text that varies. The salon part 3 is "

You need an unguarded exit? You should try going east. There is an unblocked exit to the south. There is an unguarded exit to the west.".
The description of r_15 is "[salon part 0][salon part 1][salon part 2][salon part 3]".

The r_14 is mapped west of r_15.
The r_16 is mapped south of r_15.
The r_19 is mapped east of r_15.
Understand "cookhouse" as r_16.
The internal name of r_16 is "cookhouse".
The printed name of r_16 is "-= Cookhouse =-".
The cookhouse part 0 is some text that varies. The cookhouse part 0 is "You've entered a cookhouse.

 You make out [if c_6 is locked]a locked[else if c_6 is open]an opened[otherwise]a closed[end if]".
The cookhouse part 1 is some text that varies. The cookhouse part 1 is " cabinet.[if c_6 is open and there is something in the c_6] The cabinet contains [a list of things in the c_6].[end if]".
The cookhouse part 2 is some text that varies. The cookhouse part 2 is "[if c_6 is open and the c_6 contains nothing] The cabinet is empty, what a horrible day![end if]".
The cookhouse part 3 is some text that varies. The cookhouse part 3 is "

There is an unguarded exit to the north. There is an unguarded exit to the west.".
The description of r_16 is "[cookhouse part 0][cookhouse part 1][cookhouse part 2][cookhouse part 3]".

The r_13 is mapped west of r_16.
The r_15 is mapped north of r_16.
Understand "chamber" as r_19.
The internal name of r_19 is "chamber".
The printed name of r_19 is "-= Chamber =-".
The chamber part 0 is some text that varies. The chamber part 0 is "You've entered a chamber. The room seems oddly familiar, as though it were only superficially different from the other rooms in the building.



You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_19 is "[chamber part 0]".

The r_15 is mapped west of r_19.
Understand "scullery" as r_2.
The internal name of r_2 is "scullery".
The printed name of r_2 is "-= Scullery =-".
The scullery part 0 is some text that varies. The scullery part 0 is "Well, here we are in the scullery.

 You see a fridge.[if c_7 is open and there is something in the c_7] The fridge contains [a list of things in the c_7].[end if]".
The scullery part 1 is some text that varies. The scullery part 1 is "[if c_7 is open and the c_7 contains nothing] What a letdown! The fridge is empty![end if]".
The scullery part 2 is some text that varies. The scullery part 2 is " You see a bowl. [if there is something on the s_3]You see [a list of things on the s_3] on the bowl. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The scullery part 3 is some text that varies. The scullery part 3 is "[if there is nothing on the s_3]But oh no! there's nothing on this piece of trash.[end if]".
The scullery part 4 is some text that varies. The scullery part 4 is "

 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The scullery part 5 is some text that varies. The scullery part 5 is " portal leading north. There is [if d_0 is open]an open[otherwise]a closed[end if]".
The scullery part 6 is some text that varies. The scullery part 6 is " hatch leading west. There is an unguarded exit to the east. You need an unguarded exit? You should try going south.".
The description of r_2 is "[scullery part 0][scullery part 1][scullery part 2][scullery part 3][scullery part 4][scullery part 5][scullery part 6]".

west of r_2 and east of r_3 is a door called d_0.
The r_1 is mapped south of r_2.
north of r_2 and south of r_12 is a door called d_1.
The r_6 is mapped east of r_2.
Understand "cookery" as r_3.
The internal name of r_3 is "cookery".
The printed name of r_3 is "-= Cookery =-".
The cookery part 0 is some text that varies. The cookery part 0 is "You arrive in a cookery. An ordinary kind of place. I guess you better just go and list everything you see here.

 You see a counter. [if there is something on the s_4]On the counter you see [a list of things on the s_4].[end if]".
The cookery part 1 is some text that varies. The cookery part 1 is "[if there is nothing on the s_4]However, the counter, like an empty counter, has nothing on it.[end if]".
The cookery part 2 is some text that varies. The cookery part 2 is "

 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The cookery part 3 is some text that varies. The cookery part 3 is " hatch leading east. You don't like doors? Why not try going north, that entranceway is unblocked. You need an unblocked exit? You should try going south.".
The description of r_3 is "[cookery part 0][cookery part 1][cookery part 2][cookery part 3]".

The r_4 is mapped south of r_3.
The r_5 is mapped north of r_3.
east of r_3 and west of r_2 is a door called d_0.
Understand "spare room" as r_6.
The internal name of r_6 is "spare room".
The printed name of r_6 is "-= Spare Room =-".
The spare room part 0 is some text that varies. The spare room part 0 is "You are in a spare room. A typical kind of place.

 Were you looking for a trunk? Because look over there, it's a trunk.[if c_8 is open and there is something in the c_8] The trunk contains [a list of things in the c_8].[end if]".
The spare room part 1 is some text that varies. The spare room part 1 is "[if c_8 is open and the c_8 contains nothing] What a letdown! The trunk is empty![end if]".
The spare room part 2 is some text that varies. The spare room part 2 is " What's that over there? It looks like it's a table. The table is normal.[if there is something on the s_5] On the table you can make out [a list of things on the s_5]. You idly wonder how they came up with the name TextWorld for this place. It's pretty fitting.[end if]".
The spare room part 3 is some text that varies. The spare room part 3 is "[if there is nothing on the s_5] But the thing is empty. Hopefully this doesn't make you too upset.[end if]".
The spare room part 4 is some text that varies. The spare room part 4 is "

You don't like doors? Why not try going east, that entranceway is unguarded. You don't like doors? Why not try going south, that entranceway is unguarded. You need an unblocked exit? You should try going west.".
The description of r_6 is "[spare room part 0][spare room part 1][spare room part 2][spare room part 3][spare room part 4]".

The r_2 is mapped west of r_6.
The r_0 is mapped south of r_6.
The r_7 is mapped east of r_6.
Understand "launderette" as r_7.
The internal name of r_7 is "launderette".
The printed name of r_7 is "-= Launderette =-".
The launderette part 0 is some text that varies. The launderette part 0 is "Well, here we are in a launderette.

 You see [if c_9 is locked]a locked[else if c_9 is open]an opened[otherwise]a closed[end if]".
The launderette part 1 is some text that varies. The launderette part 1 is " drawer in the room.[if c_9 is open and there is something in the c_9] The drawer contains [a list of things in the c_9].[end if]".
The launderette part 2 is some text that varies. The launderette part 2 is "[if c_9 is open and the c_9 contains nothing] The drawer is empty! This is the worst thing that could possibly happen, ever![end if]".
The launderette part 3 is some text that varies. The launderette part 3 is " You smell an interesting smell, and follow it to a bench. [if there is something on the s_6]On the bench you see [a list of things on the s_6].[end if]".
The launderette part 4 is some text that varies. The launderette part 4 is "[if there is nothing on the s_6]Looks like someone's already been here and taken everything off it, though. Aw, here you were, all excited for there to be things on it![end if]".
The launderette part 5 is some text that varies. The launderette part 5 is "

You need an unguarded exit? You should try going east. There is an unblocked exit to the west.".
The description of r_7 is "[launderette part 0][launderette part 1][launderette part 2][launderette part 3][launderette part 4][launderette part 5]".

The r_6 is mapped west of r_7.
The r_8 is mapped east of r_7.
Understand "bar" as r_8.
The internal name of r_8 is "bar".
The printed name of r_8 is "-= Bar =-".
The bar part 0 is some text that varies. The bar part 0 is "You've entered a bar. You decide to start listing off everything you see in the room, as if you were in a text adventure.



There is an unblocked exit to the north. You need an unguarded exit? You should try going south. You need an unguarded exit? You should try going west.".
The description of r_8 is "[bar part 0]".

The r_7 is mapped west of r_8.
The r_9 is mapped south of r_8.
The r_10 is mapped north of r_8.
Understand "kitchenette" as r_9.
The internal name of r_9 is "kitchenette".
The printed name of r_9 is "-= Kitchenette =-".
The kitchenette part 0 is some text that varies. The kitchenette part 0 is "You have walked into the most usual of all possible kitchenettes.

 You see a case. You can't wait to tell the folks at home about this![if c_10 is open and there is something in the c_10] The case contains [a list of things in the c_10].[end if]".
The kitchenette part 1 is some text that varies. The kitchenette part 1 is "[if c_10 is open and the c_10 contains nothing] The case is empty! What a waste of a day![end if]".
The kitchenette part 2 is some text that varies. The kitchenette part 2 is "

You need an unguarded exit? You should try going north. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_9 is "[kitchenette part 0][kitchenette part 1][kitchenette part 2]".

The r_11 is mapped west of r_9.
The r_8 is mapped north of r_9.
Understand "laundromat" as r_10.
The internal name of r_10 is "laundromat".
The printed name of r_10 is "-= Laundromat =-".
The laundromat part 0 is some text that varies. The laundromat part 0 is "You've just sauntered into a laundromat.



You need an unguarded exit? You should try going south.".
The description of r_10 is "[laundromat part 0]".

The r_8 is mapped south of r_10.
Understand "steam room" as r_12.
The internal name of r_12 is "steam room".
The printed name of r_12 is "-= Steam Room =-".
The steam room part 0 is some text that varies. The steam room part 0 is "You find yourself in a steam room.



 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The steam room part 1 is some text that varies. The steam room part 1 is " gate leading north. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The steam room part 2 is some text that varies. The steam room part 2 is " portal leading south.".
The description of r_12 is "[steam room part 0][steam room part 1][steam room part 2]".

south of r_12 and north of r_2 is a door called d_1.
north of r_12 and south of r_13 is a door called d_2.
Understand "vault" as r_4.
The internal name of r_4 is "vault".
The printed name of r_4 is "-= Vault =-".
The vault part 0 is some text that varies. The vault part 0 is "You're now in the vault.

 You can make out a rack. The rack is standard.[if there is something on the s_7] On the rack you can see [a list of things on the s_7].[end if]".
The vault part 1 is some text that varies. The vault part 1 is "[if there is nothing on the s_7] But there isn't a thing on it.[end if]".
The vault part 2 is some text that varies. The vault part 2 is "

There is an exit to the north. Don't worry, it is unguarded.".
The description of r_4 is "[vault part 0][vault part 1][vault part 2]".

The r_3 is mapped north of r_4.
Understand "basement" as r_5.
The internal name of r_5 is "basement".
The printed name of r_5 is "-= Basement =-".
The basement part 0 is some text that varies. The basement part 0 is "You've just shown up in a basement.

 You see [if c_11 is locked]a locked[else if c_11 is open]an opened[otherwise]a closed[end if]".
The basement part 1 is some text that varies. The basement part 1 is " toolbox.[if c_11 is open and there is something in the c_11] The toolbox contains [a list of things in the c_11].[end if]".
The basement part 2 is some text that varies. The basement part 2 is "[if c_11 is open and the c_11 contains nothing] The toolbox is empty! What a waste of a day![end if]".
The basement part 3 is some text that varies. The basement part 3 is "

You don't like doors? Why not try going south, that entranceway is unguarded.".
The description of r_5 is "[basement part 0][basement part 1][basement part 2][basement part 3]".

The r_3 is mapped south of r_5.

The c_0 and the c_1 and the c_10 and the c_11 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are containers.
The c_0 and the c_1 and the c_10 and the c_11 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are privately-named.
The d_1 and the d_2 and the d_0 are doors.
The d_1 and the d_2 and the d_0 are privately-named.
The k_0 and the k_1 are keys.
The k_0 and the k_1 are privately-named.
The r_0 and the r_1 and the r_11 and the r_13 and the r_18 and the r_14 and the r_17 and the r_15 and the r_16 and the r_19 and the r_2 and the r_3 and the r_6 and the r_7 and the r_8 and the r_9 and the r_10 and the r_12 and the r_4 and the r_5 are rooms.
The r_0 and the r_1 and the r_11 and the r_13 and the r_18 and the r_14 and the r_17 and the r_15 and the r_16 and the r_19 and the r_2 and the r_3 and the r_6 and the r_7 and the r_8 and the r_9 and the r_10 and the r_12 and the r_4 and the r_5 are privately-named.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 are supporters.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 are privately-named.

The description of d_1 is "The portal looks manageable. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_1 is "portal".
Understand "portal" as d_1.
The d_1 is open.
The description of d_2 is "The gate looks commanding. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_2 is "gate".
Understand "gate" as d_2.
The d_2 is open.
The description of d_0 is "it is what it is, a hatch [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_0 is "hatch".
Understand "hatch" as d_0.
The d_0 is open.
The description of c_0 is "The freezer looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_0 is "freezer".
Understand "freezer" as c_0.
The c_0 is in r_1.
The c_0 is open.
The description of c_1 is "The refrigerator looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_1 is "refrigerator".
Understand "refrigerator" as c_1.
The c_1 is in r_1.
The c_1 is closed.
The description of c_10 is "The case looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_10 is "case".
Understand "case" as c_10.
The c_10 is in r_9.
The c_10 is closed.
The description of c_11 is "The toolbox looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_11 is "toolbox".
Understand "toolbox" as c_11.
The c_11 is in r_5.
The c_11 is open.
The description of c_2 is "The crate looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_2 is "crate".
Understand "crate" as c_2.
The c_2 is in r_11.
The c_2 is open.
The description of c_3 is "The basket looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_3 is "basket".
Understand "basket" as c_3.
The c_3 is in r_13.
The c_3 is closed.
The description of c_4 is "The safe looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_4 is "safe".
Understand "safe" as c_4.
The c_4 is in r_18.
The c_4 is closed.
The description of c_5 is "The dresser looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_5 is "dresser".
Understand "dresser" as c_5.
The c_5 is in r_15.
The c_5 is open.
The description of c_6 is "The cabinet looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_6 is "cabinet".
Understand "cabinet" as c_6.
The c_6 is in r_16.
The c_6 is closed.
The description of c_7 is "The fridge looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_7 is "fridge".
Understand "fridge" as c_7.
The c_7 is in r_2.
The c_7 is locked.
The description of c_8 is "The trunk looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_8 is "trunk".
Understand "trunk" as c_8.
The c_8 is in r_6.
The c_8 is closed.
The description of c_9 is "The drawer looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_9 is "drawer".
Understand "drawer" as c_9.
The c_9 is in r_7.
The c_9 is locked.
The description of k_0 is "The key is surprisingly heavy.".
The printed name of k_0 is "key".
Understand "key" as k_0.
The k_0 is in r_1.
The description of k_1 is "The latchkey is cold to the touch".
The printed name of k_1 is "latchkey".
Understand "latchkey" as k_1.
The k_1 is in r_13.
The description of s_0 is "The workbench is an unstable piece of trash.".
The printed name of s_0 is "workbench".
Understand "workbench" as s_0.
The s_0 is in r_11.
The description of s_1 is "The shelf is reliable.".
The printed name of s_1 is "shelf".
Understand "shelf" as s_1.
The s_1 is in r_18.
The description of s_2 is "The desk is unstable.".
The printed name of s_2 is "desk".
Understand "desk" as s_2.
The s_2 is in r_17.
The description of s_3 is "The bowl is wobbly.".
The printed name of s_3 is "bowl".
Understand "bowl" as s_3.
The s_3 is in r_2.
The description of s_4 is "The counter is shaky.".
The printed name of s_4 is "counter".
Understand "counter" as s_4.
The s_4 is in r_3.
The description of s_5 is "The table is undependable.".
The printed name of s_5 is "table".
Understand "table" as s_5.
The s_5 is in r_6.
The description of s_6 is "The bench is shaky.".
The printed name of s_6 is "bench".
Understand "bench" as s_6.
The s_6 is in r_7.
The description of s_7 is "The rack is shaky.".
The printed name of s_7 is "rack".
Understand "rack" as s_7.
The s_7 is in r_4.


The player is in r_14.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "go south / go south / go south / go south / take key"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the k_1:
		end the story; [Lost]
	else if The player is in r_1 and The player carries the k_0:
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

The objective part 0 is some text that varies. The objective part 0 is "It's time to explore the amazing world of TextWorld! Here is your task for today. First off, if it's not too much trouble, I need you to take a trip south. After that, try to go to the south. After th".
The objective part 1 is some text that varies. The objective part 1 is "at, go to the south. Once you manage that, head south. And then, pick-up the key from the floor of the canteen. Alright, thanks!".

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

