import json
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class FileStorage:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.users_file = os.path.join(data_dir, "users.json")
        self.resumes_file = os.path.join(data_dir, "resumes.json")
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize files if they don't exist
        self._init_files()
    
    def _init_files(self):
        """Initialize JSON files if they don't exist"""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump([], f)
        
        if not os.path.exists(self.resumes_file):
            with open(self.resumes_file, 'w') as f:
                json.dump([], f)
    
    def _load_data(self, file_path):
        """Load data from JSON file"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_data(self, file_path, data):
        """Save data to JSON file"""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    # User management methods
    def create_user(self, email, password, name):
        """Create a new user"""
        users = self._load_data(self.users_file)
        
        # Check if user already exists
        if any(user['email'] == email for user in users):
            return None
        
        user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "password": generate_password_hash(password),
            "name": name,
            "created_at": datetime.utcnow().isoformat()
        }
        
        users.append(user)
        self._save_data(self.users_file, users)
        return user
    
    def find_user_by_email(self, email):
        """Find user by email"""
        users = self._load_data(self.users_file)
        return next((user for user in users if user['email'] == email), None)
    
    def find_user_by_id(self, user_id):
        """Find user by ID"""
        users = self._load_data(self.users_file)
        return next((user for user in users if user['id'] == user_id), None)
    
    def verify_password(self, user, password):
        """Verify user password"""
        return check_password_hash(user['password'], password)
    
    # Resume management methods
    def create_resume(self, user_id, resume_data):
        """Create a new resume"""
        resumes = self._load_data(self.resumes_file)
        
        resume = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "title": resume_data.get('title', 'Untitled Resume'),
            "personal_info": resume_data.get('personal_info', {}),
            "summary": resume_data.get('summary', ''),
            "experience": resume_data.get('experience', []),
            "education": resume_data.get('education', []),
            "skills": resume_data.get('skills', []),
            "projects": resume_data.get('projects', []),
            "template": resume_data.get('template', 'minimal'),
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        resumes.append(resume)
        self._save_data(self.resumes_file, resumes)
        return resume
    
    def get_user_resumes(self, user_id):
        """Get all resumes for a user"""
        resumes = self._load_data(self.resumes_file)
        return [resume for resume in resumes if resume['user_id'] == user_id]
    
    def get_resume(self, resume_id, user_id):
        """Get a specific resume"""
        resumes = self._load_data(self.resumes_file)
        return next((resume for resume in resumes if resume['id'] == resume_id and resume['user_id'] == user_id), None)
    
    def update_resume(self, resume_id, user_id, update_data):
        """Update a resume"""
        resumes = self._load_data(self.resumes_file)
        
        for resume in resumes:
            if resume['id'] == resume_id and resume['user_id'] == user_id:
                # Update fields
                for key, value in update_data.items():
                    if value is not None:
                        resume[key] = value
                
                resume['updated_at'] = datetime.utcnow().isoformat()
                self._save_data(self.resumes_file, resumes)
                return resume
        
        return None
    
    def delete_resume(self, resume_id, user_id):
        """Delete a resume"""
        resumes = self._load_data(self.resumes_file)
        
        for i, resume in enumerate(resumes):
            if resume['id'] == resume_id and resume['user_id'] == user_id:
                del resumes[i]
                self._save_data(self.resumes_file, resumes)
                return True
        
        return False
