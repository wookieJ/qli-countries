package qli.data;

import java.util.List;
import java.util.Map;
import java.util.Objects;

public class QualityOfLife {

    private Map<String, Map<String, List<Double>>> qualities;

    public QualityOfLife() {

    }

    public QualityOfLife(Map<String, Map<String, List<Double>>> qualities) {
        this.qualities = qualities;
    }

    public Map<String, Map<String, List<Double>>> getQualities() {
        return qualities;
    }

    public void setQualities(Map<String, Map<String, List<Double>>> qualities) {
        this.qualities = qualities;
    }

    @Override
    public boolean equals(Object o) {
        if(this == o) return true;
        if(o == null || getClass() != o.getClass()) return false;
        QualityOfLife that = (QualityOfLife) o;
        return Objects.equals(qualities,that.qualities);
    }

    @Override
    public int hashCode() {
        return Objects.hash(qualities);
    }

    @Override
    public String toString() {
        return "Quality of Life {" +
                "qualities=" + qualities + '}';
    }


}
