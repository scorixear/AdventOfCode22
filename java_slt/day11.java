package java_slt;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class day11 {

    public static void main(String[] args){
        data[] monkies = new data[4];
        ArrayList<Integer> m0 = new ArrayList<Integer>();
        m0.add(79);
        m0.add(98);
        monkies[0] = new data(m0, '*', 19, 23, 2, 3);
        ArrayList<Integer> m1 = new ArrayList<Integer>();
        m1.add(54);
        m1.add(65);
        m1.add(75);
        m1.add(74);
        monkies[1] = new data(m1, '+', 6, 19, 2, 0);
        ArrayList<Integer> m2 = new ArrayList<Integer>();
        m2.add(79);
        m2.add(60);
        m2.add(97);
        monkies[2] = new data(m2, '^', 0, 13, 1, 3);
        ArrayList<Integer> m3 = new ArrayList<Integer>();
        m3.add(74);
        monkies[3] = new data(m3, '+', 3, 17, 0, 1);
        int[] cnt = new int[monkies.length];

        for (int index = 0; index < 20; index++){
            System.out.println("\nRound "+index+"\n");
            for (int i = 0; i < monkies.length; i++){
                System.out.println("Monkey "+i);
                for (int j = 0; j < monkies[i].items.size(); j++){
                    System.out.println("\nBefore Item "+monkies[i].items.get(j));

                    if (monkies[i].operator == '+')
                        monkies[i].items.set(j, (monkies[i].items.get(j) + monkies[i].operatorNum)/3);
                    else if (monkies[i].operator == '*')
                        monkies[i].items.set(j, (monkies[i].items.get(j) * monkies[i].operatorNum)/3);
                    else 
                        monkies[i].items.set(j, (monkies[i].items.get(j) * monkies[i].items.get(j))/3);
                    System.out.println("After Item "+monkies[i].items.get(j));
                    if (monkies[i].items.get(j) % monkies[i].divisor == 0) {
                        System.out.println("Sent to "+monkies[i].truth);
                        monkies[monkies[i].truth].items.add(monkies[i].items.get(j));
                    }
                    else {
                        monkies[monkies[i].falth].items.add(monkies[i].items.get(j));
                        System.out.println("Sent to "+monkies[i].falth);
                    }
                    cnt[i]++;
                }
                monkies[i].items.clear();
            }
            int k = 0;
            for(data monkey : monkies) {
                System.out.println("Monkey "+k+": "+ String.join(", ", monkey.items.stream().map(Object::toString).collect(Collectors.toList())));
                k++;
            }
        }
        Arrays.sort(cnt);
        System.out.println(cnt[cnt.length - 2] * cnt[cnt.length - 1]);
    }
}