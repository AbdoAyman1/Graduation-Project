import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'package:camera/camera.dart';

class TrafficSignPredictionPage extends StatefulWidget {
  const TrafficSignPredictionPage({Key? key}) : super(key: key);

  @override
  _TrafficSignPredictionPageState createState() =>
      _TrafficSignPredictionPageState();
}

class _TrafficSignPredictionPageState extends State<TrafficSignPredictionPage> {
  XFile? _selectedImage;
  String _predictedClass = '';
  final picker = ImagePicker();
  CameraController? _cameraController;
  late Timer _captureTimer;

  Future<void> _initializeCamera() async {
    final cameras = await availableCameras();
    final firstCamera = cameras.first;

    _cameraController = CameraController(
      firstCamera,
      ResolutionPreset.medium,
    );

    await _cameraController!.initialize();
  }

  Future<void> _captureImageAndPredict() async {
    if (_cameraController != null && _cameraController!.value.isInitialized) {
      try {
        final XFile image = await _cameraController!.takePicture();
        setState(() {
          _selectedImage = image;
          _predictedClass = ''; // Clear previous predictions
        });

        await _predictTrafficSign();
      } catch (e) {
        print('Error capturing image: $e');
      }
    } else {
      print('Camera not initialized');
    }
  }

  Future<void> _predictTrafficSign() async {
    if (_selectedImage == null) {
      // No image captured yet
      _showErrorDialog('Please capture a traffic sign first!');
      return;
    }

    if (_cameraController != null && _cameraController!.value.isInitialized) {
      final uri = Uri.parse('http://192.168.137.215:8000/predict_traffic_sign'); // Update with your server URL

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
            _predictedClass = data['predicted_class'];
          });
        } else {
          print('Error: ${response.body}');
        }
      } catch (e) {
        print('Error: $e');
      }
    } else {
      print('Camera not initialized');
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
  void initState() {
    super.initState();
    _initializeCamera().then((_) {
      setState(() {});
    });

    // Start capturing images automatically every 15 seconds
    _captureTimer = Timer.periodic(Duration(seconds: 15), (Timer timer) {
      _captureImageAndPredict();
    });
  }

  @override
  void dispose() {
    _cameraController?.dispose();
    _captureTimer.cancel(); // Cancel the timer when disposing the widget
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_cameraController == null || !_cameraController!.value.isInitialized) {
      return Center(child: CircularProgressIndicator());
    }
    return Scaffold(
      appBar: AppBar(
        title: Text('Traffic Sign Prediction'),
      ),
      body: Center(
        child: Stack(
          children: [
            CameraPreview(_cameraController!),
            Positioned(
              bottom: 20,
              right: 20,
              child: FloatingActionButton(
                child: Icon(Icons.camera_alt),
                onPressed: _captureImageAndPredict,
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: BottomAppBar(
        child: Container(
          height: 50,
          padding: EdgeInsets.all(16),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (_predictedClass.isNotEmpty)
                Text(
                  'result: $_predictedClass',
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
