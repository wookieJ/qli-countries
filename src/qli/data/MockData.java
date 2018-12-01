package qli.data;


import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class MockData {
    private HashMap<String, ArrayList<Double>> educationValues;
    private HashMap<String, ArrayList<Double>> healthValues;
    private ArrayList<Double> valuesPoland = new ArrayList<>();
    private Random random  = new Random();

    public MockData() {
        educationValues = new HashMap<>();
        healthValues = new HashMap<>();
    }

    public void fillFakeData() {
        for (int i = 0; i < 10; i++) {
            valuesPoland.add(50.0 + (100.0 - 50.0)*random.nextDouble());
        }
        educationValues.put("PL", valuesPoland);
    }

    public ArrayList<Double> getEducationValues() {
        return educationValues.get("PL");
    }
}
