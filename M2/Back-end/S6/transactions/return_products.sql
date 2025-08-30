DO $$
BEGIN    
    -- Verify receipt
    IF NOT EXISTS ( 
        SELECT 1 
        FROM receipt 
        WHERE id = 1 
    ) THEN 
        RETURN;
    END IF;

    -- Update stock of product 
    UPDATE products
    SET
        quantity = quantity + (
            SELECT quantity
            FROM receipt_detail
            WHERE
                fk_receipt_id = 1
        )
    WHERE
        id = (
            SELECT fk_product_id
            FROM receipt_detail
            WHERE
                fk_receipt_id = 1
        );

    UPDATE receipt SET state = 'Returned' WHERE id = 1;
END;
$$ LANGUAGE plpgsql;
