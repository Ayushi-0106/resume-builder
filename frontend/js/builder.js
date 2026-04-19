class ResumeBuilder {
    constructor() {
        this.apiBase = 'http://localhost:5000/api';
        this.token = localStorage.getItem('authToken');
        this.currentResumeId = null;
        this.resumeData = {
            personal_info: {},
            summary: '',
            experience: [],
            education: [],
            skills: [],
            projects: [],
            template: 'minimal'
        };
        
        this.init();
    }
    
    init() {
        this.checkAuth();
        this.setupEventListeners();
        this.setupNavigation();
        this.updatePreview();
    }
    
    checkAuth() {
        if (!this.token) {
            window.location.href = 'index.html';
        }
    }
    
    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', () => this.showSection(item.dataset.section));
        });
        
        // Form inputs
        this.setupFormListeners();
        
        // Buttons
        document.getElementById('saveBtn').addEventListener('click', () => this.saveResume());
        document.getElementById('downloadBtn').addEventListener('click', () => this.downloadPDF());
        document.getElementById('logoutBtn').addEventListener('click', () => this.logout());
        const refreshBtn = document.getElementById('refreshPreview');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => this.updatePreview());
        }
        
        // Add buttons
        document.getElementById('addExperience').addEventListener('click', () => this.addExperience());
        document.getElementById('addEducation').addEventListener('click', () => this.addEducation());
        document.getElementById('addProject').addEventListener('click', () => this.addProject());
        
        // Template selection
        document.querySelectorAll('.template-option').forEach(option => {
            option.addEventListener('click', () => this.selectTemplate(option.dataset.template));
        });

        // AI assistance buttons (delegated)
        document.body.addEventListener('click', (e) => {
            const aiBtn = e.target.closest('.btn-ai');
            if (aiBtn) {
                const type = aiBtn.dataset.type;
                this.handleAISuggestions(type, aiBtn);
            }
        });

        // AI modal close
        const closeAiModal = document.getElementById('closeAiModal');
        if (closeAiModal) {
            closeAiModal.addEventListener('click', () => this.hideAIModal());
        }
        const aiModal = document.getElementById('aiModal');
        if (aiModal) {
            aiModal.addEventListener('click', (e) => {
                if (e.target === aiModal) this.hideAIModal();
            });
        }
    }
    
    setupFormListeners() {
        // Personal info
        document.getElementById('fullName').addEventListener('input', (e) => {
            this.resumeData.personal_info.name = e.target.value;
            this.updatePreview();
        });
        
        document.getElementById('email').addEventListener('input', (e) => {
            this.resumeData.personal_info.email = e.target.value;
            this.updatePreview();
        });
        
        document.getElementById('phone').addEventListener('input', (e) => {
            this.resumeData.personal_info.phone = e.target.value;
            this.updatePreview();
        });
        
        document.getElementById('location').addEventListener('input', (e) => {
            this.resumeData.personal_info.location = e.target.value;
            this.updatePreview();
        });

        const linkedinInput = document.getElementById('linkedin');
        if (linkedinInput) {
            linkedinInput.addEventListener('input', (e) => {
                this.resumeData.personal_info.linkedin = e.target.value;
                this.updatePreview();
            });
        }
        const githubInput = document.getElementById('github');
        if (githubInput) {
            githubInput.addEventListener('input', (e) => {
                this.resumeData.personal_info.github = e.target.value;
                this.updatePreview();
            });
        }
        
        // Summary
        document.getElementById('summaryText').addEventListener('input', (e) => {
            this.resumeData.summary = e.target.value;
            this.updatePreview();
        });
        
        // Skills
        document.getElementById('skillsInput').addEventListener('input', (e) => {
            this.resumeData.skills = e.target.value.split(',').map(s => s.trim()).filter(s => s);
            this.updatePreview();
        });
    }
    
    setupNavigation() {
        this.showSection('personal');
    }
    
    showSection(sectionName) {
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        document.querySelector(`[data-section="${sectionName}"]`).classList.add('active');
        
        document.querySelectorAll('.form-section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(sectionName).classList.add('active');
    }
    
    addExperience() {
        const id = Date.now().toString();
        const template = document.getElementById('experienceTemplate').innerHTML;
        const html = template.replace(/\{\{id\}\}/g, id).replace(/\{\{index\}\}/g, this.resumeData.experience.length + 1);
        
        document.getElementById('experienceList').insertAdjacentHTML('beforeend', html);
        
        this.resumeData.experience.push({
            id,
            title: '',
            company: '',
            startDate: '',
            endDate: '',
            description: ''
        });
        
        this.setupExperienceListeners(id);
        this.updatePreview();
    }
    
    setupExperienceListeners(id) {
        const item = document.querySelector(`[data-id="${id}"]`);
        const inputs = item.querySelectorAll('input, textarea');
        
        inputs.forEach(input => {
            input.addEventListener('input', (e) => {
                const exp = this.resumeData.experience.find(e => e.id === id);
                if (exp) {
                    exp[e.target.name] = e.target.value;
                    this.updatePreview();
                }
            });
        });
    }
    
    removeExperience(id) {
        this.resumeData.experience = this.resumeData.experience.filter(e => e.id !== id);
        document.querySelector(`[data-id="${id}"]`).remove();
        this.updatePreview();
    }
    
    addEducation() {
        const id = Date.now().toString();
        const template = document.getElementById('educationTemplate').innerHTML;
        const html = template.replace(/\{\{id\}\}/g, id).replace(/\{\{index\}\}/g, this.resumeData.education.length + 1);
        
        document.getElementById('educationList').insertAdjacentHTML('beforeend', html);
        
        this.resumeData.education.push({
            id,
            degree: '',
            institution: '',
            graduationYear: '',
            gpa: ''
        });
        
        this.setupEducationListeners(id);
        this.updatePreview();
    }
    
    setupEducationListeners(id) {
        const item = document.querySelector(`[data-id="${id}"]`);
        const inputs = item.querySelectorAll('input');
        
        inputs.forEach(input => {
            input.addEventListener('input', (e) => {
                const edu = this.resumeData.education.find(e => e.id === id);
                if (edu) {
                    edu[e.target.name] = e.target.value;
                    this.updatePreview();
                }
            });
        });
    }
    
    removeEducation(id) {
        this.resumeData.education = this.resumeData.education.filter(e => e.id !== id);
        document.querySelector(`[data-id="${id}"]`).remove();
        this.updatePreview();
    }
    
    addProject() {
        const id = Date.now().toString();
        const template = document.getElementById('projectTemplate').innerHTML;
        const html = template.replace(/\{\{id\}\}/g, id).replace(/\{\{index\}\}/g, this.resumeData.projects.length + 1);
        
        document.getElementById('projectsList').insertAdjacentHTML('beforeend', html);
        
        this.resumeData.projects.push({
            id,
            name: '',
            technologies: '',
            description: ''
        });
        
        this.setupProjectListeners(id);
        this.updatePreview();
    }
    
    setupProjectListeners(id) {
        const item = document.querySelector(`[data-id="${id}"]`);
        const inputs = item.querySelectorAll('input, textarea');
        
        inputs.forEach(input => {
            input.addEventListener('input', (e) => {
                const project = this.resumeData.projects.find(p => p.id === id);
                if (project) {
                    project[e.target.name] = e.target.value;
                    this.updatePreview();
                }
            });
        });
    }
    
    removeProject(id) {
        this.resumeData.projects = this.resumeData.projects.filter(p => p.id !== id);
        document.querySelector(`[data-id="${id}"]`).remove();
        this.updatePreview();
    }
    
    selectTemplate(templateName) {
        this.resumeData.template = templateName;
        
        document.querySelectorAll('.template-option').forEach(option => {
            option.classList.remove('selected');
        });
        document.querySelector(`[data-template="${templateName}"]`).classList.add('selected');
        
        this.updatePreview();
    }
    
    updatePreview() {
        const previewContainer = document.getElementById('resumePreview');
        
        let html = `
            <div class="resume-preview">
                <div class="preview-header">
                    <h1>${this.resumeData.personal_info.name || 'Your Name'}</h1>
                    <div class="preview-contact">
                        ${this.resumeData.personal_info.email ? `<span>${this.resumeData.personal_info.email}</span>` : ''}
                        ${this.resumeData.personal_info.phone ? `<span>${this.resumeData.personal_info.phone}</span>` : ''}
                        ${this.resumeData.personal_info.location ? `<span>${this.resumeData.personal_info.location}</span>` : ''}
                    </div>
                </div>
        `;
        
        if (this.resumeData.summary) {
            html += `
                <div class="preview-section">
                    <h2>Professional Summary</h2>
                    <p>${this.resumeData.summary}</p>
                </div>
            `;
        }
        
        if (this.resumeData.experience.length > 0) {
            html += `
                <div class="preview-section">
                    <h2>Professional Experience</h2>
                    ${this.resumeData.experience.map(exp => `
                        <div class="preview-item">
                            <h3>${exp.title || 'Job Title'}</h3>
                            <p class="preview-subtitle">${exp.company || 'Company'} | ${exp.startDate || 'Start'} - ${exp.endDate || 'Present'}</p>
                            <p>${exp.description || 'Description'}</p>
                        </div>
                    `).join('')}
                </div>
            `;
        }
        
        if (this.resumeData.education.length > 0) {
            html += `
                <div class="preview-section">
                    <h2>Education</h2>
                    ${this.resumeData.education.map(edu => `
                        <div class="preview-item">
                            <h3>${edu.degree || 'Degree'}</h3>
                            <p class="preview-subtitle">${edu.institution || 'Institution'} | ${edu.graduationYear || 'Year'}</p>
                            ${edu.gpa ? `<p>GPA: ${edu.gpa}</p>` : ''}
                        </div>
                    `).join('')}
                </div>
            `;
        }
        
        if (this.resumeData.skills.length > 0) {
            html += `
                <div class="preview-section">
                    <h2>Skills</h2>
                    <div class="preview-skills">
                        ${this.resumeData.skills.map(skill => `<span class="skill-tag">${skill}</span>`).join('')}
                    </div>
                </div>
            `;
        }
        
        if (this.resumeData.projects.length > 0) {
            html += `
                <div class="preview-section">
                    <h2>Projects</h2>
                    ${this.resumeData.projects.map(project => `
                        <div class="preview-item">
                            <h3>${project.name || 'Project Name'}</h3>
                            <p class="preview-subtitle">${project.technologies || 'Technologies'}</p>
                            <p>${project.description || 'Description'}</p>
                        </div>
                    `).join('')}
                </div>
            `;
        }
        
        html += '</div>';
        previewContainer.innerHTML = html;
        this.addPreviewStyles();
    }
    
    addPreviewStyles() {
        if (!document.getElementById('previewStyles')) {
            const style = document.createElement('style');
            style.id = 'previewStyles';
            style.textContent = `
                .resume-preview {
                    font-family: 'Inter', sans-serif;
                    max-width: 100%;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }
                .preview-header h1 {
                    font-size: 24px;
                    font-weight: 700;
                    margin-bottom: 8px;
                    color: #1a202c;
                }
                .preview-contact {
                    display: flex;
                    gap: 16px;
                    flex-wrap: wrap;
                    font-size: 14px;
                    color: #4a5568;
                    margin-bottom: 20px;
                }
                .preview-section {
                    margin-bottom: 20px;
                }
                .preview-section h2 {
                    font-size: 18px;
                    font-weight: 600;
                    color: #2d3748;
                    border-bottom: 2px solid #e2e8f0;
                    padding-bottom: 8px;
                    margin-bottom: 16px;
                }
                .preview-item {
                    margin-bottom: 16px;
                }
                .preview-item h3 {
                    font-size: 16px;
                    font-weight: 600;
                    color: #1a202c;
                    margin-bottom: 4px;
                }
                .preview-subtitle {
                    font-size: 14px;
                    color: #718096;
                    margin-bottom: 8px;
                }
                .preview-skills {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                }
                .skill-tag {
                    background: #edf2f7;
                    color: #2d3748;
                    padding: 4px 12px;
                    border-radius: 16px;
                    font-size: 12px;
                    font-weight: 500;
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    async saveResume() {
        try {
            console.log('Saving resume with data:', this.resumeData);
            console.log('Using token:', this.token ? 'Present' : 'Missing');
            
            const response = await fetch(`${this.apiBase}/resume`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.token}`
                },
                body: JSON.stringify(this.resumeData)
            });
            
            console.log('Save response status:', response.status);
            console.log('Save response ok:', response.ok);
            
            const data = await response.json();
            console.log('Save response data:', data);
            
            if (response.ok) {
                this.currentResumeId = data.resume_id || this.currentResumeId;
                console.log('Resume saved with ID:', this.currentResumeId);
                this.showMessage('Resume saved successfully!', 'success');
            } else {
                console.error('Save failed:', data);
                this.showMessage(data.error || 'Failed to save resume', 'error');
            }
            
        } catch (error) {
            console.error('Save error:', error);
            this.showMessage('Failed to save resume: ' + error.message, 'error');
        }
    }
    
    async downloadPDF() {
        try {
            console.log('Starting PDF download process...');
            // Only save if resume data is valid and not empty
            const hasData = this.resumeData && this.resumeData.personal_info && this.resumeData.personal_info.name;
            if (!this.currentResumeId && hasData) {
                console.log('No resume ID, saving resume first...');
                await this.saveResume();
            }
            if (!this.currentResumeId) {
                this.showMessage('Unable to prepare resume for download.', 'error');
                return;
            }
            console.log('Resume ID:', this.currentResumeId);
            this.showMessage('Preparing PDF download...', 'info');
            const apiUrl = `${this.apiBase}/resume/${this.currentResumeId}/pdf`;
            console.log('Downloading PDF from:', apiUrl);
            console.log('Using token:', this.token ? 'Present' : 'Missing');
            try {
                const testResponse = await fetch(`${this.apiBase}/test`);
                const testData = await testResponse.json();
                console.log('API test result:', testData);
                const pdfResponse = await fetch(apiUrl, {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${this.token}`,
                        'Accept': 'application/pdf'
                    }
                });
                if (!pdfResponse.ok) {
                    const errorText = await pdfResponse.text();
                    console.error('PDF download error response:', errorText);
                    this.showMessage(`Failed to download PDF: ${pdfResponse.status} - ${errorText}`, 'error');
                    return;
                }
                const contentType = pdfResponse.headers.get('content-type');
                console.log('Content type:', contentType);
                if (contentType && contentType.includes('text/html')) {
                    console.log('Opening HTML fallback in new window');
                    const htmlContent = await pdfResponse.text();
                    const newWindow = window.open('', '_blank');
                    newWindow.document.write(htmlContent);
                    newWindow.document.close();
                    this.showMessage('Resume opened in new window. Use Ctrl+P to print as PDF.', 'info');
                } else if (contentType && contentType.includes('application/pdf')) {
                    const blob = await pdfResponse.blob();
                    if (blob.size === 0) {
                        this.showMessage('PDF file is empty. Please try again.', 'error');
                        return;
                    }
                    const downloadUrl = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = downloadUrl;
                    a.download = `resume_${Date.now()}.pdf`;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(downloadUrl);
                    document.body.removeChild(a);
                    this.showMessage('PDF downloaded successfully!', 'success');
                } else {
                    throw new Error(`Unexpected content type: ${contentType}`);
                }
            } catch (error) {
                console.error('PDF download failed:', error);
                this.showMessage('Failed to download PDF: ' + error.message, 'error');
            }
        } catch (error) {
            console.error('PDF generation failed:', error);
            this.showMessage('Failed to generate PDF: ' + error.message, 'error');
        }
    }

    async handleAISuggestions(type, sourceButton) {
        try {
            let content = '';
            let context = '';
            if (type === 'summary') {
                content = document.getElementById('summaryText')?.value || '';
            } else if (type === 'skills') {
                content = document.getElementById('skillsInput')?.value || '';
            } else if (type === 'experience') {
                const container = sourceButton.closest('.experience-item');
                if (container) {
                    const title = container.querySelector('input[name="title"]')?.value || '';
                    const company = container.querySelector('input[name="company"]')?.value || '';
                    content = container.querySelector('textarea[name="description"]')?.value || '';
                    context = [title, company].filter(Boolean).join(' at ');
                }
            } else if (type === 'projects') {
                const container = sourceButton.closest('.project-item');
                if (container) {
                    const name = container.querySelector('input[name="name"]')?.value || '';
                    const tech = container.querySelector('input[name="technologies"]')?.value || '';
                    content = container.querySelector('textarea[name="description"]')?.value || '';
                    context = [name, tech].filter(Boolean).join(' | ');
                }
            }

            if (!content) {
                this.showMessage('Add some content first for better suggestions.', 'info');
                return;
            }

            const res = await fetch(`${this.apiBase}/ai/suggest`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.token}`
                },
                body: JSON.stringify({ type, content, context })
            });
            const data = await res.json();
            if (!res.ok) {
                this.showMessage(data.error || 'Failed to get suggestions', 'error');
                return;
            }

            const suggestions = Array.isArray(data.suggestions) ? data.suggestions : [];
            this.showAIModal(suggestions);
        } catch (err) {
            this.showMessage('Failed to get suggestions', 'error');
        }
    }

    showAIModal(suggestions) {
        const container = document.getElementById('aiSuggestions');
        const modal = document.getElementById('aiModal');
        if (!container || !modal) return;
        container.innerHTML = suggestions.length
            ? `<ul>${suggestions.map(s => `<li>${this.escapeHtml(s)}</li>`).join('')}</ul>`
            : '<p>No suggestions available.</p>';
        modal.classList.add('open');
        modal.style.display = 'block';
    }

    hideAIModal() {
        const modal = document.getElementById('aiModal');
        if (!modal) return;
        modal.classList.remove('open');
        modal.style.display = 'none';
    }

    escapeHtml(str) {
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }
    
    logout() {
        localStorage.removeItem('authToken');
        localStorage.removeItem('userData');
        window.location.href = 'index.html';
    }
    
    showMessage(message, type = 'info') {
        const messageEl = document.createElement('div');
        messageEl.className = `message message-${type}`;
        messageEl.textContent = message;
        
        messageEl.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 20px;
            border-radius: 8px;
            color: white;
            font-weight: 500;
            z-index: 1000;
            animation: slideIn 0.3s ease;
            max-width: 300px;
        `;
        
        const colors = {
            success: '#10b981',
            error: '#ef4444',
            info: '#3b82f6'
        };
        messageEl.style.backgroundColor = colors[type] || colors.info;
        
        document.body.appendChild(messageEl);
        
        setTimeout(() => {
            messageEl.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                if (messageEl.parentNode) {
                    messageEl.parentNode.removeChild(messageEl);
                }
            }, 300);
        }, 5000);
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Initialize resume builder
document.addEventListener('DOMContentLoaded', () => {
    window.resumeBuilder = new ResumeBuilder();
});

// Global functions for template removal
function removeExperience(id) {
    window.resumeBuilder?.removeExperience(id);
}

function removeEducation(id) {
    window.resumeBuilder?.removeEducation(id);
}

function removeProject(id) {
    window.resumeBuilder?.removeProject(id);
}
