<!DOCTYPE html>
<html lang="en">
<head>
  <title>StarWars_FullStack_App</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container-fluid">
  <h1>Star Wars - Quick Access!</h1>
  <p>Select the Planet / Title to know more !! </p>
  <p>You can also contribute new upcoming planets !!!</p>
 
 <div class="row">
    <div class="col-sm-4" style="background-color:lavender;">  

<?php

$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "starwars";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$title_sql = "SELECT title FROM films";
$title_result = $conn->query($title_sql);

if ($title_result->num_rows > 0) {

    echo "<table><tr><th>Titles</tr>";
    // output data of each row
    while($title_row = $title_result->fetch_assoc()) {
        echo "<tr><td>".$title_row["title"]."</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}
?>

<div class="form-group">
  <br> <br> 
  <table><tr><th>Find Planets ! </tr></table> <br>
  <form action="" method="get">
  Enter Title Name : <input type="text" class="form-control" name="titlename"  size="35">
  <br> <input type="submit" class="btn btn-info" name = "findplanets" value="Find Planets">
  </form>
</div>

<?php 

if (isset($_GET['findplanets'])) {

$name = htmlentities($_GET['titlename']);
$sql = "SELECT title, planets FROM films WHERE title = '".$name."'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table><tr><th>Title </th><th> Planet </th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>".$row["title"]."</td><td>".$row["planets"]."</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}

}


?>

</div>

<div class="col-sm-4" style="background-color:lavenderblush;">   

<?php 

$planet_sql = "SELECT name FROM planets";
$planet_result = $conn->query($planet_sql);

if ($planet_result->num_rows > 0) {

    echo "<table><tr><th>Planets</tr>";
    // output data of each row
    while($planet_row = $planet_result->fetch_assoc()) {
        echo "<tr><td>".$planet_row["name"]."</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}

?>

<div class="form-group">
  <br> <br> 
  <table><tr><th>Find Titles ! </tr></table> <br>
   <form action="" method="get">
  Enter Planet Name : <input type="text" class="form-control" name="planetname"  size="35">
  <br> <input type="submit" class="btn btn-info" name="findtitles" value="Find Titles">
</form>
</div>

<?php 

if (isset($_GET['findtitles'])) {

$planetname = htmlentities($_GET['planetname']);
$sql = "SELECT films,name FROM planets WHERE name = '".$planetname."'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table><tr><th>Title </th><th> Planet </th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>".$row["films"]."</td><td>".$row["name"]."</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}

}


?>

</div>

<div class="col-sm-4" style="background-color:lavender;"> 
<div class="form-group">

  <form  action=" " method="get">
  <table><tr><th>Add New Planets</tr></table> <br>
  Planet Name : <input type="text" class="form-control" name="name"  size="35">
  Titles: <input type="text" class="form-control" name="title" size="35">
  <br> <input type="submit" name="submit" class="btn btn-info" value="submit"> </form>
  
</div>

<?php 

if (isset($_GET['submit'])) {

$name = htmlentities($_GET['name']);
$title = htmlentities($_GET['title']);

$sql = "INSERT INTO planets (name, films)
VALUES ('".$name."', '".$title."')";

if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

}


?>


</div>

</div>
</div>

</body>
</html>
