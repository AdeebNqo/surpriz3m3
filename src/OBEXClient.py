from _obexcommon import *
import _obexcommon

class OBEXClient(object):
    __doc__ = _obexcommon._obexclientclassdoc

    def __init__(self, address, channel):

        self.__sock = None
        self.__client = None
        self.__serveraddr = (address, channel)
        self.__connectionid = None

    def connect(self, headers={}):
        if self.__client is None:
            self.__setUp()

        try:
            resp = self.__client.request(_lightblueobex.CONNECT,
                    self.__convertheaders(headers), None)
        except IOError, e:
            raise OBEXError(str(e))

        result = self.__createresponse(resp)
        if result.code == _obexcommon.OK:
            self.__connectionid = result.headers.get("connection-id", None)
        else:
            self.__closetransport()
        return result


    def disconnect(self, headers={}):
        self.__checkconnected()
        try:
            try:
                resp = self.__client.request(_lightblueobex.DISCONNECT,
                        self.__convertheaders(headers), None)
            except IOError, e:
                raise OBEXError(str(e))
        finally:
            # close bt connection regardless of disconnect response
            self.__closetransport()
        return self.__createresponse(resp)


    def put(self, headers, fileobj):
        if not hasattr(fileobj, "read"):
            raise TypeError("file-like object must have read() method")
        self.__checkconnected()

        try:
            resp = self.__client.request(_lightblueobex.PUT,
                    self.__convertheaders(headers), None, fileobj)
        except IOError, e:
            raise OBEXError(str(e))
        return self.__createresponse(resp)


    def delete(self, headers):
        self.__checkconnected()
        try:
            resp = self.__client.request(_lightblueobex.PUT,
                    self.__convertheaders(headers), None)
        except IOError, e:
            raise OBEXError(str(e))
        return self.__createresponse(resp)


    def get(self, headers, fileobj):
        if not hasattr(fileobj, "write"):
            raise TypeError("file-like must have write() method")
        self.__checkconnected()
        try:
            resp = self.__client.request(_lightblueobex.GET,
                    self.__convertheaders(headers), None, fileobj)
        except IOError, e:
            raise OBEXError(str(e))
        return self.__createresponse(resp)


    def setpath(self, headers, cdtoparent=False, createdirs=False):
        self.__checkconnected()
        flags = 0
        if cdtoparent:
            flags |= 1
        if not createdirs:
            flags |= 2
        import array
        setpathdata = array.array('B', (flags, 0))  # zero for constants byte
        try:
            resp = self.__client.request(_lightblueobex.SETPATH,
                    self.__convertheaders(headers), buffer(setpathdata))
        except IOError, e:
            raise OBEXError(str(e))
        return self.__createresponse(resp)


    def __setUp(self):
        if self.__client is None:
            import bluetooth
            self.__sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            try:
                self.__sock.connect((self.__serveraddr[0],
                                     self.__serveraddr[1]))
            except bluetooth.BluetoothError, e:
                raise OBEXError(str(e))
            try:
                self.__client = _lightblueobex.OBEXClient(self.__sock.fileno())
            except IOError, e:
                raise OBEXError(str(e))

    def __closetransport(self):
        try:
            self.__sock.close()
        except:
            pass
        self.__connectionid = None
        self.__client = None

    def __checkconnected(self):
        if self.__client is None:
            raise OBEXError("must connect() before sending other requests")

    def __createresponse(self, resp):
        headers = resp[1]
        for hid, value in headers.items():
            if hid == 0x44:
                headers[hid] = _obexcommon._datetimefromstring(value[:])
            elif hid == 0xC4:
                headers[hid] = datetime.datetime.fromtimestamp(value)
            elif type(value) == buffer:
                headers[hid] = value[:]
        return _obexcommon.OBEXResponse(resp[0], headers)

    def __convertheaders(self, headers):
        result = {}
        for header, value in headers.items():
            if isinstance(header, types.StringTypes):
                hid = \
                    _obexcommon._HEADER_STRINGS_TO_IDS.get(header.lower())
            else:
                hid = header
            if hid is None:
                raise ValueError("unknown header '%s'" % header)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y%m%dT%H%M%S")
            self.__checkheadervalue(header, hid, value)
            result[hid] = value
        if self.__connectionid is not None:
            result[_lightblueobex.CONNECTION_ID] = self.__connectionid
        return result

    def __checkheadervalue(self, header, hid, value):
        mask = hid & _HEADER_MASK
        if mask == _HEADER_UNICODE:
            if not isinstance(value, types.StringTypes):
                raise TypeError("value for '%s' must be string, was %s" %
                    (str(header), type(value)))
        elif mask == _HEADER_BYTE_SEQ:
            try:
                buffer(value)
            except:
                raise TypeError("value for '%s' must be string, array or other buffer type, was %s" % (str(header), type(value)))
        elif mask == _HEADER_1BYTE:
            if not isinstance(value, int):
                raise TypeError("value for '%s' must be int, was %s" %
                    (str(header), type(value)))
        elif mask == _HEADER_4BYTE:
            if not isinstance(value, int) and not isinstance(value, long):
                raise TypeError("value for '%s' must be int, was %s" %
                    (str(header), type(value)))

    # set method docstrings
    definedmethods = locals()   # i.e. defined methods in OBEXClient
    for name, doc in _obexcommon._obexclientdocs.items():
        try:
            definedmethods[name].__doc__ = doc
        except KeyError:
            pass

