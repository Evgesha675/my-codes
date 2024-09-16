<?php
include 'db.php';

$title = $_POST['title'];
$type = $_POST['type'];
$location = $_POST['location'];
$start_time = $_POST['start_time'];
$duration = $_POST['duration'];
$comments = $_POST['comments'];

$sql = "INSERT INTO Events (title, type, location, start_time, duration, comments) VALUES (?, ?, ?, ?, ?, ?)";
$stmt = $pdo->prepare($sql);
$stmt->execute([$title, $type, $location, $start_time, $duration, $comments]);

header("Location: index.php");
?>