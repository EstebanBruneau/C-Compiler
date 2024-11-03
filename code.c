int main() {
    int* ptr;
    ptr = malloc(1);  // Allocate space for 1 integer
    *ptr = 42;        // Store 42 at allocated address
    debug *ptr;       // Should print 42
    return 0;
}