package qli.world;

import javafx.scene.paint.Color;

import java.util.ArrayList;
import java.util.List;


/**
 * Created by hansolo on 22.11.16.
 */
public enum Country {
    AL, AM, AT, AZ,
    BE, BG, BY,
    CH, CY, CZ,
    DE_TOT, DK,
    EE, EL, ES,
    FI, FR,
    GE,
    HR, HU,
    IE, IS, IT,
    LI, LT, LU, LV,
    MD, ME, MK, MT,
    NL, NO,
    PL, PT,
    RO, RS, RU,
    SE, SI, SK,
    TR,
    UA, UK;

    private ValueObject value;
    private Color       color;


    // ******************** Constructors **************************************
    Country() {
        value = null;
        color = null;
    }


    // ******************** Methods *******************************************
    public String getName() { return name(); }

    public ValueObject getValue() { return value; }
    public void setValue(final ValueObject VALUE) { value = VALUE; }

    public Color getColor() { return color; }
    public void setColor(final Color COLOR) { color = COLOR; }
}
