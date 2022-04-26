<?php
$input1 = [1];
$input2 = [2];

print $input1 . ": " . hash("sha256", $input1) . "\n";
print $input2 . ": " . hash("sha256", $input2) . "\n";

if ($input1 == $input2) {
  print "Compare same\n";
} else if (hash("sha256", $input1) === hash("sha256", $input2)) {
  print "FLAG!!!\n";
} else {
  print "Nope\n";
}
?>
