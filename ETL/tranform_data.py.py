# Remove duplicates
credit_card_data.drop_duplicates(inplace=True)

# Handle missing values (example: fill with median for numerical columns)
credit_card_data.fillna(credit_card_data.median(), inplace=True)

# Convert date columns to datetime
credit_card_data['transaction_date'] = pd.to_datetime(credit_card_data['transaction_date'])

# Derive 'total_spent' from quantity and price
credit_card_data['total_spent'] = credit_card_data['quantity'] * credit_card_data['price']

# Additional transformations can be added as needed
