package qli.utils;

public enum ColorsLegend {
    GREEN("#00ff00"),
    LIGHT_GREEN("#b0ff01"),
    YELLOW_GREEN("#d6ff00"),
    YELLOW("#fdff01"),
    GOLD("#FFD700"),
    DARK_YELLOW("#FFDB00"),
    DARK_ORANGE("#FF4500"),
    ORANGE("#FFA500"),
    LIGHT_RED("#ff7400"),
    SALMON("#FE7C60"),
    RED("#ff0000"),
    GRAY("#a1a1a0");

    private String color;

    ColorsLegend(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return color;
    }
};
