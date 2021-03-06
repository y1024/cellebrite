#
# Upload some bootloader to the dump process. 
# The Uploader get some protocol from Protocols dir that manage all communication.
# Wrote by Itay Kahana


class IUploader:
        def __init__(self, protocol):
                self.protocol= protocol
                if protocol:
                    self.framer = protocol.framer
        def connect(self):
                raise Exception(NotImplemented)
        def handshake(self):
                raise Exception(NotImplemented)
        def upload(self, bootloader_path, load_address):
                raise Exception(NotImplemented)
