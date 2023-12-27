<?php
//fetch.php
$connect = mysqli_connect("poseidon.salford.ac.uk", "aee318", "1bd6nS33Gt2nDNS", "aee318_auction");
$output = '';
if(isset($_POST["query"]))
{
    $search = mysqli_real_escape_string($connect, $_POST["query"]);
    $query = "
  SELECT * FROM auction 
  WHERE itemID LIKE '%".$search."%'
  OR itemTitle LIKE '%".$search."%' 
 ";
}
else
{
    $query = "
  SELECT * FROM auction ORDER BY itemID
 ";
}
$result = mysqli_query($connect, $query);
if(mysqli_num_rows($result) > 0)
{
    $output .= '
  <div class="table-responsive">
   <table class="table table bordered">
    <tr>
     <th>Item ID</th>
     <th>Item Name</th>
     <th>description Name</th>
     <th>Posting User Name</th>

     
     
    </tr>
 ';
    while($row = mysqli_fetch_array($result))
    {
        $output .= '
   <tr>
    <td>'.$row["itemID"].'</td>
    <td>'.$row["itemTitle"].'</td>
        <td>'.$row["description"].'</td>
            <td>'.$row["postingUser"].'</td>
          
    


   </tr>
  ';
    }
    echo $output;
}
else
{
    echo 'Data Not Found';
}

?>