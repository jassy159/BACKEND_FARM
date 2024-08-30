#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "WantIt";
const char* password = "12345678";

const char* serverName = "https://cadd-59-96-30-178.ngrok-free.app/data/sensordata/"; //sever domain
const char* endpoints[] = {"waterstate", "lightstate","shadestate","miststate","heaterstate","fanstate"}; //server api endpoints 

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    for (int i = 0; i < 5; i++) {
      String url = String(serverName) + endpoints[i] + '/';
      http.begin(url);
      int httpResponseCode = http.GET();

      if (httpResponseCode > 0) {
        Serial.print("HTTP Response Code for endpoint ");
        Serial.print(endpoints[i]);
        Serial.print(": ");
        Serial.println(httpResponseCode);
        String payload = http.getString();
        Serial.println("Payload: ");
        Serial.println(payload);

        // Allocate the JSON document
        StaticJsonDocument<300> doc;

        // Parse JSON array
        DeserializationError error = deserializeJson(doc, payload);

        if (error) {
          Serial.print("deserializeJson() failed: ");
          Serial.println(error.c_str());
          return;
        }

        // Extract the first object from the array
        JsonArray array = doc.as<JsonArray>();
        if (!array.isNull() && array.size() > 0) {
          JsonObject obj = array[0];
          bool state = obj["state"];
          Serial.print("State for endpoint ");
          Serial.print(endpoints[i]);
          Serial.print(": ");
          
          Serial.println(state ? "ON" : "OFF");
        } else {
          Serial.println("Empty array or invalid JSON format.");
        }
      } else {
        Serial.print("Error on sending GET request for endpoint ");
        Serial.print(endpoints[i]);
        Serial.print(": ");
        Serial.println(httpResponseCode);
      }

      http.end(); // Free resources
      delay(2000); // Small delay between requests
    }

  } else {
    Serial.println("WiFi not connected");
  }

  delay(3000); // Wait 3 seconds before the next loop iteration
}
