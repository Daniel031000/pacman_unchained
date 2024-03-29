def wand_liste(anfangs_x, anfangs_y, breite, hoehe):
    raster_indizen = []
    for x in range(breite):
        for y in range(hoehe):
            raster_indizen.append([anfangs_x + x, anfangs_y + y])
    return raster_indizen


# gibt eine liste, die alle Koordinaten der Wandeinheiten enthaelt
def waende_liste(wand_position_liste):
    waende_raster_liste = []
    for wand in wand_position_liste:
        for wand_koordinate in wand_liste(wand[0], wand[1], wand[2], wand[3]):
            waende_raster_liste.append(wand_koordinate)
    return waende_raster_liste


# erstellt die Wände (blauen Teile) des Spielfelds
def BauL1(Spielfeld):  # Spielfeld von Level 1
    # Rand
    wand_position_liste = [
        [0, 0, 40, 1],
        [0, 19, 40, 1],
        [0, 1, 1, 18],
        [39, 1, 1, 18],
        [19, 1, 2, 1]
    ]
    for koordinate in waende_liste(wand_position_liste):
        Spielfeld[koordinate[0]][koordinate[1]] = 1

    # InneresLevel1 (nach jeder y Koordinate aufgeteilt)
    Spielfeld[19][1] = 1
    Spielfeld[20][1] = 1
    Spielfeld[2][2] = 1
    Spielfeld[3][2] = 1
    Spielfeld[4][2] = 1
    Spielfeld[5][2] = 1
    Spielfeld[6][2] = 1
    Spielfeld[8][2] = 1
    Spielfeld[9][2] = 1
    Spielfeld[10][2] = 1
    Spielfeld[12][2] = 1
    Spielfeld[13][2] = 1
    Spielfeld[14][2] = 1
    Spielfeld[16][2] = 1
    Spielfeld[17][2] = 1
    Spielfeld[19][2] = 1
    Spielfeld[20][2] = 1
    Spielfeld[22][2] = 1
    Spielfeld[23][2] = 1
    Spielfeld[25][2] = 1
    Spielfeld[26][2] = 1
    Spielfeld[27][2] = 1
    Spielfeld[29][2] = 1
    Spielfeld[30][2] = 1
    Spielfeld[31][2] = 1
    Spielfeld[33][2] = 1
    Spielfeld[34][2] = 1
    Spielfeld[35][2] = 1
    Spielfeld[36][2] = 1
    Spielfeld[37][2] = 1
    Spielfeld[2][3] = 1
    Spielfeld[3][3] = 1
    Spielfeld[4][3] = 1
    Spielfeld[5][3] = 1
    Spielfeld[6][3] = 1
    Spielfeld[8][3] = 1
    Spielfeld[14][3] = 1
    Spielfeld[16][3] = 1
    Spielfeld[17][3] = 1
    Spielfeld[19][3] = 1
    Spielfeld[20][3] = 1
    Spielfeld[22][3] = 1
    Spielfeld[23][3] = 1
    Spielfeld[25][3] = 1
    Spielfeld[31][3] = 1
    Spielfeld[33][3] = 1
    Spielfeld[34][3] = 1
    Spielfeld[35][3] = 1
    Spielfeld[36][3] = 1
    Spielfeld[37][3] = 1
    Spielfeld[8][4] = 1
    Spielfeld[10][4] = 1
    Spielfeld[11][4] = 1
    Spielfeld[12][4] = 1
    Spielfeld[14][4] = 1
    Spielfeld[16][4] = 1
    Spielfeld[17][4] = 1
    Spielfeld[22][4] = 1
    Spielfeld[23][4] = 1
    Spielfeld[25][4] = 1
    Spielfeld[27][4] = 1
    Spielfeld[28][4] = 1
    Spielfeld[29][4] = 1
    Spielfeld[31][4] = 1
    Spielfeld[2][5] = 1
    Spielfeld[3][5] = 1
    Spielfeld[4][5] = 1
    Spielfeld[5][5] = 1
    Spielfeld[6][5] = 1
    Spielfeld[10][5] = 1
    Spielfeld[11][5] = 1
    Spielfeld[12][5] = 1
    Spielfeld[16][5] = 1
    Spielfeld[17][5] = 1
    Spielfeld[19][5] = 1
    Spielfeld[20][5] = 1
    Spielfeld[22][5] = 1
    Spielfeld[23][5] = 1
    Spielfeld[27][5] = 1
    Spielfeld[28][5] = 1
    Spielfeld[29][5] = 1
    Spielfeld[33][5] = 1
    Spielfeld[34][5] = 1
    Spielfeld[35][5] = 1
    Spielfeld[36][5] = 1
    Spielfeld[37][5] = 1
    Spielfeld[2][6] = 1
    Spielfeld[3][6] = 1
    Spielfeld[4][6] = 1
    Spielfeld[5][6] = 1
    Spielfeld[6][6] = 1
    Spielfeld[16][6] = 1
    Spielfeld[17][6] = 1
    Spielfeld[19][6] = 1
    Spielfeld[20][6] = 1
    Spielfeld[22][6] = 1
    Spielfeld[23][6] = 1
    Spielfeld[33][6] = 1
    Spielfeld[34][6] = 1
    Spielfeld[35][6] = 1
    Spielfeld[36][6] = 1
    Spielfeld[37][6] = 1
    Spielfeld[8][6] = 1
    Spielfeld[14][6] = 1
    Spielfeld[25][6] = 1
    Spielfeld[31][6] = 1
    Spielfeld[8][7] = 1
    Spielfeld[9][7] = 1
    Spielfeld[10][7] = 1
    Spielfeld[12][7] = 1
    Spielfeld[13][7] = 1
    Spielfeld[14][7] = 1
    Spielfeld[16][7] = 1
    Spielfeld[17][7] = 1
    Spielfeld[19][7] = 1
    Spielfeld[20][7] = 1
    Spielfeld[22][7] = 1
    Spielfeld[23][7] = 1
    Spielfeld[25][7] = 1
    Spielfeld[26][7] = 1
    Spielfeld[27][7] = 1
    Spielfeld[29][7] = 1
    Spielfeld[30][7] = 1
    Spielfeld[31][7] = 1
    Spielfeld[1][8] = 1
    Spielfeld[2][8] = 1
    Spielfeld[3][8] = 1
    Spielfeld[4][8] = 1
    Spielfeld[5][8] = 1
    Spielfeld[34][8] = 1
    Spielfeld[35][8] = 1
    Spielfeld[36][8] = 1
    Spielfeld[37][8] = 1
    Spielfeld[38][8] = 1
    Spielfeld[7][9] = 1
    Spielfeld[8][9] = 1
    Spielfeld[9][9] = 1
    Spielfeld[10][9] = 1
    Spielfeld[11][9] = 1
    Spielfeld[12][9] = 1
    Spielfeld[14][9] = 1
    Spielfeld[15][9] = 1
    Spielfeld[16][9] = 1
    Spielfeld[17][9] = 1
    Spielfeld[18][9] = 1
    Spielfeld[19][9] = 1
    Spielfeld[20][9] = 1
    Spielfeld[21][9] = 1
    Spielfeld[22][9] = 1
    Spielfeld[23][9] = 1
    Spielfeld[24][9] = 1
    Spielfeld[25][9] = 1
    Spielfeld[27][9] = 1
    Spielfeld[28][9] = 1
    Spielfeld[29][9] = 1
    Spielfeld[30][9] = 1
    Spielfeld[31][9] = 1
    Spielfeld[32][9] = 1
    Spielfeld[1][10] = 1
    Spielfeld[2][10] = 1
    Spielfeld[3][10] = 1
    Spielfeld[4][10] = 1
    Spielfeld[5][10] = 1
    Spielfeld[34][10] = 1
    Spielfeld[35][10] = 1
    Spielfeld[36][10] = 1
    Spielfeld[37][10] = 1
    Spielfeld[38][10] = 1
    Spielfeld[8][11] = 1
    Spielfeld[9][11] = 1
    Spielfeld[10][11] = 1
    Spielfeld[12][11] = 1
    Spielfeld[13][11] = 1
    Spielfeld[14][11] = 1
    Spielfeld[16][11] = 1
    Spielfeld[17][11] = 1
    Spielfeld[19][11] = 1
    Spielfeld[20][11] = 1
    Spielfeld[22][11] = 1
    Spielfeld[23][11] = 1
    Spielfeld[25][11] = 1
    Spielfeld[26][11] = 1
    Spielfeld[27][11] = 1
    Spielfeld[29][11] = 1
    Spielfeld[30][11] = 1
    Spielfeld[31][11] = 1
    Spielfeld[2][12] = 1
    Spielfeld[3][12] = 1
    Spielfeld[4][12] = 1
    Spielfeld[5][12] = 1
    Spielfeld[6][12] = 1
    Spielfeld[8][12] = 1
    Spielfeld[14][12] = 1
    Spielfeld[16][12] = 1
    Spielfeld[17][12] = 1
    Spielfeld[19][12] = 1
    Spielfeld[20][12] = 1
    Spielfeld[22][12] = 1
    Spielfeld[23][12] = 1
    Spielfeld[25][12] = 1
    Spielfeld[31][12] = 1
    Spielfeld[33][12] = 1
    Spielfeld[34][12] = 1
    Spielfeld[35][12] = 1
    Spielfeld[36][12] = 1
    Spielfeld[37][12] = 1
    Spielfeld[2][13] = 1
    Spielfeld[3][13] = 1
    Spielfeld[4][13] = 1
    Spielfeld[5][13] = 1
    Spielfeld[6][13] = 1
    Spielfeld[8][13] = 1
    Spielfeld[10][13] = 1
    Spielfeld[11][13] = 1
    Spielfeld[12][13] = 1
    Spielfeld[14][12] = 1
    Spielfeld[16][13] = 1
    Spielfeld[17][13] = 1
    Spielfeld[19][13] = 1
    Spielfeld[20][13] = 1
    Spielfeld[22][13] = 1
    Spielfeld[23][13] = 1
    Spielfeld[25][13] = 1
    Spielfeld[27][13] = 1
    Spielfeld[28][13] = 1
    Spielfeld[29][13] = 1
    Spielfeld[31][13] = 1
    Spielfeld[33][13] = 1
    Spielfeld[34][13] = 1
    Spielfeld[35][13] = 1
    Spielfeld[36][13] = 1
    Spielfeld[37][13] = 1
    Spielfeld[10][14] = 1
    Spielfeld[11][14] = 1
    Spielfeld[12][14] = 1
    Spielfeld[16][14] = 1
    Spielfeld[17][14] = 1
    Spielfeld[19][14] = 1
    Spielfeld[20][14] = 1
    Spielfeld[22][14] = 1
    Spielfeld[23][14] = 1
    Spielfeld[27][14] = 1
    Spielfeld[28][14] = 1
    Spielfeld[29][14] = 1
    Spielfeld[2][15] = 1
    Spielfeld[3][15] = 1
    Spielfeld[4][15] = 1
    Spielfeld[5][15] = 1
    Spielfeld[6][15] = 1
    Spielfeld[8][15] = 1
    Spielfeld[10][15] = 1
    Spielfeld[11][15] = 1
    Spielfeld[12][15] = 1
    Spielfeld[14][15] = 1
    Spielfeld[16][15] = 1
    Spielfeld[17][15] = 1
    Spielfeld[22][15] = 1
    Spielfeld[23][15] = 1
    Spielfeld[25][15] = 1
    Spielfeld[27][15] = 1
    Spielfeld[28][15] = 1
    Spielfeld[29][15] = 1
    Spielfeld[31][15] = 1
    Spielfeld[33][15] = 1
    Spielfeld[34][15] = 1
    Spielfeld[35][15] = 1
    Spielfeld[36][15] = 1
    Spielfeld[37][15] = 1
    Spielfeld[2][16] = 1
    Spielfeld[3][16] = 1
    Spielfeld[4][16] = 1
    Spielfeld[5][16] = 1
    Spielfeld[6][16] = 1
    Spielfeld[8][16] = 1
    Spielfeld[14][16] = 1
    Spielfeld[16][16] = 1
    Spielfeld[17][16] = 1
    Spielfeld[19][16] = 1
    Spielfeld[20][16] = 1
    Spielfeld[22][16] = 1
    Spielfeld[23][16] = 1
    Spielfeld[25][16] = 1
    Spielfeld[31][16] = 1
    Spielfeld[33][16] = 1
    Spielfeld[34][16] = 1
    Spielfeld[35][16] = 1
    Spielfeld[36][16] = 1
    Spielfeld[37][16] = 1
    Spielfeld[2][17] = 1
    Spielfeld[3][17] = 1
    Spielfeld[4][17] = 1
    Spielfeld[5][17] = 1
    Spielfeld[6][17] = 1
    Spielfeld[8][17] = 1
    Spielfeld[9][17] = 1
    Spielfeld[10][17] = 1
    Spielfeld[12][17] = 1
    Spielfeld[13][17] = 1
    Spielfeld[14][17] = 1
    Spielfeld[16][17] = 1
    Spielfeld[17][17] = 1
    Spielfeld[19][17] = 1
    Spielfeld[20][17] = 1
    Spielfeld[22][17] = 1
    Spielfeld[23][17] = 1
    Spielfeld[25][17] = 1
    Spielfeld[26][17] = 1
    Spielfeld[27][17] = 1
    Spielfeld[29][17] = 1
    Spielfeld[30][17] = 1
    Spielfeld[31][17] = 1
    Spielfeld[33][17] = 1
    Spielfeld[34][17] = 1
    Spielfeld[35][17] = 1
    Spielfeld[36][17] = 1
    Spielfeld[37][17] = 1
    Spielfeld[19][19] = 1
    Spielfeld[20][19] = 1
