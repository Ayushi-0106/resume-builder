#!/usr/bin/env python3
"""
Test script for AI Resume Builder Backend
Run this to verify the backend is working correctly
"""

import requests
import json
import time
import sys

def test_backend():
    base_url = "http://localhost:5000"
    
    print("🧪 Testing AI Resume Builder Backend...")
    print("=" * 50)
    
    # Test 1: Check if server is running
    print("1. Testing server connection...")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running")
        else:
            print(f"❌ Server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on port 5000")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    # Test 2: Test user registration
    print("\n2. Testing user registration...")
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    try:
        response = requests.post(f"{base_url}/api/auth/signup", json=test_user)
        if response.status_code == 201:
            print("✅ User registration successful")
            user_data = response.json()
            token = user_data.get('access_token')
        elif response.status_code == 409:
            print("⚠️  User already exists (this is okay)")
            # Try to login instead
            login_data = {
                "email": test_user["email"],
                "password": test_user["password"]
            }
            response = requests.post(f"{base_url}/api/auth/login", json=login_data)
            if response.status_code == 200:
                print("✅ User login successful")
                user_data = response.json()
                token = user_data.get('access_token')
            else:
                print("❌ User login failed")
                return False
        else:
            print(f"❌ Registration failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error during registration: {e}")
        return False
    
    # Test 3: Test resume creation
    print("\n3. Testing resume creation...")
    if not token:
        print("❌ No authentication token available")
        return False
    
    test_resume = {
        "title": "Test Resume",
        "personal_info": {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "+1234567890",
            "location": "Test City, TC"
        },
        "summary": "This is a test resume for testing purposes.",
        "experience": [
            {
                "title": "Software Engineer",
                "company": "Test Company",
                "startDate": "2020-01",
                "endDate": "2023-12",
                "description": "Developed software applications"
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Science",
                "institution": "Test University",
                "graduationYear": "2019"
            }
        ],
        "skills": ["Python", "JavaScript", "React"],
        "projects": [
            {
                "name": "Test Project",
                "technologies": "Python, Flask",
                "description": "A test project for demonstration"
            }
        ],
        "template": "minimal"
    }
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(f"{base_url}/api/resume", json=test_resume, headers=headers)
        if response.status_code == 201:
            print("✅ Resume creation successful")
            resume_data = response.json()
            resume_id = resume_data.get('resume_id')
        else:
            print(f"❌ Resume creation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error during resume creation: {e}")
        return False
    
    # Test 4: Test AI suggestions (if API key is available)
    print("\n4. Testing AI suggestions...")
    try:
        ai_data = {
            "type": "summary",
            "content": "This is a test summary",
            "context": "Software Engineer"
        }
        response = requests.post(f"{base_url}/api/ai/suggest", json=ai_data, headers=headers)
        if response.status_code == 200:
            print("✅ AI suggestions working")
        else:
            print("⚠️  AI suggestions not available (OpenAI API key may be missing)")
    except Exception as e:
        print(f"⚠️  AI suggestions error: {e}")
    
    # Test 5: Test PDF generation
    print("\n5. Testing PDF generation...")
    if resume_id:
        try:
            response = requests.get(f"{base_url}/api/resume/{resume_id}/pdf", headers=headers)
            if response.status_code == 200:
                print("✅ PDF generation successful")
            else:
                print(f"❌ PDF generation failed: {response.status_code}")
                print(f"Response: {response.text}")
        except Exception as e:
            print(f"❌ Error during PDF generation: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Backend testing completed!")
    print("\nTo start the full application:")
    print("1. Run START_HERE.bat and choose option 1")
    print("2. Or manually start backend with: cd backend && python run.py")
    print("3. Open frontend/index.html in your browser")
    
    return True

if __name__ == "__main__":
    print("Make sure the backend server is running before testing!")
    print("Start it with: cd backend && python run.py")
    print("\nPress Enter to continue or Ctrl+C to cancel...")
    try:
        input()
        test_backend()
    except KeyboardInterrupt:
        print("\nTest cancelled.")
        sys.exit(0)
