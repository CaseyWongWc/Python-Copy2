with Scratch as a:
    print("outer1")
    # out: outer1
    with Scratch as b:
        print("inner")
        # out: inner
        # b.out: inner
    print("outer2")
    # out: outer2
    # a.out: outer1
    # a.out: outer2
