package qli.world;

import javafx.scene.paint.Color;

import java.util.ArrayList;
import java.util.List;


/**
 * Created by hansolo on 01.12.16.
 */
public class CountryRegion implements CRegion {
    private String        name;
    private List<Country> countries;


    // ******************** Constructors **************************************
    public CountryRegion(final String NAME, final Country... COUNTRIES) {
        name      = NAME;
        countries = new ArrayList<Country>(COUNTRIES.length);
        for (Country country : COUNTRIES) { countries.add(country); }
    }


    // ******************** Methods *******************************************
     public String name() { return name; }

     public List<Country> getCountries() { return countries; }

     public void setColor(final Color COLOR) {
        for (Country country : getCountries()) { country.setColor(COLOR); }
    }
}
