#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

    :Projet:             playWithTime
    :Nom du fichier:     playWithTime.py
    :dépôt GitHub:       https://github.com/poltergeist42-myLib/playWithTime.git
    :documentation:      https://poltergeist42-mylib.github.io/playWithTime/
    :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
    :Version:            20170909

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
        self._v_epochRefPrev            = 0
        self._v_epochRefNow             = 0
        slef._v_epochDiff               = 0
        
        ## Variables Clock : utilisées par time.clock()
        self._v_clkRefPrev              = 0.0
        self._v_clkRefNow               = 0.0
        self._v_clkRefDiff              = 0.0
        
        ## fomrat compréhensible des données
        self._v_understandingBaseTime   = "epoch"
        self._v_understandingRefPrev    = ""
        self._v_understandingRefNow     = ""
        self._v_understandingRefDiff    = ""
        
        
    def f_setEpochRefPrev( self, v_epochRefPrev=False ) :
        """ Définit la variable  '_v_epochRefPrev'. C'est la référence de temps 
            la plus anciennne
        """
        if not sv_epochRefPrev :
            self._v_epochRefPrev = self.f_getEpochRefNow()
        else :
            self._v_epochRefPrev = v_epochRefPrev
        
        
    def f_getEpochRefPrev( self ) :
        """ Retourne '_v_epochRefPrev' """
        if not self._v_epochRefPrev :
            self.f_setEpochRefPrev()
            
        return self._v_epochRefPrev
        
        
    def f_setEpochRefNow( self ) :
        """ Définit la variable  '_v_epochRefNow'. C'est  la référence de temps
            la plus récente
        """
        self._v_epochRefNow = time.time()
        if not self.f_getEpochRefPrev() :
            self.f_setEpochRefPrev(self._v_epochRefNow)
        
        
    def f_getEpochRefNow( self ) :
        """ Retourne '_v_epochRefNow' """
        if not self._v_epochRefNow :
            self.f_setEpochRefNow()
            
        return self._v_epochRefNow
        
        
    def f_setEpochRefDiff( self ) :
        """ Définit la variable  _v_epochDiff. c'est le resultat de 
            '_v_epochRefNow' - '_v_epochRefPrev'
        """
        self._v_epochDiff = self.f_getEpochRefNow()-self.f_getEpochRefPrev()
        
        
    def f_getEpochRefDiff( self ) :
        """ Retourne '_v_epochDiff' """
        if not self._v_epochDiff :
            self.f_setEpochRefDiff()
            
        return self._v_epochDiff
        
        
    def f_setEpochFiFo( self ) :
        """ First_In, First_Out. Copie '_v_epochRefNow' dans '_v_epochRefPrev' et
            '_v_epochRefNow' prend une nouvelle valeur. La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        self.f_setEpochRefDiff()
        self.f_setEpochRefPrev( self.f_getEpochRefNow() )
        self.f_setEpochRefNow()
        
        
    def f_getEpochPrevNowDiff( self ) :
        """ Retourne un tuple avec '_v_epochRefPrev', '_v_epochRefNow'
            et '_v_epochDiff'
        """
        return (self.f_getEpochRefPrev(), 
                self.f_getEpochRefNow(),
                self.f_getEpochRefDiff)

        
    def f_setClkRefPrev( self, v_clkRefPrev=False ) :
        """ Définit la variable  '_v_clkRefPrev'. C'est la référence de temps 
            la plus anciennne (en temp CPU depuis le début du process)
        """
        if not v_clkRefPrev :
            self._v_clkRefPrev = self.f_getClkRefNow()
        else :
            self._v_clkRefPrev = v_clkRefPrev
        
        
    def f_getClkRefPrev( self ) :
        """ Retourne '_v_clkRefPrev' """
        if not self._v_clkRefPrev :
            self.f_setClkRefPrev()
            
        return self._v_clkRefPrev
        
        
    def f_setClkRefNow( self ) :
        """ Définit la variable  '_v_clkRefNow'. C'est  la référence de temps
            la plus récente (en temp CPU depuis le début du process)
        """
        self._v_clkRefNow = time.time()
 
        
    def f_getClkRefNow( self ) :
        """ Retourne '_v_clkRefNow' """
        if not self._v_clkRefNow :
            self.f_setClkRefNow()
            
        return self._v_clkRefNow
        
        
    def f_setClkRefDiff( self ) :
        """ Définit la variable  _v_clkRefDiff. c'est le resultat de 
            '_v_clkRefNow' - '_v_clkRefPrev'
        """
        self._v_clkDiff = self.f_getClkRefNow()-self.f_getClkRefPrev()
        
        
    def f_getClkRefDiff( self ) :
        """ Retourne '_v_clkDiff' """
        if not self._v_clkDiff :
            self.f_setClkRefDiff()
            
        return self._v_clkDiff
        
        
    def f_setClkFiFo( self ) :
        """ First_In, First_Out. Copie '_v_clkRefNow' dans '_v_clkRefPrev' et
            '_v_clkRefNow' prend une nouvelle valeur  (en temp CPU depuis le début du
            process). La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        self.f_setClkRefDiff()
        self.f_setClkRefPrev( self.f_getClkRefNow() )
        self.f_setClkRefNow()
        
    def f_getClkPrevNowDiff( self ) :
        """ Retourne un tuple avec '_v_ClkRefPrev', '_v_ClkRefNow'
            et '_v_ClkDiff'
        """
        return (self.f_getClkRefPrev(), 
                self.f_getClkRefNow(),
                self.f_getClkRefDiff)
        
        
    def f_setUnderstandingBaseTime( self, v_timeType )
        """ Définit la variable '_v_understandingBaseTime'' qui permet au méthode
            'understanding' d'utiliser une base de temps de type 'epoch' ou clk'
        """
        v_timeType = v_timeType.lower()
        if v_timeType == "epoch" :
            self._v_understandingBaseTime = "Epoch"
        elif v_timeType == "clk" :
            self._v_understandingBaseTime = "Clk"
            
            
    def f_getUnderstandingBaseTime( self ) :
        """ retourne '_v_understandingBaseTime' """
        return self._v_understandingBaseTime
        
        
    def f_setUnderstandingRefPrev( self, v_uRefPrev=False ) :
        """ Définit la variable '_v_understandingRefPrev' dans un format comprehensible
            sous la forme : str( xxh xxm xxs )
        """
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}RefPrev".format( v_baseTime )
        eval( v_evalSetFn )()
        
        if not v_uRefPrev :
            self._v_understandingRefPrev = self.f_getUnderstandingRefNow()
        else :
            self._v_understandingRefPrev = v_uRefPrev
        
        
    def f_getUnderstandingRefPrev( self ) :
        """ Retourne '_v_understandingRefPrev' """
        if not self._v_understandingRefPrev :
            self.f_setUnderstandingRefPrev()
            
        return self._v_understandingRefPrev
        
        
    def f_setUnderstandingRefNow( self ) :
        """ Définit la variable '_v_understandingRefNow' dans un format comprehensible
            sous la forme : str( xxh xxm xxs )
        """
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}RefNow".format( v_baseTime )
        eval( v_evalSetFn )()
        
        self._v_understandingRefNow = time.strftime('%H:%M:%S')
 
            
    def f_getUnderstandingRefNow( self ) :
        """ Retourne '_v_understandingRefNow' """
        if not self._v_understandingRefNow :
            self.f_setUnderstandingRefNow
            
        return self._v_understandingRefNow
    
    
    def f_setUnderstandingRefDiff( self ) :
        """ Définit la variable '_v_understandingRefDiff' dans un format comprehensible
            sous la forme : str( xxh xxm xxs )
        """
        v_DeltaFinal = ""
        
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}RefDiff".format( v_baseTime )
        eval( v_evalSetFn )()
        
        v_evalGetFn = "self.f_get{}RefDiff".format( v_baseTime )
        v_uRefDiff = eval( v_evalGetFn )()
        
        ## Formatage des heures
        v_IntH = v_uRefDiff // 3600
        if v_IntH :
            v_toStr = str(v_IntH)
            if len( v_toStr ) < 2 :
                v_DeltaFinal = '0' + v_toStr + "h "
            else :
                v_DeltaFinal = v_toStr + "h"
        else :
            v_DeltaFinal = "00h "
            
        ## Formatage des minutes
        v_ModH = v_uRefDiff%3600
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
            
        self._v_understandingRefDiff = v_DeltaFinal
    
    
    def f_getUnderstandingRefDiff( self ) :
        """ retourne '_v_understandingRefDiff' """
        if not self._v_understandingRefDiff :
            self.f_setUnderstandingRefDiff()
            
        return self._v_understandingRefDiff
    
    
    def f_setUnderstandingRefFifo( self ) :
        """ First_In, First_Out. Copie '_v_understandingRefNow' dans
            '_v_understandingRefPrev' et '_v_understandingRefNow' prend une nouvelle valeur. La différence entre entre Pev et Now est calculée automatiquement avant chaque mouvement.
        """
        v_baseTime = self.f_getUnderstandingBaseTime()
        v_evalSetFn = "self.f_set{}RefFifo".format( v_baseTime )
        eval( v_evalSetFn )()
        
        self.f_setUnderstandingRefDiff()
        self.f_setUnderstandingRefPrev( self.f_getUnderstandingRefNow() )
        self.f_setUnderstandingRefNow()
        
        
    def f_getUnderstandingPrevNowDiff( self ) :
        """ Retourne un tuple avec '_v_UnderstandingRefPrev', '_v_UnderstandingRefNow'
            et '_v_UnderstandingDiff'
        """
        return (self.f_getUnderstandingRefPrev(), 
                self.f_getUnderstandingRefNow(),
                self.f_getUnderstandingRefDiff)

    
####
    
def main() :
    """ fonction principale, permtet de tester la librairie """
    ist=C_PlayWithTime()
    
    
if __name__ == '__main__':
    main()
