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
    :Version:            20170919

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

__all__ = ["C_PlayWithTime"]

class C_PlayWithTime( object ) :
    """ Class permettant de manipuler des éléments de type duréé """
    
    def __init__( self ) :
    
        ## Variables Epoch : utilisées par time.time()
        self._v_epochPrev                = 0.0
        self._v_epochNow                 = 0.0
        self._v_epochDiff                   = 0.0
        
        ## Variables Clock : utilisées par time.clock()
        self._v_clkPrev                  = 0.0
        self._v_clkNow                   = 0.0
        self._v_clkDiff                     = 0.0
        
        ## fomrat compréhensible des données
        self._v_understandingBaseTime       = ""
        self._v_understandingPrev        = ""
        self._v_understandingNow         = ""
        self._v_understandingDiff           = ""
        self._v_understandingRound   = ""
        

    def f_setEpochRAZ(self ) :
        """ Remet toutes les variables 'Epoch' à zéro """
        self._v_epochPrev   = 0.0
        self._v_epochNow    = 0.0
        self._v_epochDiff   = 0.0
        
        
    def f_setEpochPrev( self, v_epochPrev=False ) :
        """ Définit la variable  '_v_epochPrev'. C'est la référence de temps 
            la plus anciennne
        """
        if not v_epochPrev :
            self._v_epochPrev = self.f_getEpochNow()
        else :
            self._v_epochPrev = v_epochPrev
        
        
    def f_getEpochPrev( self ) :
        """ Retourne '_v_epochPrev' """
        if not self._v_epochPrev :
            self.f_setEpochPrev()
            
        return self._v_epochPrev
        
        
    def f_setEpochNow( self ) :
        """ Définit la variable  '_v_epochNow'. C'est  la référence de temps
            la plus récente
        """
        self._v_epochNow = time.time()
        if not self.f_getEpochPrev() :
            self.f_setEpochPrev(self._v_epochNow)
        
        
    def f_getEpochNow( self ) :
        """ Retourne '_v_epochNow' """
        if not self._v_epochNow :
            self.f_setEpochNow()
            
        return self._v_epochNow
        
        
    def f_setEpochDiff( self ) :
        """ Définit la variable  _v_epochDiff. c'est le resultat de 
            '_v_epochNow' - '_v_epochPrev'
        """
        self._v_epochDiff = self.f_getEpochNow()-self.f_getEpochPrev()
        
        
    def f_getEpochDiff( self ) :
        """ Retourne '_v_epochDiff' """
        if not self._v_epochDiff :
            self.f_setEpochDiff()
            
        return self._v_epochDiff
        
        
    def f_setEpochFiFo( self ) :
        """ First_In, First_Out. Copie '_v_epochNow' dans '_v_epochPrev' et
            '_v_epochNow' prend une nouvelle valeur. La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        self.f_setEpochDiff()
        self.f_setEpochPrev( self.f_getEpochNow() )
        self.f_setEpochNow()
        
        
    def f_getEpochPrevNowDiff( self ) :
        """ Retourne un tuple avec '_v_epochPrev', '_v_epochNow'
            et '_v_epochDiff'
        """
        return (self.f_getEpochPrev(), 
                self.f_getEpochNow(),
                self.f_getEpochDiff()
                )

                
    def f_setClkRAZ(self ) :
        """ Remet toutes les variables 'Clk' à zéro """
        self._v_clkPrev = 0.0
        self._v_clkNow  = 0.0
        self._v_clfDiff = 0.0
        

    def f_setClkPrev( self, v_clkPrev=False ) :
        """ Définit la variable  '_v_clkPrev'. C'est la référence de temps 
            la plus anciennne (en temp CPU depuis le début du process)
        """
        if not v_clkPrev :
            self._v_clkPrev = self.f_getClkNow()
        else :
            self._v_clkPrev = v_clkPrev
        
        
    def f_getClkPrev( self ) :
        """ Retourne '_v_clkPrev' """
        if not self._v_clkPrev :
            self.f_setClkPrev()
            
        return self._v_clkPrev
        
        
    def f_setClkNow( self ) :
        """ Définit la variable  '_v_clkNow'. C'est  la référence de temps
            la plus récente (en temp CPU depuis le début du process)
        """
        self._v_clkNow = time.time()
 
        
    def f_getClkNow( self ) :
        """ Retourne '_v_clkNow' """
        if not self._v_clkNow :
            self.f_setClkNow()
            
        return self._v_clkNow
        
        
    def f_setClkDiff( self ) :
        """ Définit la variable  _v_clkDiff. c'est le resultat de 
            '_v_clkNow' - '_v_clkPrev'
        """
        self._v_clkDiff = self.f_getClkNow()-self.f_getClkPrev()
        
        
    def f_getClkDiff( self ) :
        """ Retourne '_v_clkDiff' """
        if not self._v_clkDiff :
            self.f_setClkDiff()
            
        return self._v_clkDiff
        
        
    def f_setClkFiFo( self ) :
        """ First_In, First_Out. Copie '_v_clkNow' dans '_v_clkPrev' et
            '_v_clkNow' prend une nouvelle valeur  (en temp CPU depuis le début du
            process). La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        self.f_setClkDiff()
        self.f_setClkPrev( self.f_getClkNow() )
        self.f_setClkNow()
        
    def f_getClkPrevNowDiff( self ) :
        """ Retourne un tuple avec '_v_ClkPrev', '_v_ClkNow'
            et '_v_ClkDiff'
        """
        return (self.f_getClkPrev(), 
                self.f_getClkNow(),
                self.f_getClkDiff()
                )
        
        
    def f_setUnderstandingRAZ( self ) :
        """ Remet toutes les variables 'Understanding' à zéro ("") """
        self._v_understandingBaseTime   = ""
        self._v_understandingPrev       = ""
        self._v_understandingNow        = ""
        self._v_understandingDiff       = ""
        self._v_understandingRound  = ""
        
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
        """ Définit la variable '_v_understandingPrev' dans un format comprehensible
            sous la forme : str( xxh xxm xxs )
        """
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}Prev".format( v_baseTime )
        eval( v_evalSetFn )()
        
        if not v_uPrev :
            self._v_understandingPrev = self.f_getUnderstandingNow()
        else :
            self._v_understandingPrev = v_uPrev
        
        
    def f_getUnderstandingPrev( self ) :
        """ Retourne '_v_understandingPrev' """
        if not self._v_understandingPrev :
            self.f_setUnderstandingPrev()
            
        return self._v_understandingPrev
        
        
    def f_setUnderstandingNow( self ) :
        """ Définit la variable '_v_understandingNow' dans un format comprehensible
            sous la forme : str( xxh xxm xxs )
        """
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}Now".format( v_baseTime )
        eval( v_evalSetFn )()
        
        self._v_understandingNow = time.strftime('%H:%M:%S')
 
            
    def f_getUnderstandingNow( self ) :
        """ Retourne '_v_understandingNow' """
        if not self._v_understandingNow :
            self.f_setUnderstandingNow
            
        return self._v_understandingNow
    
    
    def f_setUnderstandingDiff( self ) :
        """ Définit la variable '_v_understandingDiff' dans un format comprehensible
            sous la forme : str( xxh xxm xxs )
        """
        v_DeltaFinal = ""
        
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}Diff".format( v_baseTime )
        eval( v_evalSetFn )()
        
        v_evalGetFn = "self.f_get{}Diff".format( v_baseTime )
        v_uDiff = eval( v_evalGetFn )()
        
        ## Formatage des heures
        v_IntH = v_uDiff // 3600
        if v_IntH :
            v_toStr = str(v_IntH)
            if len( v_toStr ) < 2 :
                v_DeltaFinal = '0' + v_toStr + "h "
            else :
                v_DeltaFinal = v_toStr + "h"
        else :
            v_DeltaFinal = "00h "
            
        ## Formatage des minutes
        v_ModH = v_uDiff%3600
        v_IntM = v_ModH // 60
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
            
        self._v_understandingDiff = v_DeltaFinal
    
    
    def f_getUnderstandingDiff( self ) :
        """ retourne '_v_understandingDiff' """
        if not self._v_understandingDiff :
            self.f_setUnderstandingDiff()
            
        return self._v_understandingDiff
        
        
    def f_setUnderstandingRound( self,  v_num=False) :
        """ Définit la variable '_v_understandingRound' dans un format comprehensible
            sous la forme : str( xxh xxm xxs ). Cette variable est une valeur arondie
            au quart d'heure près.
            **N.B : Si la différence de temps est comprise entre 15 et 20 minute, 
            l'arondie sera soit 1 quart d'heure, soit 1 tier.
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
        
        if not v_IntH :
            if (v_IntM < 20) and (v_IntM > 15) :
                if v_ModH > 17.5 :
                    v_DeltaFinal = "00h20m"
                else :
                    v_DeltaFinal = "00h15m"
        
                self._v_understandingRound = v_DeltaFinal
                break
        
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
            v_DeltaFinal = "00h "
            
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
        
        self.f_setUnderstandingDiff()
        self.f_setUnderstandingPrev( self.f_getUnderstandingNow() )
        self.f_setUnderstandingNow()
        
        
    def f_getUnderstandingPrevNowDiff( self ) :
        """ Retourne un tuple avec '_v_UnderstandingPrev', '_v_UnderstandingNow'
            et '_v_UnderstandingDiff'
        """
        return (self.f_getUnderstandingPrev(), 
                self.f_getUnderstandingNow(),
                self.f_getUnderstandingDiff()
                )

    
####
    
def main() :
    """ fonction principale, permtet de tester la librairie """
    v_boucle = 3
    v_sleep = 1
    
    ist=C_PlayWithTime()
    
    ist.f_setEpochRAZ()
    ist.f_setClkRAZ()
    ist.f_setUnderstandingRAZ()
    
    print( "\nEpoch" )
    for i in range( v_boucle ) :
        ist.f_setEpochFiFo()
        for j in ist.f_getEpochPrevNowDiff() :
            print( j )
            
        print( "\n" )
        time.sleep( v_sleep )
            
    ist.f_setEpochRAZ()
    ist.f_setClkRAZ()
    ist.f_setUnderstandingRAZ()
    
    print( "\nClk" )
    for i in range( v_boucle ) :
        ist.f_setClkFiFo()
        for j in ist.f_getClkPrevNowDiff() :
            print( j )

        print( "\n" )
        time.sleep( v_sleep )
        
    ist.f_setEpochRAZ()
    ist.f_setClkRAZ()
    ist.f_setUnderstandingRAZ()
    
    print( "\nUnderstanding" )
    for i in range( v_boucle ) :
        ist.f_setUnderstandingFiFo()
        for j in ist.f_getUnderstandingPrevNowDiff() :
            print( j )
            
        print( "\n" )
        time.sleep( v_sleep )
    
if __name__ == '__main__':
    main()