package qli;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.chart.LineChart;
import javafx.scene.control.Slider;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import qli.utils.ColorsLegend;

import javafx.scene.control.ListView;
import java.awt.*;
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
import javafx.scene.shape.Rectangle;
import qli.utils.Countries;
import qli.utils.Factors;


public class Controller {

    @FXML private Rectangle legend0;
    @FXML private Rectangle legend1;
    @FXML private Rectangle legend2;
    @FXML private Rectangle legend3;
    @FXML private Rectangle legend4;
    @FXML private Rectangle legend5;


    @FXML private ListView<String> listFactors, countryList;

    @FXML private Label legLabel0, legLabel1, legLabel2, legLabel3, legLabel4, legLabel5;

    @FXML private Button earlier, later;

    @FXML private Slider sliderYears;

    @FXML private LineChart<Float,Integer> factorChart;

    ObservableList<String> factors= FXCollections.observableArrayList();
    ObservableList<String> countries = FXCollections.observableArrayList();

    @FXML
    private void initialize() {
        System.out.println("Initialized");
        legend0.setFill(Color.valueOf(ColorsLegend.RED.toString()));
        legend1.setFill(Color.valueOf(ColorsLegend.DARK_ORANGE.toString()));
        legend2.setFill(Color.valueOf(ColorsLegend.LIGHT_ORANGE.toString()));
        legend3.setFill(Color.valueOf(ColorsLegend.YELLOW.toString()));
        legend4.setFill(Color.valueOf(ColorsLegend.LIGHT_YELLOW.toString()));
        legend5.setFill(Color.valueOf(ColorsLegend.GRAY.toString()));
        setLabels();
        setFactors();
        setCountries();
    }

    private void setLabels(){
        legLabel0.setText("> 30");
        legLabel1.setText("22 - 30");
        legLabel2.setText("14 - 22");
        legLabel3.setText("6 - 14");
        legLabel4.setText("< 6");
        legLabel5.setText("No data");
    }

    private void setFactors() {
        for(Factors factor : Factors.values()) {
            factors.add(factor.toString());
            System.out.println(factor.name());
        }

        listFactors.setItems(factors);
    }

    private void setCountries() {
        for(Countries country : Countries.values()) {
            countries.add(country.toString());
            System.out.println(country.name());
        }
        countryList.setItems(countries);
    }
}
