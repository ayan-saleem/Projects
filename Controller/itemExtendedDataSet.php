<?php

require_once 'Data/Database.php';
require_once 'itemExtendedData.php';

class itemExtendedDataSet {

protected $_dbConnection, $_dbInstance;
    
    public function __construct() {
        $this->_dbInstance = Database::getInstance();
        $this->_dbConnection = $this->_dbInstance->getDbConnection();
    }
    
    public function fetchAll() {
        $sqlQuery = 'SELECT * FROM auction ORDER BY auctionID';
               
        $statement = $this->_dbConnection->prepare($sqlQuery); // prepare a PDO statement
        $statement->execute(); // execute the PDO statement
        
        $dataSet = [];
        while ($row = $statement->fetch()) {         
            $dataSet[] = new itemExtendedData($row);
        }
        return $dataSet;
    } 
}
