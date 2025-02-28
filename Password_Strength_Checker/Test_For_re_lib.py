
import re

# Sample text for testing
sample_text = "Hello, my email is test@example.com. Call me at 123-456-7890!"

# Test for email pattern
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, sample_text)

# Test for phone number pattern
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, sample_text)

# Print results
print("Found emails:", emails)
print("Found phone numbers:", phones)


# Result
# Found emails: ['test@example.com']
# Found phone numbers: ['123-456-7890']
