import 'package:flutter/material.dart';
import 'package:camera_app/screens/ProfileDetailPage.dart';

class AboutUsSeparatePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "About Us",
          style: TextStyle(
            color: Colors.black, // Set the title color to blue
          ),
        ),
        centerTitle: true,
        backgroundColor: Color.fromRGBO(255, 255, 255, 1), // AppBar background color
      ),
      backgroundColor: Color.fromRGBO(223, 238, 255, 1), // Page background color
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Text(
                "🌟It will contribute to making the roads safer and is suitable for use in Autonomous Vehicles🌟",
                style: TextStyle(
                  fontSize: 17,
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 0, 0, 0),
                ),
                textAlign: TextAlign.center,
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  Text(
                    "Our graduation project aims to create an app that uses the phone camera to detect traffic signs and perform actions based on the detected sign. "
                    "Actions may include stopping, going backward, going forward, or adjusting the car's speed.",
                    style: TextStyle(fontSize: 16),
                    textAlign: TextAlign.center,
                  ),
                  SizedBox(height: 16),
                  Text(
                    "The project involves using computer vision algorithms and machine learning techniques to identify and interpret traffic signs in images or video streams.",
                    style: TextStyle(fontSize: 16),
                    textAlign: TextAlign.center,
                  ),
                  SizedBox(height: 16),
                  Text(
                    "It will contribute to making the roads safer and is suitable for use in Autonomous Vehicles!",
                    style: TextStyle(fontSize: 16,),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
            ClickableProfileWidget(
              name: "Abdelrahman Ayman (TL) 🌟",
              number: "+111222333",
              email: "ayman@email.com",
              imagePath:
                  "assets/images/WhatsApp Image 2023-12-09 at 14.51.19_aed2644d.jpg",
              avatarRadius: 20,
              description: "Team Leader",
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ClickableProfileWidget(
                  name: "Mariem Michael",
                  number: "+123456789",
                  email: "mariem@email.com",
                  imagePath: "assets/images/Capture44.PNG",
                  avatarRadius: 20,
                  description: "Flutter Team",
                ),
                ClickableProfileWidget(
                  name: "Abdelrahman Naser (FL) 🌟",
                  number: "+987654321",
                  email: "abdelrahman@email.com",
                  imagePath: "assets/images/photo_2023-12-01_10-55-20.png",
                  avatarRadius: 20,
                  description: "Flutter Leader",
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ClickableProfileWidget(
                  name: "Makarious Mounir",
                  number: "+444555666",
                  email: "mounir@email.com",
                  imagePath: "assets/images/MK.jpg",
                  avatarRadius: 20,
                  description: "Ai Team",
                ),
                ClickableProfileWidget(
                  name: "Mahmoud Magdy",
                  number: "+777888999",
                  email: "mahmoud@email.com",
                  imagePath: "assets/images/photo_2023-12-09_14-09-41.jpg",
                  avatarRadius: 20,
                  description: "Ai Team",
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ClickableProfileWidget(
                  name: "Ibrahim Sedek",
                  number: "+333222111",
                  email: "ibrahim@email.com",
                  imagePath: "assets/images/photo_2023-12-09_14-09-38.jpg",
                  avatarRadius: 20,
                  description: "Ai Team",
                ),
                ClickableProfileWidget(
                  name: "Mohamed Abdallah",
                  number: "+555444333",
                  email: "mohamed@email.com",
                  imagePath: "assets/images/photo_2023-12-09_14-24-10.jpg",
                  avatarRadius: 20,
                  description: "Ai Team",
                ),
              ],
            ),
            // Add more team members as needed
          ],
        ),
      ),
      bottomNavigationBar: BottomAppBar(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
            "Faculty of Computer and Information Technology EELU.2024",
            style: TextStyle(
              fontSize: 14,
              fontStyle: FontStyle.italic,
              color: Colors.grey,
            ),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}

class ClickableProfileWidget extends StatelessWidget {
  final String name;
  final String number;
  final String email;
  final String imagePath;
  final String description;
  final double avatarRadius;

  const ClickableProfileWidget({
    required this.name,
    required this.number,
    required this.email,
    required this.imagePath,
    required this.description,
    required this.avatarRadius,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ProfileDetailPage(
              name: name,
              number: number,
              email: email,
              imagePath: imagePath,
              description: description,
            ),
          ),
        );
      },
      child: Container(
        width: MediaQuery.of(context).size.width / 2.2,
        margin: EdgeInsets.all(8),
        child: Card(
          elevation: 5,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              CircleAvatar(
                radius: avatarRadius,
                backgroundImage: AssetImage(imagePath),
              ),
              SizedBox(height: 5),
              Text(
                name,
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 5),
              Text(
                description,
                style: TextStyle(fontSize: 12, fontStyle: FontStyle.italic),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 5),
              Text(
                "Number: $number",
                style: TextStyle(fontSize: 10, color: Colors.grey),
                textAlign: TextAlign.center,
              ),
              Text(
                "Email: $email",
                style: TextStyle(fontSize: 10, color: Colors.grey),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
