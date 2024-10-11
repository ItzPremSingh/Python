kb = 1024
mb = 1048576
gb = 1073741824
tb = 1099511627776

def sizeFormat(byte, round_=2):
    byte = int(byte)
    if byte < kb:
        return f"{byte} B"

    elif kb <= byte < mb:
        size, unit = (byte / kb), "KB"

    elif mb <= byte < gb:
        size, unit = (byte / mb), "MB"

    elif gb <= byte < tb:
        size, unit = (byte / gb), "GB"

    elif tb <= byte:
        size, unit = (byte / tb), "TB"

    return f"{round(float(size), round_)} {unit}"
