# The PEP 484 type hints stub file for the QtWebChannel module.
#
# Generated by SIP 6.8.3
#
# Copyright (c) 2024 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt6.sip

from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QWebChannel(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    blockUpdatesChanged: typing.ClassVar[QtCore.pyqtSignal]
    def disconnectFrom(self, transport: typing.Optional['QWebChannelAbstractTransport']) -> None: ...
    def connectTo(self, transport: typing.Optional['QWebChannelAbstractTransport']) -> None: ...
    def setPropertyUpdateInterval(self, ms: int) -> None: ...
    def propertyUpdateInterval(self) -> int: ...
    def setBlockUpdates(self, block: bool) -> None: ...
    def blockUpdates(self) -> bool: ...
    def deregisterObject(self, object: typing.Optional[QtCore.QObject]) -> None: ...
    def registerObject(self, id: typing.Optional[str], object: typing.Optional[QtCore.QObject]) -> None: ...
    def registeredObjects(self) -> typing.Dict[str, QtCore.QObject]: ...
    def registerObjects(self, objects: typing.Dict[typing.Optional[str], QtCore.QObject]) -> None: ...


class QWebChannelAbstractTransport(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    messageReceived: typing.ClassVar[QtCore.pyqtSignal]
    def sendMessage(self, message: typing.Dict[typing.Optional[str], typing.Union[QtCore.QJsonValue, QtCore.QJsonValue.Type, typing.Iterable[QtCore.QJsonValue], typing.Dict[typing.Optional[str], QtCore.QJsonValue], bool, int, float, None, typing.Optional[str]]]) -> None: ...
