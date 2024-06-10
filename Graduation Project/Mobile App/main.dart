import 'package:flutter/material.dart';
import 'package:camera_app/screens/splash_screen.dart'; // Import the splash screen

void main() {
  runApp(TSRApp());
}

class TSRApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SplashScreen(), // Use the SplashScreen widget here
    );
  }
}


