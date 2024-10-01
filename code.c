int power(int a, int b) {
    if (b == 0) {
        return 1;
    } else {
        return a * power(a, b - 1);
    }
}

int main() {
    int a;
    int b;
    int result;
    int i;

    a = 2;
    b = 3;
    result = power(a, b);
    debug result;
}