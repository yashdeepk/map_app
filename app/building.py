def getBuilding(src):
	classdict = {
	"CS" : "Computer Science Building",
	"SGMH" : "Mihaylo",
	"PL" : "Pollak Library",
	"MH" : "McCarthy Hall",
	"E" : "Engineering Building",
	"H" : "Humanities-Social Sciences",
	"KHS" : "Kinesiology & Health Science"
	}
	abv = ""
	for i in src:
		if i != "-":
			abv = abv + i
		else:
		  break
	building = classdict[abv]
	return building


        



