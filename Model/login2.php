<?php
require_once ('DataSet.php');
class login {

    protected $_email, $_password;

    public function __construct() {
    }

    public function getValues($email, $password) {
        $this->_email = $email;
        $this->_password = $password;
    }

    public function getEmail() {
        return $this->_email;
    }

    public function getPassword() {
        return $this->_password;
    }

    public function getEncryptedPassword() {
        $baseEncodedPassword = base64_encode($this->getPassword());
        return $baseEncodedPassword;
    }

    public function startUserSession() {
        if (empty($_SESSION)) {
            $DataSet = new DataSet();
            if ($DataSet->checkUserDetails($this->getEmail(),$this->getEncryptedPassword()) == 1) {
                $DataSet->beginSession($this->getEmail());
            } else {

                echo "<script type='text/javascript'>alert('Wrong log in details!  Please try again.');</script>";;
            }
        }
    }

}
