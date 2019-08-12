import java.util.Scanner;
import java.util.ArrayList;
import static java.lang.System.out;

class Tree{
    int depth ;
    int value ;
    Tree parent;
    Tree Left;
    Tree Right;

    int getValue() {
        return value;
    }


    void setDepth(Tree parent){
        this.depth = parent.depth+1;
    }


    Tree(int value,Tree parent){
        this.value = value;
        setDepth(parent);
        this.parent=parent;
    }
    Tree(int value){
        this.value = value;
        this.depth = 0;
    }
    ArrayList<Tree> getChildren(){
        ArrayList<Tree> res_arr =  new ArrayList<Tree>();
        if(this.Right!=null){
            res_arr.add(this.Right);
        }
        if(this.Left!=null){
            res_arr.add(this.Left);
        }
        return res_arr;
    }
}



public class Main {

     static int get_last_depth_nodes(Tree Tree234,int depth){
         int a =0,b = 0 ;
         if(Tree234.Left !=null){
            a= get_last_depth_nodes(Tree234.Left,depth);
         }else{
             if(depth == Tree234.depth+2){
                 a++;
             }
         }
         if(Tree234.Right !=null){
            b =  get_last_depth_nodes(Tree234.Right,depth);
         }else{
             if(depth == Tree234.depth+2){
                 b++;
             }
         }
         return a+b;
     }

     static void insert_node(int value,Tree Tree234){
        if(Tree234.value<value){
            if( Tree234.Right == null) {
                Tree newNode = new Tree(value, Tree234);
                Tree234.Right = newNode;
            }else{
                insert_node(value,Tree234.Right);
            }
        }else if(Tree234.value>value ){
            if(Tree234.Left == null){
            Tree newNode = new Tree(value,Tree234);
            Tree234.Left= newNode;
            }else{
                insert_node(value,Tree234.Left);
            }

        }
    }

    public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    out.print("set root node:");
    int root_var = Integer.parseInt(sc.next());
    Tree TreeOf234 =  new Tree(root_var);
    out.println(TreeOf234.getValue());
    out.print("set_children:");
    int child_var = Integer.parseInt(sc.next());


    insert_node(child_var,TreeOf234);
    out.println(get_last_depth_nodes(TreeOf234,2));


    }
}