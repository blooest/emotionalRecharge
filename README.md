# emotionalRecharge
My attempt at re-evaluating the autonomy in this game, using a larger score delta to allow a bit more variety.
Made in the spirit of, and largely blatantly stealing the original work of, PTME's Emotional Overcharge.
At this stage, this thing overrides over a thousand XMLs. It's a massive undertaking, certainly.

Right now it's in very early testing mode. Each type of resource is separated into its own package, and there are some splits that'll get simplified for release.
Notably, "base" and "extension" major modules will probably be merged, and the resource types will certainly be.

Currently adjusts emotional scoring.
TODO: Evaluate each social mixer interaction and add scoring preferences for traits, social contexts, and relationship bits. Other interaction classes don't seem to allow these, sadly.
Here's a quick overview of each package and its purview.

--- base_*: The resources changed by PTME's original Emotional Overcharge.
buff: Changes scorings for certain interactions when affected by some Playful, Flirty, and Angry buffs.
interaction: Changes scorings for a lot of interactions depending on mood.

--- changeYourLife_*: Allows sims to autonomously make bad decisions that will permanently affect their life. Marriage and babies, mostly.
base_interaction: The additions from the Hardcore/Change Your Life version of the original mod, separated into a module.
extended_BG_interaction: Further additions I've made. Base game.
extended_GP01_interaction: Outdoor Retreat.
extended_GP02_interaction: Spa Day.

--- extended_*: Further additions I've made in the spirit of the original mod.
basic_interaction: These are mostly just taken from weebl_101's Autonomous Interactions mod, where they weren't already adjusted by EmOv. Not revalued yet. A lot will probably need to get shunted to the changeYourLife module as it gets adjusted and.. well, found to be working at all.
BG_buff: Additional Playful/Flirty/Angry buffs that were missed in the original.
BG_interaction: I should hope by now my naming convention makes sense. Because I'm going to stop listing packages that you should contextually know the purpose of using the description of others I've already listed.
BG_scomm: This one, though, is new, because static commodities are an addition to the parameterized autonomy that came about later on in the game's life. This attempts to make Sims a little less frantic to do things they shouldn't care so much about, like dancing. I've personally not quite figured this system out yet, so I'm not sure how effective it is.
EP01_interaction: Get to Work.
SP04_interaction: Spooky Stuff.

--- napper: In my testing, I found that Sims started to want to take naps constantly and forever due to the scoring changes, so I made this module to force a test of their energy levels for consideration. Stopped that nicely.

--- repairman: Autonomous repairs. I think I've made it a bit too appealing, as just about every sim in the house wants to go repair things when they break.

--- skiller: Perhaps the biggest changes I've made. Intended to make Sims perform more actions related to skills, more consistently, vs boring things like dancing and watching TV.
    In the process, starts to fix an oversight; the Away Actions were supposed to be picked based on what the Sims were doing, but absolutely nothing was properly tagged, so it always reset to Care For Self.
    WARNING: This makes Sims able to autonomously sell non-masterpiece paintings from the easel. Move them to the walls if you want to keep them.
BG_buff: Affects Inspired and Focused buffs, to push related skill interactions.
BG_interaction: Note that this removes the requirement that most of these interactions had, wherein they'd only be considered if the Sim had 2 in the skill in question.
BG_slottypeset: This contains the slot type set used for testing for selling paintings autonomously.

--- tvTime: Adds limitations to TV watching, and attempts to adjust the scoring so Sims won't just constantly go back to the TV instead of doing more interesting things.

--- writer: This module, requiring a script to inject new interactions into the SA lists, is something a bit different, and a bit broken.
   The attempt was to get Sims to write, autonomously. That bit works.
   However, it still prompts us for the name of the books, even for inactive Sims, and they do it way too much.
   It's also supposed to give them the ability to autonomously -resume- writing, which is supposed to score higher than starting a new one so they'll do that if they have the option.
   But they don't do that. At all.
   The script is unpacked, so put the full jay_emotionalRecharge_writer folder from its source folder in your base Mods folder if you want it to work.
   Also, I didn't include a package for it, so create that from the xmls too.
