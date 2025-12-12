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


The r_10 and the r_11 and the r_12 and the r_13 and the r_14 and the r_15 and the r_16 and the r_17 and the r_19 and the r_18 and the r_2 and the r_1 and the r_3 and the r_5 and the r_4 and the r_7 and the r_6 and the r_9 and the r_0 and the r_8 are rooms.

Understand "steam room" as r_10.
The internal name of r_10 is "steam room".
The printed name of r_10 is "-= Steam Room =-".
The steam room part 0 is some text that varies. The steam room part 0 is "You've entered a steam room.

 You make out [if c_0 is locked]a locked[else if c_0 is open]an opened[otherwise]a closed[end if]".
The steam room part 1 is some text that varies. The steam room part 1 is " dresser.[if c_0 is open and there is something in the c_0] The dresser contains [a list of things in the c_0].[end if]".
The steam room part 2 is some text that varies. The steam room part 2 is "[if c_0 is open and the c_0 contains nothing] The dresser is empty! What a waste of a day![end if]".
The steam room part 3 is some text that varies. The steam room part 3 is " You can see [if c_1 is locked]a locked[else if c_1 is open]an opened[otherwise]a closed[end if]".
The steam room part 4 is some text that varies. The steam room part 4 is " trunk.[if c_1 is open and there is something in the c_1] The trunk contains [a list of things in the c_1].[end if]".
The steam room part 5 is some text that varies. The steam room part 5 is "[if c_1 is open and the c_1 contains nothing] The trunk is empty! What a waste of a day![end if]".
The steam room part 6 is some text that varies. The steam room part 6 is " You can make out a table. I guess it's true what they say, if you're looking for a table, go to TextWorld. The table is usual.[if there is something on the s_0] On the table you can see [a list of things on the s_0]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The steam room part 7 is some text that varies. The steam room part 7 is "[if there is nothing on the s_0] But the thing hasn't got anything on it.[end if]".
The steam room part 8 is some text that varies. The steam room part 8 is "

 There is [if d_3 is open]an open[otherwise]a closed[end if]".
The steam room part 9 is some text that varies. The steam room part 9 is " gate leading east. You need an unblocked exit? You should try going south. You need an unblocked exit? You should try going west.".
The description of r_10 is "[steam room part 0][steam room part 1][steam room part 2][steam room part 3][steam room part 4][steam room part 5][steam room part 6][steam room part 7][steam room part 8][steam room part 9]".

The r_11 is mapped west of r_10.
The r_14 is mapped south of r_10.
east of r_10 and west of r_9 is a door called d_3.
Understand "recreation zone" as r_11.
The internal name of r_11 is "recreation zone".
The printed name of r_11 is "-= Recreation Zone =-".
The recreation zone part 0 is some text that varies. The recreation zone part 0 is "You've entered a recreation zone. You begin to take stock of what's in the room.

 You see a couch. The couch is usual.[if there is something on the s_1] On the couch you make out [a list of things on the s_1]. There's something strange about this being here, but you can't put your finger on it.[end if]".
The recreation zone part 1 is some text that varies. The recreation zone part 1 is "[if there is nothing on the s_1] Looks like someone's already been here and taken everything off it, though. Aw, here you were, all excited for there to be things on it![end if]".
The recreation zone part 2 is some text that varies. The recreation zone part 2 is "

There is an unguarded exit to the east. You need an unblocked exit? You should try going west.".
The description of r_11 is "[recreation zone part 0][recreation zone part 1][recreation zone part 2]".

The r_12 is mapped west of r_11.
The r_10 is mapped east of r_11.
Understand "pantry" as r_12.
The internal name of r_12 is "pantry".
The printed name of r_12 is "-= Pantry =-".
The pantry part 0 is some text that varies. The pantry part 0 is "You find yourself in a pantry. An ordinary one.

 [if c_2 is locked]A locked[else if c_2 is open]An open[otherwise]A closed[end if]".
The pantry part 1 is some text that varies. The pantry part 1 is " locker is here.[if c_2 is open and there is something in the c_2] The locker contains [a list of things in the c_2].[end if]".
The pantry part 2 is some text that varies. The pantry part 2 is "[if c_2 is open and the c_2 contains nothing] The locker is empty, what a horrible day![end if]".
The pantry part 3 is some text that varies. The pantry part 3 is " You hear a noise behind you and spin around, but you can't see anything other than a shelf. [if there is something on the s_2]On the shelf you make out [a list of things on the s_2].[end if]".
The pantry part 4 is some text that varies. The pantry part 4 is "[if there is nothing on the s_2]Unfortunately, there isn't a thing on it. Oh! Why couldn't there just be stuff on it?[end if]".
The pantry part 5 is some text that varies. The pantry part 5 is "

 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The pantry part 6 is some text that varies. The pantry part 6 is " portal leading south. There is an unblocked exit to the east. There is an unguarded exit to the west.".
The description of r_12 is "[pantry part 0][pantry part 1][pantry part 2][pantry part 3][pantry part 4][pantry part 5][pantry part 6]".

The r_13 is mapped west of r_12.
south of r_12 and north of r_16 is a door called d_0.
The r_11 is mapped east of r_12.
Understand "basement" as r_13.
The internal name of r_13 is "basement".
The printed name of r_13 is "-= Basement =-".
The basement part 0 is some text that varies. The basement part 0 is "You arrive in a basement. A normal one.

 You see [if c_3 is locked]a locked[else if c_3 is open]an opened[otherwise]a closed[end if]".
The basement part 1 is some text that varies. The basement part 1 is " crate nearby.[if c_3 is open and there is something in the c_3] The crate contains [a list of things in the c_3].[end if]".
The basement part 2 is some text that varies. The basement part 2 is "[if c_3 is open and the c_3 contains nothing] The crate is empty! This is the worst thing that could possibly happen, ever![end if]".
The basement part 3 is some text that varies. The basement part 3 is " You scan the room for a counter, and you find a counter. The counter is normal.[if there is something on the s_3] On the counter you can make out [a list of things on the s_3].[end if]".
The basement part 4 is some text that varies. The basement part 4 is "[if there is nothing on the s_3] But there isn't a thing on it. Hm. Oh well[end if]".
The basement part 5 is some text that varies. The basement part 5 is "

You need an unblocked exit? You should try going east.".
The description of r_13 is "[basement part 0][basement part 1][basement part 2][basement part 3][basement part 4][basement part 5]".

The r_12 is mapped east of r_13.
Understand "garage" as r_14.
The internal name of r_14 is "garage".
The printed name of r_14 is "-= Garage =-".
The garage part 0 is some text that varies. The garage part 0 is "You're now in a garage.



You don't like doors? Why not try going north, that entranceway is unblocked. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_14 is "[garage part 0]".

The r_15 is mapped west of r_14.
The r_10 is mapped north of r_14.
Understand "bar" as r_15.
The internal name of r_15 is "bar".
The printed name of r_15 is "-= Bar =-".
The bar part 0 is some text that varies. The bar part 0 is "You've entered a bar.

 You can see a stand. [if there is something on the s_4]On the stand you can see [a list of things on the s_4].[end if]".
The bar part 1 is some text that varies. The bar part 1 is "[if there is nothing on the s_4]But the thing is empty, unfortunately.[end if]".
The bar part 2 is some text that varies. The bar part 2 is " You make out a bookshelf. The bookshelf is normal.[if there is something on the s_5] On the bookshelf you can make out [a list of things on the s_5].[end if]".
The bar part 3 is some text that varies. The bar part 3 is "[if there is nothing on the s_5] But the thing is empty, unfortunately.[end if]".
The bar part 4 is some text that varies. The bar part 4 is "

There is an unguarded exit to the east. There is an exit to the west. Don't worry, it is unguarded.".
The description of r_15 is "[bar part 0][bar part 1][bar part 2][bar part 3][bar part 4]".

The r_16 is mapped west of r_15.
The r_14 is mapped east of r_15.
Understand "dish-pit" as r_16.
The internal name of r_16 is "dish-pit".
The printed name of r_16 is "-= Dish-Pit =-".
The dish-pit part 0 is some text that varies. The dish-pit part 0 is "You are in a dish-pit. It seems to be pretty usual here. You decide to just list off a complete list of everything you see in the room, because hey, why not?



 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The dish-pit part 1 is some text that varies. The dish-pit part 1 is " portal leading north. There is [if d_2 is open]an open[otherwise]a closed[end if]".
The dish-pit part 2 is some text that varies. The dish-pit part 2 is " passageway leading west. You need an unblocked exit? You should try going east.".
The description of r_16 is "[dish-pit part 0][dish-pit part 1][dish-pit part 2]".

west of r_16 and east of r_17 is a door called d_2.
north of r_16 and south of r_12 is a door called d_0.
The r_15 is mapped east of r_16.
Understand "cubicle" as r_17.
The internal name of r_17 is "cubicle".
The printed name of r_17 is "-= Cubicle =-".
The cubicle part 0 is some text that varies. The cubicle part 0 is "You've entered a cubicle. You begin to take stock of what's in the room.

 You bend down to tie your shoe. When you stand up, you notice an armchair. The armchair is typical.[if there is something on the s_6] On the armchair you make out [a list of things on the s_6].[end if]".
The cubicle part 1 is some text that varies. The cubicle part 1 is "[if there is nothing on the s_6] Unfortunately, there isn't a thing on it. You make a mental note to not get your hopes up the next time you see an armchair in a room.[end if]".
The cubicle part 2 is some text that varies. The cubicle part 2 is " You see a chair. The chair is usual.[if there is something on the s_7] On the chair you can see [a list of things on the s_7].[end if]".
The cubicle part 3 is some text that varies. The cubicle part 3 is "[if there is nothing on the s_7] But the thing hasn't got anything on it.[end if]".
The cubicle part 4 is some text that varies. The cubicle part 4 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The cubicle part 5 is some text that varies. The cubicle part 5 is " passageway leading east. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The cubicle part 6 is some text that varies. The cubicle part 6 is " gateway leading south.".
The description of r_17 is "[cubicle part 0][cubicle part 1][cubicle part 2][cubicle part 3][cubicle part 4][cubicle part 5][cubicle part 6]".

south of r_17 and north of r_18 is a door called d_1.
east of r_17 and west of r_16 is a door called d_2.
Understand "launderette" as r_19.
The internal name of r_19 is "launderette".
The printed name of r_19 is "-= Launderette =-".
The launderette part 0 is some text that varies. The launderette part 0 is "You arrive in a launderette. A typical kind of place. You start to take note of what's in the room.

 You can see [if c_4 is locked]a locked[else if c_4 is open]an opened[otherwise]a closed[end if]".
The launderette part 1 is some text that varies. The launderette part 1 is " case.[if c_4 is open and there is something in the c_4] The case contains [a list of things in the c_4].[end if]".
The launderette part 2 is some text that varies. The launderette part 2 is "[if c_4 is open and the c_4 contains nothing] The case is empty! This is the worst thing that could possibly happen, ever![end if]".
The launderette part 3 is some text that varies. The launderette part 3 is " Oh, great. Here's a board. The board is normal.[if there is something on the s_8] On the board you can make out [a list of things on the s_8].[end if]".
The launderette part 4 is some text that varies. The launderette part 4 is "[if there is nothing on the s_8] Looks like someone's already been here and taken everything off it, though.[end if]".
The launderette part 5 is some text that varies. The launderette part 5 is "

There is an unblocked exit to the west.".
The description of r_19 is "[launderette part 0][launderette part 1][launderette part 2][launderette part 3][launderette part 4][launderette part 5]".

The r_18 is mapped west of r_19.
Understand "shower" as r_18.
The internal name of r_18 is "shower".
The printed name of r_18 is "-= Shower =-".
The shower part 0 is some text that varies. The shower part 0 is "You are in a shower. A standard kind of place. You can barely contain your excitement.



 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The shower part 1 is some text that varies. The shower part 1 is " gateway leading north. There is an exit to the east. Don't worry, it is unblocked.".
The description of r_18 is "[shower part 0][shower part 1]".

north of r_18 and south of r_17 is a door called d_1.
The r_19 is mapped east of r_18.
Understand "cookhouse" as r_2.
The internal name of r_2 is "cookhouse".
The printed name of r_2 is "-= Cookhouse =-".
The cookhouse part 0 is some text that varies. The cookhouse part 0 is "Ah, the cookhouse. This is some kind of cookhouse, really great standard vibes in this place, a wonderful standard atmosphere.

 Look over there! a refrigerator.[if c_5 is open and there is something in the c_5] The refrigerator contains [a list of things in the c_5].[end if]".
The cookhouse part 1 is some text that varies. The cookhouse part 1 is "[if c_5 is open and the c_5 contains nothing] The refrigerator is empty, what a horrible day![end if]".
The cookhouse part 2 is some text that varies. The cookhouse part 2 is "

 There is [if d_11 is open]an open[otherwise]a closed[end if]".
The cookhouse part 3 is some text that varies. The cookhouse part 3 is " hatch leading west. There is [if d_10 is open]an open[otherwise]a closed[end if]".
The cookhouse part 4 is some text that varies. The cookhouse part 4 is " door leading east.".
The description of r_2 is "[cookhouse part 0][cookhouse part 1][cookhouse part 2][cookhouse part 3][cookhouse part 4]".

west of r_2 and east of r_1 is a door called d_11.
east of r_2 and west of r_3 is a door called d_10.
Understand "bedroom" as r_1.
The internal name of r_1 is "bedroom".
The printed name of r_1 is "-= Bedroom =-".
The bedroom part 0 is some text that varies. The bedroom part 0 is "You're now in a bedroom. The room seems oddly familiar, as though it were only superficially different from the other rooms in the building.



 There is [if d_11 is open]an open[otherwise]a closed[end if]".
The bedroom part 1 is some text that varies. The bedroom part 1 is " hatch leading east. You don't like doors? Why not try going south, that entranceway is unblocked.".
The description of r_1 is "[bedroom part 0][bedroom part 1]".

The r_0 is mapped south of r_1.
east of r_1 and west of r_2 is a door called d_11.
Understand "study" as r_3.
The internal name of r_3 is "study".
The printed name of r_3 is "-= Study =-".
The study part 0 is some text that varies. The study part 0 is "You find yourself in a study. A standard one.

 You see [if c_6 is locked]a locked[else if c_6 is open]an opened[otherwise]a closed[end if]".
The study part 1 is some text that varies. The study part 1 is " standard looking portmanteau right there by you.[if c_6 is open and there is something in the c_6] The portmanteau contains [a list of things in the c_6].[end if]".
The study part 2 is some text that varies. The study part 2 is "[if c_6 is open and the c_6 contains nothing] The portmanteau is empty! This is the worst thing that could possibly happen, ever![end if]".
The study part 3 is some text that varies. The study part 3 is " You see [if c_7 is locked]a locked[else if c_7 is open]an opened[otherwise]a closed[end if]".
The study part 4 is some text that varies. The study part 4 is " bureau nearby.[if c_7 is open and there is something in the c_7] The bureau contains [a list of things in the c_7]. You idly wonder how they came up with the name TextWorld for this place. It's pretty fitting.[end if]".
The study part 5 is some text that varies. The study part 5 is "[if c_7 is open and the c_7 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The study part 6 is some text that varies. The study part 6 is "

 There is [if d_9 is open]an open[otherwise]a closed[end if]".
The study part 7 is some text that varies. The study part 7 is " cedar portal leading south. There is [if d_10 is open]an open[otherwise]a closed[end if]".
The study part 8 is some text that varies. The study part 8 is " door leading west.".
The description of r_3 is "[study part 0][study part 1][study part 2][study part 3][study part 4][study part 5][study part 6][study part 7][study part 8]".

west of r_3 and east of r_2 is a door called d_10.
south of r_3 and north of r_4 is a door called d_9.
Understand "cookery" as r_5.
The internal name of r_5 is "cookery".
The printed name of r_5 is "-= Cookery =-".
The cookery part 0 is some text that varies. The cookery part 0 is "You've come into an ordinary room. Your mind races to think of what kind of room would be ordinary. And then it hits you. Of course. You're in the cookery.



 There is [if d_7 is open]an open[otherwise]a closed[end if]".
The cookery part 1 is some text that varies. The cookery part 1 is " wooden gate leading north. There is [if d_8 is open]an open[otherwise]a closed[end if]".
The cookery part 2 is some text that varies. The cookery part 2 is " wooden passageway leading west.".
The description of r_5 is "[cookery part 0][cookery part 1][cookery part 2]".

west of r_5 and east of r_4 is a door called d_8.
north of r_5 and south of r_6 is a door called d_7.
Understand "canteen" as r_4.
The internal name of r_4 is "canteen".
The printed name of r_4 is "-= Canteen =-".
The canteen part 0 is some text that varies. The canteen part 0 is "You find yourself in a canteen. A standard kind of place.



 There is [if d_8 is open]an open[otherwise]a closed[end if]".
The canteen part 1 is some text that varies. The canteen part 1 is " wooden passageway leading east. There is [if d_9 is open]an open[otherwise]a closed[end if]".
The canteen part 2 is some text that varies. The canteen part 2 is " cedar portal leading north.".
The description of r_4 is "[canteen part 0][canteen part 1][canteen part 2]".

north of r_4 and south of r_3 is a door called d_9.
east of r_4 and west of r_5 is a door called d_8.
Understand "laundry place" as r_7.
The internal name of r_7 is "laundry place".
The printed name of r_7 is "-= Laundry Place =-".
The laundry place part 0 is some text that varies. The laundry place part 0 is "You find yourself in a laundry place. You begin to take stock of what's in the room.

 You can make out [if c_8 is locked]a locked[else if c_8 is open]an opened[otherwise]a closed[end if]".
The laundry place part 1 is some text that varies. The laundry place part 1 is " box right there by you.[if c_8 is open and there is something in the c_8] The box contains [a list of things in the c_8].[end if]".
The laundry place part 2 is some text that varies. The laundry place part 2 is "[if c_8 is open and the c_8 contains nothing] What a letdown! The box is empty![end if]".
The laundry place part 3 is some text that varies. The laundry place part 3 is "

 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The laundry place part 4 is some text that varies. The laundry place part 4 is " TextWorld limited edition gateway leading south. There is [if d_6 is open]an open[otherwise]a closed[end if]".
The laundry place part 5 is some text that varies. The laundry place part 5 is " maple gate leading west.".
The description of r_7 is "[laundry place part 0][laundry place part 1][laundry place part 2][laundry place part 3][laundry place part 4][laundry place part 5]".

west of r_7 and east of r_6 is a door called d_6.
south of r_7 and north of r_8 is a door called d_5.
Understand "vault" as r_6.
The internal name of r_6 is "vault".
The printed name of r_6 is "-= Vault =-".
The vault part 0 is some text that varies. The vault part 0 is "You arrive in a vault. A normal kind of place. You decide to just list off a complete list of everything you see in the room, because hey, why not?



 There is [if d_6 is open]an open[otherwise]a closed[end if]".
The vault part 1 is some text that varies. The vault part 1 is " maple gate leading east. There is [if d_7 is open]an open[otherwise]a closed[end if]".
The vault part 2 is some text that varies. The vault part 2 is " wooden gate leading south.".
The description of r_6 is "[vault part 0][vault part 1][vault part 2]".

south of r_6 and north of r_5 is a door called d_7.
east of r_6 and west of r_7 is a door called d_6.
Understand "salon" as r_9.
The internal name of r_9 is "salon".
The printed name of r_9 is "-= Salon =-".
The salon part 0 is some text that varies. The salon part 0 is "You've just sauntered into a salon.

 Oh, great. Here's a desk. [if there is something on the s_9]On the desk you make out [a list of things on the s_9].[end if]".
The salon part 1 is some text that varies. The salon part 1 is "[if there is nothing on the s_9]The desk appears to be empty.[end if]".
The salon part 2 is some text that varies. The salon part 2 is "

 There is [if d_4 is open]an open[otherwise]a closed[end if]".
The salon part 3 is some text that varies. The salon part 3 is " stone door leading north. There is [if d_3 is open]an open[otherwise]a closed[end if]".
The salon part 4 is some text that varies. The salon part 4 is " gate leading west.".
The description of r_9 is "[salon part 0][salon part 1][salon part 2][salon part 3][salon part 4]".

west of r_9 and east of r_10 is a door called d_3.
north of r_9 and south of r_8 is a door called d_4.
Understand "studio" as r_0.
The internal name of r_0 is "studio".
The printed name of r_0 is "-= Studio =-".
The studio part 0 is some text that varies. The studio part 0 is "You have stumbled into the most usual of all possible studios.



You need an unblocked exit? You should try going north.".
The description of r_0 is "[studio part 0]".

The r_1 is mapped north of r_0.
Understand "cellar" as r_8.
The internal name of r_8 is "cellar".
The printed name of r_8 is "-= Cellar =-".
The cellar part 0 is some text that varies. The cellar part 0 is "You are in a cellar. An ordinary one. You begin to take stock of what's here.

 You can make out a workbench. The workbench is ordinary.[if there is something on the s_10] On the workbench you can make out [a list of things on the s_10].[end if]".
The cellar part 1 is some text that varies. The cellar part 1 is "[if there is nothing on the s_10] Looks like someone's already been here and taken everything off it, though. What, you think everything in TextWorld should have stuff on it?[end if]".
The cellar part 2 is some text that varies. The cellar part 2 is "

 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The cellar part 3 is some text that varies. The cellar part 3 is " TextWorld limited edition gateway leading north. There is [if d_4 is open]an open[otherwise]a closed[end if]".
The cellar part 4 is some text that varies. The cellar part 4 is " stone door leading south.".
The description of r_8 is "[cellar part 0][cellar part 1][cellar part 2][cellar part 3][cellar part 4]".

south of r_8 and north of r_9 is a door called d_4.
north of r_8 and south of r_7 is a door called d_5.

The c_0 and the c_1 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 are containers.
The c_0 and the c_1 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 are privately-named.
The d_11 and the d_3 and the d_0 and the d_2 and the d_1 and the d_10 and the d_9 and the d_8 and the d_7 and the d_6 and the d_5 and the d_4 are doors.
The d_11 and the d_3 and the d_0 and the d_2 and the d_1 and the d_10 and the d_9 and the d_8 and the d_7 and the d_6 and the d_5 and the d_4 are privately-named.
The k_0 and the k_1 and the k_2 are keys.
The k_0 and the k_1 and the k_2 are privately-named.
The o_0 are object-likes.
The o_0 are privately-named.
The r_10 and the r_11 and the r_12 and the r_13 and the r_14 and the r_15 and the r_16 and the r_17 and the r_19 and the r_18 and the r_2 and the r_1 and the r_3 and the r_5 and the r_4 and the r_7 and the r_6 and the r_9 and the r_0 and the r_8 are rooms.
The r_10 and the r_11 and the r_12 and the r_13 and the r_14 and the r_15 and the r_16 and the r_17 and the r_19 and the r_18 and the r_2 and the r_1 and the r_3 and the r_5 and the r_4 and the r_7 and the r_6 and the r_9 and the r_0 and the r_8 are privately-named.
The s_0 and the s_1 and the s_10 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 and the s_8 and the s_9 are supporters.
The s_0 and the s_1 and the s_10 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 and the s_8 and the s_9 are privately-named.

The description of d_11 is "it's a noble hatch [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_11 is "hatch".
Understand "hatch" as d_11.
The d_11 is locked.
The description of d_3 is "it's a manageable gate [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_3 is "gate".
Understand "gate" as d_3.
The d_3 is open.
The description of d_0 is "The portal looks solid. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_0 is "portal".
Understand "portal" as d_0.
The d_0 is open.
The description of d_2 is "it is what it is, a passageway [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_2 is "passageway".
Understand "passageway" as d_2.
The d_2 is open.
The description of d_1 is "The gateway looks commanding. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_1 is "gateway".
Understand "gateway" as d_1.
The d_1 is open.
The description of d_10 is "The door looks sturdy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_10 is "door".
Understand "door" as d_10.
The d_10 is open.
The description of d_9 is "The cedar portal looks towering. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_9 is "cedar portal".
Understand "cedar portal" as d_9.
Understand "cedar" as d_9.
Understand "portal" as d_9.
The d_9 is open.
The description of d_8 is "it is what it is, a wooden passageway [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_8 is "wooden passageway".
Understand "wooden passageway" as d_8.
Understand "wooden" as d_8.
Understand "passageway" as d_8.
The d_8 is open.
The description of d_7 is "The wooden gate looks hefty. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_7 is "wooden gate".
Understand "wooden gate" as d_7.
Understand "wooden" as d_7.
Understand "gate" as d_7.
The d_7 is open.
The description of d_6 is "it's a commanding gate [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_6 is "maple gate".
Understand "maple gate" as d_6.
Understand "maple" as d_6.
Understand "gate" as d_6.
The d_6 is open.
The description of d_5 is "it is what it is, a TextWorld limited edition gateway [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_5 is "TextWorld limited edition gateway".
Understand "TextWorld limited edition gateway" as d_5.
Understand "TextWorld" as d_5.
Understand "limited" as d_5.
Understand "edition" as d_5.
Understand "gateway" as d_5.
The d_5 is locked.
The description of d_4 is "it is what it is, a stone door [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_4 is "stone door".
Understand "stone door" as d_4.
Understand "stone" as d_4.
Understand "door" as d_4.
The d_4 is open.
The description of c_0 is "The dresser looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_0 is "dresser".
Understand "dresser" as c_0.
The c_0 is in r_10.
The c_0 is open.
The description of c_1 is "The trunk looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_1 is "trunk".
Understand "trunk" as c_1.
The c_1 is in r_10.
The c_1 is closed.
The description of c_2 is "The locker looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_2 is "locker".
Understand "locker" as c_2.
The c_2 is in r_12.
The c_2 is open.
The description of c_3 is "The crate looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_3 is "crate".
Understand "crate" as c_3.
The c_3 is in r_13.
The c_3 is open.
The description of c_4 is "The case looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_4 is "case".
Understand "case" as c_4.
The c_4 is in r_19.
The c_4 is closed.
The description of c_5 is "The refrigerator looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_5 is "refrigerator".
Understand "refrigerator" as c_5.
The c_5 is in r_2.
The c_5 is locked.
The description of c_6 is "The portmanteau looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_6 is "portmanteau".
Understand "portmanteau" as c_6.
The c_6 is in r_3.
The c_6 is locked.
The description of c_7 is "The bureau looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_7 is "bureau".
Understand "bureau" as c_7.
The c_7 is in r_3.
The c_7 is open.
The description of c_8 is "The box looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_8 is "box".
Understand "box" as c_8.
The c_8 is in r_7.
The c_8 is closed.
The description of o_0 is "The fly larva is dirty.".
The printed name of o_0 is "fly larva".
Understand "fly larva" as o_0.
Understand "fly" as o_0.
Understand "larva" as o_0.
The o_0 is in r_0.
The description of s_0 is "The table is solid.".
The printed name of s_0 is "table".
Understand "table" as s_0.
The s_0 is in r_10.
The description of s_1 is "The couch is solidly built.".
The printed name of s_1 is "couch".
Understand "couch" as s_1.
The s_1 is in r_11.
The description of s_10 is "The workbench is stable.".
The printed name of s_10 is "workbench".
Understand "workbench" as s_10.
The s_10 is in r_8.
The description of s_2 is "The shelf is durable.".
The printed name of s_2 is "shelf".
Understand "shelf" as s_2.
The s_2 is in r_12.
The description of s_3 is "The counter is an unstable piece of garbage.".
The printed name of s_3 is "counter".
Understand "counter" as s_3.
The s_3 is in r_13.
The description of s_4 is "The stand is an unstable piece of garbage.".
The printed name of s_4 is "stand".
Understand "stand" as s_4.
The s_4 is in r_15.
The description of s_5 is "The bookshelf is unstable.".
The printed name of s_5 is "bookshelf".
Understand "bookshelf" as s_5.
The s_5 is in r_15.
The description of s_6 is "The armchair is shaky.".
The printed name of s_6 is "armchair".
Understand "armchair" as s_6.
The s_6 is in r_17.
The description of s_7 is "The chair is wobbly.".
The printed name of s_7 is "chair".
Understand "chair" as s_7.
The s_7 is in r_17.
The description of s_8 is "The board is an unstable piece of garbage.".
The printed name of s_8 is "board".
Understand "board" as s_8.
The s_8 is in r_19.
The description of s_9 is "The desk is balanced.".
The printed name of s_9 is "desk".
Understand "desk" as s_9.
The s_9 is in r_9.
The description of k_0 is "The latchkey looks useful".
The printed name of k_0 is "latchkey".
Understand "latchkey" as k_0.
The k_0 is in the c_6.
The description of k_1 is "The passkey looks useful".
The printed name of k_1 is "passkey".
Understand "passkey" as k_1.
The k_1 is in the c_7.
The matching key of the d_11 is the k_1.
The description of k_2 is "The TextWorld limited edition keycard is heavy.".
The printed name of k_2 is "TextWorld limited edition keycard".
Understand "TextWorld limited edition keycard" as k_2.
Understand "TextWorld" as k_2.
Understand "limited" as k_2.
Understand "edition" as k_2.
Understand "keycard" as k_2.
The matching key of the d_5 is the k_2.
The k_2 is on the s_9.


The player is in r_9.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "take TextWorld limited edition keycard from desk / go north / unlock TextWorld limited edition gateway with TextWorld limited edition keycard / open TextWorld limited edition gateway / go north / go west / go south / go west / go north / take passkey from bureau / go west / unlock hatch with passkey / open hatch / go west / go south / take fly larva"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the k_0:
		end the story; [Lost]
	else if The player is in r_0 and The player carries the o_0:
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

The objective part 0 is some text that varies. The objective part 0 is "I hope you're ready to go into rooms and interact with objects, because you've just entered TextWorld! Here is how to play! First of all, take the TextWorld limited edition keycard from the desk. And ".
The objective part 1 is some text that varies. The objective part 1 is "then, take a trip north. That done, unlock the TextWorld limited edition gateway with the TextWorld limited edition keycard. And then, open the TextWorld limited edition gateway in the cellar. And the".
The objective part 2 is some text that varies. The objective part 2 is "n, venture north. And then, make an attempt to move west. Then, travel south. Then, try to travel west. Okay, and then, venture north. Then, pick up the passkey from the bureau within the study. After".
The objective part 3 is some text that varies. The objective part 3 is " that, go to the west. Then, unlock the hatch within the cookhouse. Once you have unlocked the hatch, ensure that the hatch is open. After that, try to go west. That done, make an effort to travel sou".
The objective part 4 is some text that varies. The objective part 4 is "th. With that accomplished, pick-up the fly larva from the floor of the studio. Got that? Good!".

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

