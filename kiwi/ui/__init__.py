#
# Kiwi: a Framework and Enhanced Widgets for Python
#
# Copyright (C) 2005 Async Open Source
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307
# USA
#

"""User interface: Framework and Widget support"""


try:
    import gtk
    gtk  # pyflakes
except ImportError, e:
    try:
        import pygtk
        pygtk.require('2.0')
    except:
        pass

    try:
        import gtk
        gtk  # pyflakes
    except:
        raise SystemExit(
            "PyGTK 2.6.0 or higher is required by kiwi.ui\n"
            "Error was: %s" % e)


gtk.rc_parse_string("""
# Make multicombo buttons have less padding then a normal button
style "multicombo-close-button-style"
{
    GtkButton::focus-padding = 0
    GtkButton::focus-line-width = 0
    xthickness = 0
    ythickness = 0
}
widget_class "*MultiComboCloseButton*" style "multicombo-close-button-style"
""")
