

odd one out
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    B=set(A) 
    for val in B: 
        if A.count(val)%2==1:
            return val

shifting elements
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7
    length = len(A)
    rot = K%length or length == 0
    if rot==0 or length == 0:
        return A
    
    half = A[length-rot:length]
    half.extend(A[0:length-rot])
    return half

    frog jump

    # you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(X, Y, D):
    # write your code in Python 2.7
    if(X==Y):
        return 0
    delta = Y-X
    val = delta/D
    if (delta%D >0):
        val+=1
    return val


# missing element

# solution 1 - crappy but leeme see 60% 100 correct 20% performance
def solution(A):
    # write your code in Python 2.7
    if(len(A)==0):
        return 1
    vals = range(1,(len(A)+2))

    for elem in vals:
        if elem not in A:
            return elem

# bettur ? with sums?


# frog jump on leaves
import java.util.HashSet;

class Solution {
    public int solution(int X, int[] A) {
        // write your code in Java SE 8
        HashSet<Integer> leaves = new HashSet<Integer>();
        for (int i=0;i<A.length;i++)
        {
         leaves.add(new Integer(A[i])) ;
         if(leaves.size()==X) return i;
        }
        return -1;
    }
}


# missing positive integer
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int[] A) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i=0;i<A.length;i++) 
        {
            if(A[i]>0)set.add(new Integer(A[i]));
        }
        int cmp;
        int i =0;
        ArrayList<Integer>list = new ArrayList<Integer>(set);
        Collections.sort(list);
        
        for(i=1;i<list.size()+1;i++)
        {  
         cmp = list.get(i-1);
         
         if(i!=cmp)return i;
        }
        return i;
    }
}




# counters with modification 20% performance

// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.ArrayList;
import java.util.Collections;


class Solution {
    public int[] solution(int N, int[] A) {
        // write your code in Java SE 8
        ArrayList<Integer> cntrs = new ArrayList<Integer>(Collections.nCopies(N,0));
        int max = 0; 
        int nval;
        for (int i =0;i< A.length;i++)
        {
         if(A[i]>=1&&A[i]<=N)
         {
                nval = cntrs.get(A[i]-1)+1;
                if(nval > max)max = nval;
                cntrs.set(A[i]-1,nval);
         }
         else
         {
             if (A[i] == N+1)cntrs = new ArrayList<Integer>(Collections.nCopies(N,max));

         }
        }   
        int[] array = cntrs.stream().mapToInt(i->i).toArray();
        return  array;
        
    }
}


# liczba liczb podzielnych przez K pomiędzy A i B 62% 25 % wydajnosci


// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int A, int B, int K) {
        // write your code in Java SE 8
        int i = A;
        int num=0;
        while(i<=B)
        {
        if(i%K!=0){
            i++;
            }
            else
            {
                num++;
                break;
                }
        }
        if(num==0)return num;
        for (int j= i;j<=B;j+=K)
        {
         if(j+K<=B)num++;   
        }
            
         return num;   
            
        
    }
}


# passing cars

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int ones = 0;
        int output = 0;
        
        for (int i=0; i< A.length;i++)
        {
            if(A[i]==1)ones++;
        }
        int zeros = A.length-ones;
        if(ones>44723&&A.length>2*44723)return -1;
        for (int j=0;j<A.length;j++)
        {
            if(A[j]==0)
            {

                output+= ones;
            }
            else ones--;
                
        }
        return output;
        
    }
}

# min avg 0% performance
class Solution {
    
    public float suma(int P,int Q,int[] A)
    {
        float suma =0;
        for (int i=P;i<=Q;i++)
        {
         suma +=A[i];   
        }
        return suma/(Q-P+1);
    }
    
    public int solution(int[] A) {
        // write your code in Java SE 8
        float min = Float.MAX_VALUE;
        int pmin=0;
        float nval;
        for(int p=0;p<A.length-1;p++)
        {
         for (int q=p+1;q<A.length;q++)
         {
            nval = suma(p,q,A);
          if(nval<min){
              min= nval;
              pmin = p;
          }
         }
        }
        return pmin;
    }
}