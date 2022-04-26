grep -i hint dumped.txt | awk '{printf substr($4, 2, 2);printf $6}'
