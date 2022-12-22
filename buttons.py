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

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk



class BWStockButton(Gtk.Button):
    """
    """
    def __init__(self, stock, text=None, size=Gtk.IconSize.BUTTON):
        """
        """
        Gtk.Button.__init__(self, text)

        self.__size = size

        self.__image = Gtk.Image()
        self.__image.set_from_stock(stock, self.__size)
        self.set_image(self.__image)



class BWToggleStockButton(Gtk.ToggleButton):
    """
    """
    def __init__(self, stock, text=None, size=Gtk.IconSize.BUTTON):
        """
        """
        Gtk.ToggleButton.__init__(self, text)

        self.__size = size

        self.__image = Gtk.Image()
        self.__image.set_from_stock(stock, self.__size)
        self.set_image(self.__image)
