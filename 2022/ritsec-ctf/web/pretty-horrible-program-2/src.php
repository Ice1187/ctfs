<!--- set cookie -->
<?php
if (!isset($_COOKIE['user'])) {
  $default_user = new User;
  $_COOKIE['user'] = serialize($default_user);
  setcookie(
    'user',
    serialize($default_user),
  );
}

if (isset($_POST['user'])) {
  setcookie(
    'user',
    $_POST['user'],
  );
}
?>

<!--- User class -->
<?php
  class User
  {
    public $role = 'User';

    public function is_admin()
    {
      if ($this->role == 'Admin') {
        return true;
      } else {
        return false;
      }
    }

    public function __sleep()
    {
      return array($this->role);
    }
  }
?>

<!--- Get flag -->
<?php
  if (isset($_COOKIE['user'])) {
    try {
      $user = unserialize($_COOKIE['user']);
      if ($user->is_admin()) {
        echo '<h3 class="success">Welcome Admin</h3>';
        output_flag();
      } else {
        echo '<h3 class="error">Not Admin</h3>';
      }
    } catch (Error $e) {
      echo '<h2 class="error">Uh oh, ur input was <code>cringe</code></h2>';
    }
  }
