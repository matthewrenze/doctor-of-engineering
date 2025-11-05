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


The r_10 and the r_4 and the r_12 and the r_13 and the r_15 and the r_16 and the r_17 and the r_2 and the r_1 and the r_3 and the r_0 and the r_5 and the r_6 and the r_9 and the r_8 and the r_11 and the r_14 and the r_18 and the r_19 and the r_7 are rooms.

Understand "sauna" as r_10.
The internal name of r_10 is "sauna".
The printed name of r_10 is "-= Sauna =-".
The sauna part 0 is some text that varies. The sauna part 0 is "You arrive in a sauna.



 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The sauna part 1 is some text that varies. The sauna part 1 is " hatch leading east. There is [if d_1 is open]an open[otherwise]a closed[end if]".
The sauna part 2 is some text that varies. The sauna part 2 is " gateway leading west. There is an exit to the north. Don't worry, it is unguarded. You don't like doors? Why not try going south, that entranceway is unblocked.".
The description of r_10 is "[sauna part 0][sauna part 1][sauna part 2]".

west of r_10 and east of r_4 is a door called d_1.
The r_11 is mapped south of r_10.
The r_16 is mapped north of r_10.
east of r_10 and west of r_12 is a door called d_0.
Understand "restroom" as r_4.
The internal name of r_4 is "restroom".
The printed name of r_4 is "-= Restroom =-".
The restroom part 0 is some text that varies. The restroom part 0 is "You find yourself in a restroom. A normal one.



 There is [if d_1 is open]an open[otherwise]a closed[end if]".
The restroom part 1 is some text that varies. The restroom part 1 is " gateway leading east. There is an exit to the north. Don't worry, it is unblocked. There is an unblocked exit to the south.".
The description of r_4 is "[restroom part 0][restroom part 1]".

The r_5 is mapped south of r_4.
The r_2 is mapped north of r_4.
east of r_4 and west of r_10 is a door called d_1.
Understand "vault" as r_12.
The internal name of r_12 is "vault".
The printed name of r_12 is "-= Vault =-".
The vault part 0 is some text that varies. The vault part 0 is "You find yourself in a vault. A standard kind of place.

 You can see a trunk.[if c_0 is open and there is something in the c_0] The trunk contains [a list of things in the c_0].[end if]".
The vault part 1 is some text that varies. The vault part 1 is "[if c_0 is open and the c_0 contains nothing] The trunk is empty, what a horrible day![end if]".
The vault part 2 is some text that varies. The vault part 2 is " You bend down to tie your shoe. When you stand up, you notice a counter. The counter is typical.[if there is something on the s_0] On the counter you see [a list of things on the s_0].[end if]".
The vault part 3 is some text that varies. The vault part 3 is "[if there is nothing on the s_0] But the thing is empty, unfortunately. It would have been so cool if there was stuff on the counter.[end if]".
The vault part 4 is some text that varies. The vault part 4 is " You can see a rack! The rack is ordinary.[if there is something on the s_1] On the rack you see [a list of things on the s_1].[end if]".
The vault part 5 is some text that varies. The vault part 5 is "[if there is nothing on the s_1] Looks like someone's already been here and taken everything off it, though.[end if]".
The vault part 6 is some text that varies. The vault part 6 is "

 There is [if d_0 is open]an open[otherwise]a closed[end if]".
The vault part 7 is some text that varies. The vault part 7 is " hatch leading west. You need an unblocked exit? You should try going east. There is an unblocked exit to the north. You need an unblocked exit? You should try going south.".
The description of r_12 is "[vault part 0][vault part 1][vault part 2][vault part 3][vault part 4][vault part 5][vault part 6][vault part 7]".

west of r_12 and east of r_10 is a door called d_0.
The r_14 is mapped south of r_12.
The r_15 is mapped north of r_12.
The r_13 is mapped east of r_12.
Understand "laundromat" as r_13.
The internal name of r_13 is "laundromat".
The printed name of r_13 is "-= Laundromat =-".
The laundromat part 0 is some text that varies. The laundromat part 0 is "I am sorry to announce that you are now in the laundromat.



You don't like doors? Why not try going north, that entranceway is unguarded. There is an unguarded exit to the west.".
The description of r_13 is "[laundromat part 0]".

The r_12 is mapped west of r_13.
The r_17 is mapped north of r_13.
Understand "dish-pit" as r_15.
The internal name of r_15 is "dish-pit".
The printed name of r_15 is "-= Dish-Pit =-".
The dish-pit part 0 is some text that varies. The dish-pit part 0 is "You find yourself in a dish-pit. A standard one.



You need an unblocked exit? You should try going east. You don't like doors? Why not try going south, that entranceway is unblocked. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_15 is "[dish-pit part 0]".

The r_16 is mapped west of r_15.
The r_12 is mapped south of r_15.
The r_17 is mapped east of r_15.
Understand "workshop" as r_16.
The internal name of r_16 is "workshop".
The printed name of r_16 is "-= Workshop =-".
The workshop part 0 is some text that varies. The workshop part 0 is "Ah, the workshop. This is some kind of workshop, really great ordinary vibes in this place, a wonderful ordinary atmosphere. Okay, just remember what you're here to do, and everything will go great.

 You lean against the wall, inadvertently pressing a secret button. The wall opens up to reveal a chair. The chair is usual.[if there is something on the s_2] On the chair you can see [a list of things on the s_2].[end if]".
The workshop part 1 is some text that varies. The workshop part 1 is "[if there is nothing on the s_2] But the thing hasn't got anything on it.[end if]".
The workshop part 2 is some text that varies. The workshop part 2 is "

There is an exit to the east. Don't worry, it is unblocked. There is an exit to the south. Don't worry, it is unblocked.".
The description of r_16 is "[workshop part 0][workshop part 1][workshop part 2]".

The r_10 is mapped south of r_16.
The r_15 is mapped east of r_16.
Understand "pantry" as r_17.
The internal name of r_17 is "pantry".
The printed name of r_17 is "-= Pantry =-".
The pantry part 0 is some text that varies. The pantry part 0 is "You arrive in a pantry. A standard one. Okay, just remember what you're here to do, and everything will go great.

 You can make out a display. Hmm. You always thought you'd be more excited to see a display in a room.[if c_1 is open and there is something in the c_1] The display contains [a list of things in the c_1].[end if]".
The pantry part 1 is some text that varies. The pantry part 1 is "[if c_1 is open and the c_1 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The pantry part 2 is some text that varies. The pantry part 2 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The pantry part 3 is some text that varies. The pantry part 3 is " portal leading north. There is an exit to the south. Don't worry, it is unguarded. There is an unblocked exit to the west.".
The description of r_17 is "[pantry part 0][pantry part 1][pantry part 2][pantry part 3]".

The r_15 is mapped west of r_17.
The r_13 is mapped south of r_17.
north of r_17 and south of r_18 is a door called d_2.
Understand "closet" as r_2.
The internal name of r_2 is "closet".
The printed name of r_2 is "-= Closet =-".
The closet part 0 is some text that varies. The closet part 0 is "You arrive in a closet. An usual kind of place. Let's see what's in here.

 You bend down to tie your shoe. When you stand up, you notice a toolbox.[if c_2 is open and there is something in the c_2] The toolbox contains [a list of things in the c_2].[end if]".
The closet part 1 is some text that varies. The closet part 1 is "[if c_2 is open and the c_2 contains nothing] The toolbox is empty, what a horrible day![end if]".
The closet part 2 is some text that varies. The closet part 2 is "

There is an exit to the north. Don't worry, it is unguarded. You need an unguarded exit? You should try going south. You don't like doors? Why not try going west, that entranceway is unblocked.".
The description of r_2 is "[closet part 0][closet part 1][closet part 2]".

The r_1 is mapped west of r_2.
The r_4 is mapped south of r_2.
The r_3 is mapped north of r_2.
Understand "attic" as r_1.
The internal name of r_1 is "attic".
The printed name of r_1 is "-= Attic =-".
The attic part 0 is some text that varies. The attic part 0 is "You're now in an attic. You begin to take stock of what's here.

 You make out [if c_3 is locked]a locked[else if c_3 is open]an opened[otherwise]a closed[end if]".
The attic part 1 is some text that varies. The attic part 1 is " suitcase close by.[if c_3 is open and there is something in the c_3] The suitcase contains [a list of things in the c_3].[end if]".
The attic part 2 is some text that varies. The attic part 2 is "[if c_3 is open and the c_3 contains nothing] What a letdown! The suitcase is empty![end if]".
The attic part 3 is some text that varies. The attic part 3 is "

You don't like doors? Why not try going east, that entranceway is unguarded. There is an exit to the north. Don't worry, it is unblocked. You don't like doors? Why not try going south, that entranceway is unguarded.".
The description of r_1 is "[attic part 0][attic part 1][attic part 2][attic part 3]".

The r_7 is mapped south of r_1.
The r_0 is mapped north of r_1.
The r_2 is mapped east of r_1.
Understand "bedroom" as r_3.
The internal name of r_3 is "bedroom".
The printed name of r_3 is "-= Bedroom =-".
The bedroom part 0 is some text that varies. The bedroom part 0 is "Ah, the bedroom. This is some kind of bedroom, really great typical vibes in this place, a wonderful typical atmosphere.



You don't like doors? Why not try going north, that entranceway is unblocked. You need an unblocked exit? You should try going south. There is an unblocked exit to the west.".
The description of r_3 is "[bedroom part 0]".

The r_0 is mapped west of r_3.
The r_2 is mapped south of r_3.
The r_9 is mapped north of r_3.
Understand "shower" as r_0.
The internal name of r_0 is "shower".
The printed name of r_0 is "-= Shower =-".
The shower part 0 is some text that varies. The shower part 0 is "Well, here we are in a shower. You can barely contain your excitement.

 You make out [if c_4 is locked]a locked[else if c_4 is open]an opened[otherwise]a closed[end if]".
The shower part 1 is some text that varies. The shower part 1 is " dresser.[if c_4 is open and there is something in the c_4] The dresser contains [a list of things in the c_4].[end if]".
The shower part 2 is some text that varies. The shower part 2 is "[if c_4 is open and the c_4 contains nothing] What a letdown! The dresser is empty![end if]".
The shower part 3 is some text that varies. The shower part 3 is " You smell an interesting smell, and follow it to a drawer. You idly wonder how they came up with the name TextWorld for this place. It's pretty fitting.[if c_5 is open and there is something in the c_5] The drawer contains [a list of things in the c_5].[end if]".
The shower part 4 is some text that varies. The shower part 4 is "[if c_5 is open and the c_5 contains nothing] The drawer is empty, what a horrible day![end if]".
The shower part 5 is some text that varies. The shower part 5 is "

There is an unguarded exit to the east. There is an exit to the north. Don't worry, it is unblocked. You need an unguarded exit? You should try going south.".
The description of r_0 is "[shower part 0][shower part 1][shower part 2][shower part 3][shower part 4][shower part 5]".

The r_1 is mapped south of r_0.
The r_8 is mapped north of r_0.
The r_3 is mapped east of r_0.
Understand "cookhouse" as r_5.
The internal name of r_5 is "cookhouse".
The printed name of r_5 is "-= Cookhouse =-".
The cookhouse part 0 is some text that varies. The cookhouse part 0 is "I am sorry to announce that you are now in the cookhouse.



There is an exit to the north. Don't worry, it is unblocked. You don't like doors? Why not try going west, that entranceway is unguarded.".
The description of r_5 is "[cookhouse part 0]".

The r_6 is mapped west of r_5.
The r_4 is mapped north of r_5.
Understand "scullery" as r_6.
The internal name of r_6 is "scullery".
The printed name of r_6 is "-= Scullery =-".
The scullery part 0 is some text that varies. The scullery part 0 is "You've stumbled into a typical room. Your mind races to think of what kind of room would be typical. And then it hits you. Of course. You're in the scullery.

 You can see a case.[if c_6 is open and there is something in the c_6] The case contains [a list of things in the c_6].[end if]".
The scullery part 1 is some text that varies. The scullery part 1 is "[if c_6 is open and the c_6 contains nothing] The case is empty! What a waste of a day![end if]".
The scullery part 2 is some text that varies. The scullery part 2 is " What's that over there? It looks like it's a cabinet.[if c_7 is open and there is something in the c_7] The cabinet contains [a list of things in the c_7]. You can't wait to tell the folks at home about this![end if]".
The scullery part 3 is some text that varies. The scullery part 3 is "[if c_7 is open and the c_7 contains nothing] What a letdown! The cabinet is empty![end if]".
The scullery part 4 is some text that varies. The scullery part 4 is "

You don't like doors? Why not try going east, that entranceway is unguarded. You need an unblocked exit? You should try going north.".
The description of r_6 is "[scullery part 0][scullery part 1][scullery part 2][scullery part 3][scullery part 4]".

The r_7 is mapped north of r_6.
The r_5 is mapped east of r_6.
Understand "salon" as r_9.
The internal name of r_9 is "salon".
The printed name of r_9 is "-= Salon =-".
The salon part 0 is some text that varies. The salon part 0 is "You arrive in a salon. A typical kind of place.

 You see [if c_8 is locked]a locked[else if c_8 is open]an opened[otherwise]a closed[end if]".
The salon part 1 is some text that varies. The salon part 1 is " portmanteau.[if c_8 is open and there is something in the c_8] The portmanteau contains [a list of things in the c_8]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The salon part 2 is some text that varies. The salon part 2 is "[if c_8 is open and the c_8 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The salon part 3 is some text that varies. The salon part 3 is " Look over there! a mantle. [if there is something on the s_3]On the mantle you make out [a list of things on the s_3].[end if]".
The salon part 4 is some text that varies. The salon part 4 is "[if there is nothing on the s_3]But oh no! there's nothing on this piece of garbage.[end if]".
The salon part 5 is some text that varies. The salon part 5 is "

You don't like doors? Why not try going south, that entranceway is unblocked. You need an unguarded exit? You should try going west.".
The description of r_9 is "[salon part 0][salon part 1][salon part 2][salon part 3][salon part 4][salon part 5]".

The r_8 is mapped west of r_9.
The r_3 is mapped south of r_9.
Understand "garage" as r_8.
The internal name of r_8 is "garage".
The printed name of r_8 is "-= Garage =-".
The garage part 0 is some text that varies. The garage part 0 is "You find yourself in a garage. An usual one.



There is an unguarded exit to the east. There is an unblocked exit to the south.".
The description of r_8 is "[garage part 0]".

The r_0 is mapped south of r_8.
The r_9 is mapped east of r_8.
Understand "bedchamber" as r_11.
The internal name of r_11 is "bedchamber".
The printed name of r_11 is "-= Bedchamber =-".
The bedchamber part 0 is some text that varies. The bedchamber part 0 is "You arrive in a bedchamber. An ordinary kind of place.

 You see a chest.[if c_10 is open and there is something in the c_10] The chest contains [a list of things in the c_10].[end if]".
The bedchamber part 1 is some text that varies. The bedchamber part 1 is "[if c_10 is open and the c_10 contains nothing] The chest is empty! What a waste of a day![end if]".
The bedchamber part 2 is some text that varies. The bedchamber part 2 is " You lean against the wall, inadvertently pressing a secret button. The wall opens up to reveal a basket. Something scurries by right in the corner of your eye. Probably nothing.[if c_9 is open and there is something in the c_9] The basket contains [a list of things in the c_9]. Something scurries by right in the corner of your eye. Probably nothing.[end if]".
The bedchamber part 3 is some text that varies. The bedchamber part 3 is "[if c_9 is open and the c_9 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The bedchamber part 4 is some text that varies. The bedchamber part 4 is "

There is an exit to the north. Don't worry, it is unguarded.".
The description of r_11 is "[bedchamber part 0][bedchamber part 1][bedchamber part 2][bedchamber part 3][bedchamber part 4]".

The r_10 is mapped north of r_11.
Understand "kitchen" as r_14.
The internal name of r_14 is "kitchen".
The printed name of r_14 is "-= Kitchen =-".
The kitchen part 0 is some text that varies. The kitchen part 0 is "Well, here we are in the kitchen. You decide to just list off a complete list of everything you see in the room, because hey, why not?

 You see a table. The table is normal.[if there is something on the s_4] On the table you can make out [a list of things on the s_4]. There's something strange about this thing being here, but you don't have time to worry about that now.[end if]".
The kitchen part 1 is some text that varies. The kitchen part 1 is "[if there is nothing on the s_4] But the thing is empty, unfortunately.[end if]".
The kitchen part 2 is some text that varies. The kitchen part 2 is "

There is an unblocked exit to the north.".
The description of r_14 is "[kitchen part 0][kitchen part 1][kitchen part 2]".

The r_12 is mapped north of r_14.
Understand "studio" as r_18.
The internal name of r_18 is "studio".
The printed name of r_18 is "-= Studio =-".
The studio part 0 is some text that varies. The studio part 0 is "You find yourself in a studio. A standard one.

 You see a Canadian locker. Huh, weird.[if c_11 is open and there is something in the c_11] The Canadian locker contains [a list of things in the c_11].[end if]".
The studio part 1 is some text that varies. The studio part 1 is "[if c_11 is open and the c_11 contains nothing] The Canadian locker is empty, what a horrible day![end if]".
The studio part 2 is some text that varies. The studio part 2 is "

 There is [if d_2 is open]an open[otherwise]a closed[end if]".
The studio part 3 is some text that varies. The studio part 3 is " portal leading south. You don't like doors? Why not try going north, that entranceway is unguarded.".
The description of r_18 is "[studio part 0][studio part 1][studio part 2][studio part 3]".

south of r_18 and north of r_17 is a door called d_2.
The r_19 is mapped north of r_18.
Understand "cubicle" as r_19.
The internal name of r_19 is "cubicle".
The printed name of r_19 is "-= Cubicle =-".
The cubicle part 0 is some text that varies. The cubicle part 0 is "You are in a cubicle. A typical one.

 You make out a coffer.[if c_12 is open and there is something in the c_12] The coffer contains [a list of things in the c_12].[end if]".
The cubicle part 1 is some text that varies. The cubicle part 1 is "[if c_12 is open and the c_12 contains nothing] Empty! What kind of nightmare TextWorld is this?[end if]".
The cubicle part 2 is some text that varies. The cubicle part 2 is " You make out a safe.[if c_13 is open and there is something in the c_13] The safe contains [a list of things in the c_13]. There's something strange about this being here, but you can't put your finger on it.[end if]".
The cubicle part 3 is some text that varies. The cubicle part 3 is "[if c_13 is open and the c_13 contains nothing] The safe is empty! This is the worst thing that could possibly happen, ever![end if]".
The cubicle part 4 is some text that varies. The cubicle part 4 is " You see an armchair. The armchair is typical.[if there is something on the s_5] On the armchair you make out [a list of things on the s_5].[end if]".
The cubicle part 5 is some text that varies. The cubicle part 5 is "[if there is nothing on the s_5] The armchair appears to be empty. What, you think everything in TextWorld should have stuff on it?[end if]".
The cubicle part 6 is some text that varies. The cubicle part 6 is "

There is an unblocked exit to the south.".
The description of r_19 is "[cubicle part 0][cubicle part 1][cubicle part 2][cubicle part 3][cubicle part 4][cubicle part 5][cubicle part 6]".

The r_18 is mapped south of r_19.
Understand "spare room" as r_7.
The internal name of r_7 is "spare room".
The printed name of r_7 is "-= Spare Room =-".
The spare room part 0 is some text that varies. The spare room part 0 is "Of every spare room you could have walked into, you had to come round a standard one. The room seems oddly familiar, as though it were only superficially different from the other rooms in the building.



You don't like doors? Why not try going north, that entranceway is unblocked. There is an unguarded exit to the south.".
The description of r_7 is "[spare room part 0]".

The r_6 is mapped south of r_7.
The r_1 is mapped north of r_7.

The c_0 and the c_1 and the c_10 and the c_11 and the c_12 and the c_13 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are containers.
The c_0 and the c_1 and the c_10 and the c_11 and the c_12 and the c_13 and the c_2 and the c_3 and the c_4 and the c_5 and the c_6 and the c_7 and the c_8 and the c_9 are privately-named.
The d_0 and the d_1 and the d_2 are doors.
The d_0 and the d_1 and the d_2 are privately-named.
The f_0 are foods.
The f_0 are privately-named.
The k_0 and the k_1 are keys.
The k_0 and the k_1 are privately-named.
The o_0 are object-likes.
The o_0 are privately-named.
The r_10 and the r_4 and the r_12 and the r_13 and the r_15 and the r_16 and the r_17 and the r_2 and the r_1 and the r_3 and the r_0 and the r_5 and the r_6 and the r_9 and the r_8 and the r_11 and the r_14 and the r_18 and the r_19 and the r_7 are rooms.
The r_10 and the r_4 and the r_12 and the r_13 and the r_15 and the r_16 and the r_17 and the r_2 and the r_1 and the r_3 and the r_0 and the r_5 and the r_6 and the r_9 and the r_8 and the r_11 and the r_14 and the r_18 and the r_19 and the r_7 are privately-named.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 are supporters.
The s_0 and the s_1 and the s_2 and the s_3 and the s_4 and the s_5 are privately-named.

The description of d_0 is "it is what it is, a hatch [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_0 is "hatch".
Understand "hatch" as d_0.
The d_0 is open.
The description of d_1 is "The gateway looks towering. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_1 is "gateway".
Understand "gateway" as d_1.
The d_1 is open.
The description of d_2 is "it's a towering portal [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of d_2 is "portal".
Understand "portal" as d_2.
The d_2 is locked.
The description of c_0 is "The trunk looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_0 is "trunk".
Understand "trunk" as c_0.
The c_0 is in r_12.
The c_0 is locked.
The description of c_1 is "The display looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_1 is "display".
Understand "display" as c_1.
The c_1 is in r_17.
The c_1 is locked.
The description of c_10 is "The chest looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_10 is "chest".
Understand "chest" as c_10.
The c_10 is in r_11.
The c_10 is locked.
The description of c_11 is "The Canadian locker looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_11 is "Canadian locker".
Understand "Canadian locker" as c_11.
Understand "Canadian" as c_11.
Understand "locker" as c_11.
The c_11 is in r_18.
The c_11 is locked.
The description of c_12 is "The coffer looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_12 is "coffer".
Understand "coffer" as c_12.
The c_12 is in r_19.
The c_12 is locked.
The description of c_13 is "The safe looks strong, and impossible to destroy. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_13 is "safe".
Understand "safe" as c_13.
The c_13 is in r_19.
The c_13 is locked.
The description of c_2 is "The toolbox looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_2 is "toolbox".
Understand "toolbox" as c_2.
The c_2 is in r_2.
The c_2 is closed.
The description of c_3 is "The suitcase looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_3 is "suitcase".
Understand "suitcase" as c_3.
The c_3 is in r_1.
The c_3 is locked.
The description of c_4 is "The dresser looks strong, and impossible to break. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_4 is "dresser".
Understand "dresser" as c_4.
The c_4 is in r_0.
The c_4 is open.
The description of c_5 is "The drawer looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_5 is "drawer".
Understand "drawer" as c_5.
The c_5 is in r_0.
The c_5 is closed.
The description of c_6 is "The case looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_6 is "case".
Understand "case" as c_6.
The c_6 is in r_6.
The c_6 is locked.
The description of c_7 is "The cabinet looks strong, and impossible to destroy. [if open]It is open.[else if closed]It is closed.[otherwise]It is locked.[end if]".
The printed name of c_7 is "cabinet".
Understand "cabinet" as c_7.
The c_7 is in r_6.
The c_7 is open.
The description of c_8 is "The portmanteau looks strong, and impossible to crack. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_8 is "portmanteau".
Understand "portmanteau" as c_8.
The c_8 is in r_9.
The c_8 is open.
The description of c_9 is "The basket looks strong, and impossible to break. [if open]You can see inside it.[else if closed]You can't see inside it because the lid's in your way.[otherwise]There is a lock on it.[end if]".
The printed name of c_9 is "basket".
Understand "basket" as c_9.
The c_9 is in r_11.
The c_9 is locked.
The description of f_0 is "The licorice strip looks tantalizing.".
The printed name of f_0 is "licorice strip".
Understand "licorice strip" as f_0.
Understand "licorice" as f_0.
Understand "strip" as f_0.
The f_0 is in r_7.
The description of o_0 is "The manuscript seems out of place here".
The printed name of o_0 is "manuscript".
Understand "manuscript" as o_0.
The o_0 is in r_11.
The description of s_0 is "The counter is unstable.".
The printed name of s_0 is "counter".
Understand "counter" as s_0.
The s_0 is in r_12.
The description of s_1 is "The rack is unstable.".
The printed name of s_1 is "rack".
Understand "rack" as s_1.
The s_1 is in r_12.
The description of s_2 is "The chair is stable.".
The printed name of s_2 is "chair".
Understand "chair" as s_2.
The s_2 is in r_16.
The description of s_3 is "The mantle is shaky.".
The printed name of s_3 is "mantle".
Understand "mantle" as s_3.
The s_3 is in r_9.
The description of s_4 is "The table is unstable.".
The printed name of s_4 is "table".
Understand "table" as s_4.
The s_4 is in r_14.
The description of s_5 is "The armchair is durable.".
The printed name of s_5 is "armchair".
Understand "armchair" as s_5.
The s_5 is in r_19.
The description of k_0 is "The keycard is heavier than it looks.".
The printed name of k_0 is "keycard".
Understand "keycard" as k_0.
The k_0 is in the c_11.
The matching key of the d_2 is the k_0.
The description of k_1 is "The Canadian keycard is cold to the touch".
The printed name of k_1 is "Canadian keycard".
Understand "Canadian keycard" as k_1.
Understand "Canadian" as k_1.
Understand "keycard" as k_1.
The player carries the k_1.
The matching key of the c_11 is the k_1.


The player is in r_18.

The quest0 completed is a truth state that varies.
The quest0 completed is usually false.

Test quest0_0 with "unlock Canadian locker with Canadian keycard / open Canadian locker / take keycard from Canadian locker / unlock portal with keycard / open portal / go south / go south / go west / go west / go south / take manuscript"

Every turn:
	if quest0 completed is true:
		do nothing;
	else if The player carries the f_0:
		end the story; [Lost]
	else if The player is in r_11 and The player carries the o_0:
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

The objective part 0 is some text that varies. The objective part 0 is "It's time to explore the amazing world of TextWorld! First off, if it's not too much trouble, I need you to doublecheck that the Canadian locker is unlocked. After unlocking the Canadian locker, doubl".
The objective part 1 is some text that varies. The objective part 1 is "echeck that the Canadian locker within the studio is wide open. Then, pick up the keycard from the Canadian locker. And then, unlock the portal. Then, assure that the portal within the studio is wide ".
The objective part 2 is some text that varies. The objective part 2 is "open. After opening the portal, go to the south. After that, head south. After that, venture west. Next, try to head west. Then, attempt to take a trip south. With that accomplished, pick up the manus".
The objective part 3 is some text that varies. The objective part 3 is "cript from the floor of the bedchamber. Once that's all handled, you can stop!".

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

