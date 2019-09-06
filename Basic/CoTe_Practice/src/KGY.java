import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class KGY {
    static List<int[]> walls = new LinkedList<>();
    static boolean[][] map;
    static boolean[] visit;
    static int departure, destination;
    static Wall destinationNode;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int wallNumber = sc.nextInt();
        map   = new boolean[wallNumber+1][wallNumber+1];
        visit = new boolean[wallNumber+1];

        for (int i=0; i<wallNumber; i++) {
            int wallNo = sc.nextInt();
            int x      = sc.nextInt();
            int y      = sc.nextInt();
            int r      = sc.nextInt();
            walls.add(new int[]{wallNo, x, y, r});
        }
        departure   = sc.nextInt();
        destination = sc.nextInt();

        // Build graph
        for (int i=0; i<walls.size(); i++) {
            buildGraph(i);
        }

        findShortestRoute(departure);
        System.out.println(destinationNode);
    }

    private static void findShortestRoute(int wallNo) {
        Queue<Wall> queue = new LinkedList<>();
        queue.offer(new Wall(wallNo));
        visit[wallNo] = true;

        while(!queue.isEmpty()) {
            Wall wall = queue.poll();

            if (wall.wallNo == destination) {
                destinationNode = wall;
            }

            for (int i=0; i<map[wall.wallNo].length; i++) {
                if (map[wall.wallNo][i] == true && visit[i] == false) {
                    queue.offer(new Wall(i, wall.path));
                    visit[i] = true;
                }
            }
        }
    }

    private static void buildGraph(int idx) {
        int[] minWall = null;
        int[] currentWall = walls.get(idx);
        for (int i=0; i<walls.size(); i++) {
            if (i == idx) continue;

            int[] parentWall = walls.get(i);
            if (isContained(currentWall, parentWall)) {
                if (minWall == null || isContained(parentWall, minWall)) {
                    minWall = parentWall;
                }
            }
        }

        if (minWall == null) {
            map[0][currentWall[0]] = true;
            map[currentWall[0]][0] = true;
        }
        else {
            map[minWall[0]][currentWall[0]] = true;
            map[currentWall[0]][minWall[0]] = true;
        }
    }

    private static boolean isContained(int[] child, int[] parent) {
        return (parent[1] - parent[3] <= child[1] - child[3] && child[1] + child[3] <= parent[1] + parent[3]
                && parent[2] - parent[3] <= child[2] - child[3] && child[2] + child[3] <= parent[2] + parent[3]);
    }
}

class Wall {
    int wallNo;
    String path = "";

    public Wall(int wallNo) {
        this.wallNo = wallNo;
        this.path = wallNo + "";
    }

    public Wall(int wallNo, String prevPath) {
        this.wallNo = wallNo;
        this.path += prevPath + " " + wallNo;
    }

    @Override
    public String toString() {
        return this.path.trim();
    }
}

