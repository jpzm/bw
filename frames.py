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



class BWFrame(Gtk.Frame):
    """
    """
    def __init__(self, label=""):
        """
        """
        Gtk.Frame.__init__(self)

        self.set_border_width(3)
        self.set_shadow_type(Gtk.ShadowType.NONE)

        self.__alignment = Gtk.Alignment(xalign=0, yalign=0,
                                         xscale=1, yscale=1)
        self.__alignment.set_padding(12, 0, 24, 0)

        self.add(self.__alignment)

        self.bw_set_label(label)


    def bw_set_label(self, label):
        """
        """
        self.set_label("<b>" + label + "</b>")
        self.get_label_widget().set_use_markup(True)


    def bw_add(self, widget):
        """
        """
        self.__alignment.add(widget)


    def bw_remove(self, widget):
        """
        """
        self.__alignment.remove(widget)
