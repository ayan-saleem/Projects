<?php

//require_once('Models/StudentsExtendedDataSet.php');

require_once('itemDataSet.php');


$view = new stdClass();
$view->pageTitle = 'Item Information System';


$itemDataSet = new itemDataSet();
$view->itemDataSet = $itemDataSet->fetchAllitem();

//$studentsExtendedDataSet = new StudentsExtendedDataSet();
//$view->studentsExtendedDataSet = $studentsExtendedDataSet->fetchAll();


require_once('../../View/auction.phtml');
//require_once('Views/studentExtISv1.phtml');
