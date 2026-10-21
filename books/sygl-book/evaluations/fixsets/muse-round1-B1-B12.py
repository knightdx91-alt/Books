E=[("01","Balthazaar, or Bal to his friends, could not remember ever having a left hand.","Balthazaar Norheart, or Bal to his friends, was eighteen and could not remember ever having a left hand."),
("01","it landed on the solid concrete floor of the temple.","it landed on the solid stone floor of the temple."),
("04","Then Raizen, the storm originator, got one of his followers to kidnap a high priest of mine.","Then Raizen, the storm originator, had his own high priest kidnap a high priest of mine."),
("12","He wrote out eggs, toast, bacon and oatmeal, the same breakfast he'd had that morning, and dropped the sheet onto the silver.","He wrote out eggs, toast, bacon and oatmeal, breakfast at dinnertime, and dropped the sheet onto the silver."),
("14","It was nearly two hours before they came down the long gallery to the gray pedestal where it ended.","It was nearly two hours after leaving New Spring that they came down the long gallery to the gray pedestal where it ended."),
("15","They had decided Raizen ranked lowest of them, so dealing with her was his job.","They had decided Raizen ranked lowest of the four, so dealing with her was his job."),
("18","Once war was formally declared, neither originator could make another High Priest.","Once war was formally declared, neither originator could make another High Priest, nor any new priests."),
("18","The lake was near the end of the six weeks.","The lake was in the last week of the six."),
("18","she told him it had been adequate, and was pleased with herself all through breakfast.","she told him it had been adequate, and was pleased with herself all through breakfast.\n\nHer three Aurora felis flowers had not gone to waste, either. Ms. Summers kept her word and helped her brew the two potions before the seventy-two hours ran out."),
("21","Heath meant nothing to Bal.","The name meant nothing to Bal."),
("24","It was a small cask. Pale maple, a date on the lid, a fat new dent beside the stopper where the boot heel had gone in. They were pinning their lives on it.","It was a small cask. Pale maple, a date on the lid, the stopper driven back flush with the wood. They were pinning their lives on it."),
("25","The cask sat on the table opposite the bed, untouched since last night, with the fresh boot-heel dent in it.","The cask sat on the table opposite the bed, untouched since last night."),]
for ch,o,n in E:
    p=f"manuscript/chapter-{ch}.md"; t=open(p).read(); c=t.count(o)
    if c!=1: print("MISS",ch,c,o[:50]); continue
    open(p,'w').write(t.replace(o,n))
print("ok")
