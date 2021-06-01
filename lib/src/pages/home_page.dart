import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {

  @override
  _HomePageState createState() =>  _HomePageState();
}

class  _HomePageState extends State <HomePage> {
  // members
  static AudioCache player = AudioCache();

  // methods
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Imagen con Sonido'),
        centerTitle: true,
      ),

      body:
      TextButton(
        child: FadeInImage(
          image: NetworkImage('https://images.wallpaperscraft.com/image/cat_cosmonaut_space_suit_130111_1920x1080.jpg'),
          placeholder: AssetImage('assets/jar-loading.gif'),
          fadeInDuration: Duration(milliseconds: 200),
          height: 250.0,
          fit: BoxFit.cover,
        ),
        onPressed: (){
          player.play('meowsound.mp3');
        },
      )



    );
  }
}