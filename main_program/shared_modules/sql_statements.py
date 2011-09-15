try:
    import sys
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

setPaidToTrue = "update paid where hashid == {hashid}"