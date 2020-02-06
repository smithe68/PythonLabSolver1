from tkinter import *

NaOH = 0.050

KHPMolarMass = 204.2

correctionVolumeFloat = 0.0

window = Tk()

window.title("KHP Lab")

window.geometry('800x800')

correctionVolumeText = Label(window, text="Calculate CO_2 correction volume", font=("Arial", 14))

correctionVolumeText.grid(column=0, row=0)

mLNaOHFirst = Label(window, text="mL NaOH trail 1")

mLNaOHFirst.grid(column=0, row=1)

mLNaOHFSecond = Label(window, text="mL NaOH trail 2")

mLNaOHFSecond.grid(column=0, row=2)

mLNaOHThird = Label(window, text="mL NaOH trail 3")

mLNaOHThird.grid(column=0, row=3)

mLResponseOne = Entry(window, width=18)

mLResponseOne.grid(column=2, row=1)

mLResponseTwo = Entry(window, width=18)

mLResponseTwo.grid(column=2, row=2)

mLResponseThree = Entry(window, width=18)

mLResponseThree.grid(column=2, row=3)

averageLBL = Label(window, text="average is = ")

averageLBL.grid(column=2, row=4)

correctionVolume = Label(window, text="correction volume= ")

correctionVolume.grid(column=2, row=5)

approxMText = Label(window, text="Approximate molarity of NaOH", font=("Arial", 14))

approxMText.grid(column=0, row=6)

mLNaOHInitialFirst = Label(window, text="Initial mL NaOH trail 1")

mLNaOHInitialFirst.grid(column=0, row=7)

mLNaOHFInitialSecond = Label(window, text="Initial mL NaOH trail 2")

mLNaOHFInitialSecond.grid(column=0, row=8)

mLNaOHInitialThird = Label(window, text="Initial mL NaOH trail 3")

mLNaOHInitialThird.grid(column=0, row=9)

mLResponseInitialOne = Entry(window, width=18)

mLResponseInitialOne.grid(column=1, row=7)

mLResponseInitialTwo = Entry(window, width=18)

mLResponseInitialTwo.grid(column=1, row=8)

mLResponseInitialThree = Entry(window, width=18)

mLResponseInitialThree.grid(column=1, row=9)

mLNaOHFinalFirst = Label(window, text="Final mL NaOH trail 1")

mLNaOHFinalFirst.grid(column=2, row=7)

mLNaOHFinalSecond = Label(window, text="Final mL NaOH trail 2")

mLNaOHFinalSecond.grid(column=2, row=8)

mLNaOHFinalThird = Label(window, text="Final mL NaOH trail 3")

mLNaOHFinalThird.grid(column=2, row=9)

mLResponseFinalOne = Entry(window, width=18)

mLResponseFinalOne.grid(column=3, row=7)

mLResponseFinalTwo = Entry(window, width=18)

mLResponseFinalTwo.grid(column=3, row=8)

mLResponseFinalThree = Entry(window, width=18)

mLResponseFinalThree.grid(column=3, row=9)

weightOneText = Label(window, text="KHP weight 1 (g)")

weightOneText.grid(column=5, row=7)

weightTwoText = Label(window, text="KHP weight 2 (g)")

weightTwoText.grid(column=5, row=8)

weightThreeText = Label(window, text="KHP weight 3 (g)")

weightThreeText.grid(column=5, row=9)

weightOne = Entry(window, width=18)

weightOne.grid(column=6, row=7)

weightTwo = Entry(window, width=18)

weightTwo.grid(column=6, row=8)

weightThree = Entry(window, width=18)

weightThree.grid(column=6, row=9)

volumeUsedOne = Label(window, text="Volume NaOH used trail 1= mL")

volumeUsedOne.grid(column=2, row=10)

volumeUsedTwo = Label(window, text="volume NaOH used trail 2= mL")

volumeUsedTwo.grid(column=2, row=11)

volumeUsedThree = Label(window, text="volume NaOH used trail 3 = mL")

volumeUsedThree.grid(column=2, row=12)

usedAverage = Label(window, text="Average Used mL= ")

usedAverage.grid(column=2, row=13)

molarityNaOHOne = Label(window, text="molarity of NaOH trial 1 = ")

molarityNaOHOne.grid(column=2, row=14)

molarityNaOHTwo = Label(window, text="molarity of NaOH trial 2 = ")

molarityNaOHTwo.grid(column=2, row=15)

molarityNaOHThree = Label(window, text="molarity of NaOH trial 3 = ")

molarityNaOHThree.grid(column=2, row=16)

molarityAverage = Label(window, text="Average Molarity = M")

molarityAverage.grid(column=2, row=17)


def calculate():
    # The ratio of NaOH to KHP is 1 to 1
    calcAvg = (float(mLResponseOne.get()) + float(mLResponseTwo.get()) + float(mLResponseThree.get())) / 3
    correctionVolumeFloat = calcAvg / 4
    averageLBL.configure(text="Average= " + str(calcAvg) + " mL")
    correctionVolume.configure(text="correction volume= " + str(calcAvg / 4) + " mL")

    V1 = float(mLResponseInitialOne.get()) - float(mLResponseFinalOne.get())
    V2 = float(mLResponseInitialTwo.get()) - float(mLResponseFinalTwo.get())
    V3 = float(mLResponseInitialThree.get()) - float(mLResponseFinalThree.get())

    useAverage = ((V1 - correctionVolumeFloat) + (V2 - correctionVolumeFloat) + (V3 - correctionVolumeFloat)) / 3

    KHPmol1 = (float(weightOne.get()) / KHPMolarMass)
    KHPmol2 = (float(weightTwo.get()) / KHPMolarMass)
    KHPmol3 = (float(weightThree.get()) / KHPMolarMass)

    NaOHMolarity1 = (KHPmol1) / ((V1 - correctionVolumeFloat)/1000)
    NaOHMolarity2 = (KHPmol2) / ((V2 - correctionVolumeFloat)/1000)
    NaOHMolarity3 = (KHPmol3) / ((V3 - correctionVolumeFloat)/1000)

    molarityAvg = (NaOHMolarity1 + NaOHMolarity2 + NaOHMolarity3) / 3

    volumeUsedOne.configure(text="Volume NaOH used trail 1 =" + str(V1) + " mL")
    volumeUsedTwo.configure(text="Volume NaOH used trail 2 = " + str(V2) + " mL")
    volumeUsedThree.configure(text="Volume NaOH used trail 3 = " + str(V3) + " mL")

    usedAverage.configure(text="average volume used = " + str(useAverage) + "ml")

    molarityNaOHOne.configure(text="Molarity of NaOH  trial 1 = " + str(NaOHMolarity1) + " M")
    molarityNaOHTwo.configure(text="Molarity of NaOH  trial 2 = " + str(NaOHMolarity2) + " M")
    molarityNaOHThree.configure(text="Molarity of NaOH  trial 3 = " + str(NaOHMolarity3) + " M")

    molarityAverage.configure(text="average NaOH Molarity = " + str(molarityAvg) + "M")




solverButton = Button(window, text="Do It All For ME", command=calculate)

solverButton.grid(column=0, row=10)

window.mainloop()
