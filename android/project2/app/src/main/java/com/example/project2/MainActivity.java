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

        Toast.makeText(this,"onCreate", Toast.LENGTH_LONG).show();
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
        Toast.makeText(this,"onRestart", Toast.LENGTH_LONG).show();
    }

    @Override
    protected void onPause() {
        Log.d(LOGID,"onPause called");
        Toast.makeText(this,"onPause", Toast.LENGTH_LONG).show();
        super.onPause();
    }

    @Override
    protected void onResume() {
        Log.d(LOGID,"onResume called");
        super.onResume();
        Toast.makeText(this,"onResume", Toast.LENGTH_LONG).show();
    }

    @Override
    protected void onStart() {
        Log.d(LOGID,"onStart called");
        super.onStart();
        try{
            Toast.makeText(this,"onStart" + 5/0, Toast.LENGTH_LONG).show();
        }catch(Exception e)
        {
            Log.d(LOGID, "Err", e);
        }

    }

}