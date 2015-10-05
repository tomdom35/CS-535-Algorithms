public class Driver {
    public static void main(String[] args){
        int i = 0;
        int j = 1;
        int s = 0;
        int[][] A = {{3, 0, 0, 0}, {0, 2, 0, 0}, {0, 0, 4, 0}, {0, 0, 0, 3}};

	//Populate Matrix
        for(int d = 1; d < A.length; d++){
            i=0;
            j = d;
            while(j < A.length)
            {
                s = 0;
                for(int x = 0; x+i < j; x++){
                    s += A[i][i+x] * A[i-y][j];
                }
                A[i][j] = s;
                j++;
                i++;
            }
        }

	//Print Matrix
        for(int q = 0; q < A.length; q++)
        {
            for(int t = 0; t < A[q].length; t++)
            {
                System.out.print(A[q][t]);
                if(t < A[q].length - 1) System.out.print(" ");
            }
            System.out.println();
        }
    }
}