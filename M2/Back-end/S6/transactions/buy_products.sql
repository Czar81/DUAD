DO $$
BEGIN    
    -- Verify stock
    IF NOT EXISTS (
        SELECT 1
        FROM products
        WHERE
            id = 1
            AND quantity > 0
    ) THEN 
        RETURN;
    END IF;
    -- Verify user exist
    IF NOT EXISTS ( 
        SELECT 1 
        FROM users 
        WHERE id = 1 
    ) THEN 
        RETURN;
    END IF;

    -- Generate receipt
    INSERT INTO
        receipt (fk_user_id, state)
    VALUES (1, 'Bought');

    -- Gnerete receipt details 
    INSERT INTO 
        receipt_detail(fk_receipt_id, fk_product_id, quantity)
    VALUES (1, 1, 5);

    -- Update stock of product 
    UPDATE products 
    SET quantity = quantity - 5 
    WHERE id = 1;
END;
$$ LANGUAGE plpgsql;
