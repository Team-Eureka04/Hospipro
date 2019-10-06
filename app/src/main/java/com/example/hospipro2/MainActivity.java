package com.example.hospipro2;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.Toast;

import com.hitomi.cmlibrary.CircleMenu;
import com.hitomi.cmlibrary.OnMenuSelectedListener;

public class MainActivity extends AppCompatActivity {

    String arrayName [] = {"LogInPatient","LogInDoctor", "SignUp", "About"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CircleMenu circleMenu = (CircleMenu)findViewById(R.id.circle_menu);
        circleMenu.setMainMenu(Color.parseColor("#FFFFFF"), R.drawable.plus5, R.drawable.ic_wrong3);
        circleMenu.addSubMenu(Color.parseColor("#3BA7E6"), R.drawable.new_login);
        circleMenu.addSubMenu(Color.parseColor("#32BEA6"), R.drawable.doctor_login);
        circleMenu.addSubMenu(Color.parseColor("#FFFFFF"), R.drawable.ic_signup);
        circleMenu.addSubMenu(Color.parseColor("#FD0001"), R.drawable.new_info);
        circleMenu.setOnMenuSelectedListener(new OnMenuSelectedListener() {

            @Override
            public void onMenuSelected(int index) {
                if (index == 0) {
                    Toast.makeText(MainActivity.this, "You selected Patient's LogIn", Toast.LENGTH_SHORT).show();
                    new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
                        @Override
                        public void run() {
                            openLogin();
                        }
                    }, 800);

                }
                if (index == 1) {
                    Toast.makeText(MainActivity.this, "You selected Doctor's LogIn", Toast.LENGTH_SHORT).show();
                    new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
                        @Override
                        public void run() {
                            openDocLogin();
                        }
                    }, 800);
                }
                if (index == 2) {
                    Toast.makeText(MainActivity.this, "You selected SignUp", Toast.LENGTH_SHORT).show();
                    new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
                        @Override
                        public void run() {
                            openSignup();
                        }
                    }, 800);
                }
                if (index == 3) {
                    Toast.makeText(MainActivity.this, "You selected About", Toast.LENGTH_SHORT).show();
                    new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
                        @Override
                        public void run() {
                            openAbout();
                        }
                    }, 800);
                }
            }
        });
    }
    public void openLogin() {
        Intent intent = new Intent(this, LoginActivity.class);
        startActivity(intent);
    }
    public void openDocLogin() {
        Intent intent2 = new Intent(this, DocLoginActivity.class);
        startActivity(intent2);
    }
    public void openSignup() {
        Intent intent3 = new Intent(this, SignupActivity.class);
        startActivity(intent3);
    }
    public void openAbout() {
        Intent intent4 = new Intent(this, AboutActivity.class);
        startActivity(intent4);
    }
}