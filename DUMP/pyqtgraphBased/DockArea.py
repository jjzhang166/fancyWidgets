# -*- coding: utf-8 -*-


from pyqtgraph_karl.dockarea.DockArea import DockArea as pgDockArea
# from QtRec.QtGui import QWidget
#
# b = list(pgDockArea.__bases__)
# for n,l in enumerate(b):
# 	if l.__name__ == 'QWidget':
# 		b[n] = QWidget
# pgDockArea.__bases__ = tuple(b)


class DockArea(pgDockArea):
    """
    save the initial position of a dock and
    restores it if wished
    """

    # TODO: does not match overridden method
    def addDock(self, dock, *args, **kwargs):
        dock.init_position = kwargs
        return pgDockArea.addDock(self, dock, *args, **kwargs)

    def restore(self):
        for dock in self.docks:
            dock.embedd()
            self.moveDock(dock, dock.init_position)
