// TODO: Implement methods and fix up the issues..
public class SinglyList<T> {
    
    private Node<T> head;
    private int size;
    public SinglyList(){
        this.head = null;
        this.size = 0;
    }

    public void addFront(T item){
        if(head == null){
            head = new Node<T>(item);
        }else{
            Node<T> tempNode = new Node<T>(item);
            Node<T> curNode = head;
            tempNode.setNext(curNode.getNext());
            head.setNext(tempNode);

        }
        size++;
    }

    public T remove(T item){

        size--;
        return item;
    }

    public String print(){
        String result = "";
            Node<T> current = head;
            while(current.getNext() != null){
                result += current.getData().toString();
                if(current.getNext() != null){
                     result += ", ";
                }
                current = current.getNext();
            }
            return "List: " + result;
    }
    public int size(){
        return size;
    }

    public static void main(String[] args) {
        SinglyList<Integer> list = new SinglyList<Integer>();
        list.addFront(1);
        list.addFront(2);
        list.addFront(3);
        list.print();
        System.out.println(list.size());
    }

}
