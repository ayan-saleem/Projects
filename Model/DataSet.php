<?php
require_once ('model/Database.php');

class DataSet {
    protected $_dbHandle, $_dbInstance;

    public function __construct() {
        $this->_dbInstance = Database::getInstance();
        $this->_dbHandle = $this->_dbInstance->getdbConnection();
    }

    public function checkUserDetails($email, $password) { //Used when logging in a user
        $sqlQuery = "SELECT COUNT(userId) FROM user WHERE email = '" . $email . "' AND password = '" . $password . "'";
        $statement = $this->_dbHandle->prepare($sqlQuery);
        $statement->execute();
        while ($row = $statement->fetch()) {
            return $row[0];
        }
    }

    public function beginSession($email) { // Starts the session for the user
        $userId = $this->getUserIdByEmail($email);
        session_start();
        $_SESSION["userId"] = $userId;
        header('location: ../View/auction.phtml');
    }

    public function getUserIdByEmail($userEmail) { //Gets user info from database using the email.
        $sqlQuery = "SELECT * FROM user WHERE email = '" . $userEmail . "'";
        $statement = $this->_dbHandle->prepare($sqlQuery);
        $statement->execute();
        while ($row = $statement->fetch()) {
            return $row[0];
        }
    }


}
