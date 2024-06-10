import 'package:camera_app/screens/Predect+photo.dart';
import 'package:flutter/material.dart';
import 'package:camera_app/screens/LogoPage.dart';
import 'package:camera_app/screens/TrafficSignPredictionPage.dart';
import 'AboutUsPage.dart';

void main() {
  runApp(Startpage());
}

class Startpage extends StatefulWidget {
  final String title = "Sign Sight";

  @override
  _StartpageState createState() => _StartpageState();
}

class _StartpageState extends State<Startpage> {
  int _currentIndex = 0;

  final List<Widget> _pages = [
    LogoPage(),
    TrafficSignPredictionPage(),
    PredectWithPhoto(),
    AboutUsSeparatePage(),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: null,
        body: _pages[_currentIndex],
        bottomNavigationBar: BottomNavigationBar(
          currentIndex: _currentIndex,
          type: BottomNavigationBarType.fixed,
          backgroundColor: Color.fromRGBO(
              255, 255, 255, 1), // BottomNavigationBar background color
          selectedItemColor: Colors.blue, // Set the selected item color to blue
          unselectedItemColor: Color.fromRGBO(158, 158, 158, 1), // Set the unselected item color to grey
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: 'Home',
            ),
            BottomNavigationBarItem(
              icon: Icon(
                Icons.assistant_direction_outlined,
                size: 30, // Set the size of the icon
                color: Colors.blue, // Set the icon color to blue
              ),
              label: 'RealTime',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.camera),
              label: 'Predection',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.info),
              label: 'About Us',
            ),
          ],
          onTap: (index) {
            setState(() {
              _currentIndex = index;
            });
          },
        ),
      ),
    );
  }
}
