<?php

require_once ('Data/Database.php');
require_once ('Data/itemData.php');

class itemDataSet {
    protected $_dbHandle, $_dbInstance;
        
    public function __construct() {
        $this->_dbInstance = Database::getInstance();
        $this->_dbHandle = $this->_dbInstance->getdbConnection();
    }

    public function fetchAllitem() {
        $sqlQuery = 'SELECT * FROM auction';
                
        $statement = $this->_dbHandle->prepare($sqlQuery); // prepare a PDO statement
        $statement->execute(); // execute the PDO statement
        
        $dataSet = [];
        while ($row = $statement->fetch()) {
            $dataSet[] = new itemData($row);
        }
        return $dataSet;
    }
}


