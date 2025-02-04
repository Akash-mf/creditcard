import sqlalchemy

# Database connection
engine = sqlalchemy.create_engine('postgresql://username:password@localhost:5432/credit_card_db')

# Save the transformed data into the database
credit_card_data.to_sql('transactions', con=engine, if_exists='replace', index=False)
