for _ in range(3):
    fh, fm, fs, lh, lm, ls = map(int, input().split())
    f = (fm * 60) + (fh * 3600) + fs
    l = (lm * 60) + (lh * 3600) + ls
    time = l-f
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    print(h, m, s)