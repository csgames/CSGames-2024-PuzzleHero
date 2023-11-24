# Not there

## Write-up

This challenge hides the flag in the padding of the `Not` struct

The memcpy copies everything, including bytes in-between two struct
members:

```c
struct Not {
    char a;
    // 3 bytes of padding between a char and an int
    int b;
    int c;
    double d;
    ...
}

    char* all = "_F1AS.TQ1oe=G-W4X~iJ'mAV=uFVY+mSrq!yb%yvY}t36>vw7dM&m0rY";
    //            |--|-------|---
    //            `F1A`: 3 first letters of the flag
    //               |---------> 8 bytes filling b, c and d
    //                       |-----> `G-W`: 3 bytes are then filling the padding between d and e
    // etc
    struct Not there;
    memcpy(&there, all, sizeof(struct Not));
```

## Flag

`F1AG-W4St3dM&m0rY`
