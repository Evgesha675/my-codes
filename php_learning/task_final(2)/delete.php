<?php
include 'db.php';

$id = $_POST['id'];

$sql = "DELETE FROM Events WHERE id = ?";
$stmt = $pdo->prepare($sql);
$stmt->execute([$id]);

header("Location: index.php");
?>
