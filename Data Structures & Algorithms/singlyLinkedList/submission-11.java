class LinkedList {
    int length;
    Node head;
    Node tail;

    public LinkedList() {
        length = 0;
        head = null;
        tail = null;
    }

    public int get(int index) {
        if(index >= length || index < 0){
            return -1;
        }
        Node current = head;
        for(int i = 0; i < index; i++){
            current = current.getNext();
        }
        return current.getVal();
    }

    public void insertHead(int val) {
        Node temp = new Node(val);
        temp.setNext(head);
        this.head = temp;
        if(this.tail == null){
            this.tail = this.head;
        }
        this.length++;
    }

    public void insertTail(int val) {
        Node temp = new Node(val);
        if(this.tail != null){
            this.tail.setNext(temp);
        }else{
            this.head = temp;
        }
        this.tail = temp;
        this.length++;
    }

    public boolean remove(int index) {
        if(index >= length || index < 0){
            return false;
        }

        if(index == 0){
            head = head.next;
            if(length == 1){
                tail = null;
            }
            length--;
            return true;
        }

        Node current = head;
        for(int i = 0; i < index - 1; i++){
            current = current.getNext();
        }
        
        if(current.getNext() == tail){
            tail = current;
        }

        current.setNext(current.getNext().getNext()); 
        length--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        if(length == 0){
            return new ArrayList<>();
        }
        ArrayList<Integer> result = new ArrayList<>();
        Node current = this.head;
        result.add(current.getVal());
        for(int i = 1; i < length; i++){
            current = current.getNext();
            result.add(current.getVal());
        }

        return result;
    }
}

class Node {
    int value;
    Node next;

    public Node(int val){
        this.value = val;
        this.next = null;
    }

    public int getVal(){
        return this.value;
    }

    public Node getNext(){
        return this.next;
    }

    public void setNext(Node next){
        this.next = next;
    }

    public boolean hasNext(){
        return next != null;
    }
}
