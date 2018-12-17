package qli;

import com.fasterxml.jackson.databind.ObjectMapper;
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
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import qli.data.MockQoLData;
import qli.data.QualityOfLife;
import qli.utils.ColorsLegend;

import javafx.scene.control.ListView;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
import qli.utils.Countries;
import qli.utils.Factors;
import qli.world.BusinessRegion;
import qli.world.Country;
import qli.world.World;
import qli.world.WorldBuilder;

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

    @FXML private StackPane stackPane;

    @FXML private LineChart<Float,Double> factorChart;
    @FXML private CategoryAxis yearsAxis;
    @FXML private NumberAxis values;

    ObservableList<String> factors= FXCollections.observableArrayList();
    ObservableList<String> countries = FXCollections.observableArrayList();
    private ArrayList<String> selectedCountries = new ArrayList<String>();
    private Double currentYear;
    private String selectedFactor, selectedCountry;
    private QualityOfLife qualityOfLife;
    private int countriesCounter = 0;
    private World world;
    private MockQoLData mockData = new MockQoLData();


    @FXML
    private void initialize() {
        try {
            getData();
        } catch (Exception e) {
            e.printStackTrace();
        }
        setLegend();
        setLabels();
        setFactors();
        setCountries();
        showMap();
        listFactors.getSelectionModel().selectFirst();
        countryList.getSelectionModel().select("Poland");
        countryList.scrollTo("Poland");
        selectedCountry = countryList.getSelectionModel().getSelectedItem();
        selectedFactor = listFactors.getSelectionModel().getSelectedItem();
        currentYear = sliderYears.getValue();
        fillChart(selectedFactor,selectedCountry, true);
        listFactors.setOnMouseClicked(new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                selectedFactor = listFactors.getSelectionModel().getSelectedItem();
                fillChart(selectedFactor, selectedCountry,true);
                countriesCounter = 0;
                selectedCountries.clear();
                selectedCountries.add(selectedCountry);
            }
        });
        countryList.setOnMouseClicked(new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                boolean isSelected = false;
                selectedCountry = countryList.getSelectionModel().getSelectedItem();
                if(selectedCountries.isEmpty()) {
                    selectedCountries.add(selectedCountry);
                }

                for (String country : selectedCountries) {
                    if(country.contains(selectedCountry)) {
                        isSelected = true;
                    }
                }

                if(countriesCounter < 4 && !isSelected) {
                    selectedCountries.add(selectedCountry);
                    fillChart(selectedFactor,selectedCountry, false);
                    countriesCounter++;
                }
            }
        });
        showQOL(2018 - currentYear.intValue());
    }


    private void getData() throws IOException, InterruptedException{
        String command = "python ./script/test.py";
        Process p = null;
        try {
            p = Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            e.printStackTrace();
        }

        if(p != null) {
            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String s;
            if((s = br.readLine()) != null) {
                //System.out.println(s);
            }
            p.waitFor();
            p.destroy();

            ObjectMapper mapper = new ObjectMapper();
            qualityOfLife = mapper.readValue(s, QualityOfLife.class);
        } else {
            System.out.println("ERROR");
        }
        //System.out.println(qualityOfLife.getCountries());
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
        }

        listFactors.setItems(factors);
    }

    private void setCountries() {
        for(String country : qualityOfLife.getCountries().values()) {
            countries.add(country);
        }
        countryList.setItems(countries);
    }
    @FXML
    private void increaseYear() {
        if(currentYear < sliderYears.getMax()) {
            sliderYears.increment();
            currentYear = sliderYears.getValue();
        }
        System.out.println(currentYear);
        showQOL(2018 - currentYear.intValue());

    }
    @FXML
    private void decreaseYear() {
        if(currentYear > sliderYears.getMin()) {
            sliderYears.decrement();
            currentYear = sliderYears.getValue();
        }
        System.out.println(currentYear);
        showQOL(2018 - currentYear.intValue());

    }

    private String getCountryByName(String countryName) {
        for (Map.Entry<String,String> entry : qualityOfLife.getCountries().entrySet()) {
            if(entry.getValue().equals(countryName)) {
                System.out.println(entry.getValue());
                return entry.getKey();
            }
        }
        return "";
    }

    public String getFactorByValue(String factorName) {
        for(Factors factor : Factors.values()) {
            if(factor.toString() == factorName) {
                return factor.name();
            }
        }
        return "";
    }

    private void fillChart(String factorName, String countryName, boolean clear) {
        if(clear)
            factorChart.getData().clear();
        List<Double> realValues = qualityOfLife.getQualities().get(getCountryByName(countryName)).get(getFactorByValue(factorName));
        XYChart.Series series = new XYChart.Series();
        factorChart.setTitle(factorName);
        series.setName(countryName);
        series.getData().add(new XYChart.Data("2008", realValues.get(4)));
        series.getData().add(new XYChart.Data("2009", realValues.get(5)));
        series.getData().add(new XYChart.Data("2010", realValues.get(6)));
        series.getData().add(new XYChart.Data("2011", realValues.get(7)));
        series.getData().add(new XYChart.Data("2012", realValues.get(8)));
        series.getData().add(new XYChart.Data("2013", realValues.get(9)));
        series.getData().add(new XYChart.Data("2014", realValues.get(10)));
        series.getData().add(new XYChart.Data("2015", realValues.get(11)));
        series.getData().add(new XYChart.Data("2016", realValues.get(12)));
        series.getData().add(new XYChart.Data("2017", realValues.get(13)));

        factorChart.getData().add(series);

    }

    private void showMap() {
        world = WorldBuilder.create()
                .resolution(World.Resolution.HI_RES)
                .zoomEnabled(true)
                .selectionEnabled(true)
                .build();
        stackPane.getChildren().add(world);
    }

    private void showQOL(int year) {
        for (Country country : Country.values()) {
            if(mockData.getAllCountries().get(country.getName()) == null) {
                country.setColor(Color.valueOf(ColorsLegend.GRAY.toString()));
            }else if(mockData.getAllCountries().get(country.getName()).get(year) >= 30.0) {
                country.setColor(Color.valueOf(ColorsLegend.RED.toString()));
            } else if (mockData.getAllCountries().get(country.getName()).get(year) < 25.0 && mockData.getAllCountries().get(country.getName()).get(year) >= 22.0) {
                country.setColor(Color.valueOf(ColorsLegend.DARK_ORANGE.toString()));
            } else if (mockData.getAllCountries().get(country.getName()).get(year) < 22.0 && mockData.getAllCountries().get(country.getName()).get(year) >= 20.0) {
                country.setColor(Color.valueOf(ColorsLegend.LIGHT_ORANGE.toString()));
            }else if (mockData.getAllCountries().get(country.getName()).get(year) < 20.0 && mockData.getAllCountries().get(country.getName()).get(year) >= 15.0) {
                country.setColor(Color.valueOf(ColorsLegend.YELLOW.toString()));
            }else if (mockData.getAllCountries().get(country.getName()).get(year) < 10.0) {
                country.setColor(Color.valueOf(ColorsLegend.LIGHT_YELLOW.toString()));
            }


        }
    }



}
