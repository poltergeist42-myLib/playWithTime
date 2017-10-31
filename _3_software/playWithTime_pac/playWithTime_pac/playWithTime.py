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
    :Version:            20171031-dev

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
from devchk_pac.devchk import C_DebugMsg as dbg

__all__ = ["C_PlayWithTime", "C_Pwt_Clk", "C_Pwt_U"]

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
        
        
    @dbg()
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
            
        
    @dbg()
    def f_getCumulTime( self ) : 
        """ retourne '_d_cumulTime' """
        return self._d_cumulTime

        
    @dbg()
    def f_setDiff( self, v_prev, v_now  ) :
        """ Définit la variable  _v_diff. c'est le résultat de 
            'v_prev' - 'v_now'
        """
        self._v_diff =  v_now - v_prev

        
    @dbg()
    def f_getDiff( self ) :
        """ Retourne '_v_diff' """
        return self._v_diff
        
        
    @dbg()
    def f_setPrev( self, v_prev ) :
        """ Définit la variable  '_v_prev'. C'est la référence de temps la plus ancienne.
        """
        if self.f_getFlag() == "down" :
            self._v_prev = v_prev
            self.f_setFlag( "up" )
        
        
    @dbg()
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
                
        
        
    @dbg()
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
        
        
    @dbg()
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
        self._v_understandingBaseTime   = ""
        self._v_understandingPrev       = ""
        self._v_understandingNow        = ""
        self._v_understandingValue      = ""
        self._v_understandingRound      = ""
        

    def f_raz( self ) :
        """ Remet toutes les variables 'Understanding' à zéro ("") """
        self._v_understandingBaseTime   = ""
        self._v_understandingPrev       = ""
        self._v_understandingNow        = ""
        self._v_understandingValue      = ""
        self._v_understandingRound      = ""
        self.f_setFlag("up")
        
        
    def f_setUnderstandingBaseTime( self, v_timeType=False ) :
        """ Définit la variable '_v_understandingBaseTime'' qui permet à la méthode
            'understanding' d'utiliser une base de temps de type 'epoch' ou clk'.
            La valeur par défaut est "epoch".
        """
        if not v_timeType :
            v_timeType = "epoch"
        
        v_timeType = v_timeType.lower()
        if v_timeType == "epoch" :
            self._v_understandingBaseTime = "Epoch"
        elif v_timeType == "clk" :
            self._v_understandingBaseTime = "Clk"
        
            
    def f_getUnderstandingBaseTime( self ) :
        """ retourne '_v_understandingBaseTime' """
        if not self._v_understandingBaseTime :
            self.f_setUnderstandingBaseTime()
            
        return self._v_understandingBaseTime
        
        
    def f_setUnderstandingPrev( self, v_uPrev=False ) :
        """ Définit la variable '_v_understandingPrev' dans un format compréhensible
            sous la forme : str( xxh xxm xxs )
            
            N.B : Aucune action ne serat effectuée si self.f_setFlag est Vrai
        """
        if not self.f_getFlag() :
            v_baseTime = self.f_getUnderstandingBaseTime()
            v_evalSetFn = "self.f_set{}Prev".format( v_baseTime )
            eval( v_evalSetFn )()
            
            if not v_uPrev :
                self._v_understandingPrev = self.f_getUnderstandingNow()
            else :
                self._v_understandingPrev = v_uPrev
        
            self.f_setFlag( True )
        
        
    def f_getUnderstandingPrev( self ) :
        """ Retourne '_v_understandingPrev' """
        if not self._v_understandingPrev :
            self.f_setUnderstandingPrev()
            
        return self._v_understandingPrev
        
        
    def f_setUnderstandingNow( self ) :
        """ Définit la variable '_v_understandingNow' dans un format compréhensible
            sous la forme : str( xxh xxm xxs )
            
            N.B : Aucune action ne serat effectuée si self.f_setFlag et FAUX
        """
        if self.f_getFlag() :
            v_baseTime = self.f_getUnderstandingBaseTime()
            v_evalSetFn = "self.f_set{}Now".format( v_baseTime )
            eval( v_evalSetFn )()
            
            self._v_understandingNow = time.strftime('%H:%M:%S')
 
            self.f_setFlag( False )
            
            
    def f_getUnderstandingNow( self ) :
        """ Retourne '_v_understandingNow' """
        if not self._v_understandingNow :
            self.f_setUnderstandingNow
            
        return self._v_understandingNow
    
    
    def f_setUnderstandingValue( self, v_num=False ) :
        """ Définit la variable '_v_understandingValue' dans un format compréhensible
            sous la forme : str( xxh xxm xxs )
        """
        v_DeltaFinal = ""
        if not v_num :
            v_baseTime = self.f_getUnderstandingBaseTime()
            v_evalSetFn = "self.f_set{}Diff".format( v_baseTime )
            eval( v_evalSetFn )()
            
            v_evalGetFn = "self.f_get{}Diff".format( v_baseTime )
            v_num = eval( v_evalGetFn )()
        
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
            v_toStr = str(v_RestS)
            if len( v_toStr ) < 2 :
                v_DeltaFinal += '0' + v_toStr + "s"
            else :
                v_DeltaFinal += str(v_RestS) + "s"
        else :
            v_DeltaFinal += "00s"
            
        self._v_understandingValue = v_DeltaFinal
    
    
    def f_getUnderstandingValue( self ) :
        """ retourne '_v_understandingValue' """
        if not self._v_understandingValue :
            self.f_setUnderstandingValue()
            
        return self._v_understandingValue
        
        
    def f_setUnderstandingRound( self,  v_num=False ) :
        """ Définit la variable '_v_understandingRound' dans un format compréhensible
            sous la forme : str( xxh xxm xxs ). Cette variable est une valeur arrondie
            au quart d'heure près.
            
            **N.B** : Si la différence de temps est comprise entre 15 et 20 minute, 
            l’arrondie sera soit 1 quart d'heure, soit 1 tier.
        """
        v_DeltaFinal    = ""
        v_strM          = False
        if not v_num :
            v_baseTime = self.f_getUnderstandingBaseTime()
            v_evalSetFn = "self.f_set{}Diff".format( v_baseTime )
            eval( v_evalSetFn )()
            
            v_evalGetFn = "self.f_get{}Diff".format( v_baseTime )
            v_num = eval( v_evalGetFn )()
        
        v_IntH = v_num // 3600
        v_ModH = v_num%3600
        v_IntM = v_ModH // 60
        
        # if not v_IntH :
            # if (v_IntM < 20) and (v_IntM > 15) :
                # if v_ModH > 17.5 :
                    # v_DeltaFinal = "00h20m"
                # else :
                    # v_DeltaFinal = "00h15m"
        
                # self._v_understandingRound = v_DeltaFinal
                # break
        
        if v_IntM :
            if v_IntM <= 22.5 :
                v_strM = "15m"
                
            elif (v_IntM >= 22.5) and (v_IntM <= 37.5) :
                v_strM = "30m"
            
            elif (v_IntM >= 37.5) and (v_IntM <= 52.5) :
                v_IntM = "45m"
                
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
            
        self._v_understandingRound = v_DeltaFinal
    
    
    def f_getUnderstandingRound( self ) :
        """ retourne '_v_understandingRound' """
        return self._v_understandingRound
    
    
    def f_setUnderstandingFiFo( self ) :
        """ First_In, First_Out. Copie '_v_understandingNow' dans
            '_v_understandingPrev' et '_v_understandingNow' prend une nouvelle valeur. La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}FiFo".format( v_baseTime )
        eval( v_evalSetFn )()
        
        self.f_setUnderstandingPrev( self.f_getUnderstandingNow() )
        self.f_setUnderstandingNow()
        
        
    def f_getUnderstandingData( self ) :
        """ Retourne un tuple avec '_v_UnderstandingPrev', '_v_UnderstandingNow'
            et '_v_UnderstandingValue'
        """
        return (self.f_getUnderstandingPrev(), 
                self.f_getUnderstandingNow(),
                self.f_getUnderstandingValue()
                )

                
    def f_getUnderstandingDataBrut( self ) :
        """ Retourne toutes les données de 'undestanding' sous la forme d'un tuple """
        v_baseTime = self.f_getUnderstandingBaseTime()
        eval("self.f_set{}Diff".format( v_baseTime ))()
        v_evalGetFn = "self.f_get{}Diff".format( v_baseTime )
        v_diff = eval( v_evalGetFn )()
        
        return (    self.f_getUnderstandingPrev(),
                    self.f_getUnderstandingNow(),
                    v_diff
                )
                
####
    
def main() :
    """ fonction principale, permet de tester la librairie """
    
    ## DBG, à supprimer après la mise au point
    dbg(0)
    
    ## Main
    v_boucle = 5
    v_sleep = 3
    
    
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
    
if __name__ == '__main__':
    main()