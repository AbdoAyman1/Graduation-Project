import 'package:flutter/material.dart';

class ProfileDetailPage extends StatelessWidget {
  final String name;
  final String number;
  final String email;
  final String imagePath;
  final String description;

  const ProfileDetailPage({
    required this.name,
    required this.number,
    required this.email,
    required this.imagePath,
    required this.description,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Profile Detail",
          style: TextStyle(
            color: Colors.black, // Set the title color to blue
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.white, // Set the app bar background color to white
        iconTheme: IconThemeData(color: Colors.black), // Set the back arrow color to black
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              CircleAvatar(
                radius: 50,
                backgroundImage: AssetImage(imagePath),
              ),
              SizedBox(height: 30),
              Text(
                name,
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 20),
              Text(
                description,
                style: TextStyle(fontSize: 18),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 10),
              Text(
                "Number: $number",
                style: TextStyle(fontSize: 18),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 10),
              Text(
                "Email: $email",
                style: TextStyle(fontSize: 18),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
