package com.example.project2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

private static final String LOGID = "myLogs";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d(LOGID,"onCreate called");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Toast.makeText(this,"", Toast.LENGTH_LONG).show();
    }

    @Override
    protected void onStop() {
        Log.d(LOGID,"onStop called");
        super.onStop();
    }

    @Override
    protected void onRestart() {
        Log.d(LOGID,"onRestart called");
        super.onRestart();
    }

    @Override
    protected void onPause() {
        Log.d(LOGID,"onPause called");
        super.onPause();
    }

    @Override
    protected void onResume() {
        Log.d(LOGID,"onResume called");
        super.onResume();
    }

    @Override
    protected void onStart() {
        Log.d(LOGID,"onStart called");
        super.onStart();
    }

}