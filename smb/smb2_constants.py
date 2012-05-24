
# Bitmask for Flags field in SMB2 message header
SMB2_FLAGS_SERVER_TO_REDIR = 0x01
SMB2_FLAGS_ASYNC_COMMAND = 0x02
SMB2_FLAGS_RELATED_OPERATIONS = 0x04
SMB2_FLAGS_SIGNED = 0x08
SMB2_FLAGS_DFS_OPERATIONS = 0x10000000

# Values for Command field in SMB2 message header
SMB2_COM_NEGOTIATE = 0x0000
SMB2_COM_SESSION_SETUP = 0x0001
SMB2_COM_LOGOFF = 0x0002
SMB2_COM_TREE_CONNECT = 0x0003
SMB2_COM_TREE_DISCONNECT = 0x0004
SMB2_COM_CREATE = 0x0005
SMB2_COM_CLOSE = 0x0006
SMB2_COM_FLUSH = 0x0007
SMB2_COM_READ = 0x0008
SMB2_COM_WRITE = 0x0009
SMB2_COM_LOCK = 0x000A
SMB2_COM_IOCTL = 0x000B
SMB2_COM_CANCEL = 0x000C
SMB2_COM_ECHO = 0x000D
SMB2_COM_QUERY_DIRECTORY = 0x000E
SMB2_COM_CHANGE_NOTIFY = 0x000F
SMB2_COM_QUERY_INFO = 0x0010
SMB2_COM_SET_INFO = 0x0011
SMB2_COM_OPLOCK_BREAK = 0x0012

SMB2_COMMAND_NAMES = {
    0x0000: 'SMB2_COM_NEGOTIATE',
    0x0001: 'SMB2_COM_SESSION_SETUP',
    0x0002: 'SMB2_COM_LOGOFF',
    0x0003: 'SMB2_COM_TREE_CONNECT',
    0x0004: 'SMB2_COM_TREE_DISCONNECT',
    0x0005: 'SMB2_COM_CREATE',
    0x0006: 'SMB2_COM_CLOSE',
    0x0007: 'SMB2_COM_FLUSH',
    0x0008: 'SMB2_COM_READ',
    0x0009: 'SMB2_COM_WRITE',
    0x000A: 'SMB2_COM_LOCK',
    0x000B: 'SMB2_COM_IOCTL',
    0x000C: 'SMB2_COM_CANCEL',
    0x000D: 'SMB2_COM_ECHO',
    0x000E: 'SMB2_COM_QUERY_DIRECTORY',
    0x000F: 'SMB2_COM_CHANGE_NOTIFY',
    0x0010: 'SMB2_COM_QUERY_INFO',
    0x0011: 'SMB2_COM_SET_INFO',
    0x0012: 'SMB2_COM_OPLOCK_BREAK',
}

# Values for dialect_revision field in SMB2NegotiateResponse class
SMB2_DIALECT_2 = 0x0202
SMB2_DIALECT_21 = 0x0210
SMB2_DIALECT_2ALL = 0x02FF

# Bit mask for SecurityMode field in SMB2NegotiateResponse class
SMB2_NEGOTIATE_SIGNING_ENABLED = 0x0001
SMB2_NEGOTIATE_SIGNING_REQUIRED = 0x0002
