#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

    :Projet:             playWithTime
    :Nom du fichier:     playWithTime.py
    :dépôt GitHub:       https://github.com/poltergeist42-myLib/playWithTime.git
    :documentation:      https://poltergeist42-mylib.github.io/playWithTime/
    :Auteur:            `Poltergeist42 <https://github.com/poltergeist42>`_
    :Version:            20171115

####

    :Licence:            CC-BY-NC-SA
    :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.6
    :framework:         
    
####

Descriptif
==========

    :Projet:            
                        
    :Fichiers:          

####

lexique
=======

    :**v_**:                 variable
    :**l_**:                 list
    :**t_**:                 tuple
    :**d_**:                 dictionnaire
    :**f_**:                 fonction
    :**C_**:                 Class
    :**i_**:                 Instance
    :**m_**:                 Matrice
   
####

Référence Web
=============

    * https://docs.python.org/3/library/time.html
    
####

Liste de Lib
============

    * time

"""
import time

## DBG, à supprimer après la mise au point
# from devchk_pac.devchk import C_DebugMsg as dbg

__all__ = ["C_PlayWithTime", "C_Pwt_U"]

class C_PlayWithTime( object ) :
    """ Class permettant de manipuler des éléments de type durée 
    
        **N.B** : Le format par défaut est 'Epoch'
    """
    
    def __init__( self, v_mode = "epoch" ) :
    
        self._v_mode                    = v_mode
    
        self._v_flag                    = "up"
        self._v_cumulValue              = 0.0
        self._d_cumulTime               = {}
        self._v_diff                    = 0.0
        self._v_prev                    = 0.0
        self._v_now                     = 0.0


    # @dbg()
    def f_raz(self ) :
        """ Remet toutes les variables à zéro """
        self._v_prev        = 0.0
        self._v_now         = 0.0
        self._v_diff        = 0.0
        self._v_cumulValue  = 0.0
        self._d_cumulTime   = {}

        self.f_setFlag("up")
        

    # @dbg()
    def f_setFlag( self, v_upDown ) :
        """ permet de 'lever' ou 'baisser' un drapeau (_v_flag) """
        if v_upDown :
            self._v_flag = "up"
        if (not v_upDown) or (v_upDown.lower() == "down") :
            self._v_flag = "down"

            
    # @dbg()
    def f_getFlag( self ) :
        """ retourne '_v_flag' """
        return self._v_flag
        
        
    # @dbg()
    def f_setCumulTime( self, v_value, v_key=None, v_subKey=None ) :
        """ Permet d'additionner les valeurs de 'v_value' dans 
            les clefs correspondantes (v_key).
            Si 'v_key' n'est pas renseignée, la clef par défaut sera : 'defaultCumulKey'
        """
        self._v_cumulValue += v_value 
        if not v_key :
            v_key = "defaultCumulKey"
            
        if not v_subKey :
            self._d_cumulTime[v_key] = self._v_cumulValue
        else :
            self._d_cumulTime[v_key] = {}
            self._d_cumulTime[v_key][v_subKey] = self._v_cumulValue
            
        
    # @dbg()
    def f_getCumulTime( self ) : 
        """ retourne '_d_cumulTime' """
        return self._d_cumulTime

        
    # @dbg()
    def f_setDiff( self, v_prev, v_now  ) :
        """ Définit la variable  _v_diff. c'est le résultat de 
            'v_prev' - 'v_now'
        """
        self._v_diff =  v_now - v_prev

        
    # @dbg()
    def f_getDiff( self ) :
        """ Retourne '_v_diff' """
        return self._v_diff
        
        
    # @dbg()
    def f_setPrev( self, v_prev ) :
        """ Définit la variable  '_v_prev'. C'est la référence de temps la plus ancienne.
        """
        if self.f_getFlag() == "down" :
            self._v_prev = v_prev
            self.f_setFlag( "up" )
        
        
    # @dbg()
    def f_getPrev( self ) :
        """ Retourne '_v_prev' """
        return self._v_prev
        
        
    # @dbg()
    def f_setNow( self ) :
        """ Définit la variable  '_v_now'. C'est  la référence de temps la plus récente.
        """
        if self.f_getFlag() == "up" :
            if self._v_mode == "epoch" :
                self._v_now = time.time()
            elif self._v_mode == "clk" :
                self._v_now = time.clock()
                
            self.f_setFlag( "down" )
                
            if not self.f_getPrev() :
                self.f_setPrev(self._v_now)
                
        
    # @dbg()
    def f_getNow( self ) :
        """ Retourne '_v_now' """
        return self._v_now
        
        
    # @dbg()
    def f_setFiFo( self ) :
        """ First_In, First_Out. Copie '_v_ow' dans '_v_prev' et
            '_v_now' prend une nouvelle valeur. La différence entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        self.f_setPrev( self.f_getNow() )
        self.f_setNow()
        v_p, v_n, _ = self.f_getData()
        self.f_setDiff(v_p, v_n)
        
        
    # @dbg()
    def f_getData( self ) :
        """ Retourne un tuple avec '_v_prev', '_v_now'
            et '_v_diff'
        """
        return (self.f_getPrev(), 
                self.f_getNow(),
                self.f_getDiff()
                )


####

class C_Pwt_U( C_PlayWithTime ) :
    def __init__( self ) :
        """ Init des varriables 'U' (Understanding) """
        super().__init__()
        
        ## format compréhensible des données
        self._v_uFlag       = "up"
        self._v_uPrev       = ""
        self._v_uNow        = ""
        self._v_uValue      = ""
        self._v_uRound      = ""
        

    def f_raz( self ) :
        """ Remet toutes les variables 'Understanding' à zéro ("") """
        super().f_raz()
        self._v_uPrev       = ""
        self._v_uNow        = ""
        self._v_uValue      = ""
        self._v_uRound      = ""
        
    # @dbg()
    def f_setFlagU( self, v_upDown ) :
        """ permet de 'lever' ou 'baisser' un drapeau (_v_flag) """
        if v_upDown :
            self._v_uFlag = "up"
        if (not v_upDown) or (v_upDown.lower() == "down") :
            self._v_uFlag = "down"

            
    # @dbg()
    def f_getFlagU( self ) :
        """ retourne '_v_flag' """
        return self._v_uFlag

        
        
    # @dbg()
    def f_setPrevU( self, v_uPrev, v_prev=False  ) :
        """ Définit la variable '_v_uPrev' dans un format compréhensible
            sous la forme : str( xxh xxm xxs )
            
            N.B : Aucune action ne serat effectuée si self.f_setFlag est Vrai
        """
        if self.f_getFlagU() == "down" :
            if  v_prev :
                self.f_setPrev(v_prev)
                
            self._v_uPrev = v_uPrev
            self.f_setFlagU( "up" )
        
        
    # @dbg()
    def f_getPrevU( self ) :
        """ Retourne '_v_uPrev' """
        return self._v_uPrev
        
        
    # @dbg()
    def f_setNowU( self ) :
        """ Définit la variable '_v_uNow' dans un format compréhensible
            sous la forme : str( xxh xxm xxs )
            
            N.B : Aucune action ne serat effectuée si self.f_setFlag et FAUX
        """
        if self.f_getFlagU() == "up" :
            self.f_setNow()
            self._v_uNow = time.strftime('%H:%M:%S')
            
            self.f_setFlagU( "down" )
            
            if not self.f_getPrevU() :
                self.f_setPrevU( self._v_uNow )
                
            
            
    # @dbg()
    def f_getNowU( self ) :
        """ Retourne '_v_Now' et '_v_uNow' """
        return self._v_uNow, self._v_now
    
    
    # @dbg()
    def f_setValue( self, v_num=False ) :
        """ Définit la variable '_v_uValue' dans un format compréhensible
            sous la forme : str( xxh xxm xxs )
        """
        v_DeltaFinal = ""
        if not v_num :
            # self.f_setDiff()
            v_num = self.f_getDiff()
        
        v_IntH = v_num // 3600
        v_ModH = v_num%3600
        v_IntM = v_ModH // 60

        ## Formatage des heures
        if v_IntH :
            v_toStr = str(v_IntH)
            if len( v_toStr ) < 2 :
                v_DeltaFinal = '0' + v_toStr + "h "
            else :
                v_DeltaFinal = v_toStr + "h"
        else :
            v_DeltaFinal = "00h "
            
        ## Formatage des minutes
        if v_IntM :
            v_toStr = str(v_IntM)
            if len( v_toStr ) < 2 :
                v_DeltaFinal += '0' + v_toStr + "m "
            else :
                v_DeltaFinal += v_toStr + "m "
        else :
            v_DeltaFinal += "00m "

        ## Formatage des secondes
        v_RestS = v_ModH % 60
        if v_RestS :
            v_toStr = str(round(v_RestS))
            if len( v_toStr ) < 2 :
                v_DeltaFinal += '0' + v_toStr + "s"
            else :
                v_DeltaFinal += v_toStr + "s"
        else :
            v_DeltaFinal += "00s"
            
        self._v_uValue = v_DeltaFinal
    
    
    # @dbg()
    def f_getValue( self ) :
        """ retourne '_v_uValue' """
        return self._v_uValue
        
        
    # @dbg()
    def f_setRound( self,  v_num=False ) :
        """ Définit la variable '_v_uRound' dans un format compréhensible
            sous la forme : str( xxh xxm xxs ). Cette variable est une valeur arrondie
            au quart d'heure près.
            
            **N.B** : Si la différence de temps est comprise entre 15 et 20 minute, 
            l’arrondie sera soit 1 quart d'heure, soit 1 tiers.
        """
        v_DeltaFinal    = ""
        v_strM          = False
        if not v_num :
            # self.f_setDiff()
            v_num = self.f_getDiff()
        
        v_IntH = v_num // 3600
        v_ModH = v_num%3600
        v_IntM = v_ModH // 60
        
        if v_IntM :
            if v_IntM <= 22.5 :
                v_strM = "15m"
                
            elif (v_IntM >= 22.5) and (v_IntM <= 37.5) :
                v_strM = "30m"
            
            elif (v_IntM >= 37.5) and (v_IntM <= 52.5) :
                v_strM = "45m"
                
            elif v_IntM >= 52.5 :
                v_strM  = "00m"
                v_IntH += 1
            
        if v_IntH :
            v_toStr = str(v_IntH)
            if len( v_toStr ) < 2 :
                v_DeltaFinal = '0' + v_toStr + "h "
            else :
                v_DeltaFinal = v_toStr + "h "
        else :
            if (v_IntM < 20) and (v_IntM > 15) :
                if v_ModH > 17.5 :
                    v_DeltaFinal = "00h20m"
                    v_strM = False
                else :
                    v_DeltaFinal = "00h15m"
                    v_strM = False
            else :
                v_DeltaFinal = "00h "
            
        if v_strM :
            v_DeltaFinal += v_strM
            
        self._v_uRound = v_DeltaFinal
    
    
    # @dbg()
    def f_getRound( self ) :
        """ retourne '_v_uRound' """
        return self._v_uRound
    
    
    # @dbg()
    def f_setFiFoU( self ) :
        """ First_In, First_Out. Copie '_v_uNow' dans
            '_v_uPrev' et '_v_uNow' prend une nouvelle valeur. La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        v_uNow, v_now = self.f_getNowU()
        self.f_setPrevU( v_uNow, v_now )
        self.f_setNowU()
        v_p, v_n, _ = self.f_getDataBrut()
        self.f_setDiff( v_p, v_n )
        
        
    # @dbg()
    def f_getDataU( self ) :
        """ Retourne un tuple avec '_v_UPrev', '_v_UNow'
            et '_v_UValue'
        """
        return (self.f_getPrevU(), 
                self.f_getNowU(),
                self.f_getValue(),
                self.f_getRound()
                )

                
    # @dbg()
    def f_getDataBrut( self ) :
        """ Retourne toutes les données de 'undestanding' sous la forme d'un tuple """
        return  super().f_getData()

       
####
    
def main() :
    """ fonction principale, permet de tester la librairie """
    
    ## DBG, à supprimer après la mise au point
    # dbg(1)
    
    ## Main
    v_boucle = 3
    v_sleep = 0.5

    v_boucleU = 3
    v_sleepU = 1
    
    
    ## C_PlayWithTime
    print( "\t## C_PlayWithTime ##\n" )
    i_ist = C_PlayWithTime()
    i_ist.f_raz()
    for i in range(v_boucle) :
        i_ist.f_setFiFo()
        v_p, v_n, v_d = i_ist.f_getData()
        i_ist.f_setCumulTime( v_d )
        print( f"prev : {v_p}, now: {v_n} diff : {v_d}, cumul : {i_ist.f_getCumulTime()}" )
        time.sleep( v_sleep )

    del(i_ist)
    
    print( "\n\t## C_Pwt_U ##" )
    u= C_Pwt_U()
    u.f_raz()
    for i in range(v_boucleU) :
        u.f_setFiFoU()
        _, _, v_d = u.f_getDataBrut()
        u.f_setCumulTime( v_d )
        u.f_setValue( u.f_getCumulTime()["defaultCumulKey"])
        u.f_setRound( u.f_getCumulTime()["defaultCumulKey"])
        v_p, v_n, v_v, v_r = u.f_getDataU()
        print( f"prev : {v_p}, now: {v_n[0]} diff : {v_d}, val : {v_v}, r : {v_r}" )
        time.sleep( v_sleepU )

    u.f_setRound( 4500 )
    print( f"h+m15 : {u.f_getRound()}" )

    u.f_setRound( 5400 )
    print( f"h+m30 : {u.f_getRound()}" )

    u.f_setRound( 6300 )
    print( f"h+m45 : {u.f_getRound()}" )

    u.f_setRound( 7200 )
    print( f"h2 : {u.f_getRound()}" )

    u.f_setRound( 8100 )
    print( f"h2+m15 : {u.f_getRound()}" )

    u.f_setRound( 40500 )
    print( f"h11+m15 : {u.f_getRound()}" )

    del( u )

    
if __name__ == '__main__':
    main()