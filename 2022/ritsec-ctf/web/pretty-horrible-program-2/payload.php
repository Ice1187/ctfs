<?php
  class User
  {
    public $role = 'Admin';

    public function is_admin()
    {
      if ($this->role == 'Admin') {
        return true;
      } else {
        return false;
      }
    }

    /*
    public function __sleep()
    {
      return array($this->role);
    }
     */
  }


  $admin = new User;
  print serialize($admin);

?>

