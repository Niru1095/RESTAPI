# RESTAPI
1) Write a program that retrieves data representing all, what we’ll call “subway” routes:
“Light Rail” (type 0) and “Heavy Rail” (type 1). The program should list their “long names”
on the console.
Ans: The following url fetches the routes in json format and displays it in Django RESTAPI framework.<br/><br/>
      ● Created a Django framework based REST API application for following input and output
      parameters:
      ● INPUT - <JSON structure>
      [
      ‘url_1’,
      ‘url_2’,
      …
      ‘url_n’,
      ]
      ● OUTPUT - <JSON structure>
      {
      ‘url_1’: output_data,
      ‘url_2’: output_data,
      ‘url_3’: output_data,
      }

<br/><br/> 
![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drfroutes.png) <br/><br/>
  
  2) Extend your program so it displays the following additional information.
      a) The name of the subway route with the most stops as well as a count its stops.
          Ans. The subway routes with direction_name ["West", "East"] as most stops and the count is length of list that is 5 are most stops.
      
  ![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drf_most_stops.png) <br/><br/>
  
      b) The name of the subway route with the fewest stops as well as a count its stops.
           Ans. The subway routes with direction_name ["Outbound", "Inbound"] as fewest stops and the count is length of list that is 1 stop.
  
  ![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drf_fewest_stops.png) <br/><br/>
  
  
  
  
  
  
