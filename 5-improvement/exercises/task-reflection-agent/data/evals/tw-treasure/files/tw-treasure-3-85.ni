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


The r_0 and the r_12 and the r_1 and the r_10 and the r_11 and the r_14 and the r_13 and the r_15 and the r_17 and the r_19 and the r_2 and the r_3 and the r_4 and the r_7 and the r_8 and the r_9 and the r_16 and the r_18 and the r_5 and the r_6 are rooms.

Understand "bedroom" as r_0.
The internal name of r_0 is "bedroom".
The printed name of r_0 is "-= Bedroom =-".
The bedroom part 0 is some text that varies. The bedroom part 0 is "Well I'll be, you are in the place we're calling the bedroom. The room seems oddly familiar, as though it were only superficially different from the other rooms in the building.

 You see [if c_0 is locked]a locked[else if c_0 is open]an opened[otherwise]a closed[end if]".
The bedroom part 1 is some text that varies. The bedroom part 1 is " locker.[if c_0 is open and there is something in the c_0] The locker contains [a list of things in the c_0]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The bedroom part 2 is some text that varies. The bedroom part 2 is "[if c_0 is open and the c_0 contains nothing] What a letdown! The locker is empty![end if]".
The bedroom part 3 is some text that varies. The bedroom part 3 is "

You need an unblocked exit? You should try going east. There is an exit to the west. Don't worry, it is unblocked.".
The description of r_0 is "[bedroom part 0][bedroom part 1][bedroom part 2][bedroom part 3]".

The r_12 is mapped west of r_0.
The r_1 is mapped east of r_0.
Understand "vault" as r_12.
The internal name of r_12 is "vault".
The printed name of r_12 is "-= Vault =-".
The vault part 0 is some text that varies. The vault part 0 is "Look at you, bigshot, walking into a vault like it isn't some huge deal. You can barely contain your excitement.



You need an unblocked exit? You should try going east. You don't like doors? Why not try going north, that entranceway is unblocked. You need an unblocked exit? You should try going west.".
The description of r_12 is "[vault part 0]".

The r_13 is mapped west of r_12.
The r_11 is mapped north of r_12.
The r_0 is mapped east of r_12.
Understand "recreation zone" as r_1.
The internal name of r_1 is "recreation zone".
The printed name of r_1 is "-= Recreation Zone =-".
The recreation zone part 0 is some text that varies. The recreation zone part 0 is "You find yourself in a recreation zone. A typical kind of place.

 You see a bed stand. [if there is something on the s_0]On the bed stand you can see [a list of things on the s_0].[end if]".
The recreation zone part 1 is some text that varies. The recreation zone part 1 is "[if there is nothing on the s_0]Looks like someone's already been here and taken everything off it, though. You make a mental note to not get your hopes up the next time you see a bed stand in a room.[end if]".
The recreation zone part 2 is some text that varies. The recreation zone part 2 is "

There is an unblocked exit to the east. There is an exit to the north. Don't worry, it is unguarded. You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_1 is "[recreation zone part 0][recreation zone part 1][recreation zone part 2]".

The r_0 is mapped west of r_1.
The r_2 is mapped north of r_1.
The r_4 is mapped east of r_1.
Understand "cubicle" as r_10.
The internal name of r_10 is "cubicle".
The printed name of r_10 is "-= Cubicle =-".
The cubicle part 0 is some text that varies. The cubicle part 0 is "Well, here we are in the cubicle.



 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The cubicle part 1 is some text that varies. The cubicle part 1 is " TextWorld portal leading north. There is an exit to the east. Don't worry, it is unguarded. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_10 is "[cubicle part 0][cubicle part 1]".

The r_11 is mapped west of r_10.
north of r_10 and south of r_15 is a door called d_5.
The r_2 is mapped east of r_10.
Understand "office" as r_11.
The internal name of r_11 is "office".
The printed name of r_11 is "-= Office =-".
The office part 0 is some text that varies. The office part 0 is "You find yourself in an office. A normal kind of place. The room seems oddly familiar, as though it were only superficially different from the other rooms in the building.

 You can see [if c_1 is locked]a locked[else if c_1 is open]an opened[otherwise]a closed[end if]".
The office part 1 is some text that varies. The office part 1 is " toolbox here.[if c_1 is open and there is something in the c_1] The toolbox contains [a list of things in the c_1].[end if]".
The office part 2 is some text that varies. The office part 2 is "[if c_1 is open and the c_1 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The office part 3 is some text that varies. The office part 3 is "

There is an unguarded exit to the east. There is an unguarded exit to the south. There is an exit to the west. Don't worry, it is unblocked.".
The description of r_11 is "[office part 0][office part 1][office part 2][office part 3]".

The r_14 is mapped west of r_11.
The r_12 is mapped south of r_11.
The r_10 is mapped east of r_11.
Understand "basement" as r_14.
The internal name of r_14 is "basement".
The printed name of r_14 is "-= Basement =-".
The basement part 0 is some text that varies. The basement part 0 is "Well, here we are in a basement. I guess you better just go and list everything you see here.



You need an unguarded exit? You should try going east. You don't like doors? Why not try going south, that entranceway is unguarded.".
The description of r_14 is "[basement part 0]".

The r_13 is mapped south of r_14.
The r_11 is mapped east of r_14.
Understand "dish-pit" as r_13.
The internal name of r_13 is "dish-pit".
The printed name of r_13 is "-= Dish-Pit =-".
The dish-pit part 0 is some text that varies. The dish-pit part 0 is "You arrive in a dish-pit. An ordinary one.

 You can see a bowl. [if there is something on the s_1]You see [a list of things on the s_1] on the bowl.[end if]".
The dish-pit part 1 is some text that varies. The dish-pit part 1 is "[if there is nothing on the s_1]But the thing is empty.[end if]".
The dish-pit part 2 is some text that varies. The dish-pit part 2 is " You can make out a shelf. Wow, isn't TextWorld just the best? [if there is something on the s_2]On the shelf you see [a list of things on the s_2].[end if]".
The dish-pit part 3 is some text that varies. The dish-pit part 3 is "[if there is nothing on the s_2]But the thing is empty.[end if]".
The dish-pit part 4 is some text that varies. The dish-pit part 4 is "

There is an unguarded exit to the east. You need an unblocked exit? You should try going north.".
The description of r_13 is "[dish-pit part 0][dish-pit part 1][dish-pit part 2][dish-pit part 3][dish-pit part 4]".

The r_14 is mapped north of r_13.
The r_12 is mapped east of r_13.
Understand "closet" as r_15.
The internal name of r_15 is "closet".
The printed name of r_15 is "-= Closet =-".
The closet part 0 is some text that varies. The closet part 0 is "Well I'll be, you are in the place we're calling the closet.

 Oh, great. Here's a cabinet. There's something strange about this being here, but you can't put your finger on it.[if c_2 is open and there is something in the c_2] The cabinet contains [a list of things in the c_2].[end if]".
The closet part 1 is some text that varies. The closet part 1 is "[if c_2 is open and the c_2 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The closet part 2 is some text that varies. The closet part 2 is " You can make out a table. [if there is something on the s_3]On the table you see [a list of things on the s_3]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The closet part 3 is some text that varies. The closet part 3 is "[if there is nothing on the s_3]But the thing is empty, unfortunately.[end if]".
The closet part 4 is some text that varies. The closet part 4 is "

 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The closet part 5 is some text that varies. The closet part 5 is " TextWorld portal leading south. There is [if d_4 is open]an open[otherwise]a closed[end if]".
The closet part 6 is some text that varies. The closet part 6 is " hatch leading west. You need an unguarded exit? You should try going north.".
The description of r_15 is "[closet part 0][closet part 1][closet part 2][closet part 3][closet part 4][closet part 5][closet part 6]".

west of r_15 and east of r_17 is a door called d_4.
south of r_15 and north of r_10 is a door called d_5.
The r_16 is mapped north of r_15.
Understand "bedchamber" as r_17.
The internal name of r_17 is "bedchamber".
The printed name of r_17 is "-= Bedchamber =-".
The bedchamber part 0 is some text that varies. The bedchamber part 0 is "You find yourself in a bedchamber. A normal one.



 There is [if d_4 is open]an open[otherwise]a closed[end if]".
The bedchamber part 1 is some text that varies. The bedchamber part 1 is " hatch leading east. There is an unguarded exit to the north. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_17 is "[bedchamber part 0][bedchamber part 1]".

The r_19 is mapped west of r_17.
The r_18 is mapped north of r_17.
east of r_17 and west of r_15 is a door called d_4.
Understand "workshop" as r_19.
The internal name of r_19 is "workshop".
The printed name of r_19 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "Ah, the workshop. This is some kind of workshop, really great usual vibes in this place, a wonderful usual atmosphere. The room is well lit.

 You make out a chair. The chair is standard.[if there is something on the s_4] On the chair you can make out [a list of things on the s_4]. You shudder, but continue examining the room.[end if]".
The workshop part 1 is some text that varies. The workshop part 1 is "[if there is nothing on the s_4] Looks like someone's already been here and taken everything off it, though.[end if]".
The workshop part 2 is some text that varies. The workshop part 2 is " You see a stand. The stand is usual.[if there is something on the s_5] On the stand you make out [a list of things on the s_5].[end if]".
The workshop part 3 is some text that varies. The workshop part 3 is "[if there is nothing on the s_5] However, the stand, like an empty stand, has nothing on it. It would have been so cool if there was stuff on the stand.[end if]".
The workshop part 4 is some text that varies. The workshop part 4 is "

There is an unblocked exit to the east.".
The description of r_19 is "[workshop part 0][workshop part 1][workshop part 2][workshop part 3][workshop part 4]".

The r_17 is mapped east of r_19.
Understand "canteen" as r_2.
The internal name of r_2 is "canteen".
The printed name of r_2 is "-= Canteen =-".
The canteen part 0 is some text that varies. The canteen part 0 is "Ah, the canteen. This is some kind of canteen, really great standard vibes in this place, a wonderful standard atmosphere. And now, well, you're in it. You can barely contain your excitement.

 You can see [if c_3 is locked]a locked[else if c_3 is open]an opened[otherwise]a closed[end if]".
The canteen part 1 is some text that varies. The canteen part 1 is " refrigerator nearby.[if c_3 is open and there is something in the c_3] The refrigerator contains [a list of things in the c_3].[end if]".
The canteen part 2 is some text that varies. The canteen part 2 is "[if c_3 is open and the c_3 contains nothing] The refrigerator is empty! This is the worst thing that could possibly happen, ever![end if]".
The canteen part 3 is some text that varies. The canteen part 3 is "

You don't like doors? Why not try going east, that entranceway is unguarded. There is an unguarded exit to the south. There is an unblocked exit to the west.".
The description of r_2 is "[canteen part 0][canteen part 1][canteen part 2][canteen part 3]".

The r_10 is mapped west of r_2.
The r_1 is mapped south of r_2.
The r_3 is mapped east of r_2.
Understand "study" as r_3.
The internal name of r_3 is "study".
The printed name of r_3 is "-= Study =-".
The study part 0 is some text that varies. The study part 0 is "You've just shown up in a study.

 Oh wow! Is that what I think it is? It is! It's an armchair. [if there is something on the s_6]You see [a list of things on the s_6] on the armchair. Wow! Just like in the movies![end if]".
The study part 1 is some text that varies. The study part 1 is "[if there is nothing on the s_6]But oh no! there's nothing on this piece of junk.[end if]".
The study part 2 is some text that varies. The study part 2 is "

 There is [if d_3 is open]an open[otherwise]a closed[end if]".
The study part 3 is some text that varies. The study part 3 is " gateway leading north. There is an exit to the south. Don't worry, it is unblocked. There is an unblocked exit to the west.".
The description of r_3 is "[study part 0][study part 1][study part 2][study part 3]".

The r_2 is mapped west of r_3.
The r_4 is mapped south of r_3.
north of r_3 and south of r_5 is a door called d_3.
Understand "kitchenette" as r_4.
The internal name of r_4 is "kitchenette".
The printed name of r_4 is "-= Kitchenette =-".
The kitchenette part 0 is some text that varies. The kitchenette part 0 is "Look at you, bigshot, walking into a kitchenette like it isn't some huge deal.

 You can see [if c_4 is locked]a locked[else if c_4 is open]an opened[otherwise]a closed[end if]".
The kitchenette part 1 is some text that varies. The kitchenette part 1 is " case in the corner.[if c_4 is open and there is something in the c_4] The case contains [a list of things in the c_4]. Suddenly, you bump your head on the ceiling, but it's not such a bad bump that it's going to prevent you from looking at objects and even things.[end if]".
The kitchenette part 2 is some text that varies. The kitchenette part 2 is "[if c_4 is open and the c_4 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The kitchenette part 3 is some text that varies. The kitchenette part 3 is " You can make out a board. The board is usual.[if there is something on the s_7] On the board you can make out [a list of things on the s_7].[end if]".
The kitchenette part 4 is some text that varies. The kitchenette part 4 is "[if there is nothing on the s_7] Unfortunately, there isn't a thing on it.[end if]".
The kitchenette part 5 is some text that varies. The kitchenette part 5 is " You make out a plate. The plate is usual.[if there is something on the s_8] On the plate you make out [a list of things on the s_8].[end if]".
The kitchenette part 6 is some text that varies. The kitchenette part 6 is "[if there is nothing on the s_8] The plate appears to be empty.[end if]".
The kitchenette part 7 is some text that varies. The kitchenette part 7 is "

There is an unblocked exit to the north. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_4 is "[kitchenette part 0][kitchenette part 1][kitchenette part 2][kitchenette part 3][kitchenette part 4][kitchenette part 5][kitchenette part 6][kitchenette part 7]".

The r_1 is mapped west of r_4.
The r_3 is mapped north of r_4.
Understand "washroom" as r_7.
The internal name of r_7 is "washroom".
The printed name of r_7 is "-= Washroom =-".
The washroom part 0 is some text that varies. The washroom part 0 is "You are in a washroom.



 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The washroom part 1 is some text that varies. The washroom part 1 is " door leading south. There is [if d_0 is open]an open[otherwise]a closed[end if]".
The washroom part 2 is some text that varies. The washroom part 2 is " passageway leading west.".
The description of r_7 is "[washroom part 0][washroom part 1][washroom part 2]".

west of r_7 and east of r_8 is a door called d_0.
south of r_7 and north of r_6 is a door called d_1.
Understand "spare room" as r_8.
The internal name of r_8 is "spare room".
The printed name of r_8 is "-= Spare Room =-".
The spare room part 0 is some text that varies. The spare room part 0 is "You find yourself in a spare room. An usual one.



 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The spare room part 1 is some text that varies. The spare room part 1 is " passageway leading east. There is an unblocked exit to the west.".
The description of r_8 is "[spare room part 0][spare room part 1]".

The r_9 is mapped west of r_8.
east of r_8 and west of r_7 is a door called d_0.
Understand "parlor" as r_9.
The internal name of r_9 is "parlor".
The printed name of r_9 is "-= Parlor =-".
The parlor part 0 is some text that varies. The parlor part 0 is "You've entered a parlor. You begin looking for stuff.

 Oh, great. Here's a mantelpiece. [if there is something on the s_9]You see [a list of things on the s_9] on the mantelpiece.[end if]".
The parlor part 1 is some text that varies. The parlor part 1 is "[if there is nothing on the s_9]However, the mantelpiece, like an empty mantelpiece, has nothing on it. Hm. Oh well[end if]".
The parlor part 2 is some text that varies. The parlor part 2 is "

There is an exit to the east. Don't worry, it is unguarded.".
The description of r_9 is "[parlor part 0][parlor part 1][parlor part 2]".

The r_8 is mapped east of r_9.
Understand "pantry" as r_16.
The internal name of r_16 is "pantry".
The printed name of r_16 is "-= Pantry =-".
The pantry part 0 is some text that varies. The pantry part 0 is "You arrive in a pantry. An ordinary kind of place.



There is an unguarded exit to the south.".
The description of r_16 is "[pantry part 0]".

The r_15 is mapped south of r_16.
Understand "cellar" as r_18.
The internal name of r_18 is "cellar".
The printed name of r_18 is "-= Cellar =-".
The cellar part 0 is some text that varies. The cellar part 0 is "You've seen better cellars, but at least this one seems pretty ordinary.

 You can see [if c_5 is locked]a locked[else if c_5 is open]an opened[otherwise]a closed[end if]".
The cellar part 1 is some text that varies. The cellar part 1 is " box.[if c_5 is open and there is something in the c_5] The box contains [a list of things in the c_5].[end if]".
The cellar part 2 is some text that varies. The cellar part 2 is "[if c_5 is open and the c_5 contains nothing] What a letdown! The box is empty![end if]".
The cellar part 3 is some text that varies. The cellar part 3 is " You see a counter. You wonder idly who left that here. [if there is something on the s_10]On the counter you make out [a list of things on the s_10].[end if]".
The cellar part 4 is some text that varies. The cellar part 4 is "[if there is nothing on the s_10]But the thing is empty.[end if]".
The cellar part 5 is some text that varies. The cellar part 5 is "

There is an unblocked exit to the south.".
The description of r_18 is "[cellar part 0][cellar part 1][cellar part 2][cellar part 3][cellar part 4][cellar part 5]".

The r_17 is mapped south of r_18.
Understand "lounge" as r_5.
The internal name of r_5 is "lounge".
The printed name of r_5 is "-= Lounge =-".
The lounge part 0 is some text that varies. The lounge part 0 is "You've just shown up in a lounge.

 You see a bar. You shudder, but continue examining the bar. The bar is standard.[if there is something on the s_11] On the bar you see [a list of things on the s_11].[end if]".
The lounge part 1 is some text that varies. The lounge part 1 is "[if there is nothing on the s_11] But there isn't a thing on it. Hm. Oh well[end if]".
The lounge part 2 is some text that varies. The lounge part 2 is " You scan the room, seeing a mantle. The mantle is usual.[if there is something on the s_12] On the mantle you see [a list of things on the s_12].[end if]".
The lounge part 3 is some text that varies. The lounge part 3 is "[if there is nothing on the s_12] Unfortunately, there isn't a thing on it.[end if]".
The lounge part 4 is some text that varies. The lounge part 4 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The lounge part 5 is some text that varies. The lounge part 5 is " gate leading north. There is [if d_3 is open]an open[otherwise]a closed[end if]".
The lounge part 6 is some text that varies. The lounge part 6 is " gateway leading south.".
The description of r_5 is "[lounge part 0][lounge part 1][lounge part 2][lounge part 3][lounge part 4][lounge part 5][lounge part 6]".

south of r_5 and north of r_3 is a door called d_3.
north of r_5 and south of r_6 is a door called d_2.
Understand "studio" as r_6.
The internal name of r_6 is "studio".
The printed name of r_6 is "-= Studio =-".
The studio part 0 is some text that varies. The studio part 0 is "You are in a studio. An ordinary one.

 You see a bookshelf. [if there is something on the s_13]You see [a list of things on the s_13] on the bookshelf. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The studio part 1 is some text that varies. The studio part 1 is "[if there is nothing on the s_13]But the thing is empty.[end if]".
The studio part 2 is some text that varies. The studio part 2 is "

 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The studio part 3 is some text that varies. The studio part 3 is " door leading north. There is [if d_2 is open]an open[otherwise]a closed[end if]".
The studio part 4 is some text that varies. The studio part 4 is " gate leading south.".
The description of r_6 is "[studio part 0][studio part 1][studio part 2][studio part 3][studio part 4]".

south of r_6 and north of r_5 is a door called d_2.
north of r_6 and south of r_7 is a door called d_1.

The c_0 and the c_1 and the c_2 and the c_3 and the c_4 and the c_5 are containers.
The c_0 and the c_1 and the c_2 and the c_3 and the c_4 and the c_5 are privately-named.
The d_5 and the d_4 and the d_3 and the d_2 and the d_1 and the d_0 are doors.
The d_5 and the d_4 and the d_3 and the d_2 and the d_1 and the d_0 are privately-named.
The f_0 are foods.
The f_0 are privately-named.
The k_1 and the k_3 and the k_2 and the k_0 are keys.
The k_1 and the k_3 and the k_2 and the k_0 are privately-named.
The r_0 and the r_12 and the r_1 and the r_10 and the r_11 and the r_14 and the r_13 and the r_15 and the r_17 and the r_19 and the r_2 and the r_3 and the r_4 and the r_7 and the r_8 and the r_9 and the r_16 and the r_18 and the r_5 and the r_6 are rooms.
The r_0 and the r_12 and the r_1 and the r_10 and the r_11 and the r_14 and the r_13 and the r_15 and the r_17 and the r_19 and the r_2 and the r_3 and the r_4 and the r_7 and the r_8 and the r_9 and the r_16 and the r_18 and the r_5 and the r_6 are privately-named.
The s_0 and the s_1 and the s_10 and the s_11 and the s_12 and the s_13 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 and the s_8 and the s_9 are supporters.
The s_0 and the s_1 and the s_10 and the s_11 and the s_12 and the s_13 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 and the s_8 and the s_9 are privately-named.

The description of d_5 is "it's a sturdy TextWorld portal [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_5 is "TextWorld portal".
Understand "TextWorld portal" as d_5.
Understand "TextWorld" as d_5.
Understand "portal" as d_5.
The d_5 is locked.
The description of d_4 is "The hatch looks solid. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_4 is "hatch".
Understand "hatch" as d_4.
The d_4 is locked.
The description of d_3 is "The gateway looks imposing. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_3 is "gateway".
Understand "gateway" as d_3.
The d_3 is open.
The description of d_2 is "it's a towering gate [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_2 is "gate".
Understand "gate" as d_2.
The d_2 is open.
The description of d_1 is "it's a sturdy door [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_1 is "door".
Understand "door" as d_1.
The d_1 is open.
The description of d_0 is "The passageway looks imposing. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_0 is "passageway".
Understand "passageway" as d_0.
The d_0 is open.
The description of c_0 is "The locker looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_0 is "locker".
Understand "locker" as c_0.
The c_0 is in r_0.
The c_0 is closed.
The description of c_1 is "The toolbox looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_1 is "toolbox".
Understand "toolbox" as c_1.
The c_1 is in r_11.
The c_1 is open.
The description of c_2 is "The cabinet looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_2 is "cabinet".
Understand "cabinet" as c_2.
The c_2 is in r_15.
The c_2 is locked.
The description of c_3 is "The refrigerator looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_3 is "refrigerator".
Understand "refrigerator" as c_3.
The c_3 is in r_2.
The c_3 is closed.
The description of c_4 is "The case looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_4 is "case".
Understand "case" as c_4.
The c_4 is in r_4.
The c_4 is open.
The description of c_5 is "The box looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_5 is "box".
Understand "box" as c_5.
The c_5 is in r_18.
The c_5 is locked.
The description of k_1 is "The TextWorld keycard is surprisingly heavy.".
The printed name of k_1 is "TextWorld keycard".
Understand "TextWorld keycard" as k_1.
Understand "TextWorld" as k_1.
Understand "keycard" as k_1.
The k_1 is in r_15.
The matching key of the d_5 is the k_1.
The description of k_3 is "The metal of the keycard is satin.".
The printed name of k_3 is "keycard".
Understand "keycard" as k_3.
The k_3 is in r_19.
The matching key of the c_5 is the k_3.
The description of s_0 is "The bed stand is solid.".
The printed name of s_0 is "bed stand".
Understand "bed stand" as s_0.
Understand "bed" as s_0.
Understand "stand" as s_0.
The s_0 is in r_1.
The description of s_1 is "The bowl is shaky.".
The printed name of s_1 is "bowl".
Understand "bowl" as s_1.
The s_1 is in r_13.
The description of s_10 is "The counter is unstable.".
The printed name of s_10 is "counter".
Understand "counter" as s_10.
The s_10 is in r_18.
The description of s_11 is "The bar is wobbly.".
The printed name of s_11 is "bar".
Understand "bar" as s_11.
The s_11 is in r_5.
The description of s_12 is "The mantle is shaky.".
The printed name of s_12 is "mantle".
Understand "mantle" as s_12.
The s_12 is in r_5.
The description of s_13 is "The bookshelf is wobbly.".
The printed name of s_13 is "bookshelf".
Understand "bookshelf" as s_13.
The s_13 is in r_6.
The description of s_2 is "The shelf is solid.".
The printed name of s_2 is "shelf".
Understand "shelf" as s_2.
The s_2 is in r_13.
The description of s_3 is "The table is stable.".
The printed name of s_3 is "table".
Understand "table" as s_3.
The s_3 is in r_15.
The description of s_4 is "The chair is solidly built.".
The printed name of s_4 is "chair".
Understand "chair" as s_4.
The s_4 is in r_19.
The description of s_5 is "The stand is durable.".
The printed name of s_5 is "stand".
Understand "stand" as s_5.
The s_5 is in r_19.
The description of s_6 is "The armchair is unstable.".
The printed name of s_6 is "armchair".
Understand "armchair" as s_6.
The s_6 is in r_3.
The description of s_7 is "The board is shaky.".
The printed name of s_7 is "board".
Understand "board" as s_7.
The s_7 is in r_4.
The description of s_8 is "The plate is reliable.".
The printed name of s_8 is "plate".
Understand "plate" as s_8.
The s_8 is in r_4.
The description of s_9 is "The mantelpiece is solidly built.".
The printed name of s_9 is "mantelpiece".
Understand "mantelpiece" as s_9.
The s_9 is in r_9.
The description of k_2 is "The passkey is cold to the touch".
The printed name of k_2 is "passkey".
Understand "passkey" as k_2.
The k_2 is in the c_5.
The matching key of the d_4 is the k_2.
The description of f_0 is "You couldn't pay me to eat that normal thing.".
The printed name of f_0 is "coconut".
Understand "coconut" as f_0.
The f_0 is on the s_8.
The description of k_0 is "The latchkey is cold to the touch".
The printed name of k_0 is "latchkey".
Understand "latchkey" as k_0.
The k_0 is on the s_6.


The player is in r_17.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "go west / take keycard / go east / go north / unlock box with keycard / open box / take passkey from box / go south / unlock hatch with passkey / open hatch / go east / take TextWorld keycard / unlock TextWorld portal with TextWorld keycard / open TextWorld portal / go south / go east / go east / take latchkey from armchair"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the f_0:
		end the story; [Lost]
	else if The player is in r_3 and The s_6 is in r_3 and The player carries the k_0:
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

The objective part 0 is some text that varies. The objective part 0 is "Who's got a virtual machine and is about to play through an exciting round of TextWorld? You do! Your first objective is to venture west. With that over with, lift the keycard from the floor of the wo".
The objective part 1 is some text that varies. The objective part 1 is "rkshop. If you can get your hands on the keycard, make an effort to venture east. Then, take a trip north. Okay, and then, assure that the box is unlocked with the keycard. Then, ensure that the box i".
The objective part 2 is some text that varies. The objective part 2 is "s open. Then, retrieve the passkey from the box. And then, go to the south. After that, unlock the hatch. After unlocking the hatch, open the hatch inside the bedchamber. And then, go to the east. Wit".
The objective part 3 is some text that varies. The objective part 3 is "h that done, retrieve the TextWorld keycard from the floor of the closet. And then, check that the TextWorld portal within the closet is unlocked with the TextWorld keycard. Then, assure that the Text".
The objective part 4 is some text that varies. The objective part 4 is "World portal in the closet is ajar. And then, try to travel south. That done, move east. Then, attempt to head east. If you can accomplish that, recover the latchkey from the armchair. Alright, thanks".
The objective part 5 is some text that varies. The objective part 5 is "!".

An objective is some text that varies. The objective is "[objective part 0][objective part 1][objective part 2][objective part 3][objective part 4][objective part 5]".
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

