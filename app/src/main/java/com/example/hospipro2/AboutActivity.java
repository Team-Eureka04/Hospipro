package com.example.hospipro2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebView;

public class AboutActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);
        /*
        To Show The About:

        WebView myWebView = new WebView(this);
        setContentView(myWebView);
        myWebView.loadUrl("url");
        */
    }
}
