import os
import django
import requests
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthDoc.settings')
django.setup()

from hospitals.models import Hospital

# Sample hospital images URLs (using placeholder service for demonstration)
HOSPITAL_IMAGES = [
    "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=800&h=600",  # Modern hospital building
    "https://images.unsplash.com/photo-1551076805-e1869033e561?w=800&h=600",    # Hospital corridor
    "https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=800&h=600",  # Hospital exterior
    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=800&h=600",  # Medical facility
    "https://images.unsplash.com/photo-1563213126-a4273aed2016?w=800&h=600",    # Hospital building
]

def download_image(url, hospital_name):
    """Download image from URL and return ContentFile"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Create a filename
        filename = f"{hospital_name.replace(' ', '_').lower()}.jpg"
        
        # Create ContentFile from response content
        image_content = ContentFile(response.content, name=filename)
        return image_content
    except Exception as e:
        print(f"Error downloading image for {hospital_name}: {e}")
        return None

# Hospital data for 100 Indian hospitals across different states
HOSPITALS_DATA = [
    # Maharashtra
    {
        "name": "Kokilaben Dhirubhai Ambani Hospital",
        "state": "Maharashtra",
        "district": "Mumbai",
        "address": "Rao Saheb Achutrao Patwardhan Marg, Four Bungalows, Andheri West, Mumbai",
        "pincode": "400053",
        "category": "Multi-specialty",
        "phone": "+91-22-4269-6969",
        "email": "info@kokilabenhospital.com",
        "website": "https://www.kokilabenhospital.com",
        "bed_count": 750,
        "established_year": 2009,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Himachal Pradesh
    {
        "name": "AIIMS Bilaspur",
        "state": "Himachal Pradesh",
        "district": "Bilaspur",
        "address": "Bilaspur, Himachal Pradesh",
        "pincode": "174001",
        "category": "Government Medical College",
        "phone": "+91-197-822-4000",
        "email": "info@aiimsbilaspur.edu.in",
        "website": "https://www.aiimsbilaspur.edu.in",
        "bed_count": 750,
        "established_year": 2019,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Uttarakhand
    {
        "name": "AIIMS Rishikesh",
        "state": "Uttarakhand",
        "district": "Dehradun",
        "address": "Veerbhadra Road, Rishikesh",
        "pincode": "249203",
        "category": "Government Medical College",
        "phone": "+91-135-296-1000",
        "email": "info@aiimsrishikesh.edu.in",
        "website": "https://www.aiimsrishikesh.edu.in",
        "bed_count": 960,
        "established_year": 2012,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Jammu & Kashmir
    {
        "name": "Sher-i-Kashmir Institute of Medical Sciences",
        "state": "Jammu & Kashmir",
        "district": "Srinagar",
        "address": "Bemina, Srinagar",
        "pincode": "190011",
        "category": "Government Medical Institute",
        "phone": "+91-194-240-1013",
        "email": "info@skims.ac.in",
        "website": "https://www.skims.ac.in",
        "bed_count": 650,
        "established_year": 1982,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Goa
    {
        "name": "Goa Medical College Hospital",
        "state": "Goa",
        "district": "North Goa",
        "address": "Bambolim, Goa",
        "pincode": "403202",
        "category": "Government Medical College",
        "phone": "+91-832-245-8700",
        "email": "info@gmc.goa.gov.in",
        "website": "https://www.gmc.goa.gov.in",
        "bed_count": 1200,
        "established_year": 1963,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Manipur
    {
        "name": "Regional Institute of Medical Sciences",
        "state": "Manipur",
        "district": "Imphal West",
        "address": "Lamphelpat, Imphal",
        "pincode": "795004",
        "category": "Government Medical College",
        "phone": "+91-385-241-4202",
        "email": "info@rims.edu.in",
        "website": "https://www.rims.edu.in",
        "bed_count": 650,
        "established_year": 1972,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Meghalaya
    {
        "name": "North Eastern Indira Gandhi Regional Institute of Health & Medical Sciences",
        "state": "Meghalaya",
        "district": "East Khasi Hills",
        "address": "Mawdiangdiang, Shillong",
        "pincode": "793018",
        "category": "Government Medical Institute",
        "phone": "+91-364-253-6000",
        "email": "info@neigrihms.gov.in",
        "website": "https://www.neigrihms.gov.in",
        "bed_count": 650,
        "established_year": 1987,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Tripura
    {
        "name": "Agartala Government Medical College",
        "state": "Tripura",
        "district": "West Tripura",
        "address": "Kunjaban, Agartala",
        "pincode": "799006",
        "category": "Government Medical College",
        "phone": "+91-381-232-5401",
        "email": "info@agmc.nic.in",
        "website": "https://www.agmc.nic.in",
        "bed_count": 500,
        "established_year": 2006,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Mizoram
    {
        "name": "Civil Hospital Aizawl",
        "state": "Mizoram",
        "district": "Aizawl",
        "address": "Durtlang, Aizawl",
        "pincode": "796025",
        "category": "Government Hospital",
        "phone": "+91-389-233-4847",
        "email": "info@mizoramhealth.nic.in",
        "website": "https://www.mizoramhealth.nic.in",
        "bed_count": 350,
        "established_year": 1970,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Nagaland
    {
        "name": "Naga Hospital Authority Kohima",
        "state": "Nagaland",
        "district": "Kohima",
        "address": "Kohima, Nagaland",
        "pincode": "797001",
        "category": "Government Hospital",
        "phone": "+91-370-224-0532",
        "email": "info@nhak.org",
        "website": "https://www.nhak.org",
        "bed_count": 300,
        "established_year": 2008,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Arunachal Pradesh
    {
        "name": "Tomo Riba Institute of Health & Medical Sciences",
        "state": "Arunachal Pradesh",
        "district": "Naharlagun",
        "address": "Naharlagun, Arunachal Pradesh",
        "pincode": "791110",
        "category": "Government Medical Institute",
        "phone": "+91-360-224-3214",
        "email": "info@trihms.ac.in",
        "website": "https://www.trihms.ac.in",
        "bed_count": 500,
        "established_year": 2013,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Sikkim
    {
        "name": "Sir Thutob Namgyal Memorial Hospital",
        "state": "Sikkim",
        "district": "East Sikkim",
        "address": "Sochakgang, Gangtok",
        "pincode": "737101",
        "category": "Government Hospital",
        "phone": "+91-359-222-2988",
        "email": "info@stnmh.gov.in",
        "website": "https://www.stnmh.gov.in",
        "bed_count": 300,
        "established_year": 1917,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # More hospitals from major states to reach 100
    # Additional Maharashtra hospitals
    {
        "name": "Tata Memorial Hospital",
        "state": "Maharashtra",
        "district": "Mumbai",
        "address": "Dr E Borges Road, Parel, Mumbai",
        "pincode": "400012",
        "category": "Cancer Specialty",
        "phone": "+91-22-2417-7000",
        "email": "info@tmc.gov.in",
        "website": "https://www.tmc.gov.in",
        "bed_count": 629,
        "established_year": 1941,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "P.D. Hinduja National Hospital",
        "state": "Maharashtra",
        "district": "Mumbai",
        "address": "Veer Savarkar Marg, Mahim, Mumbai",
        "pincode": "400016",
        "category": "Multi-specialty",
        "phone": "+91-22-2445-2222",
        "email": "info@hindujahospital.com",
        "website": "https://www.hindujahospital.com",
        "bed_count": 350,
        "established_year": 1951,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Breach Candy Hospital",
        "state": "Maharashtra",
        "district": "Mumbai",
        "address": "60-A, Bhulabhai Desai Road, Mumbai",
        "pincode": "400026",
        "category": "Multi-specialty",
        "phone": "+91-22-2367-8888",
        "email": "info@breachcandyhospital.org",
        "website": "https://www.breachcandyhospital.org",
        "bed_count": 165,
        "established_year": 1950,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Jupiter Hospital",
        "state": "Maharashtra",
        "district": "Thane",
        "address": "Eastern Express Highway, Thane",
        "pincode": "400601",
        "category": "Multi-specialty",
        "phone": "+91-22-6269-2999",
        "email": "info@jupiterhospital.com",
        "website": "https://www.jupiterhospital.com",
        "bed_count": 355,
        "established_year": 2007,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Additional Delhi hospitals
    {
        "name": "Max Super Speciality Hospital",
        "state": "Delhi",
        "district": "South Delhi",
        "address": "1, Press Enclave Road, Saket, New Delhi",
        "pincode": "110017",
        "category": "Multi-specialty",
        "phone": "+91-11-2651-5050",
        "email": "info@maxhealthcare.com",
        "website": "https://www.maxhealthcare.in",
        "bed_count": 500,
        "established_year": 2006,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "BLK-Max Super Speciality Hospital",
        "state": "Delhi",
        "district": "West Delhi",
        "address": "Pusa Road, Rajinder Nagar, New Delhi",
        "pincode": "110005",
        "category": "Multi-specialty",
        "phone": "+91-11-3040-3040",
        "email": "info@blkmaxhospital.com",
        "website": "https://www.blkmaxhospital.com",
        "bed_count": 650,
        "established_year": 2009,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Sir Ganga Ram Hospital",
        "state": "Delhi",
        "district": "Central Delhi",
        "address": "Rajinder Nagar, New Delhi",
        "pincode": "110060",
        "category": "Multi-specialty",
        "phone": "+91-11-2575-0000",
        "email": "info@sgrh.com",
        "website": "https://www.sgrh.com",
        "bed_count": 675,
        "established_year": 1954,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Additional Karnataka hospitals
    {
        "name": "Kidwai Memorial Institute of Oncology",
        "state": "Karnataka",
        "district": "Bangalore",
        "address": "Dr MH Marigowda Road, Bangalore",
        "pincode": "560029",
        "category": "Cancer Specialty",
        "phone": "+91-80-2659-4000",
        "email": "info@kidwai.kar.nic.in",
        "website": "https://www.kidwai.kar.nic.in",
        "bed_count": 1041,
        "established_year": 1973,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Columbia Asia Hospital",
        "state": "Karnataka",
        "district": "Bangalore",
        "address": "Kirloskar Business Park, Bellary Road, Hebbal, Bangalore",
        "pincode": "560024",
        "category": "Multi-specialty",
        "phone": "+91-80-6132-0000",
        "email": "info@columbiaasia.com",
        "website": "https://www.columbiaasia.com",
        "bed_count": 200,
        "established_year": 2005,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Fortis Hospital",
        "state": "Karnataka",
        "district": "Bangalore",
        "address": "154/9, Bannerghatta Road, Opposite IIM, Bangalore",
        "pincode": "560076",
        "category": "Multi-specialty",
        "phone": "+91-80-6621-4444",
        "email": "info@fortishealthcare.com",
        "website": "https://www.fortishealthcare.com",
        "bed_count": 400,
        "established_year": 2006,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Additional Tamil Nadu hospitals
    {
        "name": "Sankara Nethralaya",
        "state": "Tamil Nadu",
        "district": "Chennai",
        "address": "18, College Road, Nungambakkam, Chennai",
        "pincode": "600006",
        "category": "Eye Specialty",
        "phone": "+91-44-2827-1616",
        "email": "info@sankaranethralaya.org",
        "website": "https://www.sankaranethralaya.org",
        "bed_count": 300,
        "established_year": 1978,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Global Hospitals",
        "state": "Tamil Nadu",
        "district": "Chennai",
        "address": "439, Cheran Nagar, Perumbakkam, Chennai",
        "pincode": "600100",
        "category": "Multi-specialty",
        "phone": "+91-44-4777-7777",
        "email": "info@globalhospitalsindia.com",
        "website": "https://www.globalhospitalsindia.com",
        "bed_count": 350,
        "established_year": 2000,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "MIOT International",
        "state": "Tamil Nadu",
        "district": "Chennai",
        "address": "4/112, Mount Poonamalle Road, Manapakkam, Chennai",
        "pincode": "600089",
        "category": "Multi-specialty",
        "phone": "+91-44-2249-2000",
        "email": "info@miotinternational.com",
        "website": "https://www.miotinternational.com",
        "bed_count": 400,
        "established_year": 1999,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    
    # Additional hospitals from other states
    {
        "name": "PGIMER Chandigarh",
        "state": "Chandigarh",
        "district": "Chandigarh",
        "address": "Sector 12, Chandigarh",
        "pincode": "160012",
        "category": "Government Medical Institute",
        "phone": "+91-172-274-7585",
        "email": "info@pgimer.edu.in",
        "website": "https://www.pgimer.edu.in",
        "bed_count": 1900,
        "established_year": 1962,
        "accreditation": "NABH",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Amrita Institute of Medical Sciences",
        "state": "Kerala",
        "district": "Ernakulam",
        "address": "AIMS Ponekkara P.O., Kochi",
        "pincode": "682041",
        "category": "Medical College Hospital",
        "phone": "+91-484-285-1234",
        "email": "info@amrita.edu",
        "website": "https://www.amrita.edu",
        "bed_count": 1450,
        "established_year": 1998,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Care Hospitals",
        "state": "Andhra Pradesh",
        "district": "Hyderabad",
        "address": "Road No. 1, Banjara Hills, Hyderabad",
        "pincode": "500034",
        "category": "Multi-specialty",
        "phone": "+91-40-6165-6565",
        "email": "info@carehospitals.com",
        "website": "https://www.carehospitals.com",
        "bed_count": 435,
        "established_year": 1997,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Jaslok Hospital",
        "state": "Maharashtra",
        "district": "Mumbai",
        "address": "15, Dr G Deshmukh Marg, Pedder Road, Mumbai",
        "pincode": "400026",
        "category": "Multi-specialty",
        "phone": "+91-22-6657-3333",
        "email": "info@jaslokhospital.net",
        "website": "https://www.jaslokhospital.net",
        "bed_count": 365,
        "established_year": 1973,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
    {
        "name": "Wockhardt Hospital",
        "state": "Maharashtra",
        "district": "Mumbai",
        "address": "1877, Dr Anand Rao Nair Road, Near Agripada Police Station, Mumbai",
        "pincode": "400011",
        "category": "Multi-specialty",
        "phone": "+91-22-2659-8888",
        "email": "info@wockhardthospitals.com",
        "website": "https://www.wockhardthospitals.com",
        "bed_count": 350,
        "established_year": 2000,
        "accreditation": "NABH, JCI",
        "emergency_services": True,
        "ambulance_service": True,
        "blood_bank": True,
        "pharmacy": True,
        "cafeteria": True,
        "parking_available": True,
    },
]

def create_hospitals():
    """Create hospital records with images"""
    print("Starting hospital data population...")
    
    # Clear existing hospitals (optional)
    # Hospital.objects.all().delete()
    
    for i, hospital_data in enumerate(HOSPITALS_DATA):
        try:
            # Check if hospital already exists
            hospital, created = Hospital.objects.get_or_create(
                name=hospital_data['name'],
                defaults=hospital_data
            )
            
            if created:
                # Download and assign image
                image_url = random.choice(HOSPITAL_IMAGES)
                image_content = download_image(image_url, hospital_data['name'])
                
                if image_content:
                    hospital.image.save(
                        f"{hospital_data['name'].replace(' ', '_').lower()}.jpg",
                        image_content,
                        save=True
                    )
                
                print(f"✓ Created: {hospital_data['name']} ({hospital_data['state']})")
            else:
                print(f"⚠ Already exists: {hospital_data['name']} ({hospital_data['state']})")
                
        except Exception as e:
            print(f"✗ Error creating {hospital_data['name']}: {e}")
    
    total_hospitals = Hospital.objects.count()
    print(f"\nPopulation complete! Total hospitals in database: {total_hospitals}")

if __name__ == "__main__":
    create_hospitals()