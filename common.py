# vim: set fileencoding=utf-8 :

# Copyright (C) 2015 Joao Paulo de Souza Medeiros
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
from gi.repository import Gtk, Gdk

gtk_version_major = Gtk.get_major_version()
gtk_version_minor = Gtk.get_minor_version()
gtk_version_micro = Gtk.get_micro_version()

def update_gui():
    """
    """
    while (Gtk.events_pending() or Gdk.events_pending()):
        Gtk.main_iteration_do(True)
