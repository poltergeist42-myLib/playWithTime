#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

    :Projet:             playWithTime
    :Nom du fichier:     playWithDate.py
    :dépôt GitHub:       https://github.com/poltergeist42-myLib/playWithTime.git
    :documentation:      https://poltergeist42-mylib.github.io/playWithTime/
    :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
    :Version:            20170913

####

    :Licence:            CC-BY-NC-SA
    :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.4
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
    
    * https://fr.wikipedia.org/wiki/Date
    
    * https://www.englishclub.com/vocabulary/time-date.htm
    
####

Liste de Lib
============

    * time

"""

import time

__all__ = ["C_PlayWithDate"]

class C_PlayWithDate( object ) :
    """ Class permettant d'afficher et de manipuler les dates sous diférents format """
    def __init__( self ) :
        """ initiation des variables """
        ## Eléments de la date
        self._v_yy                  = ""
        self._v_mm                  = ""
        self._v_dd                  = ""
        self._v_month               = ""
        self._v_weekday             = ""
        
        ## variables retournées par les méthodes f_get*
        self._v_reverseShortFormat  = ""
        self._v_frShortFormat       = ""
        self._v_usShortFormat       = ""
        self._v_frLongFormat        = ""
        self._v_usLongFormat        = ""
        
        ## Dictionnaire de mise en forme
        self.d_weekday              = { "Monday":"Lundi",
                                        "Tuesday":"Mardi",
                                        "Wednesday":"Mercredi",
                                        "Thursday":"Jeudi",
                                        "Friday":"Vendredi",
                                        "Saturday":"Samedi",
                                        "Sunday":"Dimanche"
                                    }
                                    
        self._d_month               = { "January":"Janvier",
                                        "February":"Février",
                                        "March":"Mars",
                                        "April":"Avril",
                                        "May":"Mai",
                                        "June":"Juin",
                                        "July":"Juillet",
                                        "August":"Aout",
                                        "September":"Septembre",
                                        "October":"Octobre",
                                        "November":"Novembre",
                                        "December":"Décembre"
                                    }
                                    
        self._d_usDayNumber         = { "01":"1st", "02":"2nd",
                                        "03":"3rd", "04":"4th",
                                        "05":"5th", "06":"6th",
                                        "07":"7th", "08":"8th",
                                        "09":"9th", "10":"10th",
                                        "11":"11th", "12":"12th",
                                        "13":"13th", "14":"14th",
                                        "15":"15th", "16":"16th",
                                        "17":"17th", "18":"18th",
                                        "19":"19th", "20":"20th",
                                        "21":"21st", "22":"22nd",
                                        "23":"23rd", "24":"24th",
                                        "25":"25th", "26":"26th",
                                        "27":"27th", "28":"28th",
                                        "29":"29th", "30":"30th",
                                        "31":"31st"
                                    }

    def f_setDateItems( self, v_yy=False, v_mm=False, 
                        v_dd=False, v_month=False, v_weekday=False ) :
        """ Permet de définir l'année, le mois (int et str) et le jour (int et str).
            Ces données sont placées dans les variables '_v_yy', '_v_mm', 
            '_v_dd','_v_month',  '_v_weekday'
            
            Si l'un des argument n'est pas False, sa valeur sera utilisée pour définir
            la variable équivalent.
        """
        if v_yy :
            self._v_yy = v_yy
        else :
            self._v_yy = time.strftime( '%Y' )
        
        if v_mm :
            self._v_mm = v_mm
        else :
            self._v_mm = time.strftime( '%m' )
        
        if v_dd :
            self._v_dd = v_dd
        else :
            self._v_dd = time.strftime( '%d' )
            
        if v_month :
            self._v_month = v_month
        else :
            self._v_month = time.strftime( "%B" )
            
        if v_weekday :
            self._v_weekday = v_weekday
        else :
            self._v_weekday = time.strftime( "%A" )
        
        
    def f_getDateItems( self ) :
        """ retourne les variables : '_v_yy', '_v_mm', '_v_dd', '_v_month', '_v_weekday'
        """
        if (not self._v_yy) or (not self._v_mm) or (not self._v_dd) :
            self.f_setDateItems()
            
        return self._v_yy, self._v_mm, self._v_dd, self._v_month, self._v_weekday
        
    
    def f_setReverseShortFormat( self, v_cutYear = False, v_spacer = False) :
        """ Permet de definir la variable '_v_reverseShortFormat' sous la forme
            d'une str :
            
                'YYYYMMDD'
                
            * Si l'argument 'v_cutYear' est True, la date sera sur 2 digit
                
            * Si l'argument 'v_spacer' est utiliser, sa valeur sera utilisée
              comme spérateur.
            
            ex : ::
            
                >>> f_setReverseShortFormat( )
                '20170905'
                
                >>> f_setReverseShortFormat( v_cutYear = True )
                '170905'
                
                >>> f_setReverseShortFormat( v_spacer = '-' )
                '2017-09-05'
                
                >>> f_setReverseShortFormat( v_cutYear = True, v_spacer = '-' )
                '17-09-05'
                
        """
        v_yy, v_mm, v_dd, _, _ = self.f_getDateItems()
        
        if not v_spacer :
            v_spacer = ""
            
        if v_cutYear :
            v_yy = v_yy[-2:]
        
        self._v_reverseShortFormat = "{}{}{}{}{}".format( 
                                                    v_yy, v_spacer, v_mm, v_spacer, v_dd )
        
        
    def f_getReverseShortFormat( self ) :
        """ retourne '_v_reverseShortFormat' """
        if not self._v_reverseShortFormat :
            self.f_setReverseShortFormat()
            
        return self._v_reverseShortFormat
        

    def f_setFrShortFormat( self, v_cutYear = False, v_spacer = False ) :
        """ Permet de definir la variable '_v_frShortFormat' sous la forme d'une str :
                'DDMMYYYY'
                
            * Si l'argument 'v_cutYear' est True, la date sera sur 2 digit
                
            * Si l'argument 'v_spacer' est utiliser, sa valeur sera utilisée
              comme spérateur.
            
            ex : ::
            
                >>> f_setFrShortFormat( )
                '05092017'
                
                >>> f_setFrShortFormat( v_cutYear = True )
                '050917'
                
                >>> f_setFrShortFormat( v_spacer = '-' )
                '05-09-2017'

                >>> f_setFrShortFormat( v_cutYear = True, v_spacer = '-' )
                '05-09-17'
        """
        v_yy, v_mm, v_dd, _, _ = self.f_getDateItems()

        if not v_spacer :
            v_spacer = ""
            
        if v_cutYear :
            v_yy = v_yy[-2:]
        
        self._v_frShortFormat = "{}{}{}{}{}".format( 
                                                    v_dd, v_spacer, v_mm, v_spacer, v_yy )
        
        
    def f_getFrShortFormat( self ) :
        """ retourne '_v_frShortFormat' """
        if not self._v_frShortFormat :
            self.f_setFrShortFormat()
            
        return self._v_frShortFormat
        

    def f_setUsShortFormat( self, v_cutYear = False, v_spacer = False ) :
        """ Permet de definir la variable '_v_usShortFormat' sous la forme d'une str :
                'MMDDYYYY'
                
            * Si l'argument 'v_cutYear' est True, la date sera sur 2 digit
                
            * Si l'argument 'v_spacer' est utiliser, sa valeur sera utilisée
              comme spérateur.
            
            ex : ::
            
                >>> f_setUsShortFormat( )
                '09052017'
                
                >>> f_setUsShortFormat( v_cutYear = True )
                '090517'
                
                >>> f_setUsShortFormat( v_spacer = '-' )
                '09-05-2017'
                
                >>> f_setUsShortFormat( v_cutYear = True, v_spacer = '-' )
                '09-05-17'
        """
        v_yy, v_mm, v_dd, _, _ = self.f_getDateItems()

        if not v_spacer :
            v_spacer = ""
            
        if v_cutYear :
            v_yy = v_yy[-2:]
        
        self._v_usShortFormat = "{}{}{}{}{}".format( 
                                                    v_mm, v_spacer, v_dd, v_spacer, v_yy )


    def f_getUsShortFormat( self, v_cutYear = False, v_spacer = False ) :
        """ retourne '_v_usShortFormat' """
        if not self._v_usShortFormat :
            self.f_setUsShortFormat()
            
        return self._v_usShortFormat
        
        
    def f_setFrLongFormat( self, v_wDay = False ) :
        """ Définit la variable '_v_frLongFormat'  sous forme développée de la date
            au format Fr.
            Si 'v_weekDay' est 'True' le jour de la semaine sera ajouté devant la date
            ex : ::
            
                v_wDay = False
                
                    '06 Septembre 2017'
                
                v_wDay = True
                
                    'Mercredi 06 Septembre 2017'
        """
        v_yy, _, v_dd, v_month, v_weekday = self.f_getDateItems()
        
        if not v_wDay :
            self._v_frLongFormat = "{} {} {}".format( v_dd, self._d_month[v_month], v_yy )
        else :
            self._v_frLongFormat = "{} {} {} {}".format( self.d_weekday[v_weekday], v_dd,
                                                        self._d_month[v_month], v_yy )

        
    def f_getFrLongFormat( self ) :
        """ retourne _v_frLongFormat """
        if not self._v_frLongFormat :
            self.f_setFrLongFormat()
            
        return self._v_frLongFormat


    def f_setUsLongFormat( self, v_wDay = False ) :
        """ Définit la variable '_v_usLongFormat'  sous forme développée de la date
            au format US.
            Si 'v_weekDay' est 'True' le jour de la semaine sera ajouté devant la date
            ex : ::
            
                v_wDay = False
                
                    'September 6th 2017'
                
                v_wDay = True
                
                    'Wednesday, September 6th 2017'
        """
        v_yy, _, v_dd, v_month, v_weekday = self.f_getDateItems()
        
        if not v_wDay :
            self._v_usLongFormat = "{} {} {}".format(   v_month,
                                                        self._d_usDayNumber[v_dd], v_yy )
        else :
            self._v_usLongFormat = "{}, {} {} {}".format(v_weekday, v_month,
                                                        self._d_usDayNumber[v_dd], v_yy )

        
    def f_getUsLongFormat( self ) :
        """ retourne _v_usLongFormat """
        if not self._v_usLongFormat :
            self.f_setUsLongFormat()
            
        return self._v_usLongFormat
        
        
####
    
def main() :
    """ fonction principale, permtet de tester la librairie """
    ist = C_PlayWithDate()
    l_getList = []
    l_getList.append( ist.f_getDateItems() )
    l_getList.append( ist.f_getReverseShortFormat() )
    l_getList.append( ist.f_getFrShortFormat() )
    l_getList.append( ist.f_getUsShortFormat() )
    l_getList.append( ist.f_getFrLongFormat() )
    l_getList.append( ist.f_getUsLongFormat() )
    ist.f_setReverseShortFormat(True, '/')
    l_getList.append( ist.f_getReverseShortFormat() )
    ist.f_setFrShortFormat( True, '/' )
    l_getList.append( ist.f_getFrShortFormat() )
    ist.f_setUsShortFormat( True, '/')
    l_getList.append( ist.f_getUsShortFormat() )
    ist.f_setFrLongFormat( True )
    l_getList.append( ist.f_getFrLongFormat() )
    ist.f_setUsLongFormat( True )
    l_getList.append( ist.f_getUsLongFormat() )
    ist.f_setDateItems( "2017", "09", "08", "September", "Friday" )
    l_getList.append( ist.f_getDateItems() )
    
    for i in l_getList :
        print( i )

    
if __name__ == '__main__':
    main()
