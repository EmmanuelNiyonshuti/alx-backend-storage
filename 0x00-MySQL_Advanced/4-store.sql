-- creates a trigger that decreases the quantity of an item after it is ordered.

-- Set the delimiter to something other than semicolon
DELIMITER $$

-- Create the trigger
CREATE TRIGGER derease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

-- Reset the delimiter to something other than a semicolon
DELIMITER ;
