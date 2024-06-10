import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';

class PredectWithPhoto extends StatefulWidget {
  const PredectWithPhoto({Key? key}) : super(key: key);

  @override
  _PredectWithPhotoState createState() => _PredectWithPhotoState();
}

class _PredectWithPhotoState extends State<PredectWithPhoto> {
  XFile? _selectedImage;
  String _predictedClass = '';
  final picker = ImagePicker();

  Future<void> _selectImage() async {
    final XFile? selectedImage =
        await picker.pickImage(source: ImageSource.gallery);
    setState(() {
      _selectedImage = selectedImage;
      _predictedClass = ''; // Clear previous predictions
    });
  }

  Future<void> _predictTrafficSign() async {
    if (_selectedImage == null) {
      // No image selected
      _showErrorDialog('No image selected. Please select one!');
      return;
    }

    final uri = Uri.parse(
        'http://192.168.137.215:8000/predict_traffic_sign'); // Update with your server URL

    final request = http.MultipartRequest('POST', uri)
      ..files.add(await http.MultipartFile.fromPath(
        'image',
        _selectedImage!.path,
      ));

    try {
      final response = await http.Response.fromStream(await request.send());
      if (response.statusCode == 200) {
        final Map<String, dynamic> data = jsonDecode(response.body);
        setState(() {
          _predictedClass = data['predicted_class']; // Corrected line
        });
      } else {
        print('Error: ${response.body}');
      }
    } catch (e) {
      print('Error: $e');
    }
  }

  void _showErrorDialog(String errorMessage) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Error'),
          content: Text(errorMessage),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white, // Set the background color to white
        title: Text(
          'Traffic Sign Prediction',
          style: TextStyle(
            color: Colors.black, // Set the text color to black
          ),
        ),
        centerTitle: true, // Center the title
      ),
      body: Container(
        color: Color.fromRGBO(
            223, 238, 255, 1), // Set the background color to gray
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                if (_selectedImage != null)
                  Image.file(
                    File(_selectedImage!.path),
                    height: 150,
                  ),
                SizedBox(height: 16),
                ElevatedButton(
                  onPressed: _selectImage,
                  child: Text('Select Image'),
                  style: ElevatedButton.styleFrom(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20.0),
                    ),
                    fixedSize: Size.fromWidth(120),
                  ),
                ),
                SizedBox(height: 16),
                ElevatedButton(
                  onPressed: _predictTrafficSign,
                  child: Text('Predict'),
                  style: ElevatedButton.styleFrom(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20.0),
                    ),
                    fixedSize: Size.fromWidth(120), // Set the fixed size
                  ),
                ),
                SizedBox(height: 16),
                if (_predictedClass.isNotEmpty)
                  Text(
                    'Result: $_predictedClass',
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
