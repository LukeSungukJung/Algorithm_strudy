import java.util.Iterator;
import java.util.Scanner;
import static java.lang.System.out;
import java.util.ArrayList;

class wall{
    private int x_Point;
    private int y_Point;
    private int r_Size;
    private int wallCode;
    int Str_convert_to_Int(String str){
        return Integer.parseInt(str);
    }

    int get_xPoint(){
        return this.x_Point;
    }

    wall(String []element_list){
        int loop_count =0;;
        for(String oneEle: element_list){
            int temp_val = Str_convert_to_Int(oneEle);

            switch (loop_count){
                case 0: this.wallCode=temp_val;
                case 1: this.x_Point=temp_val;
                case 2: this.y_Point = temp_val;
                case 3: this.r_Size = temp_val;
            }


            loop_count++;
        }
    }

    int get_yPoint(){
        return this.y_Point;
    }

    int get_rSize(){
        return this.r_Size;
    }

    int get_wallCode(){
        return this.wallCode;
    }

}
public class Main {

    static void printWalls(ArrayList<wall> walls){
        Iterator<wall> walls_iterator = walls.iterator();
        while(walls_iterator.hasNext()){
            wall now = walls_iterator.next();
            out.println("wall_code: "+ now.get_wallCode());
            out.println("x: "+ now.get_xPoint());
            out.println("y: "+ now.get_yPoint());
            out.println("r: "+ now.get_rSize());
        }
    }
    static wall get_wall_by_wallCode(int code,ArrayList<wall>walls){
        Iterator<wall> walls_iterator = walls.iterator();
        while(walls_iterator.hasNext()){
            wall now = walls_iterator.next();
            if(now.get_wallCode() == code){
                return now;
            }
        }
        return null;

    }
    static double getXYdistance(int x1,int y1,int x2,int y2){
        return Math.sqrt(Math.pow(Math.abs(x1-x2),2)+Math.pow(Math.abs(y1-y2),2));
    }

    static boolean isApproached(wall wallA, wall wallB){
        int A_r_size = wallA.get_rSize();
        int A_x = wallA.get_xPoint();
        int A_y = wallA.get_yPoint();
        int B_R_size = wallB.get_rSize();
        int B_x = wallB.get_xPoint();
        int B_y = wallB.get_yPoint();
        double distance = getXYdistance(A_x,A_y,B_x,B_y);
        if(A_r_size + B_R_size < distance){
            return false;

        }else{
            return true;
        }
    }
    static wall getAnotherRoute(wall now,ArrayList<wall> walls){
        wall wall_next =null;
        double prev_distance=99999;
        for(wall one : walls){
            if(wall_next==null){
                wall_next=one;
                prev_distance= getXYdistance(now.get_xPoint(),now.get_yPoint(),one.get_xPoint(),one.get_yPoint());
            }
            double now_distance = getXYdistance(now.get_xPoint(),now.get_yPoint(),one.get_xPoint(),one.get_yPoint());
            if(Math.min(prev_distance,now_distance)==now_distance){
                wall_next=one;
                prev_distance= now_distance;
            }
        }
        return wall_next;
    }

    static void find_Least_route(int start,int end, ArrayList<wall> walls,ArrayList answer){
        wall wall_start = get_wall_by_wallCode(start,walls);
        ArrayList res = answer;
        walls.remove(wall_start);
        res.add(wall_start.get_wallCode());
        wall wall_next =null;
        double min_distance = 999999;
        boolean approach = true;
        boolean zero_meet = false;
        boolean the_end = false;
        for(wall one :walls){

            approach = true && isApproached(wall_start,one);

            if(approach){
                double now_distance = getXYdistance(wall_start.get_xPoint(),wall_start.get_yPoint(),one.get_xPoint(),one.get_yPoint());
                if(wall_next==null){
                    min_distance = Math.min(min_distance,now_distance);
                    wall_next = one;
                }else{
                    min_distance = Math.min(min_distance,now_distance);
                    if(now_distance==min_distance){
                        wall_next=one;
                    }
                }
            }
            if(wall_next!=null){
                approach=true;
            }


        }
        if(!approach){
            res.add(0);
            wall_next = getAnotherRoute(wall_start,walls);


        }

        if(wall_next.get_wallCode()==end)
            the_end=true;
        if(the_end){
            for(Object a : res){
                out.println(a);
            }
            return ;
        }
        find_Least_route(wall_next.get_wallCode(),end,walls,res);
//end랑 거리를 어케 조절잘해야됨 넓이로 영역에 드가는지 비교하는 구문 하나 만들어야됨 내일하자 ㅅㅂ


    }


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int wallNumbers = Integer.parseInt(sc.nextLine());
        ArrayList<wall> walls =  new ArrayList<wall>();
        for( int i = 0;i<wallNumbers;i++){
            String wall_info = sc.nextLine();
            String  []wall_info_arr = wall_info.split(" ");
            walls.add(new wall(wall_info_arr));
        }
        String []start_end =  sc.nextLine().split(" ");
        find_Least_route(Integer.parseInt(start_end[0]),Integer.parseInt(start_end[1]),walls,new ArrayList());

    }
}
