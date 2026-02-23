def get_frames(signal, size, overlap):
    n = len(signal)
    if n == 0:
        return

    step = max(1, int(size * (1 - overlap)))

    for start in range(0, n - size + 1, step):
        yield signal[start : start + size]