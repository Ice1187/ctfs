1. Send some strings and decode base64 cookie. Seems need to do some (de)serializations.
```
O:4:"User":2:{s:4:"name";s:3:"abc";s:11:"�User�token";s:32:"a7215f03903aa3112062c6d291819561";}

O:4:"User":2:{s:4:"name";s:5:"admin";s:11:"�User�token";s:32:"d694327d490d97d13f90196871c21d2e";}

// O:strlen(object name):object name:object size:{s:strlen(property name):property name:property definition;(repeated per property)}
```

2. 
