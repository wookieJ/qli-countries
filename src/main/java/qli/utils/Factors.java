package qli.utils;

public enum Factors {
    MAT_LIVING("Materialne warunki życiowe"), HEALTH("Zdrowie"),
    EDUCATION("Edukacja"), ECON_SAFETY("Bezpieczeństwo materialne i fizyczne"),
    GOVERN("Stabilność polityczna"), LIVING_ENV("Srodowisko życia"),
    EMPLOY("Poziom zatrudnienia");

    private String factor;

    Factors(String factor) {
        this.factor = factor;
    }

    @Override
    public String toString() {
        return factor;
    }
}
