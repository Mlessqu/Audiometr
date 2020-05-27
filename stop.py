def stop(p, stream):
    stream.close()
    p.terminate()
