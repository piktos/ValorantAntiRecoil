import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import ast

def ParseRawData(ConfigFile):

    Count = 1
    BulletsData = {1 : [], 2 : [], 3 : []}
    File = open(ConfigFile, 'r')
    Lines = File.read().split('\n')
    for Line in Lines:
        if Line != '':
            ParsedLine = ast.literal_eval(Line)
            BulletsData[Count].append(ConvertPlotType(RelativeMouseMovement(ParsedLine)))
        else:
            Count += 1

    return BulletsData

def RelativeMouseMovement(Set):

    RelativeSet = []
    for i in range(len(Set) - 1):
        X = Set[i + 1][0] - Set[i][0]
        Y = Set[i + 1][1] - Set[i][1]
        RelativeSet.append((X, Y))

    return RelativeSet

def ConvertPlotType(RelativeSet):
    X = [val[0] for val in RelativeSet]
    Y = [val[1] for val in RelativeSet]
    PlotData = [X, Y]
    return PlotData

def ScatterXVariation(Data):

    ModifData = {2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : [], 10 : []}
    ConstantY = [0] * 4
    for Bullet in range(2, 11):
        for val in Data:
            ModifData[Bullet].append(val[0][Bullet - 2])

    plt.figure(figsize = [10, 8])
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.scatter(ModifData[i + 2], ConstantY)
        plt.title('Bullet : {} - {}'.format(i + 1, i + 2), fontsize = 8)
        plt.yticks([])

def ScatterYVariation(Data):

    ModifData = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
    ConstantX = [0] * 4
    for Bullet in range(2, 11):
        for val in Data:
            ModifData[Bullet].append(val[1][Bullet - 2])

    plt.figure(figsize=[8, 10])
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.scatter(ConstantX, ModifData[i + 2])
        plt.title('Bullet : {} - {}'.format(i + 1, i + 2), fontsize=8)
        plt.xticks([])

ParsedData = ParseRawData('Vandal.txt')
ScatterYVariation(ParsedData[1])
ScatterXVariation(ParsedData[1])
plt.show()