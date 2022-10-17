from tkinter import *
from tkinter import ttk

players = ["iCast",
	"Danielaibett",
	"Matatena",
	"brandyjm",
	"Dirty",
	"Nami Twinkies",
	"MrTroflex",
	"RivSV_",
	"Par0xyst",
	"UROH",
	"blo0dy8evans",
	"sushiifake",
	"Raven",
	"Ghost",
	"fnx",
	"TrikiBeats",
	"einargretch",
	"Adminssru",
	"ManelHC",
	"JulianDNS",
	"ElPuchuGaming",
	"Blvcky",
	"reyarturro",
	"JaViking",
	"M3ilon",
	"balleno",
	"Puqqi",
	"Beanskristy",
	"sietekeke",
	"Aliza",
	"Bebocho",
	"Strongls98",
	"PokRic",
	"ZakParanoia",
	"NachooSky",
	"Karenpinkwing",
	"Lucifer",
	"AnnPink_",
	"Foko-jotaro",
	"HaruHanamiVT",
	"Moont",
	"DnDiego",
	"Dansilvaph",
	"ElQueizo",
	"Samjiro_13",
	"DIL Ssj",
	"happysadkiddo",
	"shizuka1001",
	"Tomomi_uwu",
	"Sin Senal",
	"Macxco",
	"Daniel Urrea",
	"Kevin.db2020",
	"TroncoTueur",
	"Ediardo",
	"P A C M A N 17",
	"anabananna",
	"Karycatura",
	"Paulinowsky",
	"Mario Alvarado"]
players.sort()

fillInPlayers = ["jaeldraw (DONJ)",
	"LUISIRIANO",
	"BENJA700XD",
	"Bruno Gonz lez",
	"Lagito",
	"Shanksino"]
print(fillInPlayers)

buttonDict = {}
columnRowDict = {}
imageDict = {}
loserImageDict = {}
loserColumnRowDict = {}
loserButtonDict = {}
winnerImageDict = {}
replacementImageDict = {}


root = Tk()
root.title("Fall Guys Tournament")
root.attributes('-fullscreen',True)
root.geometry('1920x1080')

bckgrdimg = PhotoImage(file="./Background.png")
label = Label(
    root,
    image=bckgrdimg
)
label.place(x=0, y=0)


bannerFrame = ttk.Frame(root)
#root.config(bg='#000000')
bannerFrame.grid()
frame = Frame(root)#, bd=10)
frame.grid()
label2 = Label(
    frame,
    image=bckgrdimg
)
label2.place(x=0, y=0)

label3 = Label(
    bannerFrame,
    image=bckgrdimg
)
label3.place(x=0, y=0)

def changePicture(thisPlayer):
	BWimage = PhotoImage(file='./' + thisPlayer + '-BW.png')
	button = Button(frame, image=BWimage)
	loserImageDict[thisPlayer] = BWimage
	thisColumn = columnRowDict[thisPlayer][0]
	thisRow = columnRowDict[thisPlayer][1]
	loserButtonDict[thisPlayer] = button
	button.grid(column=thisColumn, row=thisRow, padx=20, pady=2)
def resetPlayers():
	pass
winnerRow = 2
def addWinner():
	global winnerRow
	if winnerRow < 12:
		winner = winnerEntry.get()
		replacement = replacementEntry.get()
		image = PhotoImage(file='./' + winner + '.png')
		winnerImageDict[winner] = image
		Button(frame, bg='yellow', image=image).grid(column=7, row=winnerRow, padx=20, pady=2)
		image = PhotoImage(file='./' + replacement + '.png')
		replacementImageDict[replacement] = image
		columnRowDict[replacement] = [columnRowDict[winner][0],columnRowDict[winner][1]]
		Button(frame, bg='yellow', image=image, command=lambda replacement=replacement: changePicture(replacement)).grid(column=columnRowDict[winner][0], row=columnRowDict[winner][1], padx=20, pady=2)
		for button in loserButtonDict:
			loserButtonDict[button].grid_remove()
		loserImageDict.clear()
		loserColumnRowDict.clear()
		loserButtonDict.clear()
		winnerEntry.delete(0, END)
		replacementEntry.delete(0, END)
		winnerRow = winnerRow + 1

banner = PhotoImage(file='./FallGuysTournament.png') 
Label(bannerFrame, image=banner).grid()

playerIndex = 0
for i in range(5):
	for j in range(1,13):
		image = PhotoImage(file='./' + players[playerIndex] + '.png')
		imageDict[players[playerIndex]] = image
		button = Button(frame, bg='yellow', image=image, command=lambda playerIndex=playerIndex: changePicture(players[playerIndex]))
		buttonDict[players[playerIndex]] = button
		button.grid(column=i, row=j, padx=20, pady=2)
		columnRowDict[players[playerIndex]] = [i,j]
		playerIndex = playerIndex + 1
Label(frame, text="").grid(column=6,padx=345)
winnerLabel = Label(frame, text="Enter winner here", font=("Arial", 25)).grid(column=6, row=5)
winnerEntry = Entry(frame)
winnerEntry.place(height=15, width=20)
winnerEntry.grid(column=6, row=6)

Label(frame, text="Enter replacement here", font=("Arial", 25)).grid(column=6, row=7)
replacementEntry = Entry(frame)
replacementEntry.place(height=15, width=20)
replacementEntry.grid(column=6, row=8)

Button(frame, text="submit", command= addWinner, height=5, width=20).grid(column=6, row=9)

#Button(frame, text="Reset Players", command= resetPlayers, height=5, width=20).grid(column=8, row=12) 
#for i in range(2,12):
	#Button(frame, image=image, command=lambda i=i: changePicture(7, i)).grid(column=7, row=i, padx=20, pady=2)
Label(frame, text="").grid(column=8,padx=100)
#ttk.Label(frame, text="Hello honey!").grid(column=0, row=0)
#ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
