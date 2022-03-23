<?php

$res = [];
$conn = new mysqli("localhost", "ptdsn_admin", "bismillah", "ptdsn");
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM status";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while ($row = $result->fetch_assoc()) {
        array_push($res, $row);
    }
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($res);