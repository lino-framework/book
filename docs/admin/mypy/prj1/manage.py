#!/usr/bin/env python
if __name__ == "__main__":
    import sys ; sys.path.append('/usr/local/src/lino')
    from lino_local import manage ; manage(__file__, 'settings')
