from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from services.ai_service import AIService
from services.pdf_service import PDFService
from services.file_storage import FileStorage

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET', 'your-secret-key-here')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

jwt = JWTManager(app)
CORS(app)

# File-based storage
storage = FileStorage()

# Initialize services
ai_service = AIService()
pdf_service = PDFService()

@app.route('/')
def index():
    return jsonify({"message": "AI Resume Builder API"})

@app.route('/api/test')
def test_api():
    return jsonify({"message": "API is working", "timestamp": datetime.utcnow().isoformat()})

# Authentication routes
@app.route('/api/auth/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        
        if not email or not password or not name:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create user
        user = storage.create_user(email, password, name)
        if not user:
            return jsonify({"error": "User already exists"}), 409
        
        # Create access token
        access_token = create_access_token(identity=user['id'])
        
        return jsonify({
            "message": "User created successfully",
            "access_token": access_token,
            "user": {
                "id": user['id'],
                "email": user['email'],
                "name": user['name']
            }
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Find user
        user = storage.find_user_by_email(email)
        if not user or not storage.verify_password(user, password):
            return jsonify({"error": "Invalid credentials"}), 401
        
        # Create access token
        access_token = create_access_token(identity=user['id'])
        
        return jsonify({
            "message": "Login successful",
            "access_token": access_token,
            "user": {
                "id": user['id'],
                "email": user['email'],
                "name": user['name']
            }
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Resume management routes
@app.route('/api/resume', methods=['POST'])
@jwt_required()
def create_resume():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        resume = storage.create_resume(user_id, data)
        
        return jsonify({
            "message": "Resume created successfully",
            "resume_id": resume['id']
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/resume', methods=['GET'])
@jwt_required()
def get_resumes():
    try:
        user_id = get_jwt_identity()
        resumes = storage.get_user_resumes(user_id)
        
        return jsonify(resumes), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/resume/<resume_id>', methods=['GET'])
@jwt_required()
def get_resume(resume_id):
    try:
        user_id = get_jwt_identity()
        resume = storage.get_resume(resume_id, user_id)
        
        if not resume:
            return jsonify({"error": "Resume not found"}), 404
        
        return jsonify(resume), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/resume/<resume_id>', methods=['PUT'])
@jwt_required()
def update_resume(resume_id):
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        update_data = {
            "title": data.get('title'),
            "personal_info": data.get('personal_info'),
            "summary": data.get('summary'),
            "experience": data.get('experience'),
            "skills": data.get('skills'),
            "education": data.get('education'),
            "projects": data.get('projects'),
            "template": data.get('template')
        }
        
        
        update_data = {k: v for k, v in update_data.items() if v is not None}
        
        resume = storage.update_resume(resume_id, user_id, update_data)
        
        if not resume:
            return jsonify({"error": "Resume not found"}), 404
        
        return jsonify({"message": "Resume updated successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/resume/<resume_id>', methods=['DELETE'])
@jwt_required()
def delete_resume(resume_id):
    try:
        user_id = get_jwt_identity()
        success = storage.delete_resume(resume_id, user_id)
        
        if not success:
            return jsonify({"error": "Resume not found"}), 404
        
        return jsonify({"message": "Resume deleted successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# AI assistance routes
@app.route('/api/ai/suggest', methods=['POST'])
@jwt_required()
def get_ai_suggestions():
    try:
        data = request.get_json()
        content_type = data.get('type')
        content = data.get('content')
        context = data.get('context', '')
        
        if not content_type or not content:
            return jsonify({"error": "Missing required fields"}), 400
        
        suggestions = ai_service.get_suggestions(content_type, content, context)
        
        return jsonify({
            "suggestions": suggestions,
            "type": content_type
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PDF generation routes
@app.route('/api/resume/<resume_id>/pdf', methods=['GET'])
@jwt_required()
def download_pdf(resume_id):
    try:
        print(f"PDF download request for resume_id: {resume_id}")
        user_id = get_jwt_identity()
        print(f"User ID: {user_id}")
        resume = storage.get_resume(resume_id, user_id)
        print(f"Resume data received for PDF generation:")
        import pprint
        pprint.pprint(resume)
        if not resume:
            print(f"Resume not found for ID: {resume_id}")
            return jsonify({"error": "Resume not found"}), 404
        print(f"Resume found: {resume.get('title', 'Untitled')}")
        try:
            content = pdf_service.generate_pdf(resume)
            print(f"Generated content length: {len(content) if content else 'None'} bytes")
            if content and content[:4] == b'%PDF':
                print("Returning PDF content")
                response = app.response_class(
                    response=content,
                    status=200,
                    mimetype='application/pdf'
                )
                response.headers['Content-Disposition'] = f'attachment; filename=resume_{resume_id}.pdf'
            else:
                print("Returning HTML content (fallback)")
                response = app.response_class(
                    response=content,
                    status=200,
                    mimetype='text/html'
                )
                response.headers['Content-Disposition'] = f'inline; filename=resume_{resume_id}.html'
            return response
        except Exception as pdf_error:
            print(f"PDF generation inner error: {pdf_error}")
            import traceback
            traceback.print_exc()
            return jsonify({"error": f"PDF generation failed: {pdf_error}"}), 500
    except Exception as e:
        print(f"PDF generation outer error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
