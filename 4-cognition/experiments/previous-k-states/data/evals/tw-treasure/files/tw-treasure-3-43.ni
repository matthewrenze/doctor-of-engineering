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


The r_10 and the r_6 and the r_12 and the r_17 and the r_16 and the r_3 and the r_2 and the r_4 and the r_14 and the r_5 and the r_9 and the r_7 and the r_13 and the r_0 and the r_1 and the r_11 and the r_15 and the r_18 and the r_19 and the r_8 are rooms.

Understand "basement" as r_10.
The internal name of r_10 is "basement".
The printed name of r_10 is "-= Basement =-".
The basement part 0 is some text that varies. The basement part 0 is "I am sorry to announce that you are now in the basement.

 You can see [if c_0 is locked]a locked[else if c_0 is open]an opened[otherwise]a closed[end if]".
The basement part 1 is some text that varies. The basement part 1 is " display, which looks typical, here.[if c_0 is open and there is something in the c_0] The display contains [a list of things in the c_0].[end if]".
The basement part 2 is some text that varies. The basement part 2 is "[if c_0 is open and the c_0 contains nothing] The display is empty! What a waste of a day![end if]".
The basement part 3 is some text that varies. The basement part 3 is "

 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The basement part 4 is some text that varies. The basement part 4 is " door leading south. There is [if d_6 is open]an open[otherwise]a closed[end if]".
The basement part 5 is some text that varies. The basement part 5 is " passageway leading west. You don't like doors? Why not try going east, that entranceway is unblocked.".
The description of r_10 is "[basement part 0][basement part 1][basement part 2][basement part 3][basement part 4][basement part 5]".

west of r_10 and east of r_6 is a door called d_6.
south of r_10 and north of r_11 is a door called d_5.
The r_12 is mapped east of r_10.
Understand "bedchamber" as r_6.
The internal name of r_6 is "bedchamber".
The printed name of r_6 is "-= Bedchamber =-".
The bedchamber part 0 is some text that varies. The bedchamber part 0 is "You are in a bedchamber.

 You can make out a bed stand. [if there is something on the s_0]You see [a list of things on the s_0] on the bed stand. Classic TextWorld.[end if]".
The bedchamber part 1 is some text that varies. The bedchamber part 1 is "[if there is nothing on the s_0]But the thing hasn't got anything on it.[end if]".
The bedchamber part 2 is some text that varies. The bedchamber part 2 is "

 There is [if d_6 is open]an open[otherwise]a closed[end if]".
The bedchamber part 3 is some text that varies. The bedchamber part 3 is " passageway leading east. There is [if d_0 is open]an open[otherwise]a closed[end if]".
The bedchamber part 4 is some text that varies. The bedchamber part 4 is " wooden door leading west. You need an unblocked exit? You should try going south.".
The description of r_6 is "[bedchamber part 0][bedchamber part 1][bedchamber part 2][bedchamber part 3][bedchamber part 4]".

west of r_6 and east of r_9 is a door called d_0.
The r_5 is mapped south of r_6.
east of r_6 and west of r_10 is a door called d_6.
Understand "office" as r_12.
The internal name of r_12 is "office".
The printed name of r_12 is "-= Office =-".
The office part 0 is some text that varies. The office part 0 is "If you're wondering why everything seems so standard all of a sudden, it's because you've just shown up in the office. You begin to take stock of what's here.

 You lean against the wall, inadvertently pressing a secret button. The wall opens up to reveal a cabinet.[if c_1 is open and there is something in the c_1] The cabinet contains [a list of things in the c_1].[end if]".
The office part 1 is some text that varies. The office part 1 is "[if c_1 is open and the c_1 contains nothing] What a letdown! The cabinet is empty![end if]".
The office part 2 is some text that varies. The office part 2 is " You see a stand. [if there is something on the s_1]You see [a list of things on the s_1] on the stand.[end if]".
The office part 3 is some text that varies. The office part 3 is "[if there is nothing on the s_1]But oh no! there's nothing on this piece of junk.[end if]".
The office part 4 is some text that varies. The office part 4 is " You see a chair. [if there is something on the s_2]You see [a list of things on the s_2] on the chair.[end if]".
The office part 5 is some text that varies. The office part 5 is "[if there is nothing on the s_2]Unfortunately, there isn't a thing on it.[end if]".
The office part 6 is some text that varies. The office part 6 is "

There is an unguarded exit to the west.".
The description of r_12 is "[office part 0][office part 1][office part 2][office part 3][office part 4][office part 5][office part 6]".

The r_10 is mapped west of r_12.
Understand "workshop" as r_17.
The internal name of r_17 is "workshop".
The printed name of r_17 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "You are in a workshop. An ordinary kind of place.

 You can make out [if c_2 is locked]a locked[else if c_2 is open]an opened[otherwise]a closed[end if]".
The workshop part 1 is some text that varies. The workshop part 1 is " bureau close by.[if c_2 is open and there is something in the c_2] The bureau contains [a list of things in the c_2]. The light flickers for a second, but nothing else happens.[end if]".
The workshop part 2 is some text that varies. The workshop part 2 is "[if c_2 is open and the c_2 contains nothing] The bureau is empty, what a horrible day![end if]".
The workshop part 3 is some text that varies. The workshop part 3 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The workshop part 4 is some text that varies. The workshop part 4 is " hatch leading west. There is an exit to the south. Don't worry, it is unguarded.".
The description of r_17 is "[workshop part 0][workshop part 1][workshop part 2][workshop part 3][workshop part 4]".

west of r_17 and east of r_16 is a door called d_2.
The r_18 is mapped south of r_17.
Understand "studio" as r_16.
The internal name of r_16 is "studio".
The printed name of r_16 is "-= Studio =-".
The studio part 0 is some text that varies. The studio part 0 is "You are in a studio. A standard kind of place.

 You can make out a mantelpiece. The mantelpiece is typical.[if there is something on the s_3] On the mantelpiece you can see [a list of things on the s_3].[end if]".
The studio part 1 is some text that varies. The studio part 1 is "[if there is nothing on the s_3] But the thing is empty, unfortunately. Aw, and here you were, all excited for there to be things on it![end if]".
The studio part 2 is some text that varies. The studio part 2 is " What's that over there? It looks like it's a desk. [if there is something on the s_4]You see [a list of things on the s_4] on the desk. Suddenly, you bump your head on the ceiling, but it's not such a bad bump that it's going to prevent you from looking at objects and even things.[end if]".
The studio part 3 is some text that varies. The studio part 3 is "[if there is nothing on the s_4]Unfortunately, there isn't a thing on it.[end if]".
The studio part 4 is some text that varies. The studio part 4 is " You can make out a table. [if there is something on the s_5]You see [a list of things on the s_5] on the table.[end if]".
The studio part 5 is some text that varies. The studio part 5 is "[if there is nothing on the s_5]But oh no! there's nothing on this piece of garbage.[end if]".
The studio part 6 is some text that varies. The studio part 6 is "

 There is [if d_3 is open]an open[otherwise]a closed[end if]".
The studio part 7 is some text that varies. The studio part 7 is " Canadian limited edition gate leading north. There is [if d_2 is open]an open[otherwise]a closed[end if]".
The studio part 8 is some text that varies. The studio part 8 is " hatch leading east. There is an exit to the south. Don't worry, it is unblocked.".
The description of r_16 is "[studio part 0][studio part 1][studio part 2][studio part 3][studio part 4][studio part 5][studio part 6][studio part 7][studio part 8]".

The r_19 is mapped south of r_16.
north of r_16 and south of r_15 is a door called d_3.
east of r_16 and west of r_17 is a door called d_2.
Understand "recreation zone" as r_3.
The internal name of r_3 is "recreation zone".
The printed name of r_3 is "-= Recreation Zone =-".
The recreation zone part 0 is some text that varies. The recreation zone part 0 is "You arrive in a recreation zone. A standard kind of place. You can barely contain your excitement.



 There is [if d_7 is open]an open[otherwise]a closed[end if]".
The recreation zone part 1 is some text that varies. The recreation zone part 1 is " wooden gate leading east. There is [if d_8 is open]an open[otherwise]a closed[end if]".
The recreation zone part 2 is some text that varies. The recreation zone part 2 is " wooden portal leading north. There is [if d_9 is open]an open[otherwise]a closed[end if]".
The recreation zone part 3 is some text that varies. The recreation zone part 3 is " gateway leading west.".
The description of r_3 is "[recreation zone part 0][recreation zone part 1][recreation zone part 2][recreation zone part 3]".

west of r_3 and east of r_2 is a door called d_9.
north of r_3 and south of r_4 is a door called d_8.
east of r_3 and west of r_7 is a door called d_7.
Understand "vault" as r_2.
The internal name of r_2 is "vault".
The printed name of r_2 is "-= Vault =-".
The vault part 0 is some text that varies. The vault part 0 is "You've entered a vault.



 There is [if d_9 is open]an open[otherwise]a closed[end if]".
The vault part 1 is some text that varies. The vault part 1 is " gateway leading east. There is [if d_10 is open]an open[otherwise]a closed[end if]".
The vault part 2 is some text that varies. The vault part 2 is " portal leading south.".
The description of r_2 is "[vault part 0][vault part 1][vault part 2]".

south of r_2 and north of r_1 is a door called d_10.
east of r_2 and west of r_3 is a door called d_9.
Understand "spare room" as r_4.
The internal name of r_4 is "spare room".
The printed name of r_4 is "-= Spare Room =-".
The spare room part 0 is some text that varies. The spare room part 0 is "A rusty sign tells you that you are now in the spare room. You begin to take stock of what's here.

 You can make out a workbench. The workbench is typical.[if there is something on the s_6] On the workbench you make out [a list of things on the s_6].[end if]".
The spare room part 1 is some text that varies. The spare room part 1 is "[if there is nothing on the s_6] But the thing hasn't got anything on it.[end if]".
The spare room part 2 is some text that varies. The spare room part 2 is "

 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The spare room part 3 is some text that varies. The spare room part 3 is " walnut portal leading north. There is [if d_8 is open]an open[otherwise]a closed[end if]".
The spare room part 4 is some text that varies. The spare room part 4 is " wooden portal leading south. You don't like doors? Why not try going east, that entranceway is unblocked. You need an unguarded exit? You should try going west.".
The description of r_4 is "[spare room part 0][spare room part 1][spare room part 2][spare room part 3][spare room part 4]".

The r_14 is mapped west of r_4.
south of r_4 and north of r_3 is a door called d_8.
north of r_4 and south of r_9 is a door called d_1.
The r_5 is mapped east of r_4.
Understand "shower" as r_14.
The internal name of r_14 is "shower".
The printed name of r_14 is "-= Shower =-".
The shower part 0 is some text that varies. The shower part 0 is "You arrive in a shower. An usual kind of place. You try to gain information on your surroundings by using a technique you call 'looking.'



There is an unblocked exit to the east.".
The description of r_14 is "[shower part 0]".

The r_4 is mapped east of r_14.
Understand "kitchen" as r_5.
The internal name of r_5 is "kitchen".
The printed name of r_5 is "-= Kitchen =-".
The kitchen part 0 is some text that varies. The kitchen part 0 is "You arrive in a kitchen. A typical kind of place.

 You see a fridge. Suddenly, you bump your head on the ceiling, but it's not such a bad bump that it's going to prevent you from looking at objects and even things.[if c_3 is open and there is something in the c_3] The fridge contains [a list of things in the c_3]. Wow, check out the price tag that's still affixed to the fridge! A hundred bucks![end if]".
The kitchen part 1 is some text that varies. The kitchen part 1 is "[if c_3 is open and the c_3 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The kitchen part 2 is some text that varies. The kitchen part 2 is " You make out a freezer.[if c_4 is open and there is something in the c_4] The freezer contains [a list of things in the c_4]. Huh, weird.[end if]".
The kitchen part 3 is some text that varies. The kitchen part 3 is "[if c_4 is open and the c_4 contains nothing] The freezer is empty, what a horrible day![end if]".
The kitchen part 4 is some text that varies. The kitchen part 4 is "

You need an unblocked exit? You should try going north. There is an exit to the south. Don't worry, it is unguarded. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_5 is "[kitchen part 0][kitchen part 1][kitchen part 2][kitchen part 3][kitchen part 4]".

The r_4 is mapped west of r_5.
The r_7 is mapped south of r_5.
The r_6 is mapped north of r_5.
Understand "pantry" as r_9.
The internal name of r_9 is "pantry".
The printed name of r_9 is "-= Pantry =-".
The pantry part 0 is some text that varies. The pantry part 0 is "You are in a pantry. It seems to be pretty typical here.

 You can see [if c_5 is locked]a locked[else if c_5 is open]an opened[otherwise]a closed[end if]".
The pantry part 1 is some text that varies. The pantry part 1 is " crate.[if c_5 is open and there is something in the c_5] The crate contains [a list of things in the c_5].[end if]".
The pantry part 2 is some text that varies. The pantry part 2 is "[if c_5 is open and the c_5 contains nothing] The crate is empty! This is the worst thing that could possibly happen, ever![end if]".
The pantry part 3 is some text that varies. The pantry part 3 is "

 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The pantry part 4 is some text that varies. The pantry part 4 is " wooden door leading east. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The pantry part 5 is some text that varies. The pantry part 5 is " walnut portal leading south. You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_9 is "[pantry part 0][pantry part 1][pantry part 2][pantry part 3][pantry part 4][pantry part 5]".

The r_13 is mapped west of r_9.
south of r_9 and north of r_4 is a door called d_1.
east of r_9 and west of r_6 is a door called d_0.
Understand "steam room" as r_7.
The internal name of r_7 is "steam room".
The printed name of r_7 is "-= Steam Room =-".
The steam room part 0 is some text that varies. The steam room part 0 is "Guess what, you are in the place we're calling the steam room. You decide to start listing off everything you see in the room, as if you were in a text adventure.

 Hey, want to see a bench? Look over there, a bench. [if there is something on the s_7]On the bench you can make out [a list of things on the s_7]. Huh, weird.[end if]".
The steam room part 1 is some text that varies. The steam room part 1 is "[if there is nothing on the s_7]But the thing hasn't got anything on it.[end if]".
The steam room part 2 is some text that varies. The steam room part 2 is "

 There is [if d_7 is open]an open[otherwise]a closed[end if]".
The steam room part 3 is some text that varies. The steam room part 3 is " wooden gate leading west. You need an unblocked exit? You should try going north. There is an unguarded exit to the south.".
The description of r_7 is "[steam room part 0][steam room part 1][steam room part 2][steam room part 3]".

west of r_7 and east of r_3 is a door called d_7.
The r_8 is mapped south of r_7.
The r_5 is mapped north of r_7.
Understand "canteen" as r_13.
The internal name of r_13 is "canteen".
The printed name of r_13 is "-= Canteen =-".
The canteen part 0 is some text that varies. The canteen part 0 is "You arrive in a canteen. A normal kind of place. Okay, just remember what you're here to do, and everything will go great.

 You make out a case.[if c_6 is open and there is something in the c_6] The case contains [a list of things in the c_6]. Something scurries by right in the corner of your eye. Probably nothing.[end if]".
The canteen part 1 is some text that varies. The canteen part 1 is "[if c_6 is open and the c_6 contains nothing] The case is empty! This is the worst thing that could possibly happen, ever![end if]".
The canteen part 2 is some text that varies. The canteen part 2 is "

There is an exit to the east. Don't worry, it is unguarded.".
The description of r_13 is "[canteen part 0][canteen part 1][canteen part 2]".

The r_9 is mapped east of r_13.
Understand "study" as r_0.
The internal name of r_0 is "study".
The printed name of r_0 is "-= Study =-".
The study part 0 is some text that varies. The study part 0 is "You find yourself in a study. A normal kind of place. You decide to start listing off everything you see in the room, as if you were in a text adventure.



You don't like doors? Why not try going north, that entranceway is unguarded.".
The description of r_0 is "[study part 0]".

The r_1 is mapped north of r_0.
Understand "salon" as r_1.
The internal name of r_1 is "salon".
The printed name of r_1 is "-= Salon =-".
The salon part 0 is some text that varies. The salon part 0 is "You arrive in a salon. An ordinary one.



 There is [if d_10 is open]an open[otherwise]a closed[end if]".
The salon part 1 is some text that varies. The salon part 1 is " portal leading north. There is an unblocked exit to the south.".
The description of r_1 is "[salon part 0][salon part 1]".

The r_0 is mapped south of r_1.
north of r_1 and south of r_2 is a door called d_10.
Understand "restroom" as r_11.
The internal name of r_11 is "restroom".
The printed name of r_11 is "-= Restroom =-".
The restroom part 0 is some text that varies. The restroom part 0 is "You're now in the restroom. You begin looking for stuff.

 Look out! It's a- oh, never mind, it's just a counter. [if there is something on the s_8]On the counter you make out [a list of things on the s_8].[end if]".
The restroom part 1 is some text that varies. The restroom part 1 is "[if there is nothing on the s_8]Unfortunately, there isn't a thing on it. Hm. Oh well[end if]".
The restroom part 2 is some text that varies. The restroom part 2 is " You scan the room for a board, and you find a board. The board is ordinary.[if there is something on the s_9] On the board you can see [a list of things on the s_9].[end if]".
The restroom part 3 is some text that varies. The restroom part 3 is "[if there is nothing on the s_9] However, the board, like an empty board, has nothing on it. What, you think everything in TextWorld should have stuff on it?[end if]".
The restroom part 4 is some text that varies. The restroom part 4 is "

 There is [if d_5 is open]an open[otherwise]a closed[end if]".
The restroom part 5 is some text that varies. The restroom part 5 is " door leading north. There is [if d_4 is open]an open[otherwise]a closed[end if]".
The restroom part 6 is some text that varies. The restroom part 6 is " gate leading south.".
The description of r_11 is "[restroom part 0][restroom part 1][restroom part 2][restroom part 3][restroom part 4][restroom part 5][restroom part 6]".

south of r_11 and north of r_15 is a door called d_4.
north of r_11 and south of r_10 is a door called d_5.
Understand "cubicle" as r_15.
The internal name of r_15 is "cubicle".
The printed name of r_15 is "-= Cubicle =-".
The cubicle part 0 is some text that varies. The cubicle part 0 is "Look around you. Take it all in. It's not every day someone gets to be in a cubicle.

 You scan the room for a locker, and you find a locker. Hmmm... what else, what else?[if c_7 is open and there is something in the c_7] The locker contains [a list of things in the c_7].[end if]".
The cubicle part 1 is some text that varies. The cubicle part 1 is "[if c_7 is open and the c_7 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The cubicle part 2 is some text that varies. The cubicle part 2 is " You lean against the wall, inadvertently pressing a secret button. The wall opens up to reveal a bookshelf. You wonder idly who left that here. The bookshelf is usual.[if there is something on the s_10] On the bookshelf you see [a list of things on the s_10].[end if]".
The cubicle part 3 is some text that varies. The cubicle part 3 is "[if there is nothing on the s_10] But oh no! there's nothing on this piece of junk. It would have been so cool if there was stuff on the bookshelf.[end if]".
The cubicle part 4 is some text that varies. The cubicle part 4 is " You see a mantle. The mantle is typical.[if there is something on the s_11] On the mantle you can make out [a list of things on the s_11].[end if]".
The cubicle part 5 is some text that varies. The cubicle part 5 is "[if there is nothing on the s_11] But the thing hasn't got anything on it.[end if]".
The cubicle part 6 is some text that varies. The cubicle part 6 is "

 There is [if d_3 is open]an open[otherwise]a closed[end if]".
The cubicle part 7 is some text that varies. The cubicle part 7 is " Canadian limited edition gate leading south. There is [if d_4 is open]an open[otherwise]a closed[end if]".
The cubicle part 8 is some text that varies. The cubicle part 8 is " gate leading north.".
The description of r_15 is "[cubicle part 0][cubicle part 1][cubicle part 2][cubicle part 3][cubicle part 4][cubicle part 5][cubicle part 6][cubicle part 7][cubicle part 8]".

south of r_15 and north of r_16 is a door called d_3.
north of r_15 and south of r_11 is a door called d_4.
Understand "lounge" as r_18.
The internal name of r_18 is "lounge".
The printed name of r_18 is "-= Lounge =-".
The lounge part 0 is some text that varies. The lounge part 0 is "You have entered a lounge. Not the lounge you'd expect. No, this is a lounge. Okay, just remember what you're here to do, and everything will go great.



There is an exit to the north. Don't worry, it is unblocked.".
The description of r_18 is "[lounge part 0]".

The r_17 is mapped north of r_18.
Understand "garage" as r_19.
The internal name of r_19 is "garage".
The printed name of r_19 is "-= Garage =-".
The garage part 0 is some text that varies. The garage part 0 is "You arrive in a garage. A typical kind of place.



You need an unblocked exit? You should try going north.".
The description of r_19 is "[garage part 0]".

The r_16 is mapped north of r_19.
Understand "kitchenette" as r_8.
The internal name of r_8 is "kitchenette".
The printed name of r_8 is "-= Kitchenette =-".
The kitchenette part 0 is some text that varies. The kitchenette part 0 is "You find yourself in a kitchenette. A standard one. You decide to just list off a complete list of everything you see in the room, because hey, why not?



You need an unguarded exit? You should try going north.".
The description of r_8 is "[kitchenette part 0]".

The r_7 is mapped north of r_8.

The c_0 and the c_1 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 are containers.
The c_0 and the c_1 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 are privately-named.
The d_10 and the d_5 and the d_6 and the d_4 and the d_3 and the d_2 and the d_9 and the d_7 and the d_8 and the d_1 and the d_0 are doors.
The d_10 and the d_5 and the d_6 and the d_4 and the d_3 and the d_2 and the d_9 and the d_7 and the d_8 and the d_1 and the d_0 are privately-named.
The f_0 are foods.
The f_0 are privately-named.
The k_0 are keys.
The k_0 are privately-named.
The o_0 are object-likes.
The o_0 are privately-named.
The r_10 and the r_6 and the r_12 and the r_17 and the r_16 and the r_3 and the r_2 and the r_4 and the r_14 and the r_5 and the r_9 and the r_7 and the r_13 and the r_0 and the r_1 and the r_11 and the r_15 and the r_18 and the r_19 and the r_8 are rooms.
The r_10 and the r_6 and the r_12 and the r_17 and the r_16 and the r_3 and the r_2 and the r_4 and the r_14 and the r_5 and the r_9 and the r_7 and the r_13 and the r_0 and the r_1 and the r_11 and the r_15 and the r_18 and the r_19 and the r_8 are privately-named.
The s_0 and the s_1 and the s_10 and the s_11 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 and the s_8 and the s_9 are supporters.
The s_0 and the s_1 and the s_10 and the s_11 and the s_2 and the s_3 and the s_4 and the s_5 and the s_6 and the s_7 and the s_8 and the s_9 are privately-named.

The description of d_10 is "The portal looks towering. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_10 is "portal".
Understand "portal" as d_10.
The d_10 is open.
The description of d_5 is "The door looks towering. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_5 is "door".
Understand "door" as d_5.
The d_5 is open.
The description of d_6 is "The passageway looks rugged. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_6 is "passageway".
Understand "passageway" as d_6.
The d_6 is open.
The description of d_4 is "The gate looks manageable. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_4 is "gate".
Understand "gate" as d_4.
The d_4 is open.
The description of d_3 is "it's a towering Canadian limited edition gate [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_3 is "Canadian limited edition gate".
Understand "Canadian limited edition gate" as d_3.
Understand "Canadian" as d_3.
Understand "limited" as d_3.
Understand "edition" as d_3.
Understand "gate" as d_3.
The d_3 is locked.
The description of d_2 is "it's a manageable hatch [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_2 is "hatch".
Understand "hatch" as d_2.
The d_2 is open.
The description of d_9 is "it's a robust gateway [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_9 is "gateway".
Understand "gateway" as d_9.
The d_9 is open.
The description of d_7 is "it's a manageable gate [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_7 is "wooden gate".
Understand "wooden gate" as d_7.
Understand "wooden" as d_7.
Understand "gate" as d_7.
The d_7 is open.
The description of d_8 is "The wooden portal looks grand. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_8 is "wooden portal".
Understand "wooden portal" as d_8.
Understand "wooden" as d_8.
Understand "portal" as d_8.
The d_8 is open.
The description of d_1 is "it is what it is, a walnut portal [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of d_1 is "walnut portal".
Understand "walnut portal" as d_1.
Understand "walnut" as d_1.
Understand "portal" as d_1.
The d_1 is open.
The description of d_0 is "The wooden door looks rugged. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_0 is "wooden door".
Understand "wooden door" as d_0.
Understand "wooden" as d_0.
Understand "door" as d_0.
The d_0 is open.
The description of c_0 is "The display looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_0 is "display".
Understand "display" as c_0.
The c_0 is in r_10.
The c_0 is closed.
The description of c_1 is "The cabinet looks strong, and impossible to destroy. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_1 is "cabinet".
Understand "cabinet" as c_1.
The c_1 is in r_12.
The c_1 is open.
The description of c_2 is "The bureau looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_2 is "bureau".
Understand "bureau" as c_2.
The c_2 is in r_17.
The c_2 is closed.
The description of c_3 is "The fridge looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_3 is "fridge".
Understand "fridge" as c_3.
The c_3 is in r_5.
The c_3 is closed.
The description of c_4 is "The freezer looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_4 is "freezer".
Understand "freezer" as c_4.
The c_4 is in r_5.
The c_4 is closed.
The description of c_5 is "The crate looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_5 is "crate".
Understand "crate" as c_5.
The c_5 is in r_9.
The c_5 is closed.
The description of c_6 is "The case looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_6 is "case".
Understand "case" as c_6.
The c_6 is in r_13.
The c_6 is open.
The description of c_7 is "The locker looks strong, and impossible to crack. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_7 is "locker".
Understand "locker" as c_7.
The c_7 is in r_15.
The c_7 is closed.
The description of f_0 is "that's a standard fondue!".
The printed name of f_0 is "fondue".
Understand "fondue" as f_0.
The f_0 is in r_14.
The description of k_0 is "The Canadian limited edition latchkey is cold to the touch".
The printed name of k_0 is "Canadian limited edition latchkey".
Understand "Canadian limited edition latchkey" as k_0.
Understand "Canadian" as k_0.
Understand "limited" as k_0.
Understand "edition" as k_0.
Understand "latchkey" as k_0.
The k_0 is in r_18.
The matching key of the d_3 is the k_0.
The description of o_0 is "The butterfly appears to fit in here".
The printed name of o_0 is "butterfly".
Understand "butterfly" as o_0.
The o_0 is in r_10.
The description of s_0 is "The bed stand is solidly built.".
The printed name of s_0 is "bed stand".
Understand "bed stand" as s_0.
Understand "bed" as s_0.
Understand "stand" as s_0.
The s_0 is in r_6.
The description of s_1 is "The stand is unstable.".
The printed name of s_1 is "stand".
Understand "stand" as s_1.
The s_1 is in r_12.
The description of s_10 is "The bookshelf is solidly built.".
The printed name of s_10 is "bookshelf".
Understand "bookshelf" as s_10.
The s_10 is in r_15.
The description of s_11 is "The mantle is solidly built.".
The printed name of s_11 is "mantle".
Understand "mantle" as s_11.
The s_11 is in r_15.
The description of s_2 is "The chair is stable.".
The printed name of s_2 is "chair".
Understand "chair" as s_2.
The s_2 is in r_12.
The description of s_3 is "The mantelpiece is shaky.".
The printed name of s_3 is "mantelpiece".
Understand "mantelpiece" as s_3.
The s_3 is in r_16.
The description of s_4 is "The desk is solid.".
The printed name of s_4 is "desk".
Understand "desk" as s_4.
The s_4 is in r_16.
The description of s_5 is "The table is balanced.".
The printed name of s_5 is "table".
Understand "table" as s_5.
The s_5 is in r_16.
The description of s_6 is "The workbench is stable.".
The printed name of s_6 is "workbench".
Understand "workbench" as s_6.
The s_6 is in r_4.
The description of s_7 is "The bench is undependable.".
The printed name of s_7 is "bench".
Understand "bench" as s_7.
The s_7 is in r_7.
The description of s_8 is "The counter is stable.".
The printed name of s_8 is "counter".
Understand "counter" as s_8.
The s_8 is in r_11.
The description of s_9 is "The board is wobbly.".
The printed name of s_9 is "board".
Understand "board" as s_9.
The s_9 is in r_11.


The player is in r_16.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "go east / go south / take Canadian limited edition latchkey / go north / go west / unlock Canadian limited edition gate with Canadian limited edition latchkey / open Canadian limited edition gate / go north / go north / go north / take butterfly"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the f_0:
		end the story; [Lost]
	else if The player is in r_10 and The player carries the o_0:
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

The objective part 0 is some text that varies. The objective part 0 is "I hope you're ready to go into rooms and interact with objects, because you've just entered TextWorld! Here is how to play! First off, try to go east. With that over with, try to go south. That done, ".
The objective part 1 is some text that varies. The objective part 1 is "lift the Canadian limited edition latchkey from the floor of the lounge. If you can get your hands on the Canadian limited edition latchkey, attempt to move north. Once you get through with that, move".
The objective part 2 is some text that varies. The objective part 2 is " west. Once you accomplish that, insert the Canadian limited edition latchkey into the Canadian limited edition gate's lock to unlock it. Then, open the Canadian limited edition gate within the studio".
The objective part 3 is some text that varies. The objective part 3 is ". And then, make an effort to go to the north. Then, take a trip north. That done, go to the north. If you can do that, retrieve the butterfly from the floor of the basement. Alright, thanks!".

An objective is some text that varies. The objective is "[objective part 0][objective part 1][objective part 2][objective part 3]".
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

