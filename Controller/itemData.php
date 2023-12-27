<?php

class itemData {
    
    protected $_auctionID, $_auctionStart, $_itemID, $_postingUser, $_itemTitle, $_description, $_productImage;

    public function __construct($dbRow) {
        $this->_auctionID = $dbRow['auction_id'];
        $this->_auctionStart= $dbRow['auction_Start'];
        $this->_itemID = $dbRow['item_id'];
        $this->_postingUser = $dbRow['posting_User'];
        $this->_itemTitle = $dbRow['item_Title'];
        $this->_description = $dbRow['description'];
        $this->_productImage = $dbRow['product_Image'];
    }

    public function getAuctionID() {
        return $this->_auctionID;
    }
   
    public function getAuctionStart() {
       return $this->_auctionStart;
    }
    
    public function getItem() {
       return $this->_itemID;
    }
    
    public function getPostingUser() {
       return $this->_postingUser;
    }
    
    public function getItemTitle() {
       return $this->_itemTitle;
    }

    public function getDescription() {
        return $this->_description;
    }

    public function getProductImage() {
        return $this->_productImage;
    }

            
}


