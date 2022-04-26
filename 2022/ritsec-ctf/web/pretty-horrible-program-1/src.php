 <?php
  if (isset($_GET['bingus'])) {
    $input = $_GET['bingus'];
    $to_replace = 'bingus';
    $clean_string = preg_replace("/$to_replace/", '', $input);
    echo "<p>Your string is: $clean_string</p>";
    if ($clean_string == $to_replace) {
      echo "<h2 class=\"answer\">Bingus <span style=\"color: green;\">IS</span> your beloved</h2>";
      output_flag();
    } else {
      echo "<h2 class=\"answer\">Bingus <span style=\"color: red;\">IS NOT</span> your beloved</h2>";
    }
  }
?>
