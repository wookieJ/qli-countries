package qli.utils;

public enum Factors {
    MAT_LIVING("Materialne warunki życiowe"), HEALTH("Zdrowie"),
    EDUCATION("Edukacja"), ECON_SAFETY("Bezpieczeństwo materialne i fizyczne"), LEISURE("Czas wolny i interakcje społeczne"),
    GOVERN("Stabilność polityczna"), LIVING_ENV("Srodowisko życia"), LIFE_EXP("Satysfakcja z życia"),
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
