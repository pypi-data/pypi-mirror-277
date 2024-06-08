from pydantic import Field
from instructor import OpenAISchema
import os
import requests
import json

class GetOktaUser(OpenAISchema):
    """
    Use this tool to get more detailed user profile information. Call it when you need supplemental info like where someone is located, title, etc.

    Relevance:
    - This tool relies on data from Okta, which is an internal PGA tool
    - It only has information about users who are PGA employees or PGA section employees

    Returns:
        JSON string with user profile information. Specifically: city, costCenter, department, displayName, email, firstName, lastName, manager, mobilePhone, organization, profileUrl, secondEmail, state, streetAddress, title, userType, zipCode, Location
    """
    email: str = Field(description="The email of the user to fetch the profile for")

    def run(self):
        api_token = os.getenv('OKTA_API_KEY')
        okta_domain = os.getenv('OKTA_DOMAIN')  # e.g. https://your-domain.okta.com
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'SSWS {api_token}'
        }
        
        try:
            search_url = f"{okta_domain}/api/v1/users"
            params = {'filter': f'profile.email eq "{self.email}"'}
            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()
            user = response.json()
            if not user:
                return(f"No information found at {okta_domain} for the user with email {self.email}")
            
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
        keys_to_keep = ['city', 'costCenter', 'department', 'displayName', 'email', 'firstName', 'lastName', 'manager', 'mobilePhone', 'organization', 'profileUrl', 'secondEmail', 'state', 'streetAddress', 'title', 'userType', 'zipCode', 'Location']
        profile_dict = user[0]['profile']
        filtered_profile = {key: profile_dict[key] for key in keys_to_keep if key in profile_dict}
        return json.dumps(filtered_profile) # tools should always return a string

if __name__ == "__main__":
    get_okta_user = GetOktaUser(email="user@example.com")
    user_profile = get_okta_user.run()
    print(user_profile)
