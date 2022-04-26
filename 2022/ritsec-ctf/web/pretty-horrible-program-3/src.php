<?php
  if (isset($_GET['input1']) and isset($_GET['input2'])) {
    if ($_GET['input1'] == $_GET['input2']) {
      print '<h3 class="error">Nice try, but it won\'t be that easy ;)</h3>';
    } else if (hash("sha256", $_GET['input1']) === hash("sha256", $_GET['input2'])) {
      output_flag();
    } else {
      print '<h3 class="error">Your inputs don\'t match</h3>';
    }
  }
?>
