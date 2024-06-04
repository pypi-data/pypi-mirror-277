# The PEP 484 type hints stub file for the QtPdf module.
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


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore
from PyQt6 import QtGui

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QPdfBookmarkModel(QtCore.QAbstractItemModel):

    class Role(enum.IntEnum):
        Title = ... # type: QPdfBookmarkModel.Role
        Level = ... # type: QPdfBookmarkModel.Role
        Page = ... # type: QPdfBookmarkModel.Role
        Location = ... # type: QPdfBookmarkModel.Role
        Zoom = ... # type: QPdfBookmarkModel.Role

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...

    documentChanged: typing.ClassVar[QtCore.pyqtSignal]
    def roleNames(self) -> typing.Dict[int, QtCore.QByteArray]: ...
    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def parent(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex: ...
    def data(self, index: QtCore.QModelIndex, role: int) -> typing.Any: ...
    def setDocument(self, document: typing.Optional['QPdfDocument']) -> None: ...
    def document(self) -> typing.Optional['QPdfDocument']: ...


class QPdfDocument(QtCore.QObject):

    class PageModelRole(enum.IntEnum):
        Label = ... # type: QPdfDocument.PageModelRole
        PointSize = ... # type: QPdfDocument.PageModelRole

    class MetaDataField(enum.Enum):
        Title = ... # type: QPdfDocument.MetaDataField
        Subject = ... # type: QPdfDocument.MetaDataField
        Author = ... # type: QPdfDocument.MetaDataField
        Keywords = ... # type: QPdfDocument.MetaDataField
        Producer = ... # type: QPdfDocument.MetaDataField
        Creator = ... # type: QPdfDocument.MetaDataField
        CreationDate = ... # type: QPdfDocument.MetaDataField
        ModificationDate = ... # type: QPdfDocument.MetaDataField

    class Error(enum.Enum):
        None_ = ... # type: QPdfDocument.Error
        Unknown = ... # type: QPdfDocument.Error
        DataNotYetAvailable = ... # type: QPdfDocument.Error
        FileNotFound = ... # type: QPdfDocument.Error
        InvalidFileFormat = ... # type: QPdfDocument.Error
        IncorrectPassword = ... # type: QPdfDocument.Error
        UnsupportedSecurityScheme = ... # type: QPdfDocument.Error

    class Status(enum.Enum):
        Null = ... # type: QPdfDocument.Status
        Loading = ... # type: QPdfDocument.Status
        Ready = ... # type: QPdfDocument.Status
        Unloading = ... # type: QPdfDocument.Status
        Error = ... # type: QPdfDocument.Status

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...

    pageModelChanged: typing.ClassVar[QtCore.pyqtSignal]
    pageCountChanged: typing.ClassVar[QtCore.pyqtSignal]
    statusChanged: typing.ClassVar[QtCore.pyqtSignal]
    passwordChanged: typing.ClassVar[QtCore.pyqtSignal]
    def pageIndexForLabel(self, label: typing.Optional[str]) -> int: ...
    def getAllText(self, page: int) -> 'QPdfSelection': ...
    def getSelectionAtIndex(self, page: int, startIndex: int, maxLength: int) -> 'QPdfSelection': ...
    def getSelection(self, page: int, start: QtCore.QPointF, end: QtCore.QPointF) -> 'QPdfSelection': ...
    def render(self, page: int, imageSize: QtCore.QSize, options: 'QPdfDocumentRenderOptions' = ...) -> QtGui.QImage: ...
    def pageModel(self) -> typing.Optional[QtCore.QAbstractListModel]: ...
    def pageLabel(self, page: int) -> str: ...
    def pagePointSize(self, page: int) -> QtCore.QSizeF: ...
    def pageCount(self) -> int: ...
    def close(self) -> None: ...
    def error(self) -> 'QPdfDocument.Error': ...
    def metaData(self, field: 'QPdfDocument.MetaDataField') -> typing.Any: ...
    def password(self) -> str: ...
    def setPassword(self, password: typing.Optional[str]) -> None: ...
    def status(self) -> 'QPdfDocument.Status': ...
    @typing.overload
    def load(self, fileName: typing.Optional[str]) -> 'QPdfDocument.Error': ...
    @typing.overload
    def load(self, device: typing.Optional[QtCore.QIODevice]) -> None: ...


class QPdfDocumentRenderOptions(PyQt6.sip.simplewrapper):

    class RenderFlag(enum.Enum):
        None_ = ... # type: QPdfDocumentRenderOptions.RenderFlag
        Annotations = ... # type: QPdfDocumentRenderOptions.RenderFlag
        OptimizedForLcd = ... # type: QPdfDocumentRenderOptions.RenderFlag
        Grayscale = ... # type: QPdfDocumentRenderOptions.RenderFlag
        ForceHalftone = ... # type: QPdfDocumentRenderOptions.RenderFlag
        TextAliased = ... # type: QPdfDocumentRenderOptions.RenderFlag
        ImageAliased = ... # type: QPdfDocumentRenderOptions.RenderFlag
        PathAliased = ... # type: QPdfDocumentRenderOptions.RenderFlag

    class Rotation(enum.Enum):
        None_ = ... # type: QPdfDocumentRenderOptions.Rotation
        Clockwise90 = ... # type: QPdfDocumentRenderOptions.Rotation
        Clockwise180 = ... # type: QPdfDocumentRenderOptions.Rotation
        Clockwise270 = ... # type: QPdfDocumentRenderOptions.Rotation

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QPdfDocumentRenderOptions') -> None: ...

    def __eq__(self, other: object): ...
    def __ne__(self, other: object): ...
    def setScaledSize(self, s: QtCore.QSize) -> None: ...
    def scaledSize(self) -> QtCore.QSize: ...
    def setScaledClipRect(self, r: QtCore.QRect) -> None: ...
    def scaledClipRect(self) -> QtCore.QRect: ...
    def setRenderFlags(self, r: 'QPdfDocumentRenderOptions.RenderFlag') -> None: ...
    def renderFlags(self) -> 'QPdfDocumentRenderOptions.RenderFlag': ...
    def setRotation(self, r: 'QPdfDocumentRenderOptions.Rotation') -> None: ...
    def rotation(self) -> 'QPdfDocumentRenderOptions.Rotation': ...


class QPdfLink(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QPdfLink') -> None: ...

    def copyToClipboard(self, mode: QtGui.QClipboard.Mode = ...) -> None: ...
    def toString(self) -> str: ...
    def rectangles(self) -> typing.List[QtCore.QRectF]: ...
    def contextAfter(self) -> str: ...
    def contextBefore(self) -> str: ...
    def url(self) -> QtCore.QUrl: ...
    def zoom(self) -> float: ...
    def location(self) -> QtCore.QPointF: ...
    def page(self) -> int: ...
    def isValid(self) -> bool: ...
    def swap(self, other: 'QPdfLink') -> None: ...


class QPdfLinkModel(QtCore.QAbstractListModel):

    class Role(enum.Enum):
        Link = ... # type: QPdfLinkModel.Role
        Rectangle = ... # type: QPdfLinkModel.Role
        Url = ... # type: QPdfLinkModel.Role
        Page = ... # type: QPdfLinkModel.Role
        Location = ... # type: QPdfLinkModel.Role
        Zoom = ... # type: QPdfLinkModel.Role

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    pageChanged: typing.ClassVar[QtCore.pyqtSignal]
    documentChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setPage(self, page: int) -> None: ...
    def setDocument(self, document: typing.Optional[QPdfDocument]) -> None: ...
    def linkAt(self, point: QtCore.QPointF) -> QPdfLink: ...
    def page(self) -> int: ...
    def data(self, index: QtCore.QModelIndex, role: int) -> typing.Any: ...
    def rowCount(self, parent: QtCore.QModelIndex) -> int: ...
    def roleNames(self) -> typing.Dict[int, QtCore.QByteArray]: ...
    def document(self) -> typing.Optional[QPdfDocument]: ...


class QPdfPageNavigator(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...

    jumped: typing.ClassVar[QtCore.pyqtSignal]
    forwardAvailableChanged: typing.ClassVar[QtCore.pyqtSignal]
    backAvailableChanged: typing.ClassVar[QtCore.pyqtSignal]
    currentZoomChanged: typing.ClassVar[QtCore.pyqtSignal]
    currentLocationChanged: typing.ClassVar[QtCore.pyqtSignal]
    currentPageChanged: typing.ClassVar[QtCore.pyqtSignal]
    def back(self) -> None: ...
    def forward(self) -> None: ...
    def update(self, page: int, location: QtCore.QPointF, zoom: float) -> None: ...
    @typing.overload
    def jump(self, destination: QPdfLink) -> None: ...
    @typing.overload
    def jump(self, page: int, location: QtCore.QPointF, zoom: float = ...) -> None: ...
    def clear(self) -> None: ...
    def forwardAvailable(self) -> bool: ...
    def backAvailable(self) -> bool: ...
    def currentZoom(self) -> float: ...
    def currentLocation(self) -> QtCore.QPointF: ...
    def currentPage(self) -> int: ...


class QPdfPageRenderer(QtCore.QObject):

    class RenderMode(enum.Enum):
        MultiThreaded = ... # type: QPdfPageRenderer.RenderMode
        SingleThreaded = ... # type: QPdfPageRenderer.RenderMode

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...

    renderModeChanged: typing.ClassVar[QtCore.pyqtSignal]
    documentChanged: typing.ClassVar[QtCore.pyqtSignal]
    def requestPage(self, pageNumber: int, imageSize: QtCore.QSize, options: QPdfDocumentRenderOptions = ...) -> int: ...
    def setDocument(self, document: typing.Optional[QPdfDocument]) -> None: ...
    def document(self) -> typing.Optional[QPdfDocument]: ...
    def setRenderMode(self, mode: 'QPdfPageRenderer.RenderMode') -> None: ...
    def renderMode(self) -> 'QPdfPageRenderer.RenderMode': ...


class QPdfSearchModel(QtCore.QAbstractListModel):

    class Role(enum.IntEnum):
        Page = ... # type: QPdfSearchModel.Role
        IndexOnPage = ... # type: QPdfSearchModel.Role
        Location = ... # type: QPdfSearchModel.Role
        ContextBefore = ... # type: QPdfSearchModel.Role
        ContextAfter = ... # type: QPdfSearchModel.Role

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...

    def timerEvent(self, event: typing.Optional[QtCore.QTimerEvent]) -> None: ...
    searchStringChanged: typing.ClassVar[QtCore.pyqtSignal]
    documentChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setDocument(self, document: typing.Optional[QPdfDocument]) -> None: ...
    def setSearchString(self, searchString: typing.Optional[str]) -> None: ...
    def data(self, index: QtCore.QModelIndex, role: int) -> typing.Any: ...
    def rowCount(self, parent: QtCore.QModelIndex) -> int: ...
    def roleNames(self) -> typing.Dict[int, QtCore.QByteArray]: ...
    def searchString(self) -> str: ...
    def document(self) -> typing.Optional[QPdfDocument]: ...
    def resultAtIndex(self, index: int) -> QPdfLink: ...
    def resultsOnPage(self, page: int) -> typing.List[QPdfLink]: ...


class QPdfSelection(PyQt6.sip.simplewrapper):

    def __init__(self, other: 'QPdfSelection') -> None: ...

    def copyToClipboard(self, mode: QtGui.QClipboard.Mode = ...) -> None: ...
    def endIndex(self) -> int: ...
    def startIndex(self) -> int: ...
    def boundingRectangle(self) -> QtCore.QRectF: ...
    def text(self) -> str: ...
    def bounds(self) -> typing.List[QtGui.QPolygonF]: ...
    def isValid(self) -> bool: ...
    def swap(self, other: 'QPdfSelection') -> None: ...
