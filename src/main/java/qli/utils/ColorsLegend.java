package qli.utils;

public enum ColorsLegend {
    RED("CC0000"), DARK_ORANGE("#cc6700"), LIGHT_ORANGE("#ec8f01"), YELLOW("#ecca01"), LIGHT_YELLOW("#f2e283"), GRAY("#a1a1a0");

    private String color;

    ColorsLegend(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return color;
    }
};
