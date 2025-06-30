import requests
import pandas as pd
from openpyxl import load_workbook

# Set the API URL and your API key
url = "https://api.joshuaproject.net/v1/people_groups_global.json?api_key=f4e3ed6c35ee"

# Make the request
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Load the existing Excel file
    excel_path = "/Users/jgotay/Desktop/Desktop - Joselyn's MacBook Pro/dashboard_data.xlsx"
    
    # Load the existing workbook
    with pd.ExcelWriter(excel_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="JoshuaData", index=False)
    
    print("✅ Done! Data written to 'JoshuaData' sheet in dashboard_data.xlsx")

else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)




