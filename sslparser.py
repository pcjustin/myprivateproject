RecordType = {
    0x14: 'Change Cipher Spec',
    0x16: 'Handshake',
    0x17: 'Application Data',
}

VersionType = {
    0x0300: 'SSL 3.0',
    0x0301: 'TLS 1.0',
    0x0302: 'TLS 1.1',
    0x0303: 'TLS 1.2',
}

HandshakeType = {
    0x1: 'Client Hello',
    0x2: 'Server Hello',
    0xb: 'Certificate',
    0xc: 'Server Key Exchange',
}

def readChangecipherspec(stream, size):
    print('readChangecipherspec')
    return size

def readHandshake(stream, size):
    type = stream[0]
    print('Content Type: ' + HandshakeType.get(type, hex(type)) + ' (' + str(type) + ')')
    length = stream[1] << 16 | stream[2] << 8 | stream[3]
    print('Length: ' + str(length))
    if type == 0x1 or type == 0x2:
        version = stream[4] << 8 | stream[5]
        print('Version: ' + VersionType[version] + ' (' + hex(version) + ')')
    return length + 4

def readApplication(stream, size):
    print('readApplication')
    return size

RecordFunc = {
    0x14: readChangecipherspec,
    0x16: readHandshake,
    0x17: readApplication,
}

def hexdump(log):
    for c in log.readlines():
        stream = bytes().fromhex(c.rstrip())
        readRecordLayer(stream)
        print('====================')

def readRecordLayer(stream):
    type = stream[0]
    print('Content Type: ' + RecordType[type] + ' (' + str(type) + ')')
    version = stream[1] << 8 | stream[2]
    print('Version: ' + VersionType[version] + ' (' + hex(version) + ')')
    multilength = stream[3] << 8 | stream[4]
    print('Length: ' + str(multilength))
    size = 0
    index = 5
    length = multilength
    # while True:
    #     index = index + size
    #     size = RecordFunc[type](stream[index:], length)
    #     length = length - size
    #     if length == 0:
    #         break
    #     print('====================')
    if len(stream) == multilength+5:
        return
    else:
        print('====================')
        readRecordLayer(stream[5+multilength:])


log = open('ssl.log')
hexdump(log)
