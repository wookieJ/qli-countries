package qli.utils;

public enum Countries {
    AL("Albania"),      AM("Armenia"),      AT("Austria"),      AZ("Azerbejdżan"),
    BE("Belgia"),       BG("Bułgaria"),     BY("Białoruś"),
    CY("Cypr"),         CZ("Czechy"),       CH("Szwajcaria"),
    DE_TOT("Niemcy"),   DK("Dania"),
    EE("Estonia"),      EL("Grecja"),       ES("Hiszpania"),
    FI("Finlandia"),    FR("Francja"),
    GE("Gruzja"),
    HR("Chorwacja"),    HU("Węgry"),
    IE("Irlandia"),     IS("Islandia"),     IT("Włochy"),
    LI("Lichtenstein"), LT("Litwa"),        LU("Luxemburg"),    LV("Łotwa"),
    MD("Mołdawia"),     ME("Czarnogora"),   MT("Malta"),
    NL("Holandia"),     NO("Norwegia"),
    PL("Polska"),       PT("Portugalia"),
    RO("Rumunia"),      RS("Serbia"),       RU("Rosja"),
    SE("Szwecja"),      SI("Słowenia"),     SK("Słowacja"),
    TR("Turcja"),
    UA("Ukraina"),      UK("Wielka Brytania");

    private String country;

    Countries(String country) {
        this.country = country;
    }

    @Override
    public String toString() {
        return country;
    }
}
