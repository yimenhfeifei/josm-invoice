try:
    import sys
    import hashlib
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class ByteCountHasher(object):
    def __init__(self, algorithm):
        self.hasher = hashlib.new(algorithm)
        self.bytesHashed = 0
        
    def getNumBytesHashed(self):
        return self.bytesHashed
    
    def hexdigest(self):
        return self.hasher.hexdigest().upper()
        
    def update(self, arg):
        arg = bytes(arg, "UTF-8")
        self.hasher.update(arg)
        self.bytesHashed += len(arg)