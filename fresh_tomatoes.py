#!/usr/bin/env python
import webbrowser
import os
import re
# styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<head >
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Movie trailers</title>
    <style>
  .modal {
    display: none;
    position: fixed;
    z-index: 1;
    padding-top:100px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.4);
}
.modal-content {
    margin: 10% auto;
    padding: 40px;
    width: 60%;
    min-height:350px;
}
/* The Close Button */
.close{
    position:absolute;
    top:17%;
    left:31%;
    margin:10% auto;
    color:blue;
    float:right;
    font-size:28px;
    font-weight:bold;
}

.close:hover,
.close:focus {
    background-color:steelblue;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}

      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       }
     .movie{
          width:100%;
          min-height:150px;
          cursor:pointer;
        }
         @media screen and (min-width :850px)  {
       div.v1:hover{
             border:1px;
             border-radius:10px;
             background-color:royalblue;
             }
       div.v2:hover{
             border:1px;
             border-radius:10px;
             background-color:springgreen;
             }
       div.v3:hover{
             border:1px;
             border-radius:10px;
             background-color:teal;
             }
       div.v4:hover{
             border:1px;
             border-radius:10px;
             background-color:tomato;
             }
        div.v5:hover{
             border:1px;
             background-color:red;
             }
         div.v6:hover{
             border:1px;
             background-color:skyblue;
             }
       .v1{width:33%;}
       .v2{width:34%;}
       .v3{width:33%;}
       .v4{width:33%;}
       .v5{width:34%;}
       .v6{width:33%;}
       h1 {background-color:blue;}
        }
         h1 {background-color:blue;
         font-family:arial,cursive;}
         </style>
       <div>
    <!-- The Modal -->
       <div id="myModal" class="modal">
<!-- Modal content -->
         <div class="modal-content">
              <span class="close">&times;</span>
    <iframe id="g" width="60%" height="300" src=""
         frameborder="0" allow="autoplay; encrypted-media"
         allowfullscreen></iframe>
        </div>
         </div>
</div>
<script>
  var modal = document.getElementById('myModal');
  var span = document.getElementsByClassName("close")[0];
   onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("g").setAttribute("src",c);
  }
   span.onclick = function() {
        document.getElementById("g").src=document.getElementById("g").src;
        modal.style.display = "none";
  }
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
  }
  </script>
   '''
# The main page layout and title bar
main_page_content = '''
<body style="text-align:center">
   <h1 style="color:white">MOVIE TRAILERS</h1>
   <div class="container">
       <div class="movie v1" onclick ="onc('RaO7Fyc1RMQ')">
               <img vspace="30" src="https://bit.ly/2IV9sDd"
                   style="width:60%"height="300" hspace="30";>
                       <h2 style="color:white;">Jakkanna</h2></div>
       <div class="movie v2" onclick="onc('16OL_60bnKc')">
           <img vspace="30" src="https://bit.ly/2IWTbOa"
               style="width:60%"height="300" hspace="30">
                   <h2 style="color:white;">Paddanandi premalomari</h2></div>
       <div class="movie v3" onclick="onc('2e-eXJ6HgkQ')">
           <img vspace="30" src="https://bit.ly/2wYtAzG"
               style="width:60%" height="300" hspace="30">
                   <h2 style="color:white;">Titanic</h2></div>
       <div class="movie v4" onclick ="onc('KEWUDWYDdYs')">
           <img vspace="30" src="https://bit.ly/2s02eTY"
                 style="width:60%"height="300"  hspace="30">
                       <h2 style="color:white;">Shaolinsoccer</h2></div>
      <div class="movie v5" onclick="onc('xz3j8gKRUTg')">
          <img vspace="30" src="https://bit.ly/2kd4h3K"
              style="width:60%"height="300"  hspace="30">
                      <h2 style="color:white;">Tintin</h2></div>
      <div class="movie v6" onclick="onc('_I0xx8Oj3Ww')">
              <img vspace="30" src="https://bit.ly/2GyUwFO"
                  style="width:60%"height="300"  hspace="30">
                      <h2 style="color:white;">Ghajini</h2></div>
</body>
</html>
'''
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center"
data-trailer-youtube-id="{trailer_youtube_id}"
data-toggle="modal" data-target="#trailer">
<img src="{poster_image_url}"width="220" height="342">
<h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):

    movie_file = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        movie_file += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
            )
    return movie_file


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_movie_file = main_page_content.format(
        movie_tile=create_movie_tiles_content(movies))
    # Output the file
    output_file.write(main_page_head + rendered_movie_file)
    output_file.close()
    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
