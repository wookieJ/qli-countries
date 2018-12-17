package qli.world;

import javafx.scene.paint.Color;

import java.util.ArrayList;
import java.util.List;

import static qli.world.Country.*;

public enum BusinessRegion implements CRegion {
    EU(BE, EL, LT, PT, BG, ES, LU, RO, CZ, FR, HU, SI, DK, HR, MT, SK, DE_TOT, IT, NL, FI, EE, CY, AT, SE, IE, LV, PL, UK);

    private List<Country> countries;


    // ******************** Constructors **************************************
    BusinessRegion(final Country... COUNTRIES) {
        countries = new ArrayList<>(COUNTRIES.length);
        for(Country country : COUNTRIES) { countries.add(country); }
    }


    // ******************** Methods *******************************************
    @Override public List<Country> getCountries() { return countries; }

    @Override public void setColor(final Color COLOR) {
        for (Country country : getCountries()) { country.setColor(COLOR); }
    }
}
