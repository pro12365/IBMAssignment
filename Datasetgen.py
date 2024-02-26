import os
from faker import Faker
import random
from datetime import datetime, timedelta
from fpdf import FPDF

fake = Faker()

# List of product names
product_names = [
    "smartphone", "laptop", "television", "refrigerator", "washing machine", 
    "microwave", "coffee maker", "blender", "toaster", "air conditioner", 
    "vacuum cleaner", "camera", "headphones", "tablet", "printer", 
    "router", "smartwatch", "fitness tracker", "gaming console", "speaker", 
    "backpack", "shoes", "sunglasses", "watch", "jacket", 
    "earphones", "guitar", "bike", "umbrella", "perfume", 
    "wallet", "suitcase", "skincare product", "cosmetics", "handbag", 
    "desk", "chair", "bed", "desk lamp", "mirror", 
    "table", "oven", "cutlery set", "towel", "pillow", 
    "blanket", "candles", "plant", "painting",
    "apple", "banana", "orange", "strawberry", "blueberry", 
    "tomato", "broccoli", "carrot", "cucumber", "lettuce", 
    "onion", "potato", "avocado", "watermelon", "pineapple", 
    "mango", "pear", "grapes", "kiwi", "peach", 
    "lemon", "lime", "melon", "corn", "peas"
]

# Function to generate negotiation data with engine intervention details
def generate_negotiation_data_with_engine(num_entries):
    negotiation_data = []

    for _ in range(num_entries):
        buyer = fake.name()
        seller = fake.company()
        product = random.choice(product_names)  # Randomly select from product names

        # Define initial stipulations and resolutions based on product category
        if product in ["smartphone", "laptop", "television"]:
            # Tech-related product
            buyer_stipulation = f"{buyer} wants specific technical features for the {product}."
            seller_stipulation = f"{seller} claims the {product} comes with standard technical specifications."
            resolution = f"{seller} offers a technical support package for the {product}."
        elif product in ["fruits", "vegetables"]:
            # Food items related product
            buyer_stipulation = f"{buyer} insists on quality and freshness for the {product}."
            seller_stipulation = f"{seller} assures quality but can't always guarantee freshness due to sourcing reasons."
            resolution = f"{seller} provides detailed sourcing information for the {product}."
        else:
            # Other products
            buyer_stipulation = f"{buyer} requires additional specifications for the {product}."
            seller_stipulation = f"{seller} can consider optional upgrades for the {product}."
            resolution = f"A coupon code will be provided for future purchases of {product}."

        # Generate variations in stipulation and resolution
        for _ in range(random.randint(1, 5)):  # Generating 1 to 5 variations
            if product in ["smartphone", "laptop", "television"]:
                buyer_stipulation += f" {buyer} also seeks warranty extension for the {product}."
                seller_stipulation += f" However, {seller} can provide limited warranty extensions for the {product}."
                resolution += f" {seller} agrees to provide a refund for technical issues with the {product}."
            elif product in ["fruits", "vegetables"]:
                buyer_stipulation += f" Additionally, {buyer} wants specific certifications for the {product}."
                seller_stipulation += f" {seller} assures quality but lacks specific certifications for the {product}."
                resolution += f" {seller} agrees to provide detailed certifications for the {product}."
            else:
                buyer_stipulation += f" Also, {buyer} requires additional specifications for the {product}."
                seller_stipulation += f" However, {seller} can consider optional upgrades for the {product}."
                resolution += f" A coupon code will be provided for future purchases of {product}."

        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        negotiation_date = start_date + (end_date - start_date) * random.random()

        engine_intervention = random.choice([
            "Conflict Identification",
            "Notification and Mediated Discussion",
            "Offering Potential Solutions",
            "Logging and Documentation",
            "Agreement and Implementation"
        ])

        negotiation_data.append({
            "Buyer": buyer,
            "Seller": seller,
            "Product": product,
            "Stipulation_Buyer": buyer_stipulation,
            "Stipulation_Seller": seller_stipulation,
            "Resolution": resolution,
            "Negotiation_Date": negotiation_date.strftime("%Y-%m-%d"),
            "Engine_Intervention": engine_intervention
        })

    return negotiation_data

# Generate negotiation data with engine intervention details
negotiation_data_with_engine = generate_negotiation_data_with_engine(200)

# Create a PDF file
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add negotiation data to the PDF
for data in negotiation_data_with_engine:
    pdf.cell(200, 10, txt=f"Buyer: {data['Buyer']}", ln=True)
    pdf.cell(200, 10, txt=f"Seller: {data['Seller']}", ln=True)
    pdf.cell(200, 10, txt=f"Product: {data['Product']}", ln=True)
    pdf.cell(200, 10, txt=f"Stipulation (Buyer): {data['Stipulation_Buyer']}", ln=True)
    pdf.cell(200, 10, txt=f"Stipulation (Seller): {data['Stipulation_Seller']}", ln=True)
    pdf.cell(200, 10, txt=f"Resolution: {data['Resolution']}", ln=True)
    pdf.cell(200, 10, txt=f"Negotiation Date: {data['Negotiation_Date']}", ln=True)
    pdf.cell(200, 10, txt=f"Engine Intervention: {data['Engine_Intervention']}", ln=True)
    pdf.cell(200, 10, ln=True)  # Add a blank line between entries

# Save the PDF file
pdf_file_path = "Negotiationdata.pdf"
pdf.output(pdf_file_path)
print(f"Negotiation data saved as '{pdf_file_path}'")
