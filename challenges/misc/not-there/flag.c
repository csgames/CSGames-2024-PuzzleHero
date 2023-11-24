#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Not {
    char a;
    int b;
    int c;
    double d;
    int e;
    char f[3];
    double g;
    char h, i;
    float j;
    char k;
};

void main()
{
    char* all = "_F1AS.TQ1oe=G-W4X~iJ'mAV=uFVY+mSrq!yb%yvY}t36>vw7dM&m0rY";
    struct Not there;
    memcpy(&there, all, sizeof(struct Not));

    printf("%c\n", there.a);
    printf("%d\n", there.b);
    printf("%d\n", there.c);
    printf("%lf\n", there.d);
    printf("%d\n", there.e);
    printf("%c%c%c\n", there.f[0], there.f[1], there.f[2]);
    printf("%lf\n", there.g);
    printf("%c\n", there.h);
    printf("%c\n", there.i);
    printf("%f\n", there.j);
    printf("%c\n", there.k);
}
