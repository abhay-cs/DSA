public class Node<T> {
    private T item;
    Node<T> next;

    public Node(T item){
        this.item = item;
        next = null;
    }


    public Node<T> getNext(){
        return next;
    }

    public T getData(){
        return item;
    }

    public void setNext(Node<T> node){
        this.next = node;
    }

    public void setData(T data){
        this.item = data;
    }

}
 