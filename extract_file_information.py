from accounting.models import TransactionCSV

# Get the model's fields using _meta
model_fields = TransactionCSV._meta.get_fields()

# Print the names of the attributes
for field in model_fields:
    print(field.name)
