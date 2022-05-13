# RESTAPI
1) Write a program that retrieves data representing all, what we’ll call “subway” routes:
“Light Rail” (type 0) and “Heavy Rail” (type 1). The program should list their “long names”
on the console.
Ans: The following url fetches the routes in json format and displays it in Django RESTAPI framework.<br/><br/>
      ● Created a Django framework based REST API application for following input and output <br/>
      parameters: <br/>
      ● INPUT - <JSON structure> <br/>
      [ <br/>
      ‘url_1’, <br/>
      ‘url_2’, <br/>
      … <br/>
      ‘url_n’, <br/>
      ] <br/>
      ● OUTPUT - <JSON structure> <br/>
      { <br/>
      ‘url_1’: output_data, <br/>
      ‘url_2’: output_data, <br/>
      ‘url_3’: output_data, <br/>
      } <br/>

<br/><br/> 
![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drfroutes.png) <br/><br/>
  
  2) Extend your program so it displays the following additional information. <br/>
      a) The name of the subway route with the most stops as well as a count its stops. <br/>
          Ans. The subway routes with most stops are from direction_name ["West", "East"] and the count is length of list that is 5 are most stops. <br/>
      
  ![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drf_most_stops.png) <br/><br/>
  
      b) The name of the subway route with the fewest stops as well as a count its stops. <br/>
           Ans. The subway routes with fewest stops are from direction_name ["Outbound", "Inbound"] and the count is length of list that is 1 stop. <br/>
  
  ![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drf_fewest_stops.png) <br/><br/>
         
      c) A list of the stops that connect two or more subway routes along with the relevant route names for each of those stops.
         Ans. The subway routes with two or more routes are from direction_name ["West", "East"] & ["South", "North"]
      
      ![image](https://github.com/Niru1095/RESTAPI/blob/master/DRF_screenshots/drf_routes_2_more.png) <br/><br/> <br/><br/>
      
      
      
      
      ● Virtual environment and requirements.txt must be created.
      Ans. Created with name myvenv.
      

  
  
  
  
  
  
