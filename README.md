 # Weather App                                                                                   
                                                                                                   
   A simple desktop weather application built with Python that displays real-time weather data for 
 any city in the world.                                                                            
                                                                                                   
   ![Weather App Screenshot](screenshot.png)                                                       
                                                                                                   
   ## Features                                                                                     
                                                                                                   
   - 🌡️ Current temperature (°C)                                                                   
   - 💨 Wind speed (km/h)                                                                          
   - 🔽 Atmospheric pressure (hPa)                                                                 
   - 🌅 Sunrise and sunset times for the searched location                                         
   - Clean dark-themed GUI built with CustomTkinter                                                
                                                                                                   
   ## Requirements                                                                                 
                                                                                                   
   - Python 3.8+                                                                                   
   - `customtkinter`                                                                               
   - `requests`                                                                                    
                                                                                                   
   Install dependencies:                                                                           
                                                                                                   
   ```bash                                                                                         
   pip install customtkinter requests                                                              
 ```                                                                                               
                                                                                                   
 Setup                                                                                             
                                                                                                   
 1. Clone the repository:                                                                          
 ```bash                                                                                           
   git clone https://github.com/Ticbruh-jpg/weather_app.git                                        
   cd weather_app                                                                                  
 ```                                                                                               
                                                                                                   
 2. Get a free API key from OpenWeatherMap (https://openweathermap.org/api)                        
 3. Open weather_app.py and replace your_api_key_here with your key:                               
 ```python                                                                                         
   api_key = 'your_actual_api_key'                                                                 
 ```                                                                                               
                                                                                                   
 Usage                                                                                             
                                                                                                   
 ```bash                                                                                           
   python weather_app.py                                                                           
 ```                                                                                               
                                                                                                   
 Type a city name into the search box and click Search.                                            
                                                                                                   
 APIs Used                                                                                         
                                                                                                   
 - OpenWeatherMap API (https://openweathermap.org/api) — weather data                              
 - Sunrise-Sunset API (https://sunrise-sunset.org/api) — sunrise/sunset times (no key required)    
                                                                                                   
 License                                                                                           
                                                                                                   
 MIT
