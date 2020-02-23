package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.widget.TextView;
import android.os.AsyncTask;

import java.io.File;
import java.io.IOException;
import java.text.DateFormat;
import java.util.Date;
import android.os.Build;

import com.opencsv.CSVWriter;

import java.io.FileWriter;
import java.util.List;
import java.util.ArrayList;

import java.io.*;
import java.net.*;




public class MainActivity extends AppCompatActivity {

    String BrandModel;
    String sendLongLat;
    String Pressure;

    //variable declaration for pressure reading
    private TextView txt;
    private SensorManager sensorManager;
    private Sensor pressureSensor;
    private SensorEventListener sensorEventListener = new SensorEventListener() {
        @Override
        public void onSensorChanged(SensorEvent sensorEvent) {
            float[] values = sensorEvent.values; //variable to send values[0]
            Pressure = String.format("%.3f", values[0]);
            txt.setText("Pressure= "+ Pressure + " mBar");
        }

        @Override
        public void onAccuracyChanged(Sensor sensor, int i) {
        }
    };

    //variable declare for location
    private TextView txt2;
    private LocationManager locationManager;
    private LocationListener locationListener = new LocationListener() {
        @Override
        public void onLocationChanged(Location location) {
            double latitude = location.getLatitude();
            double longitude = location.getLongitude();
            txt2.setText("Longitude: " + longitude + "\n" + "Latitude: " + latitude);
            sendLongLat = longitude + "," + latitude; //variable to send sendLongLat
        }

        @Override
        public void onStatusChanged(String provider, int status, Bundle extras) {

        }

        @Override
        public void onProviderEnabled(String provider) {

        }

        @Override
        public void onProviderDisabled(String provider) {

        }
    };

    //variable dec for datetime
    private TextView txt3;

    //variable dec for phone model

    private TextView txt4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //find gui label
        txt = findViewById(R.id.txt);
        txt2 = findViewById(R.id.txt2);
        txt3 = findViewById(R.id.txt3);
        txt4 = findViewById(R.id.txt4);

        //sensordata
        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE); // instantiate sensor manager
        pressureSensor = sensorManager.getDefaultSensor(Sensor.TYPE_PRESSURE); // instantiate sensor


        //location
        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE); //instantiate location manager
        if (checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            //    Activity#requestPermissions
            // here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for Activity#requestPermissions for more details.
            return;
        }
        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000, 0, locationListener);
        //needed to update every 1s location
        if (checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && checkSelfPermission(Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            //    Activity#requestPermissions
            // here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for Activity#requestPermissions for more details.
            return;
        }
        Location location = locationManager.getLastKnownLocation(locationManager.NETWORK_PROVIDER);
        locationListener.onLocationChanged(location);

        //thread for datetime
         final Thread thread = new Thread(){
            @Override
            public void run() {
                try {
                    while (true) {
                        Thread.sleep(10000);
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                String currentDateTimeString = DateFormat.getDateTimeInstance().format(new Date()); //variable to send currentDateTimeString
                                txt3.setText(currentDateTimeString);
                                try {
                                    exportDataIntoCSV(currentDateTimeString, BrandModel, sendLongLat, Pressure );
                                } catch (Exception e) {
                                    e.printStackTrace();
                                }

                                //send data
                               new Connecting().execute("10.0.2.2:50500");
                            }
                        });
                    }
                } catch (InterruptedException e) {
                }
            }
        };

        thread.start();

        //phone model number return
        BrandModel = (Build.MANUFACTURER + " " + Build.MODEL); //variable to change BrandModel
        txt4.setText(BrandModel);
    }




    @Override
    protected  void onResume(){
        super.onResume();
        sensorManager.registerListener(sensorEventListener, pressureSensor, SensorManager.SENSOR_DELAY_UI); //barmoeter listen
        //current time

    }

    @Override
    protected void onPause() {
        super.onPause();
        sensorManager.unregisterListener(sensorEventListener); //barometer delisten
    }


    void exportDataIntoCSV(String Date, String Model , String Location, String Barometric_Pressure ) throws Exception{

        String baseDir = android.os.Environment.getExternalStorageDirectory().getAbsolutePath();
        String fileName = "data.csv";
        String filePath = baseDir + File.separator + fileName;
        File file = new File(filePath);
        CSVWriter writer;


        writer = new CSVWriter(new FileWriter(filePath));


        //Create record
        List<String[]> data = new ArrayList<String[]>();
        data.add(new String[] {"Date","Model", "Location", "Barometric Pressure"});
        data.add(new String[] {Date,Model, Location, Barometric_Pressure});

        writer.writeAll(data);

        writer.flush();
        //close the writer
        writer.close();

    }

    private class Connecting extends AsyncTask<String, Integer, String>
    {
        @Override
        protected String doInBackground(String... serverAdd)
        {
            String baseDir = android.os.Environment.getExternalStorageDirectory().getAbsolutePath();
            String fileName = "data.csv";
            String filePath = baseDir + File.separator + fileName;

            File sdFile = new File(filePath);

            try {

                Socket client = new Socket("10.0.2.2", 50500);

                System.out.println("REEEEEEEE");

                OutputStream outputStream = client.getOutputStream();
                System.out.println("REEEEEEEE");

                byte[] buffer = new byte[1024];
                FileInputStream in = new FileInputStream(sdFile);
                int rBytes;
                while((rBytes = in.read(buffer, 0, 1024)) != -1)
                {
                    outputStream.write(buffer, 0, rBytes);
                }

                outputStream.flush();
                outputStream.close();
                client.close();


            } catch (UnknownHostException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }

            return null;
        }
    }

}
