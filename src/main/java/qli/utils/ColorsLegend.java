package qli.utils;

public enum ColorsLegend {
    GREEN("#23ff01"), LIGHT_GREEN("#b0ff01"), YELLOW("#fdff01"), ORANGE("#ff9b01"), RED("#ff0101"), GRAY("#a1a1a0");

    private String color;

    ColorsLegend(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return color;
    }
};
