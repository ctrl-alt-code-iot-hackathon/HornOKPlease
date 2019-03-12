#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

int M1C=12;
int M1IN=14;
int M2C=13;
int M2IN=15;
const int trigPin = 2;  //D4
const int echoPin = 0;  //D3

int isOn=1;
long duration;
int distance;

// Replace with your network credentials

const char* ssid = "raspberrypi";
const char* password = "pirocks@1";

ESP8266WebServer server(80);   //instantiate server at port 80 (http port)
 
void rotate_left()
{
  digitalWrite(M1C,LOW);
  digitalWrite(M1IN,HIGH);
  digitalWrite(M2C,HIGH);
  digitalWrite(M2IN,LOW);
}
void rotate_right()
{
  digitalWrite(M2C,LOW);
  digitalWrite(M2IN,HIGH);
  digitalWrite(M1C,HIGH);
  digitalWrite(M1IN,LOW);
}
void straight()
{
  digitalWrite(M2C,HIGH);
  digitalWrite(M2IN,LOW);
  digitalWrite(M1C,HIGH);
  digitalWrite(M1IN,LOW);
  
}
void back()
{
  digitalWrite(M2C,LOW);
  digitalWrite(M2IN,HIGH);
  digitalWrite(M1C,LOW);
  digitalWrite(M1IN,HIGH);
}
void halt()
{
   digitalWrite(M2C,LOW);
  digitalWrite(M2IN,LOW);
  digitalWrite(M1C,LOW);
  digitalWrite(M1IN,LOW);
}
void setup(void){
pinMode(M1C,OUTPUT);
pinMode(M1IN,OUTPUT);
pinMode(M2C,OUTPUT);
pinMode(M2IN,OUTPUT);
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  
  Serial.begin(115200);
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");
 
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  server.on("/right", [](){
    server.send(200, "text/html", "success_right");
    rotate_right();
  });
  server.on("/left", [](){
    server.send(200, "text/html", "success_left");
    rotate_left();
  });
  
  server.on("/forward", [](){
    server.send(200, "text/html", "success_forward");
    straight();
  });
  
  server.on("/backward", [](){
    server.send(200, "text/html", "success_backward");
    back();
  });
  
  server.on("/halt", [](){
    server.send(200, "text/html", "success_halt");
    halt();
  });
  server.on("/on", [](){
    server.send(200, "text/html", "success_on");
    isOn=1;
  });
  server.on("/off", [](){
    server.send(200, "text/html", "success_off");
    isOn=0;
    halt();
  });
  
  halt();
  server.begin();
  Serial.println("Web server started!");
}
void distance_() {

// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);
if(distance<10 && distance>0){
  halt();
  }
else if(distance>10 && distance<50){
  if(isOn)
  straight();
  }
delay(100);
}
void loop(void){
  server.handleClient();
  distance_();
}
