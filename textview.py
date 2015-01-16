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
import gobject

from boxes import BWScrolledWindow, BWHBox
from common import update_gui


class BWTextView(BWScrolledWindow):
    """
    """
    def __init__(self):
        """
        """
        BWScrolledWindow.__init__(self)

        self.__scroll = False

        self.__create_widgets()


    def __create_widgets(self):
        """
        """
        self.__textbuffer = gtk.TextBuffer()
        self.__textview = gtk.TextView(self.__textbuffer)

        self.add_with_viewport(self.__textview)


    def bw_set_scroll(self, scroll):
        """
        """
        self.__scroll = scroll


    def bw_set_editable(self, editable):
        """
        """
        self.__textview.set_editable(False)


    def bw_modify_font(self, font):
        """
        """
        self.__textview.modify_font(font)


    def bw_set_text(self, text, f_before_scroll=None):
        """
        """
        self.__textbuffer.set_text(text)

        if self.__scroll:

            if f_before_scroll:
                f_before_scroll()

            update_gui()

            value  = self.get_vadjustment().upper
            value -= self.get_vadjustment().page_size

            self.get_vadjustment().set_value(value)


    def bw_set_wrap_mode(self, mode):
        """
        """
        self.__textview.set_wrap_mode(mode)


    def bw_get_text(self):
        """
        """
        return self.__textbuffer.get_text(self.__textbuffer.get_start_iter(),
                                          self.__textbuffer.get_end_iter())


    def bw_get_textbuffer(self):
        """
        """
        return self.__textbuffer


    def bw_remove_all_tags(self):
        """
        """
        self.__textbuffer.remove_all_tags(self.__textbuffer.get_start_iter(),
                                          self.__textbuffer.get_end_iter())



class BWTextEditor(BWScrolledWindow):
    """
    """
    def __init__(self):
        """
        """
        BWScrolledWindow.__init__(self)
        self.connect('expose_event', self.__expose)

        self.__scroll = False

        self.__create_widgets()


    def __create_widgets(self):
        """
        """
        self.__hbox = BWHBox(spacing=6)

        self.__textbuffer = gtk.TextBuffer()
        self.__textview = gtk.TextView(self.__textbuffer)

        self.__linebuffer = gtk.TextBuffer()
        self.__lineview = gtk.TextView(self.__linebuffer)
        self.__lineview.set_justification(gtk.JUSTIFY_RIGHT)
        self.__lineview.set_editable(False)
        self.__lineview.set_sensitive(False)

        self.__hbox.bw_pack_start_noexpand_nofill(self.__lineview)
        self.__hbox.bw_pack_start_expand_fill(self.__textview)

        self.add_with_viewport(self.__hbox)


    def __expose(self, widget, event):
        """
        """
        # code to fix a gtk issue that don't show text correctly
        self.__hbox.check_resize()


    def bw_set_scroll(self, scroll):
        """
        """
        self.__scroll = scroll


    def bw_set_editable(self, editable):
        """
        """
        self.__textview.set_editable(False)


    def bw_modify_font(self, font):
        """
        """
        self.__textview.modify_font(font)
        self.__lineview.modify_font(font)


    def bw_set_text(self, text, f_before_scroll=None):
        """
        """
        if text != "":

            count = text.count('\n') + text.count('\r')

            lines = range(1, count + 2)
            lines = [str(i).strip() for i in lines]

            self.__textbuffer.set_text(text)
            self.__linebuffer.set_text('\n'.join(lines))

            if self.__scroll:

                if f_before_scroll:
                    f_before_scroll()

                update_gui()

                value  = self.get_vadjustment().upper
                value -= self.get_vadjustment().page_size

                self.get_vadjustment().set_value(value)

        else:

            self.__textbuffer.set_text("")
            self.__linebuffer.set_text("")


    def bw_get_text(self):
        """
        """
        return self.__textbuffer.get_text(self.__textbuffer.get_start_iter(),
                                          self.__textbuffer.get_end_iter())
