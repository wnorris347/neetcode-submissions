class DynamicArray {

    int capacity;
    int size;

    int[] arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.arr = new int[capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(size == capacity){
            resize();
        }
        arr[size] = n;
        size++;
    }

    public int popback() {
        int val = arr[size - 1];
        size--;
        return val;
    }

    private void resize() {
        capacity *= 2;
        int[] newArray = new int[capacity];
        System.arraycopy(arr, 0, newArray, 0, size);
        arr = newArray;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
