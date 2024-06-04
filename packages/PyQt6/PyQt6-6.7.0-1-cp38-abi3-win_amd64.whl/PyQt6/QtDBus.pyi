# The PEP 484 type hints stub file for the QtDBus module.
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

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QDBusAbstractAdaptor(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject]) -> None: ...

    def autoRelaySignals(self) -> bool: ...
    def setAutoRelaySignals(self, enable: bool) -> None: ...


class QDBusAbstractInterface(QtCore.QObject):

    def __init__(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], connection: 'QDBusConnection', parent: typing.Optional[QtCore.QObject]) -> None: ...

    def isInteractiveAuthorizationAllowed(self) -> bool: ...
    def setInteractiveAuthorizationAllowed(self, enable: bool) -> None: ...
    def disconnectNotify(self, signal: QtCore.QMetaMethod) -> None: ...
    def connectNotify(self, signal: QtCore.QMetaMethod) -> None: ...
    def asyncCallWithArgumentList(self, method: typing.Optional[str], args: typing.Iterable[typing.Any]) -> 'QDBusPendingCall': ...
    def asyncCall(self, method: typing.Optional[str], *args: typing.Any) -> 'QDBusPendingCall': ...
    @typing.overload
    def callWithCallback(self, method: typing.Optional[str], args: typing.Iterable[typing.Any], returnMethod: PYQT_SLOT, errorMethod: PYQT_SLOT) -> bool: ...
    @typing.overload
    def callWithCallback(self, method: typing.Optional[str], args: typing.Iterable[typing.Any], slot: PYQT_SLOT) -> bool: ...
    def callWithArgumentList(self, mode: 'QDBus.CallMode', method: typing.Optional[str], args: typing.Iterable[typing.Any]) -> 'QDBusMessage': ...
    @typing.overload
    def call(self, method: typing.Optional[str], *args: typing.Any) -> 'QDBusMessage': ...
    @typing.overload
    def call(self, mode: 'QDBus.CallMode', method: typing.Optional[str], *args: typing.Any) -> 'QDBusMessage': ...
    def timeout(self) -> int: ...
    def setTimeout(self, timeout: int) -> None: ...
    def lastError(self) -> 'QDBusError': ...
    def interface(self) -> str: ...
    def path(self) -> str: ...
    def service(self) -> str: ...
    def connection(self) -> 'QDBusConnection': ...
    def isValid(self) -> bool: ...


class QDBusArgument(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QDBusArgument') -> None: ...
    @typing.overload
    def __init__(self, arg: typing.Any, id: int = ...) -> None: ...

    def swap(self, other: 'QDBusArgument') -> None: ...
    def endMapEntry(self) -> None: ...
    def beginMapEntry(self) -> None: ...
    def endMap(self) -> None: ...
    @typing.overload
    def beginMap(self, keyMetaType: QtCore.QMetaType, valueMetaType: QtCore.QMetaType) -> None: ...
    @typing.overload
    def beginMap(self, kid: int, vid: int) -> None: ...
    def endArray(self) -> None: ...
    @typing.overload
    def beginArray(self, elementMetaType: QtCore.QMetaType) -> None: ...
    @typing.overload
    def beginArray(self, id: int) -> None: ...
    def endStructure(self) -> None: ...
    def beginStructure(self) -> None: ...
    def add(self, arg: typing.Any, id: int = ...) -> None: ...


class QDBus(PyQt6.sip.simplewrapper):

    class CallMode(enum.Enum):
        NoBlock = ... # type: QDBus.CallMode
        Block = ... # type: QDBus.CallMode
        BlockWithGui = ... # type: QDBus.CallMode
        AutoDetect = ... # type: QDBus.CallMode


class QDBusConnection(PyQt6.sip.simplewrapper):

    class ConnectionCapability(enum.Flag):
        UnixFileDescriptorPassing = ... # type: QDBusConnection.ConnectionCapability

    class UnregisterMode(enum.Enum):
        UnregisterNode = ... # type: QDBusConnection.UnregisterMode
        UnregisterTree = ... # type: QDBusConnection.UnregisterMode

    class RegisterOption(enum.Flag):
        ExportAdaptors = ... # type: QDBusConnection.RegisterOption
        ExportScriptableSlots = ... # type: QDBusConnection.RegisterOption
        ExportScriptableSignals = ... # type: QDBusConnection.RegisterOption
        ExportScriptableProperties = ... # type: QDBusConnection.RegisterOption
        ExportScriptableInvokables = ... # type: QDBusConnection.RegisterOption
        ExportScriptableContents = ... # type: QDBusConnection.RegisterOption
        ExportNonScriptableSlots = ... # type: QDBusConnection.RegisterOption
        ExportNonScriptableSignals = ... # type: QDBusConnection.RegisterOption
        ExportNonScriptableProperties = ... # type: QDBusConnection.RegisterOption
        ExportNonScriptableInvokables = ... # type: QDBusConnection.RegisterOption
        ExportNonScriptableContents = ... # type: QDBusConnection.RegisterOption
        ExportAllSlots = ... # type: QDBusConnection.RegisterOption
        ExportAllSignals = ... # type: QDBusConnection.RegisterOption
        ExportAllProperties = ... # type: QDBusConnection.RegisterOption
        ExportAllInvokables = ... # type: QDBusConnection.RegisterOption
        ExportAllContents = ... # type: QDBusConnection.RegisterOption
        ExportAllSignal = ... # type: QDBusConnection.RegisterOption
        ExportChildObjects = ... # type: QDBusConnection.RegisterOption

    class BusType(enum.Enum):
        SessionBus = ... # type: QDBusConnection.BusType
        SystemBus = ... # type: QDBusConnection.BusType
        ActivationBus = ... # type: QDBusConnection.BusType

    @typing.overload
    def __init__(self, name: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, other: 'QDBusConnection') -> None: ...

    def swap(self, other: 'QDBusConnection') -> None: ...
    @staticmethod
    def systemBus() -> 'QDBusConnection': ...
    @staticmethod
    def sessionBus() -> 'QDBusConnection': ...
    @staticmethod
    def localMachineId() -> QtCore.QByteArray: ...
    @staticmethod
    def disconnectFromPeer(name: typing.Optional[str]) -> None: ...
    @staticmethod
    def disconnectFromBus(name: typing.Optional[str]) -> None: ...
    @staticmethod
    def connectToPeer(address: typing.Optional[str], name: typing.Optional[str]) -> 'QDBusConnection': ...
    @typing.overload
    @staticmethod
    def connectToBus(type: 'QDBusConnection.BusType', name: typing.Optional[str]) -> 'QDBusConnection': ...
    @typing.overload
    @staticmethod
    def connectToBus(address: typing.Optional[str], name: typing.Optional[str]) -> 'QDBusConnection': ...
    def interface(self) -> typing.Optional['QDBusConnectionInterface']: ...
    def unregisterService(self, serviceName: typing.Optional[str]) -> bool: ...
    def registerService(self, serviceName: typing.Optional[str]) -> bool: ...
    def objectRegisteredAt(self, path: typing.Optional[str]) -> typing.Optional[QtCore.QObject]: ...
    def unregisterObject(self, path: typing.Optional[str], mode: 'QDBusConnection.UnregisterMode' = ...) -> None: ...
    @typing.overload
    def registerObject(self, path: typing.Optional[str], object: typing.Optional[QtCore.QObject], options: 'QDBusConnection.RegisterOption' = ...) -> bool: ...
    @typing.overload
    def registerObject(self, path: typing.Optional[str], interface: typing.Optional[str], object: typing.Optional[QtCore.QObject], options: 'QDBusConnection.RegisterOption' = ...) -> bool: ...
    @typing.overload
    def disconnect(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str], slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def disconnect(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str], signature: typing.Optional[str], slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def disconnect(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str], argumentMatch: typing.Iterable[typing.Optional[str]], signature: typing.Optional[str], slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def connect(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str], slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def connect(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str], signature: typing.Optional[str], slot: PYQT_SLOT) -> bool: ...
    @typing.overload
    def connect(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str], argumentMatch: typing.Iterable[typing.Optional[str]], signature: typing.Optional[str], slot: PYQT_SLOT) -> bool: ...
    def asyncCall(self, message: 'QDBusMessage', timeout: int = ...) -> 'QDBusPendingCall': ...
    def call(self, message: 'QDBusMessage', mode: QDBus.CallMode = ..., timeout: int = ...) -> 'QDBusMessage': ...
    def callWithCallback(self, message: 'QDBusMessage', returnMethod: PYQT_SLOT, errorMethod: PYQT_SLOT, timeout: int = ...) -> bool: ...
    def send(self, message: 'QDBusMessage') -> bool: ...
    def connectionCapabilities(self) -> 'QDBusConnection.ConnectionCapability': ...
    def name(self) -> str: ...
    def lastError(self) -> 'QDBusError': ...
    def baseService(self) -> str: ...
    def isConnected(self) -> bool: ...


class QDBusConnectionInterface(QDBusAbstractInterface):

    class RegisterServiceReply(enum.Enum):
        ServiceNotRegistered = ... # type: QDBusConnectionInterface.RegisterServiceReply
        ServiceRegistered = ... # type: QDBusConnectionInterface.RegisterServiceReply
        ServiceQueued = ... # type: QDBusConnectionInterface.RegisterServiceReply

    class ServiceReplacementOptions(enum.Enum):
        DontAllowReplacement = ... # type: QDBusConnectionInterface.ServiceReplacementOptions
        AllowReplacement = ... # type: QDBusConnectionInterface.ServiceReplacementOptions

    class ServiceQueueOptions(enum.Enum):
        DontQueueService = ... # type: QDBusConnectionInterface.ServiceQueueOptions
        QueueService = ... # type: QDBusConnectionInterface.ServiceQueueOptions
        ReplaceExistingService = ... # type: QDBusConnectionInterface.ServiceQueueOptions

    def disconnectNotify(self, a0: QtCore.QMetaMethod) -> None: ...
    def connectNotify(self, a0: QtCore.QMetaMethod) -> None: ...
    callWithCallbackFailed: typing.ClassVar[QtCore.pyqtSignal]
    serviceOwnerChanged: typing.ClassVar[QtCore.pyqtSignal]
    serviceUnregistered: typing.ClassVar[QtCore.pyqtSignal]
    serviceRegistered: typing.ClassVar[QtCore.pyqtSignal]
    def startService(self, name: typing.Optional[str]) -> QDBusReply: ...
    def serviceUid(self, serviceName: typing.Optional[str]) -> QDBusReply: ...
    def servicePid(self, serviceName: typing.Optional[str]) -> QDBusReply: ...
    def registerService(self, serviceName: typing.Optional[str], qoption: 'QDBusConnectionInterface.ServiceQueueOptions' = ..., roption: 'QDBusConnectionInterface.ServiceReplacementOptions' = ...) -> QDBusReply: ...
    def unregisterService(self, serviceName: typing.Optional[str]) -> QDBusReply: ...
    def serviceOwner(self, name: typing.Optional[str]) -> QDBusReply: ...
    def isServiceRegistered(self, serviceName: typing.Optional[str]) -> QDBusReply: ...
    def activatableServiceNames(self) -> QDBusReply: ...
    def registeredServiceNames(self) -> QDBusReply: ...


class QDBusError(PyQt6.sip.simplewrapper):

    class ErrorType(enum.Enum):
        NoError = ... # type: QDBusError.ErrorType
        Other = ... # type: QDBusError.ErrorType
        Failed = ... # type: QDBusError.ErrorType
        NoMemory = ... # type: QDBusError.ErrorType
        ServiceUnknown = ... # type: QDBusError.ErrorType
        NoReply = ... # type: QDBusError.ErrorType
        BadAddress = ... # type: QDBusError.ErrorType
        NotSupported = ... # type: QDBusError.ErrorType
        LimitsExceeded = ... # type: QDBusError.ErrorType
        AccessDenied = ... # type: QDBusError.ErrorType
        NoServer = ... # type: QDBusError.ErrorType
        Timeout = ... # type: QDBusError.ErrorType
        NoNetwork = ... # type: QDBusError.ErrorType
        AddressInUse = ... # type: QDBusError.ErrorType
        Disconnected = ... # type: QDBusError.ErrorType
        InvalidArgs = ... # type: QDBusError.ErrorType
        UnknownMethod = ... # type: QDBusError.ErrorType
        TimedOut = ... # type: QDBusError.ErrorType
        InvalidSignature = ... # type: QDBusError.ErrorType
        UnknownInterface = ... # type: QDBusError.ErrorType
        InternalError = ... # type: QDBusError.ErrorType
        UnknownObject = ... # type: QDBusError.ErrorType
        InvalidService = ... # type: QDBusError.ErrorType
        InvalidObjectPath = ... # type: QDBusError.ErrorType
        InvalidInterface = ... # type: QDBusError.ErrorType
        InvalidMember = ... # type: QDBusError.ErrorType
        UnknownProperty = ... # type: QDBusError.ErrorType
        PropertyReadOnly = ... # type: QDBusError.ErrorType

    def __init__(self, other: 'QDBusError') -> None: ...

    def swap(self, other: 'QDBusError') -> None: ...
    @staticmethod
    def errorString(error: 'QDBusError.ErrorType') -> str: ...
    def isValid(self) -> bool: ...
    def message(self) -> str: ...
    def name(self) -> str: ...
    def type(self) -> 'QDBusError.ErrorType': ...


class QDBusObjectPath(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, objectPath: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDBusObjectPath') -> None: ...

    def __ge__(self, rhs: 'QDBusObjectPath') -> bool: ...
    def __eq__(self, other: object): ...
    def __ne__(self, other: object): ...
    def __lt__(self, rhs: 'QDBusObjectPath') -> bool: ...
    def swap(self, other: 'QDBusObjectPath') -> None: ...
    def __hash__(self) -> int: ...
    def setPath(self, objectPath: typing.Optional[str]) -> None: ...
    def path(self) -> str: ...


class QDBusSignature(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, dBusSignature: typing.Optional[str]) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDBusSignature') -> None: ...

    def __ge__(self, rhs: 'QDBusSignature') -> bool: ...
    def __eq__(self, other: object): ...
    def __ne__(self, other: object): ...
    def __lt__(self, rhs: 'QDBusSignature') -> bool: ...
    def swap(self, other: 'QDBusSignature') -> None: ...
    def __hash__(self) -> int: ...
    def setSignature(self, dBusSignature: typing.Optional[str]) -> None: ...
    def signature(self) -> str: ...


class QDBusVariant(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, dBusVariant: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDBusVariant') -> None: ...

    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...
    def swap(self, other: 'QDBusVariant') -> None: ...
    def setVariant(self, dBusVariant: typing.Any) -> None: ...
    def variant(self) -> typing.Any: ...


class QDBusInterface(QDBusAbstractInterface):

    def __init__(self, service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str] = ..., connection: QDBusConnection = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...


class QDBusMessage(PyQt6.sip.simplewrapper):

    class MessageType(enum.Enum):
        InvalidMessage = ... # type: QDBusMessage.MessageType
        MethodCallMessage = ... # type: QDBusMessage.MessageType
        ReplyMessage = ... # type: QDBusMessage.MessageType
        ErrorMessage = ... # type: QDBusMessage.MessageType
        SignalMessage = ... # type: QDBusMessage.MessageType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QDBusMessage') -> None: ...

    def isInteractiveAuthorizationAllowed(self) -> bool: ...
    def setInteractiveAuthorizationAllowed(self, enable: bool) -> None: ...
    @staticmethod
    def createTargetedSignal(service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str]) -> 'QDBusMessage': ...
    def swap(self, other: 'QDBusMessage') -> None: ...
    def __lshift__(self, arg: typing.Any) -> 'QDBusMessage': ...
    def arguments(self) -> typing.List[typing.Any]: ...
    def setArguments(self, arguments: typing.Iterable[typing.Any]) -> None: ...
    def autoStartService(self) -> bool: ...
    def setAutoStartService(self, enable: bool) -> None: ...
    def isDelayedReply(self) -> bool: ...
    def setDelayedReply(self, enable: bool) -> None: ...
    def isReplyRequired(self) -> bool: ...
    def signature(self) -> str: ...
    def type(self) -> 'QDBusMessage.MessageType': ...
    def errorMessage(self) -> str: ...
    def errorName(self) -> str: ...
    def member(self) -> str: ...
    def interface(self) -> str: ...
    def path(self) -> str: ...
    def service(self) -> str: ...
    @typing.overload
    def createErrorReply(self, name: typing.Optional[str], msg: typing.Optional[str]) -> 'QDBusMessage': ...
    @typing.overload
    def createErrorReply(self, error: QDBusError) -> 'QDBusMessage': ...
    @typing.overload
    def createErrorReply(self, type: QDBusError.ErrorType, msg: typing.Optional[str]) -> 'QDBusMessage': ...
    @typing.overload
    def createReply(self, arguments: typing.Iterable[typing.Any] = ...) -> 'QDBusMessage': ...
    @typing.overload
    def createReply(self, argument: typing.Any) -> 'QDBusMessage': ...
    @typing.overload
    @staticmethod
    def createError(name: typing.Optional[str], msg: typing.Optional[str]) -> 'QDBusMessage': ...
    @typing.overload
    @staticmethod
    def createError(error: QDBusError) -> 'QDBusMessage': ...
    @typing.overload
    @staticmethod
    def createError(type: QDBusError.ErrorType, msg: typing.Optional[str]) -> 'QDBusMessage': ...
    @staticmethod
    def createMethodCall(service: typing.Optional[str], path: typing.Optional[str], interface: typing.Optional[str], method: typing.Optional[str]) -> 'QDBusMessage': ...
    @staticmethod
    def createSignal(path: typing.Optional[str], interface: typing.Optional[str], name: typing.Optional[str]) -> 'QDBusMessage': ...


class QDBusPendingCall(PyQt6.sip.simplewrapper):

    def __init__(self, other: 'QDBusPendingCall') -> None: ...

    def swap(self, other: 'QDBusPendingCall') -> None: ...
    @staticmethod
    def fromCompletedCall(message: QDBusMessage) -> 'QDBusPendingCall': ...
    @staticmethod
    def fromError(error: QDBusError) -> 'QDBusPendingCall': ...


class QDBusPendingCallWatcher(QtCore.QObject, QDBusPendingCall):

    def __init__(self, call: QDBusPendingCall, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    finished: typing.ClassVar[QtCore.pyqtSignal]
    def waitForFinished(self) -> None: ...
    def isFinished(self) -> bool: ...


class QDBusServiceWatcher(QtCore.QObject):

    class WatchModeFlag(enum.Flag):
        WatchForRegistration = ... # type: QDBusServiceWatcher.WatchModeFlag
        WatchForUnregistration = ... # type: QDBusServiceWatcher.WatchModeFlag
        WatchForOwnerChange = ... # type: QDBusServiceWatcher.WatchModeFlag

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, service: typing.Optional[str], connection: QDBusConnection, watchMode: 'QDBusServiceWatcher.WatchModeFlag' = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    serviceOwnerChanged: typing.ClassVar[QtCore.pyqtSignal]
    serviceUnregistered: typing.ClassVar[QtCore.pyqtSignal]
    serviceRegistered: typing.ClassVar[QtCore.pyqtSignal]
    def setConnection(self, connection: QDBusConnection) -> None: ...
    def connection(self) -> QDBusConnection: ...
    def setWatchMode(self, mode: 'QDBusServiceWatcher.WatchModeFlag') -> None: ...
    def watchMode(self) -> 'QDBusServiceWatcher.WatchModeFlag': ...
    def removeWatchedService(self, service: typing.Optional[str]) -> bool: ...
    def addWatchedService(self, newService: typing.Optional[str]) -> None: ...
    def setWatchedServices(self, services: typing.Iterable[typing.Optional[str]]) -> None: ...
    def watchedServices(self) -> typing.List[str]: ...


class QDBusUnixFileDescriptor(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, fileDescriptor: int) -> None: ...
    @typing.overload
    def __init__(self, other: 'QDBusUnixFileDescriptor') -> None: ...

    def swap(self, other: 'QDBusUnixFileDescriptor') -> None: ...
    @staticmethod
    def isSupported() -> bool: ...
    def setFileDescriptor(self, fileDescriptor: int) -> None: ...
    def fileDescriptor(self) -> int: ...
    def isValid(self) -> bool: ...


class QDBusPendingReply(QDBusPendingCall):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QDBusPendingReply') -> None: ...
    @typing.overload
    def __init__(self, call: QDBusPendingCall) -> None: ...
    @typing.overload
    def __init__(self, reply: QDBusMessage) -> None: ...

    def value(self, type: typing.Any = ...) -> typing.Any: ...
    def waitForFinished(self) -> None: ...
    def reply(self) -> QDBusMessage: ...
    def isValid(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isError(self) -> bool: ...
    def error(self) -> QDBusError: ...
    def argumentAt(self, index: int) -> typing.Any: ...


class QDBusReply(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self, reply: QDBusMessage) -> None: ...
    @typing.overload
    def __init__(self, call: QDBusPendingCall) -> None: ...
    @typing.overload
    def __init__(self, error: QDBusError) -> None: ...
    @typing.overload
    def __init__(self, other: 'QDBusReply') -> None: ...

    def value(self, type: typing.Any = ...) -> typing.Any: ...
    def isValid(self) -> bool: ...
    def error(self) -> QDBusError: ...
