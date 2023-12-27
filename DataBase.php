<?php
function OpenCon()
{
    $dbhost = "poseidon.salford.ac.uk";
    $dbuser = "aee318";
    $dbpass = "1bd6nS33Gt2nDNS";
    $db = "aee318";
    $conn = new mysqli($dbhost, $dbuser, $dbpass,$db) or die("Connect failed: %s\n". $conn -> error);

    return $conn;
}

function CloseCon($conn)
{
    $conn -> close();
}

