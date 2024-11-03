int main() {
    int x;
    int* ptr;
    x = 42;
    debug x;          // Should print 42
    ptr = &x;         // ptr points to x
    debug ptr;        // Should print the address of x
    *ptr = 43;        // x = 43
    debug x;          // Should print 43
    debug *ptr;       // Should print 43
    debug ptr;        // Should print the address of x
    return 0;
}