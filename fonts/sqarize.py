#!/usr/bin/python

#Python fontforge script to build a square notation font.
#Copyright (C) 2007 Elie Roux
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#This script takes a very simple .sfd file with a few symbols and builds a
#complete square notation font.
#
# See http://fontforge.sourceforge.net/python.html for documentation
# on the fontforge python scripts

 - définir les hauteurs des lignes et l'espace entre
 - définir la hauteur d'un punctum, ses points d'ancrage
 - pareil avec les barres des porrectus


import fontforge                                 #Load the module
amb=fontforge.open("gregorio-base.sfd")               #Open a font

n=fontforge.font()  
n.fontname="gregorio.sfd"                             #Give the new font a name
n.save("gregorio.sfd")                            #and save it.