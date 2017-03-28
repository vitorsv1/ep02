import random
def Batalha(meu,oponente):

    while ipmons[meu][vida] > 0 and ipmons[oponente][vida]>0:
        ipmons[oponente][vida] = ipmons[oponente][vida] - ipmons[meu][ataque] + ipmons[oponente][defesa]
        if ipmon[oponente][vida] <= 0:
            return("Você derrotou seu oponente!")
        else:
            ipmons[meu][vida] = ipmons[meu][vida] - ipmons[oponente][ataque] + ipmons[meu][defesa]
        if ipmons[meu][vida] <= 0:
            return("Você foi derrotado!")
        
