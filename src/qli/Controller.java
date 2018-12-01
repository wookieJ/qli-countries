package qli;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import qli.data.MockData;
import qli.utils.ColorsLegend;

import javafx.scene.control.ListView;
import java.awt.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.function.DoubleToIntFunction;

import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
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

    @FXML private LineChart<Float,Double> factorChart;
    @FXML private CategoryAxis yearsAxis;
    @FXML private NumberAxis values;

    ObservableList<String> factors= FXCollections.observableArrayList();
    ObservableList<String> countries = FXCollections.observableArrayList();
    private double currentYear;
    private String selectedFactor, selectedCountry;


    @FXML
    private void initialize() {
        setLegend();
        setLabels();
        setFactors();
        setCountries();
        listFactors.getSelectionModel().selectFirst();
        countryList.getSelectionModel().select("Polska");
        countryList.scrollTo("Polska");
        selectedCountry = countryList.getSelectionModel().getSelectedItem();
        selectedFactor = listFactors.getSelectionModel().getSelectedItem();
        currentYear = sliderYears.getValue();
        System.out.println(currentYear);
        listFactors.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                selectedFactor = listFactors.getSelectionModel().getSelectedItem();
                fillChart(selectedFactor,selectedCountry);
            }
        });
        countryList.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                selectedCountry = countryList.getSelectionModel().getSelectedItem();
                fillChart(selectedFactor,selectedCountry);
            }
        });
    }

    private void setLegend() {
        legend0.setFill(Color.valueOf(ColorsLegend.RED.toString()));
        legend1.setFill(Color.valueOf(ColorsLegend.DARK_ORANGE.toString()));
        legend2.setFill(Color.valueOf(ColorsLegend.LIGHT_ORANGE.toString()));
        legend3.setFill(Color.valueOf(ColorsLegend.YELLOW.toString()));
        legend4.setFill(Color.valueOf(ColorsLegend.LIGHT_YELLOW.toString()));
        legend5.setFill(Color.valueOf(ColorsLegend.GRAY.toString()));
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
    @FXML
    private void increaseYear() {
        if(currentYear < sliderYears.getMax()) {
            sliderYears.increment();
            currentYear = sliderYears.getValue();
            System.out.println(currentYear);
        }
    }
    @FXML
    private void decreaseYear() {
        if(currentYear > sliderYears.getMin()) {
            sliderYears.decrement();
            currentYear = sliderYears.getValue();
            System.out.println(currentYear);
        }
    }

    private void fillChart(String factorName, String countryName) {
        factorChart.getData().clear();
        MockData mockData = new MockData();
        mockData.fillFakeData();
        ArrayList<Double> fakeValues = mockData.getEducationValues();
        XYChart.Series series = new XYChart.Series();
        series.setName(countryName);
        series.getData().add(new XYChart.Data("2008", fakeValues.get(0)));
        series.getData().add(new XYChart.Data("2009", fakeValues.get(1)));
        series.getData().add(new XYChart.Data("2010", fakeValues.get(2)));
        series.getData().add(new XYChart.Data("2011", fakeValues.get(3)));
        series.getData().add(new XYChart.Data("2012", fakeValues.get(4)));
        series.getData().add(new XYChart.Data("2013", fakeValues.get(5)));
        series.getData().add(new XYChart.Data("2014", fakeValues.get(6)));
        series.getData().add(new XYChart.Data("2015", fakeValues.get(7)));
        series.getData().add(new XYChart.Data("2016", fakeValues.get(8)));
        series.getData().add(new XYChart.Data("2017", fakeValues.get(9)));

        factorChart.getData().add(series);

    }

}
