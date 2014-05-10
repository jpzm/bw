# vim: set fileencoding=utf-8 :

# Copyright (C) 2008 Joao Paulo de Souza Medeiros
#
# Author(s): Joao Paulo de Souza Medeiros <ignotus21@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import gtk



class BWNotebook(gtk.Notebook):
    """
    """
    def __init__(self, label=""):
        """
        """
        gtk.Notebook.__init__(self)
        self.set_border_width(3)
        self.__alignment = []

    def bw_append_page(self, widget, label):
        """
        """
        self.__alignment.append(gtk.Alignment(0, 0, 1, 1))
        self.__alignment[-1].set_padding(12, 0, 24, 0)
        self.__alignment[-1].add(widget)
        self.append_page(self.__alignment[-1], label)
